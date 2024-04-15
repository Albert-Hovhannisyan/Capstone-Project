from Classes.Video import Video
from Classes.Audio import Audio
import base64

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

print(f'There are {video.get_frame_count()} frames in the video.')
print(f'The FPS is {video.get_fps()}.')
print(f'Each video frame is {video.get_frame_duration()} seconds.\n')

print(f'There are {audio.get_frames()} frames in the audio.')
print(f'The sample framerate is {audio.get_sample_framerate()}.')
print(f'In one video frame there are approximately {int(video.get_frame_duration() * audio.get_sample_framerate())} audio frames.\n')

print(f'The inputs\'s text length is {len(text)}')
print(f'The inputs\'s text length in base64 encoeding is {len(text64)}')

file.close()