import cv2

class Video():
    def __init__(self, path):

        self.path = path
        self.video = cv2.VideoCapture(path)

        self.frame_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH)) 
        self.frame_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

        self.frame_count = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = self.video.get(cv2.CAP_PROP_FPS)
        
        self.time = self.frame_count / self.fps
    
    def get_frame_count(self):
        return self.frame_count
    
    def get_fps(self):
        return self.fps
    
    def get_time(self):
        return self.time

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

        video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        boolean, frame = video.read()

        cv2.imwrite(image_path, frame)

        video.release()
