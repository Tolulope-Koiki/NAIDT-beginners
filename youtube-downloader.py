#import urllib.request  # Built-in library for network requests

# def download_youtube_video(url):
#     # 1. Fetch the video data (simplified, not production-ready)
#     response = urllib.request.urlopen(url)
#     video_data = response.read()

#     # 2. Extract video title and extension (placeholder example)
#     title = input("enter the title: ")
#     extension = "mp4"  # Assumed for simplicity

#     # 3. Write video data to a file
#     filename = f"{title}.{extension}"
#     with open(filename, "wb") as f:
#         f.write(video_data)

#     print(f"Download complete: {filename}")

# # Example usage
# video_url = input("Enter YouTube video URL: ")
# download_youtube_video(video_url)



from pytube import YouTube
 
 # Enter video URL
 video_url = input("Enter YouTube video URL: ")
 
 # Download video (highest resolution)
 YouTube(video_url).streams.first().download()
 
 print("Download complete!")
