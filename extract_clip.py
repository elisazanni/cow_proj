from moviepy.editor import VideoFileClip

input_path = "DJI_0429.MP4"
start_time = 105
duration = 20

clip = VideoFileClip(input_path)

subclip = clip.subclip(start_time, start_time + duration)

subclip.write_videofile("output.mp4")
