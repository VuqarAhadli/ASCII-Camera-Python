# ASCII Camera

A real-time ASCII art renderer that converts your webcam feed into colorful ASCII characters in the terminal.

## Features

- Real-time webcam to ASCII conversion
- Full RGB color support in terminal
- Adjustable resolution and frame rate
- Clean terminal interface

## Demo

The application captures your webcam feed and displays it as ASCII art with colors directly in your terminal.

## Requirements

- Python 3.7+
- Webcam/Camera
- Terminal with true color support (most modern terminals)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ascii-camera.git
cd ascii-camera
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python ascii_camera.py
```

### Customization

You can adjust the parameters in the script:

```python
camera_ascii(interval=0.1, width=200)
```

- `interval`: Time between frames (in seconds). Lower = faster, higher = slower
- `width`: Width of ASCII output in characters. Higher = more detail

### Controls

- Press `Ctrl+C` to exit the program

## How It Works

1. Captures frames from your webcam using OpenCV
2. Converts each frame to RGB format
3. Resizes the image based on specified width
4. Maps pixel brightness to ASCII characters
5. Applies RGB colors to each character using ANSI escape codes
6. Displays the result in the terminal

## Troubleshooting

**Camera not accessible error:**
- Ensure your webcam is connected and not in use by another application
- On Linux, you may need camera permissions
- Try changing the camera index: `cv2.VideoCapture(1)` for external cameras

**Colors not displaying:**
- Ensure your terminal supports true color (24-bit color)
- Most modern terminals support this (iTerm2, Windows Terminal, GNOME Terminal, etc.)

## License

MIT License - see [LICENSE](LICENSE) file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Uses OpenCV for camera capture
- Uses Pillow for image processing
