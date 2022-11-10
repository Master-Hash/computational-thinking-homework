from typing import Callable, TypeAlias

Name: TypeAlias = str
Lyric: TypeAlias = str
Line = dict[Name, Lyric]

x = input()
with open("在未来的你跟我说声嗨.txt", encoding="utf-8") as f:
    LYRIC = map(lambda x: x.strip(), f.readlines())

a = filter(lambda x: "：" in x, LYRIC)
b = list(map(lambda x: {"name": x.split("：")[0], "lyric": x.split("：")[1]}, a))


def group_by(f: Callable[[Line], str], x: list[Line]) -> dict[str, list[Line]]:
    d: dict[str, list[Line]] = {}
    for i in x:
        if f(i) not in d:
            d[f(i)] = [i]
        else:
            d[f(i)].append(i)
    return d


def main():
    c = group_by(lambda x: x["name"], b)
    for i in c[x]:
        print(f"{i['name']}：{i['lyric']}")


if __name__ == "__main__":
    main()
