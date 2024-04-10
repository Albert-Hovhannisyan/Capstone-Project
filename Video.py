import cv2
from moviepy.editor import VideoFileClip

class Video():
    def __init__(self, path):

        self.path = path
        self.video = cv2.VideoCapture(path)

        self.frame_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH)) 
        self.frame_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

        self.frame_count = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = self.video.get(cv2.CAP_PROP_FPS)
        
        self.time = self.frame_count / self.fps
        self.frame_duration = 1 / self.fps
    
    def get_frame_count(self):
        return self.frame_count
    
    def get_fps(self):
        return self.fps
    
    def get_time(self):
        return self.time
    
    def get_frame_duration(self):
        return self.frame_duration

    def convert_to_avi(self, output_path):
        fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
        output = cv2.VideoWriter(output_path, fourcc, self.fps, (self.frame_width, self.frame_height)) 

        boolean = True
        while(boolean): 
            boolean, frame = self.video.read() 
            output.write(frame) 

        self.video.release() 
        output.release()

    def get_frame(self, frame_number, image_path):
        video = cv2.VideoCapture(self.path)

        if frame_number < 0 or frame_number >= self.frame_count:
            print(f"Invalid frame number. Please choose a frame between 0 and {self.frame_count - 1}.")
            return

        video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        boolean, frame = video.read()

        cv2.imwrite(image_path, frame)

        video.release()
