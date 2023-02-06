import uuid

from pydantic import BaseModel, Field


def _uid_factory():
    return uuid.uuid4().hex


class TemplateString:
    """
    This is a marker class for strings that should be treated as templates.
    """

    def __init__(self, value):
        self.value = value

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError("string required")
        return cls(v)


class Component(BaseModel):
    id: str = Field(None, allow_mutation=False)

    def __init__(self, **data):
        if "id" not in data:
            data["id"] = _uid_factory()
        super().__init__(**data)

    class Config:
        validate_assignment = True
