from Audio import Audio
from Video import Video
from stegano_encode import stegano_encode
from ffmpeg import attach_wav_to_avi
import base64
import random

seed = 12345
random.seed(seed)

video_path = "resources/video.avi"
video_frame_path = "resources/frame.jpg"
audio_path = "resources/audio.wav"
text_path = "resources/input.txt"

new_audio_path = "resources/stegano.wav"
new_video_path = "resources/stegano.avi"

file = open(text_path, "r")
secret_text = file.read()
file.close()

secret_text = secret_text.encode("ascii")
secret_text = base64.b64encode(secret_text)
secret_text = list(str(secret_text))[2:-1]

print(secret_text)

video = Video(video_path)
audio = Audio(audio_path)

samples = audio.get_sample_values()

video_frame_start = random.randint(int(video.get_frame_count() / 8), int(video.get_frame_count() / 4))

new_sample = stegano_encode(video, audio, video_frame_start, secret_text, video_frame_path, samples, seed)

audio.save_audio(new_audio_path, new_sample)

# requires ffmpeg installation 
attach_wav_to_avi(video_path, new_audio_path, new_video_path)