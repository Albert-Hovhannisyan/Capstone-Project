import subprocess

# def ffmpeg(type, video_path, audio_path, new_audio_path):
#     match type:
#         case 0:
#             command = f'ffmpeg -i {video_path} -c copy -acodec pcm_s16le {audio_path}'
#         case 1:
#             command = f'ffmpeg -i {video_path} -c copy -acodec copy {audio_path}'
#         case 2:
#             command = f'ffmpeg -i {video_path} -i {audio_path} -c copy {new_audio_path}'
#     subprocess.call(command, shell=True)


# # extract audio from mp4 to wav
# command = "ffmpeg -i resources/test/video.mp4 -c copy -acodec pcm_s16le resources/test/audio.wav"

# # extract audio from avi to wav
command = "ffmpeg -i resources/test/new.avi -acodec copy resources/test/ext.wav"

# attach wav to avi
# command = "ffmpeg -i resources/test/video.avi -i resources/test/new_audio.wav -c copy resources/test/new.avi"

subprocess.call(command, shell=True)