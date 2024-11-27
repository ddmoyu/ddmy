import json
from dataclasses import dataclass
from typing import Optional, Union, Dict, Any, List


@dataclass
class ExploreKind:
    title: Optional[List[str]] = None
    url: Optional[str] = None
    style: Optional[str] = None

    @classmethod
    def from_json(cls, json_data: Union[str, Dict[str, Any]]) -> "ExploreKind":
        if isinstance(json_data, str):
            json_obj = json.loads(json_data)
        else:
            json_obj = json_data

        return cls(**json_obj)
