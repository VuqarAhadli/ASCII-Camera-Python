<div align="center">

#  ASCII Camera Python

### Transform your webcam feed into colorful ASCII art in real-time

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg)](https://opencv.org/)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [How It Works](#-how-it-works) • [Contributing](#-contributing)

---

</div>

## Technical Overview

This project implements a live video-to-ASCII conversion pipeline using OpenCV for frame capture and PIL for image processing. Each frame undergoes brightness analysis and character mapping, with ANSI 24-bit color codes applied to preserve the original RGB values in the terminal output.

## Requirements

### System Requirements
- Python 3.7 or higher
- Webcam or integrated camera device
- Terminal emulator with true color (24-bit) support

### Supported Terminals
- Windows Terminal
- iTerm2 (macOS)
- GNOME Terminal (Linux)
- Konsole (Linux)
- Alacritty
- Hyper
- Any terminal supporting ANSI escape sequences with 24-bit color

## Installation

Clone the repository:
```bash
git clone https://github.com/VuqarAhadli/ASCII-Camera-Python.git
cd ASCII-Camera-Python
```

Create and activate a virtual environment (recommended):
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Execution

Run the main script:
```bash
python ascii_camera.py
```

Terminate the program with `Ctrl+C`.

### Configuration Parameters

The `camera_ascii()` function accepts two parameters:

```python
camera_ascii(interval=0.1, width=200)
```

**interval** (float): Time delay between frame updates in seconds
- Lower values (0.05-0.1): Higher frame rate, increased CPU usage
- Higher values (0.2-0.5): Lower frame rate, reduced CPU usage
- Default: 0.2

**width** (int): ASCII output width in characters
- Range: 50-300 (recommended)
- Higher values: More detail, slower processing
- Lower values: Less detail, faster processing
- Default: 200

### Camera Selection

To use an external camera, modify the VideoCapture index:
```python
capture = cv2.VideoCapture(1)  # 0 = default camera, 1+ = external cameras
```

## Algorithm Details

### Processing Pipeline

1. **Frame Acquisition**: OpenCV captures frames from the VideoCapture device at the specified interval
2. **Color Space Conversion**: Frames are converted from BGR (OpenCV default) to RGB color space
3. **Image Resizing**: The frame is scaled to the target width while maintaining aspect ratio (with 0.5 height adjustment for character spacing)
4. **Brightness Calculation**: For each pixel, brightness is computed as the average of RGB values: `(R + G + B) / 3`
5. **Character Mapping**: Brightness values (0-255) are mapped to ASCII characters based on visual density
6. **Color Application**: ANSI escape sequence `\x1b[38;2;{r};{g};{b}m` applies 24-bit RGB color to each character
7. **Terminal Rendering**: The output buffer is flushed to the terminal with cursor positioning codes

### Character Set

The brightness-to-character mapping uses increasing visual density:
```
. , : ; + * ? Y G # @
```
Characters are selected by dividing the brightness value by 256 and multiplying by the character set length.

### ANSI Escape Sequences Used

- `\x1b[2J` - Clear entire screen
- `\x1b[H` - Move cursor to home position (0,0)
- `\x1b[38;2;{r};{g};{b}m` - Set foreground color to RGB
- `\x1b[0m` - Reset all attributes

## File Structure

```
ASCII-Camera-Python/
├── ascii_camera.py      # Main application script
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # Documentation
```

## Troubleshooting

### Camera Access Issues

**Error: "Camera not accessible"**

Possible causes and solutions:
- Camera is in use by another application - close other programs using the camera
- Insufficient permissions (Linux) - add user to video group: `sudo usermod -a -G video $USER`
- Wrong camera index - try different indices (0, 1, 2) in `cv2.VideoCapture()`
- Driver issues - ensure camera drivers are properly installed

### Terminal Compatibility

If ANSI escape codes are displayed as text rather than interpreted:
- Verify terminal supports ANSI escape sequences
- On Windows, use Windows Terminal or enable virtual terminal processing
- Update terminal emulator to the latest version

### Performance Optimization

For systems with limited resources:
- Increase `interval` parameter (0.2-0.5 seconds)
- Reduce `width` parameter (100-150 characters)
- Close unnecessary background processes
- Reduce terminal window size

## Known Limitations

- No audio capture or processing
- Single-threaded processing (no parallel frame handling)
- Terminal refresh rate dependent on system performance
- Character aspect ratio may vary between terminal emulators
- Colors may appear differently based on terminal color profiles

## Future Development

Potential improvements and features:
- Command-line argument parsing (argparse)
- Configuration file support (YAML/JSON)
- Multiple character set options
- Image file input support
- Video file recording (save to text file)
- Edge detection and contrast enhancement
- Multi-camera support
- Performance profiling and optimization
- Unit test coverage

## Contributing

Contributions are welcome. Please follow these guidelines:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Write clear, commented code following PEP 8 style guidelines
4. Test thoroughly on multiple platforms if possible
5. Commit with descriptive messages: `git commit -m "Add feature description"`
6. Push to your fork: `git push origin feature-name`
7. Submit a pull request with detailed description of changes

## License

This project is licensed under the MIT License. See the LICENSE file for full terms.

## Technical Dependencies

- **OpenCV (cv2)**: Video capture and frame processing
- **Pillow (PIL)**: Image manipulation and pixel data access
- **Standard Library**: time (frame rate control), os (system operations)

## Author

Vuqar Ahadli  
GitHub: [@VuqarAhadli](https://github.com/VuqarAhadli)

## Repository

[https://github.com/VuqarAhadli/ASCII-Camera-Python](https://github.com/VuqarAhadli/ASCII-Camera-Python)
