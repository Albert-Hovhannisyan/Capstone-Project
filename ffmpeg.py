import subprocess

def extract_wav_from_video(video_path, audio_path):
    command = ["ffmpeg", "-i", f'{video_path}', "-c", "copy", "-acodec", "pcm_s16le", f'{audio_path}']
    subprocess.call(command, shell=True)

def attach_wav_to_avi(video_path, audio_path, new_video_path):
    command = ["ffmpeg", "-i", f'{video_path}', "-i", f'{audio_path}', "-c", "copy", f'{new_video_path}']
    subprocess.call(command, shell=True)