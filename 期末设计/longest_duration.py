from spider import data


def time_to_seconds(time: str) -> int:
    """转换 "MM:SS" 格式时间字符串为秒数。

    按照 api.bilibili.com 的数据格式，
    长于一小时的时间表示如 "85:04"（前端会改成 01:25:04，抓前端八爪鱼的朋友自求多福）
    短于一分钟的时间显示如 "00:44"（前后端一致）
    """
    times = time.split(":")
    return int(times[0]) * 60 + int(times[1])


data.sort(key=lambda x: time_to_seconds(x["length"]), reverse=True)

longest_duration = time_to_seconds(data[0]["length"])

for video in data:
    if time_to_seconds(video["length"]) == longest_duration:
        print(video["title"], f"{video['length']}长")
    else:
        break
