from ._base import Component, TemplateString


class Paragraph(Component):
    text: TemplateString
    strong: bool = False
