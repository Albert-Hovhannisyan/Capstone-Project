from mapping import mapping
import random

def stegano_decode(video, audio, start, image_path, samples, seed):

    random.seed(seed)
    text = ""

    for i in range(start, video.get_frame_count()):
        video.get_frame(i, image_path)
        alphabet, colors = mapping(image_path, seed)

        dictionary = {}
        for j in range(len(colors)):
            dictionary[colors[j]] = alphabet[j]

        samples_per_frame = video.get_frame_duration() * audio.get_sample_framerate()
        start = int(i * samples_per_frame)
        end = int((i + 1) * samples_per_frame)

        limit = random.randint(100, 200)
        count = 0

        for j in range(start, end):
            if count == limit:
                break

            if len(str(samples[j])) >= 6:
                value = str(samples[j])[-3:]
                
                if value in dictionary:
                    text = text + dictionary[value]
                    if text[:-2] == "..":
                        return text
                    count = count + 1
                else:
                    return text
            
        # seed = random.randint(min((-1) * seed, seed), max((-1) * seed, seed))

    return text