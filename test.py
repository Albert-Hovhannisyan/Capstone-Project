from Classes.Audio import Audio
import numpy as np

original_audio_path = "resources/audio.wav"
stegano_audio_path = "resources/stegano.wav"

original = Audio(original_audio_path).get_sample_values()
stegano = Audio(stegano_audio_path).get_sample_values()

mse = np.mean(np.square(np.array(original) - np.array(stegano)))

psnr = 10 * np.log10((max(original) ** 2) / mse)

print(f'The MSE is = {mse}')
print(f'The PSNR is = {psnr}')