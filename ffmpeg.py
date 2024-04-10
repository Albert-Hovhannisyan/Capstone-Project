import subprocess

def extract_wav_from_video(video_path, audio_path):
    command = f'ffmpeg -i {video_path} -c copy -acodec pcm_s16le {audio_path}'
    subprocess.call(command, shell=True)

def attach_wav_to_avi(video_path, audio_path, new_audio_path):
    command = command = f'ffmpeg -i {video_path} -i {audio_path} -c copy {new_audio_path}'
    subprocess.call(command, shell=True)

# def extract_wav_from_avi(video_path, audio_path):
#     command = f'ffmpeg -i {video_path} -c copy -acodec copy {audio_path}'
#     subprocess.call(command, shell=True)