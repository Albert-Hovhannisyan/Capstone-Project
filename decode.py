from Audio import Audio
from Video import Video
from stegano_decode import stegano_decode
import random

seed = 12345
random.seed(seed)

video_path = "resources/stegano.avi"
video_frame_path = "resources/frame.jpg"
audio_path = "resources/ext.wav"

video = Video(video_path)
audio = Audio(audio_path)

samples = audio.get_sample_values()

video_frame_start = random.randint(0, int(video.get_frame_count() / 4))

output = stegano_decode(video, audio, video_frame_start, video_frame_path, samples, seed)

print(output)
print(len(output))