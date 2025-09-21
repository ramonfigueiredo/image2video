# Image2Video - Static Image to Video Converter

A tool to create videos by combining a static image with an audio track. Perfect for creating podcast videos, music visualizers, or any content where you need a static image displayed for the duration of an audio file.

## Quick Start

```bash
# Clone or download the repository
cd image2video

# Run with your files
python image2video.py your_image.png your_audio.mp3

# Output: your_image.mp4 (in the same directory)
```

## Requirements

- Python 3.6 or higher
- FFmpeg installed on your system

## Installation

### Installing FFmpeg:

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html)

## Usage

### Basic usage:

```bash
python image2video.py <image_path> <audio_path>
```

By default, the video will be created in the **same directory as the image file** with the **same name as the image** but with a `.mp4` extension.

### Specify custom output filename:

```bash
python image2video.py <image_path> <audio_path> -o <output_path>
```

### Command-line arguments:

- `image` (required): Path to the image file (PNG, JPG, etc.)
- `audio` (required): Path to the audio file (MP3, M4A, MP4, WAV, etc.)
- `-o, --output` (optional): Path for the output video file (default: same directory and name as image with .mp4 extension)

## Examples

### Example 1: Basic usage (output in same folder as image)
```bash
python image2video.py files/image.png files/audio.mp3
```
Creates `files/image.mp4` with the image and audio.

### Example 2: Custom output filename
```bash
python image2video.py photo.jpg music.mp3 -o custom_video.mp4
```
Creates `custom_video.mp4` with the specified image and audio.

## Output

The script will:
1. Load the audio file and determine its duration
2. Create a video clip using the image for the entire audio duration
3. Combine the image and audio into a video file
4. Export as MP4 with H.264 video codec and AAC audio codec

## Features

- **Automatic naming**: Output video uses the same name as the input image
- **Same directory output**: Video is saved in the same folder as the source image
- **Fast processing**: Direct FFmpeg integration for optimal performance
- **Wide format support**: Works with most image and audio formats
- **Custom output option**: Override default naming when needed

## Troubleshooting

### Common issues:

1. **FFmpeg not found**: Make sure FFmpeg is installed (see Installation section above)
2. **File not found**: Verify that the image and audio file paths are correct
3. **Permission denied**: Ensure you have write permissions in the output directory
4. **Output file conflict**: If the audio file is an MP4 with the same name as the image, the script will automatically append "_output" to prevent overwriting the audio file

## Notes

- The output video will have 24 fps (frames per second)
- The image aspect ratio is preserved
- The video duration matches the audio duration exactly
- Supported formats:
  - Images: PNG, JPG, JPEG, GIF, BMP, etc.
  - Audio: MP3, M4A, MP4, WAV, OGG, AAC, FLAC, etc.
  - Output: MP4 (recommended), AVI, MOV, etc.
