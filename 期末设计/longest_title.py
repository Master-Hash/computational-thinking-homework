from spider import data

data.sort(key=lambda x: len(x["title"]), reverse=True)

longest_title_length = len(data[0]["title"])

for video in data:
    if len(video["title"]) == longest_title_length:
        print(video["title"], f"{longest_title_length}字符长")
    else:
        break
