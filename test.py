from Classes.Audio import Audio
import numpy as np
import matplotlib.pyplot as plt

audio_path1 = "resources/audio.wav"
audio_path2 = "resources/stegano.wav"

audio1 = Audio(audio_path1)
audio2 = Audio(audio_path2)

s1 = audio1.get_sample_values()
s2 = audio2.get_sample_values()

start = 1.66005
end = 1.6603

start_sample = (start * audio1.get_sample_framerate())
end_sample = (end * audio1.get_sample_framerate())
              
duration = np.linspace(start, end, num=int(end_sample - start_sample))
                       
plt.figure(figsize=(10, 5))
plt.plot(duration, s1[int(start_sample):int(end_sample)], color="blue")
plt.plot(duration, s2[int(start_sample):int(end_sample)], color="red")
plt.legend(['Original', 'Stegano'])
plt.title("Audio Waveform")
plt.ylabel("Samples")
plt.xlabel("Seconds")
plt.xlim(start, end)
plt.show()