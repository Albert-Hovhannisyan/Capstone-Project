# Capstone-Project
 
The code uses FFmpeg. Use the following installation guide as a reference: https://phoenixnap.com/kb/ffmpeg-windows

If you do not want to install FFmpeg, you can use a VLC media player to extract the audio as a WAV with WAV codec and convert the video to AVI with M-JPEG codec without the audio. In that case, in the info.py, encode.py, and decode.py, change the variable use_ffmpeg to False.

Then, you need a .txt file containing the text that needs to be hidden and a cover video. Run the info.py code by specifying the input paths, seed and limit to convert the video to AVI and extract the audio as a WAV. Info.py will also output all the relevant information. If you are satisfied with the output, run the encode.py by specifying the input paths, seed and limit. To decode use decode.py which works similar to encode.py. 