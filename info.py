from Classes.Video import Video
from Classes.Audio import Audio

video_path = "resources/video.avi"
audio_path = "resources/audio.wav"

video = Video(video_path)
audio = Audio(audio_path)

print(f'There are {video.get_frame_count()} frames in the video.')
print(f'The FPS is {video.get_fps()}.')
print(f'Each video frame is {video.get_frame_duration()} seconds.')

print(f'There are {audio.get_frames()} frames in the audio.')
print(f'The sample framerate is {audio.get_sample_framerate()}.')
print(f'In one video frame there are approximately {int(video.get_frame_duration() * audio.get_sample_framerate())} audio frames.')