from Classes.Video import Video
from Classes.Audio import Audio
import base64
import random

seed = 12345
random.seed(seed)

video_path = "resources/video.avi"
audio_path = "resources/audio.wav"
text_path = "resources/input.txt"

video = Video(video_path)
audio = Audio(audio_path)

file = open(text_path, "r")
text = file.read()

text64 = text.encode("ascii")
text64 = base64.b64encode(text64)
text64 = str(text64)[2:-1]

video_frame_start = random.randint(int(video.get_frame_count() / 8), int(video.get_frame_count() / 4))

print(f'There are {video.get_frame_count()} frames in the video.')
print(f'The FPS is {video.get_fps()}.\n')

print(f'There are {audio.get_frames()} samples in the audio.')
print(f'The sample rate is {audio.get_sample_framerate()}.\n')

print(f'In one video frame there are approximately {int(audio.get_sample_framerate() / video.get_fps())} audio samples.\n')

print(f'The inputs\'s text length is {len(text)}')
print(f'The inputs\'s text length in base64 encoding is {len(text64)}')
print(f'{len(text64) * 3} audio samples are needed to hide the data\n')

print(f'The data can be hidden in {video.get_frame_count() - video_frame_start} video frames')
print(f'The minimum amount of video frames in which the data will be hidden is {int(len(text64) / 100)}')

file.close()