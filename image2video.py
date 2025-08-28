#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
import subprocess

def create_video_with_ffmpeg(image_path, audio_path, output_path="output_video.mp4"):
    try:
        print(f"Creating video from:")
        print(f"  Image: {image_path}")
        print(f"  Audio: {audio_path}")
        print(f"  Output: {output_path}")
        
        # Use ffmpeg directly to create the video
        cmd = [
            'ffmpeg',
            '-loop', '1',  # Loop the image
            '-i', image_path,  # Input image
            '-i', audio_path,  # Input audio
            '-c:v', 'libx264',  # Video codec
            '-tune', 'stillimage',  # Optimize for still image
            '-c:a', 'aac',  # Audio codec
            '-b:a', '192k',  # Audio bitrate
            '-pix_fmt', 'yuv420p',  # Pixel format for compatibility
            '-shortest',  # Stop when the shortest input ends (audio)
            '-y',  # Overwrite output file if it exists
            output_path
        ]
        
        print(f"\nRunning ffmpeg...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"\nVideo successfully created: {output_path}")
        else:
            print(f"\nError creating video:", file=sys.stderr)
            print(result.stderr, file=sys.stderr)
            sys.exit(1)
            
    except FileNotFoundError:
        print("Error: ffmpeg not found. Please install ffmpeg:", file=sys.stderr)
        print("  macOS: brew install ffmpeg", file=sys.stderr)
        print("  Ubuntu/Debian: sudo apt-get install ffmpeg", file=sys.stderr)
        print("  Windows: Download from https://ffmpeg.org/download.html", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Create a video from a static image and audio file using ffmpeg")
    parser.add_argument("image", help="Path to the image file")
    parser.add_argument("audio", help="Path to the audio file (.mp3, .m4a, or other audio formats)")
    parser.add_argument("-o", "--output", default=None, help="Output video file path (default: same as image name with .mp4 extension in same directory)")
    
    args = parser.parse_args()
    
    image_path = Path(args.image)
    audio_path = Path(args.audio)
    
    if not image_path.exists():
        print(f"Error: Image file '{image_path}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    if not audio_path.exists():
        print(f"Error: Audio file '{audio_path}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    # If output not specified, use same name as image with .mp4 extension in same directory
    if args.output is None:
        output_path = image_path.parent / (image_path.stem + ".mp4")
    else:
        output_path = Path(args.output)
    
    create_video_with_ffmpeg(str(image_path), str(audio_path), str(output_path))

if __name__ == "__main__":
    main()