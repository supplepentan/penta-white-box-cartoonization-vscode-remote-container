import os
import shutil
import cv2
import subprocess
from cartoonize import cartoonize
from video import video_2_images

def main():
    video_file = './test_video/test1.mp4'
    load_folder = 'test_images'
    save_folder = 'cartoonized_images'
    model_path = 'saved_models'
    
    if os.path.isdir('test_images'):
        shutil.rmtree('test_images')
    os.makedirs('test_images', exist_ok=True)
    if os.path.isdir('cartoonized_images'):
        shutil.rmtree('cartoonized_images')
    os.makedirs('cartoonized_images', exist_ok=True)

    video_2_images(video_file, load_folder)
    cartoonize(load_folder, save_folder, model_path)
    subprocess.run(["ffmpeg", "-r", "30", "-i", "cartoonized_images/%06d.jpg", "-vcodec", "libx264", "-r", "60", "cartoonized_images/out.mp4"])

    
if __name__ == '__main__':
    main()