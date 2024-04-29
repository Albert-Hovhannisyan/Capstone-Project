from Classes.Audio import Audio
from Classes.Video import Video
from Functions.stegano_encode import stegano_encode
from Functions.ffmpeg import attach_wav_to_avi
import base64
import random

seed = 12345
random.seed(seed)

video_path_avi = "resources/video.avi"
video_frame_path = "resources/frame.jpg"
audio_path = "resources/audio.wav"
text_path = "resources/input.txt"

new_audio_path = "resources/stegano.wav"
new_video_path = "resources/stegano.avi"

use_ffmpeg = True

file = open(text_path, "r")
secret_text = file.read()
file.close()

secret_text = secret_text.encode("ascii")
secret_text = base64.b64encode(secret_text)
secret_text = str(secret_text)[2:-1]
secret_text = list(secret_text + "|")

video = Video(video_path_avi)
audio = Audio(audio_path)

samples = audio.get_sample_values()

video_frame_start = random.randint(int(video.get_frame_count() / 8), int(video.get_frame_count() / 4))

new_sample = stegano_encode(video, audio, video_frame_start, secret_text, video_frame_path, samples)

audio.save_audio(new_audio_path, new_sample)

if use_ffmpeg == True:
    # requires ffmpeg installation 
    attach_wav_to_avi(video_path_avi, new_audio_path, new_video_path, False)