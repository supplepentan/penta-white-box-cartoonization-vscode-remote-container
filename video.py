import os
import cv2

def video_2_images(video_file, image_dir):
    image_file = '%s.jpg' 
    # Initial setting
    i = 0
    interval = 1
    length = 300000  # 最大フレーム数
    
    cap = cv2.VideoCapture(video_file)
    while(cap.isOpened()):
        flag, frame = cap.read()  
        if flag == False:
            break
        if i == length*interval:
            break
        if i % interval == 0:
            file_name = image_file % str(int(i/interval)).zfill(6)
            cv2.imwrite(os.path.join(image_dir, file_name), frame)
        i += 1 
    cap.release()