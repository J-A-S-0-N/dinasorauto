import mss
import mss.tools
import cv2
import os

path = "C:\\Users\\jason\\Desktop\\_\\coding\\python\\python\\else\\dinasorauto\\ideas"

def main():    
    os.chdir(path)
    with mss.mss() as sct:
        # The screen part to capture
        region = {'top': 320, 'left': 410, 'width': 63, 'height': 42}
    
        # Grab the data
        img = sct.grab(region)
    
        # Save to the picture file
        mss.tools.to_png(img.rgb, img.size, output='dino.png')

    image = cv2.imread(path)
    window_name = 'dino'
    ksize = (63, 42)
    image = cv2.blur(image, ksize)
    cv2.imshow(window_name, image) 

if __name__ == "__main__":
    main()
    