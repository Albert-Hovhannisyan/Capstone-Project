from Classes.Audio import Audio
from Classes.Video import Video
from Functions.stegano_decode import stegano_decode
from Functions.ffmpeg import extract_wav_from_video
import base64
import random

seed = 12345
random.seed(seed)

video_path = "resources/stegano.avi"
audio_path = "resources/ext.wav"
text_path = "resources/output.txt"

limit = 100

use_ffmpeg = True

if use_ffmpeg == True:
    # requires ffmpeg installation 
    extract_wav_from_video(video_path, audio_path, hide_output = False)

video = Video(video_path)
audio = Audio(audio_path)

video_frame_start = random.randint(int(video.get_frame_count() / 8), int(video.get_frame_count() / 4))

output = stegano_decode(video, audio, video_frame_start, limit)

output = base64.b64decode(output)
output = str(output)[2:-1]

file = open(text_path, "w")
file.write(output)
file.close()