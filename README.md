# ASCII Camera Python

Transform your webcam feed into colorful ASCII art in real-time

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg)](https://opencv.org/)

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [How It Works](#how-it-works) • [Contributing](#contributing)

---

## Features

- **Full RGB Color Support** - Every ASCII character displays in true color
- **Real-time Processing** - Smooth frame-by-frame conversion
- **Customizable Resolution** - Adjust width for detail vs. performance
- **Adjustable Frame Rate** - Control refresh speed to match your needs
- **Terminal-based** - No GUI required, works in any modern terminal
- **Simple & Lightweight** - Minimal dependencies, easy to set up

## Requirements

- Python 3.7 or higher
- Webcam or built-in camera
- Terminal with true color (24-bit) support
  - Windows Terminal
  - iTerm2 (macOS)
  - GNOME Terminal (Linux)
  - Konsole (Linux)
  - Alacritty
  - Hyper

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/VuqarAhadli/ASCII-Camera-Python.git
cd ASCII-Camera-Python
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Simply run the script to start the ASCII camera:

```bash
python ascii_camera.py
```

Press `Ctrl+C` to stop the camera and exit.

### Advanced Configuration

You can customize the display by modifying the parameters in the script:

```python
camera_ascii(
    interval=0.1,  # Time between frames (seconds)
    width=200      # Width in characters
)
```

**Parameters:**
- `interval`: Lower values = faster refresh (e.g., 0.05 for smoother motion)
- `width`: Higher values = more detail (e.g., 150-250 recommended)

### Command Line Arguments

Edit the script to add your preferred settings:

```python
if __name__ == "__main__":
    camera_ascii(interval=0.1, width=200)
```

## How It Works

The ASCII Camera follows a clever process to transform video into art:

1. **Frame Capture** - Grabs live frames from your webcam using OpenCV
2. **Color Conversion** - Converts BGR to RGB format for accurate colors
3. **Resizing** - Scales the image to your specified width (maintaining aspect ratio)
4. **Brightness Mapping** - Analyzes each pixel's brightness (0-255)
5. **Character Selection** - Maps brightness to ASCII characters from light to dark:
   ```
   . , : ; + * ? Y G # @
   ```
6. **Color Application** - Applies true RGB colors to each character using ANSI escape codes
7. **Terminal Display** - Renders the colorful ASCII art in real-time

## Troubleshooting

### Camera Not Found

**Error:** `RuntimeError: Camera not accessible`

**Solutions:**
- Ensure your webcam is connected and not in use by another application
- On Linux, check camera permissions:
  ```bash
  sudo usermod -a -G video $USER
  ```
- Try changing the camera index in the code:
  ```python
  capture = cv2.VideoCapture(1)  # Try 1, 2, etc. for external cameras
  ```

### Colors Not Displaying

**Problem:** Seeing escape codes instead of colors?

**Solutions:**
- Verify your terminal supports true color (24-bit color)
- On Windows, use Windows Terminal or a compatible terminal
- Update your terminal application to the latest version

### Performance Issues

**Problem:** Slow or laggy display?

**Solutions:**
- Increase the `interval` parameter (e.g., 0.2 or 0.3)
- Decrease the `width` parameter (e.g., 100 or 120)
- Close other applications using the camera

## Future Enhancements

Ideas for expanding this project:

- Add command-line arguments for easy configuration
- Record ASCII videos
- Add different ASCII character sets
- Implement filters and effects
- Support for image file input
- GUI version with tkinter or PyQt

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code follows Python best practices and includes appropriate comments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [OpenCV](https://opencv.org/) for camera capture
- Uses [Pillow](https://python-pillow.org/) for image processing
- Inspired by the classic ASCII art community

## Contact

**Vuqar Ahadli** - [@VuqarAhadli](https://github.com/VuqarAhadli)

Project Link: [https://github.com/VuqarAhadli/ASCII-Camera-Python](https://github.com/VuqarAhadli/ASCII-Camera-Python)

---

Made with Python

If you found this project interesting, please consider giving it a star!
