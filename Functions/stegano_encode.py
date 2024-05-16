from Functions.mapping import mapping
import os

def stegano_encode(video, audio, start, text, limit):

    video_frame_path = "tmp.jpg"    
    
    samples = audio.get_sample_values()

    for i in range(start, video.get_frame_count()):

        video.get_frame(i, video_frame_path)
        dictionary = mapping(video_frame_path, method = "encode")

        samples_per_frame = audio.get_sample_framerate() / video.get_fps()

        sample_start = int(i * samples_per_frame)
        sample_end = int((i + 1) * samples_per_frame)

        count = 0
        j = sample_start

        while j < sample_end:
            if len(text) != 0:
                if count == limit:
                    break

                k = 0
                value = dictionary[text.pop(0)]

                while k < 3:
                    if abs(samples[j]) > 9:
                        string = str(samples[j])
                        samples[j] = int(string[:-1] + value[k])                        
                        k = k + 1

                    j = j + 1

                count = count + 1
                
            else:
                os.remove(video_frame_path)
                return samples