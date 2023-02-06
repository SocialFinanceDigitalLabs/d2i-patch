from dataclasses import dataclass


@dataclass
class Paragraph:
    text: str
    strong: bool = False

    def __json__(self):
        return dict(
            type="paragraph",
            text=self.text,
            strong=self.strong,
        )
