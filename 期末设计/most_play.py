from spider import data

data.sort(key=lambda x: x["play"], reverse=True)

max_play_times = data[0]["play"]

for video in data:
    if video["play"] == max_play_times:
        print(video["title"], f"{max_play_times}次播放")
    else:
        break
