from ffmpeg import extract_wav_from_video
from Audio import Audio
from Video import Video

video = Video("resources/video.mp4")
video.convert_to_avi("resources/video.avi")

extract_wav_from_video("resources/video.mp4", "resources/audio.wav")