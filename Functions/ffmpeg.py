import subprocess
import os

def extract_wav_from_video(video_path, audio_path, hide_output):
    command = ["ffmpeg", "-i", f'{video_path}', "-c", "copy", "-acodec", "pcm_s16le", "-ac", "1", f'{audio_path}']

    if hide_output == True:
        subprocess.call(command, shell = True, stdout = open(os.devnull, 'w'), stderr = subprocess.STDOUT)
    else:
        subprocess.call(command, shell = True)

def attach_wav_to_avi(video_path, audio_path, new_video_path, hide_output):
    command = ["ffmpeg", "-i", f'{video_path}', "-i", f'{audio_path}', "-c", "copy", "-acodec", "pcm_s16le", "-ac", "1", f'{new_video_path}']
    
    if hide_output == True:
        subprocess.call(command, shell = True, stdout = open(os.devnull, 'w'), stderr = subprocess.STDOUT)
    else:
        subprocess.call(command, shell = True)