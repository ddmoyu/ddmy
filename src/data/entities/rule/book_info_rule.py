import json
from dataclasses import dataclass
from typing import Optional, Union, Dict, Any, List


@dataclass
class BookInfoRule:
    init: Optional[str] = None
    name: Optional[str] = None
    author: Optional[str] = None
    intro: Optional[str] = None
    kind: Optional[str] = None
    last_chapter: Optional[str] = None
    update_time: Optional[str] = None
    cover_url: Optional[str] = None
    toc_url: Optional[str] = None
    word_count: Optional[int] = None
    can_rename: Optional[bool] = None
    download_urls: Optional[List[str]] = None

    def __post_init__(self):
        camel_to_snake = {
            "lastChapter": "last_chapter",
            "updateTime": "update_time",
            "coverUrl": "cover_url",
            "tocUrl": "toc_url",
            "wordCount": "word_count",
            "canReName": "can_rename",
            "downloadUrls": "download_urls",
        }

        for camel, snake in camel_to_snake.items():
            if hasattr(self, camel):
                setattr(self, snake, getattr(self, camel))
                delattr(self, camel)

    @classmethod
    def from_json(cls, json_data: Union[str, Dict[str, Any]]) -> "BookInfoRule":
        if isinstance(json_data, str):
            json_obj = json.loads(json_data)
        else:
            json_obj = json_data

        return cls(**json_obj)
