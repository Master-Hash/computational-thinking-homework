from datetime import datetime
from dataclasses import dataclass


@dataclass
class Notes:
    name: str

    def __post_init__(self):
        self._notes: list[tuple[str, str]] = []

    def add_notes(self, text: str):
        date_str = datetime.now().strftime("%Y/%m/%d")
        self._notes.append((date_str, text))

    def get_notes(self):
        return self._notes

    def __str__(self) -> str:
        # for ni ma
        return "\n".join(map(lambda x: f"{x[1]}记录于{x[0]}", self.get_notes()))


def main():
    notes = Notes("test")
    notes.add_notes("今天天气不错！")
    notes.add_notes("今天去吃了小崔真面。")
    notes.add_notes("南操的音乐会很棒！")
    print(notes)


if __name__ == "__main__":
    main()
