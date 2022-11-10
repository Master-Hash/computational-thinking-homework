with open("中文歌词.txt", encoding="utf-8") as f:
    # 读取中文歌词到列表变量lyric_zh中
    LYRIC_ZH = map(lambda i: i.strip(), f.readlines())

with open("外文歌词.txt", encoding="utf-8") as f:
    # 读取外文歌词到列表变量lyric_foreign中
    LYRIC_FOREIGN = map(lambda i: i.strip(), f.readlines())

LEN = 15
for zh, foreign in zip(LYRIC_ZH, LYRIC_FOREIGN):
    # 逐行打印中文歌词和外文歌词
    print(zh)
    print(foreign)
