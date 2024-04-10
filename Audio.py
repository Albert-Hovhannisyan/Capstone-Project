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
        self.sample_values = np.frombuffer(self.sample_values_bit, dtype=np.int32).copy()

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
    
    # def close_audio(self):
    #     self.audio.close()

    def plot_waveform(self, start, end):
        start_sample = (start * self.sample_framerate)
        end_sample = (end * self.sample_framerate)

        duration = np.linspace(start, end, num=int(end_sample - start_sample))

        plt.figure(figsize=(10, 5))
        plt.plot(duration, self.sample_values[int(start_sample):int(end_sample)])
        plt.title("Audio Waveform")
        plt.ylabel("Samples")
        plt.xlabel("Seconds")
        plt.xlim(start, end)
        plt.show()

    def save_audio(self, output_path, new_frames):
        audio = wave.open(output_path, "wb")

        new_frames = new_frames.tobytes()

        audio.setnchannels(self.channels)
        audio.setsampwidth(self.sampwidth)
        audio.setnframes(self.frames)
        audio.setframerate(self.sample_framerate)

        audio.writeframes(new_frames)

        audio.close()
        print("Done")