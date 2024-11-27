import json
from dataclasses import dataclass
from typing import Optional, Union, Dict, Any


# 定义 ContentRule 类
@dataclass
class ContentRule:
    content: Optional[str] = None
    title: Optional[str] = None
    next_content_url: Optional[str] = None
    web_js: Optional[str] = None
    source_regex: Optional[str] = None
    replace_regex: Optional[str] = None
    image_style: Optional[str] = None
    image_decode: Optional[str] = None
    pay_action: Optional[str] = None

    def __post_init__(self):
        camel_to_snake = {
            "nextContentUrl": "next_content_url",
            "webJs": "web_js",
            "sourceRegex": "source_regex",
            "replaceRegex": "replace_regex",
            "imageStyle": "image_style",
            "imageDecode": "image_decode",
            "payAction": "pay_action",
        }

        for camel, snake in camel_to_snake.items():
            if hasattr(self, camel):
                setattr(self, snake, getattr(self, camel))
                delattr(self, camel)

    @classmethod
    def from_json(cls, json_data: Union[str, Dict[str, Any]]) -> "ContentRule":
        if isinstance(json_data, str):
            json_obj = json.loads(json_data)
        else:
            json_obj = json_data

        return cls(**json_obj)
