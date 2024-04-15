from Functions.ffmpeg import extract_wav_from_video
from Classes.Video import Video

video_path_mp4 = "resources/video.mp4"
video_path_avi = "resources/video.avi"
audio_path = "resources/audio.wav"

video = Video(video_path_mp4)
video.convert_to_avi(video_path_avi)

# requires ffmpeg installation 
extract_wav_from_video(video_path_mp4, audio_path)