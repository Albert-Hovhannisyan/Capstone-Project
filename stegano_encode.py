from mapping import mapping
import random

def stegano_encode(video, audio, start, text, image_path, samples, seed):    
    random.seed(seed)
    for i in range(start, video.get_frame_count()):
        video.get_frame(i, image_path)
        alphabet, colors = mapping(image_path, seed)

        dictionary = {}
        for j in range(len(alphabet)):
            dictionary[alphabet[j]] = colors[j]

        samples_per_frame = video.get_frame_duration() * audio.get_sample_framerate()

        start = int(i * samples_per_frame)
        end = int((i + 1) * samples_per_frame)

        limit = random.randint(100, 200)
        count = 0

        for j in range(start, end):
            if len(text) != 0:
                if count == limit:
                    break
                
                if len(str(samples[j])) >= 6:
                    string = str(samples[j])
                    samples[j] = int(string[:-3] + dictionary[text.pop(0)])
                    count = count + 1
            else:
                return samples
                
        # seed = random.randint(min((-1) * seed, seed), max((-1) * seed, seed))