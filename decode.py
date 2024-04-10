from Audio import Audio
from Video import Video
from stegano_decode import stegano_decode
from ffmpeg import extract_wav_from_video
import random

seed = 12345
random.seed(seed)

video_path = "resources/stegano.avi"
video_frame_path = "resources/frame.jpg"
audio_path = "resources/ext.wav"
text_path = "resources/output.txt"

extract_wav_from_video(video_path, audio_path)

video = Video(video_path)
audio = Audio(audio_path)

samples = audio.get_sample_values()

video_frame_start = random.randint(0, int(video.get_frame_count() / 4))

output = stegano_decode(video, audio, video_frame_start, video_frame_path, samples, seed)

print(len(output))

file = open(text_path, "w")
file.write(output)
file.close()