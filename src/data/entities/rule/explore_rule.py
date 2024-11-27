import json
from dataclasses import dataclass
from typing import Optional, Union, Dict, Any


@dataclass
class ExploreRule:
    book_list: Optional[str] = None
    name: Optional[str] = None
    author: Optional[str] = None
    intro: Optional[str] = None
    kind: Optional[str] = None
    last_chapter: Optional[str] = None
    update_time: Optional[str] = None
    book_url: Optional[str] = None
    cover_url: Optional[str] = None
    word_count: Optional[str] = None

    def __post_init__(self):
        camel_to_snake = {
            "bookList": "book_list",
            "lastChapter": "last_chapter",
            "updateTime": "update_time",
            "bookUrl": "book_url",
            "coverUrl": "cover_url",
            "wordCount": "word_count",
        }

        for camel, snake in camel_to_snake.items():
            if hasattr(self, camel):
                setattr(self, snake, getattr(self, camel))
                delattr(self, camel)

    @classmethod
    def from_json(cls, json_data: Union[str, Dict[str, Any]]) -> "ExploreRule":
        if isinstance(json_data, str):
            json_obj = json.loads(json_data)
        else:
            json_obj = json_data

        return cls(**json_obj)
