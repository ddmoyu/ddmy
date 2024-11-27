import json
from dataclasses import dataclass
from typing import Optional, Union, Dict, Any


@dataclass
class TocRule:
    pre_update_js: Optional[str] = None
    chapter_list: Optional[str] = None
    chapter_name: Optional[str] = None
    chapter_url: Optional[str] = None
    format_js: Optional[str] = None
    is_volume: Optional[str] = None
    is_vip: Optional[str] = None
    is_pay: Optional[str] = None
    update_time: Optional[str] = None
    next_toc_url: Optional[str] = None

    def __post_init__(self):
        camel_to_snake = {
            "preUpdateJs": "pre_update_js",
            "chapterList": "chapter_list",
            "chapterName": "chapter_name",
            "chapterUrl": "chapter_url",
            "formatJs": "format_js",
            "isVolume": "is_volume",
            "isVip": "is_vip",
            "isPay": "is_pay",
            "updateTime": "update_time",
            "nextTocUrl": "next_toc_url",
        }

        for camel, snake in camel_to_snake.items():
            if hasattr(self, camel):
                setattr(self, snake, getattr(self, camel))
                delattr(self, camel)

    @classmethod
    def from_json(cls, json_data: Union[str, Dict[str, Any]]) -> "TocRule":
        if isinstance(json_data, str):
            json_obj = json.loads(json_data)
        else:
            json_obj = json_data

        return cls(**json_obj)
