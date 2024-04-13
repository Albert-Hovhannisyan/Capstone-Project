from Functions.ffmpeg import extract_wav_from_video
from Classes.Audio import Audio
from Classes.Video import Video

video = Video("resources/video.mp4")
video.convert_to_avi("resources/video.avi")

# requires ffmpeg installation 
extract_wav_from_video("resources/video.mp4", "resources/audio.wav")