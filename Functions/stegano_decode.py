from Functions.mapping import mapping

def stegano_decode(video, audio, start, image_path):

    samples = audio.get_sample_values()
    text = ""

    for i in range(start, video.get_frame_count()):
        video.get_frame(i, image_path)
        alphabet, colors = mapping(image_path)

        dictionary = {}
        for j in range(len(colors)):
            dictionary[colors[j]] = alphabet[j]

        samples_per_frame = audio.get_sample_framerate() / video.get_fps()

        sample_start = int(i * samples_per_frame)
        sample_end = int((i + 1) * samples_per_frame)

        limit = 100
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
                else:
                    j = j + 1
                
            if value in dictionary:
                if dictionary[value] == "|":
                    return text
                text = text + dictionary[value]
                count = count + 1