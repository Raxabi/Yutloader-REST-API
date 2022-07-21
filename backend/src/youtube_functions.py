from pytube import YouTube

# Get the video and work with
def get_audio_from_video(video_url):
    f = YouTube(video_url)
    video_selection = f.streams.get_audio_only()
    return video_selection.download("videos/")


