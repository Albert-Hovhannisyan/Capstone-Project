from Classes.Video import Video
from Classes.Audio import Audio
from Functions.ffmpeg import extract_wav_from_video
import base64
import random
import os

seed = 12345
random.seed(seed)

video_path_original = "resources/video.mp4"
video_path_avi = "resources/video.avi"
audio_path = "resources/audio.wav"
text_path = "resources/input.txt"

if os.path.exists(video_path_avi) == False:
    Video(video_path_original).convert_to_avi(video_path_avi)

if os.path.exists(audio_path) == False:
    # requires ffmpeg installation 
    extract_wav_from_video(video_path_original, audio_path, hide_output = True)

video = Video(video_path_avi)
audio = Audio(audio_path)

file = open(text_path, "r")
text = file.read()

text64 = text.encode("ascii")
text64 = base64.b64encode(text64)
text64 = str(text64)[2:-1]

video_frame_start = random.randint(int(video.get_frame_count() / 8), int(video.get_frame_count() / 4))

print(f'There are {video.get_frame_count()} frames in the video.')
print(f'The frame rate is {video.get_fps()}.\n')

print(f'There are {audio.get_frames()} samples in the audio.')
print(f'The sample rate is {audio.get_sample_framerate()}Hz.\n')

print(f'In one video frame there are approximately {int(audio.get_sample_framerate() / video.get_fps())} audio samples.\n')

print(f'The input text length is {len(text)} characters')
print(f'The input text length in base64 encoding is {len(text64)} characters\n')

print(f'The number of audio samples needed to hide the data is {len(text64) * 3} samples\n')

print(f'The total amount of available video frames for hiding the data is {video.get_frame_count() - video_frame_start} frames')
print(f'The minimum amount of video frames in which the data will be hidden is {int(len(text64) / 100)} frames')

file.close()