import json
from dataclasses import dataclass
from typing import Optional, Union, Dict, Any


@dataclass
class CategoryEntity:
    url: Optional[str] = None
    category_list: Optional[str] = None
    category_name: Optional[str] = None
    category_url: Optional[str] = None

    @classmethod
    def from_json(cls, json_data: Union[str, Dict[str, Any]]) -> "CategoryEntity":
        if isinstance(json_data, str):
            json_obj = json.loads(json_data)
        else:
            json_obj = json_data

        # 将骆驼命名法转换为蛇形命名法
        camel_to_snake = {
            "categoryList": "category_list",
            "categoryName": "category_name",
            "categoryUrl": "category_url",
        }

        # 转换属性名称
        for camel, snake in camel_to_snake.items():
            if camel in json_obj:
                json_obj[snake] = json_obj.pop(camel)

        return cls(**json_obj)


@dataclass
class ExploreEntity:
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

    @classmethod
    def from_json(cls, json_data: Union[str, Dict[str, Any]]) -> "ExploreEntity":
        if isinstance(json_data, str):
            json_obj = json.loads(json_data)
        else:
            json_obj = json_data

        # 将骆驼命名法转换为蛇形命名法
        camel_to_snake = {
            "categoryList": "category_list",
            "categoryName": "category_name",
            "categoryUrl": "category_url",
            "bookList": "book_list",
            "lastChapter": "last_chapter",
            "updateTime": "update_time",
            "bookUrl": "book_url",
            "coverUrl": "cover_url",
            "wordCount": "word_count",
        }

        # 转换属性名称
        for camel, snake in camel_to_snake.items():
            if camel in json_obj:
                json_obj[snake] = json_obj.pop(camel)

        return cls(**json_obj)
