import wave
import numpy as np
import matplotlib.pyplot as plt

class Audio:
    def __init__(self, path):
        self.audio = wave.open(path, "rb")

        self.sample_framerate = self.audio.getframerate()
        self.frames = self.audio.getnframes()
        self.channels = self.audio.getnchannels()
        self.sampwidth = self.audio.getsampwidth()

        self.time = self.frames / self.sample_framerate
        self.sample_values_bit = self.audio.readframes(-1)

        self.sample_values = np.frombuffer(self.sample_values_bit, dtype=np.int16).copy()

    def get_sample_framerate(self):
        return self.sample_framerate
    
    def get_frames(self):
        return self.frames
    
    def get_sample_values_bit(self):
        return self.sample_values_bit
    
    def get_time(self):
        return self.time
    
    def get_sample_values(self):
        return self.sample_values.copy()

    def plot_waveform(self, start, end):
        start_sample = int(start * self.sample_framerate)
        end_sample = int(end * self.sample_framerate)

        linspace = np.linspace(start, end, num = end_sample - start_sample)

        plt.figure(figsize=(10, 5))
        plt.plot(linspace, self.sample_values[start_sample:end_sample])
        plt.title("Audio Waveform")
        plt.ylabel("Samples")
        plt.xlabel("Seconds")
        plt.xlim(start, end)
        plt.show()

    def save_audio(self, output_path, new_sample):
        audio = wave.open(output_path, "wb")
        new_sample = new_sample.tobytes()

        audio.setnchannels(self.channels)
        audio.setsampwidth(self.sampwidth)
        audio.setnframes(self.frames)
        audio.setframerate(self.sample_framerate)

        audio.writeframes(new_sample)
        
        audio.close()