from pytube import YouTube

# Get the video and work with
def get_video(video_url: str, **kwargs):
    f = YouTube(video_url)

