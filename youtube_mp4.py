import os
import subprocess

try:
    import pytube
except ImportError:
    subprocess.check_call(["pip", "install", "pytube"])
    import pytube

while True:
    # Ask user for video url
    url = input("Enter the YouTube video url: ")

    # Create YouTube object with video url
    youtube = pytube.YouTube(url)

    # Get the highest resolution video stream
    video = youtube.streams.get_highest_resolution()

    # Download the video to the "Downloads" folder
    video.download(output_path=os.path.expanduser("~\Downloads"))

    # Print "Downloaded!"
    print("Downloaded!")


