from Functions.mapping import mapping
import os

def stegano_encode(video, audio, start, text, image_path, limit):    
    
    samples = audio.get_sample_values()

    for i in range(start, video.get_frame_count()):

        video.get_frame(i, image_path)
        dictionary = mapping(image_path, method = "encode")

        samples_per_frame = audio.get_sample_framerate() / video.get_fps()

        sample_start = int(i * samples_per_frame)
        sample_end = int((i + 1) * samples_per_frame)

        count = 0
        j = sample_start

        while j < sample_end:
            if len(text) != 0:
                if count == limit:
                    break
                
                value = dictionary[text.pop(0)]

                k = 0
                while k < 3:
                    if abs(samples[j]) > 9:
                        string = str(samples[j])
                        samples[j] = int(string[:-1] + value[k])                        
                        k = k + 1

                    j = j + 1

                count = count + 1
                
            else:
                os.remove(image_path)
                return samples