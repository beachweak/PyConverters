import os
import time
import subprocess
import sys

try:
    from pytube import YouTube
    from moviepy.editor import *
except ImportError:
    print("Installing required libraries...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytube", "moviepy"])
    from pytube import YouTube
    from moviepy.editor import *


def download_and_convert_to_mp3(yt_url, output_path):
    try:
        yt = YouTube(yt_url)
        video = yt.streams.filter(only_audio=True).order_by('bitrate').desc().first()
        temp_audio_file = os.path.join(output_path, "temp_audio.mp4")
        video.download(output_path=output_path, filename=temp_audio_file)
        
        # Convert mp4 to mp3
        mp3_file = os.path.join(output_path, f"{yt.title}.mp3")
        audioclip = AudioFileClip(temp_audio_file)
        audioclip.write_audiofile(mp3_file)

        # Remove temp mp4 file
        os.remove(temp_audio_file)
        print("Converted!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    output_path = os.path.join(os.path.expanduser("~"), "Downloads")
    while True:
        yt_url = input("Please enter a YouTube link: ")
        download_and_convert_to_mp3(yt_url, output_path)
        time.sleep(1)