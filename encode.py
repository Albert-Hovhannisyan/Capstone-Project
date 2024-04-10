from Audio import Audio
from Video import Video
from stegano_encode import stegano_encode
import random

seed = 12345
random.seed(seed)

secret_text = "Steganography is the practice of representing information within another message or physical object, in such a manner that the presence of the information is not evident to human inspection. In computing/electronic contexts, a computer file, message, image, or video is concealed within another file, message, image, or video. The word steganography comes from Greek steganographia, which combines the words steganos, meaning covered or concealed, and graphia meaning writing."
secret_text = list(secret_text.lower())

video_path = "resources/test/video.avi"
video_frame_path = "resources/test/frame.jpg"
audio_path = "resources/test/audio.wav"

video = Video(video_path)
audio = Audio(audio_path)

samples = audio.get_sample_values()

video_frame_start = random.randint(0, int(video.get_frame_count() / 2))

new_sample = stegano_encode(video, audio, video_frame_start, secret_text, video_frame_path, samples, seed)

audio.save_audio("resources/test/new_audio.wav", new_sample)