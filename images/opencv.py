import cv2


def load_and_detect_edges(fname: str):
    img = cv2.imread(fname)
    # luma
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # sobel
    sobelx = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
    # write
    cv2.imwrite("edges.png", sobelxy)
    return


load_and_detect_edges("my_file.png")

