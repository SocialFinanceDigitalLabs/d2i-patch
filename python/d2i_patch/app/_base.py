import yaml.representer
from pydantic import BaseModel


def _str_presenter(dumper, data):
    if len(data.splitlines()) > 1:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.representer.SafeRepresenter.add_representer(str, _str_presenter)


class BaseComponent(BaseModel):
    def yaml(self):
        obj_representation = self.dict(exclude_none=True)
        return yaml.safe_dump(obj_representation, sort_keys=False)
