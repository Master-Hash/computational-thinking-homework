import requests

# 请求参数说明
# pn = page number
# ps = page size 上限为50

data1 = requests.get(
    "https://api.bilibili.com/x/space/wbi/arc/search?mid=2765893&pn=1&ps=50",
    headers={
        # "Referer": "https://space.bilibili.com/2765893",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
    },
).json()

data2 = requests.get(
    "https://api.bilibili.com/x/space/wbi/arc/search?mid=2765893&pn=2&ps=50",
    headers={
        # "Referer": "https://space.bilibili.com/2765893",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
    },
).json()

data = [*data1["data"]["list"]["vlist"], *data2["data"]["list"]["vlist"]]

if __name__ == "__main__":
    print(data)
