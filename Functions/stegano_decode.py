from Functions.mapping import mapping
import os

def stegano_decode(video, audio, start, limit):

    video_frame_path = "tmp.jpg"

    samples = audio.get_sample_values()
    text = ""

    for i in range(start, video.get_frame_count()):

        video.get_frame(i, video_frame_path)
        dictionary = mapping(video_frame_path, method = "decode")

        samples_per_frame = audio.get_sample_framerate() / video.get_fps()

        sample_start = int(i * samples_per_frame)
        sample_end = int((i + 1) * samples_per_frame)

        count = 0
        j = sample_start

        while j < sample_end:
            if count == limit:
                break

            k = 0
            value = ""

            while k < 3:
                if abs(samples[j]) > 9:
                    value = value + str(samples[j])[-1]
                    k = k + 1

                j = j + 1
                
            if value in dictionary:
                if dictionary[value] == "|":
                    os.remove(video_frame_path)
                    return text
                
                else:
                    text = text + dictionary[value]
                    count = count + 1