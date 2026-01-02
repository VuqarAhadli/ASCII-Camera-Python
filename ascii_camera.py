import cv2
import time
from PIL import Image
import os
import sys

def ascii_color_from_frame(frame, width=200):
    """
    Convert a BGR frame to colored ASCII string.
    """
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    w, h = img.size
    height = int(width * (h / w) * 0.5)
    img = img.resize((width, height))

    pixels = img.getdata()
    chars = [".", ",", ":", ";", "*", "+", "?", "Y", "G", "#", "@"]

    out = ""
    idx = 0

    for r, g, b in pixels:
        brightness = (r + g + b) // 3
        ch = chars[brightness * len(chars) // 256]
        out += f"\x1b[38;2;{r};{g};{b}m{ch}"

        idx += 1
        if idx % width == 0:
            out += "\x1b[0m\n"

    return out


def camera_ascii(interval=0.2, width=200):
    """
    Capture webcam frames and print them as colored ASCII.
    """
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        raise RuntimeError("Camera not accessible")

    # Clear terminal 
    sys.stdout.write("\x1b[2J")
    sys.stdout.flush()

    try:
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            # Move cursor to top-left for 0 indentation
            sys.stdout.write("\x1b[H")
            sys.stdout.write(ascii_color_from_frame(frame, width))
            sys.stdout.flush()

            time.sleep(interval)

    except KeyboardInterrupt:
        pass
    finally:
        video_capture.release()
        # Reset terminal styling
        sys.stdout.write("\x1b[0m")
        sys.stdout.flush()


if __name__ == "__main__":
    # Parameters can be changed
    camera_ascii(interval=0.01, width=200)


