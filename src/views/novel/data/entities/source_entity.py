import json
from dataclasses import dataclass
from typing import Optional, Union, Dict, Any
from src.views.novel.data.entities.explore_entity import ExploreEntity, CategoryEntity


@dataclass
class SourceEntity:
    book_source_group: Optional[str] = None
    book_source_name: Optional[str] = None
    book_source_url: Optional[str] = None

    enabled: Optional[bool] = True
    enabled_explore: Optional[bool] = True
    last_update_time: Optional[str] = None

    rule_book_info: Optional[str] = None
    rule_content: Optional[str] = None
    rule_category: Optional[CategoryEntity] = None
    rule_explore: Optional[ExploreEntity] = None
    rule_search: Optional[str] = None
    rule_toc: Optional[str] = None

    search_url: Optional[str] = None

    @classmethod
    def from_json(cls, json_data: Union[str, Dict[str, Any]]) -> "SourceEntity":
        if isinstance(json_data, str):
            try:
                json_obj = json.loads(json_data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return cls()  # 返回空对象或默认对象
        else:
            json_obj = json_data

        # 将骆驼命名法转换为蛇形命名法
        camel_to_snake = {
            "bookSourceGroup": "book_source_group",
            "bookSourceName": "book_source_name",
            "bookSourceUrl": "book_source_url",
            "enabledExplore": "enabled_explore",
            "lastUpdateTime": "last_update_time",
            "ruleBookInfo": "rule_book_info",
            "ruleContent": "rule_content",
            "ruleCategory": "rule_category",
            "ruleExplore": "rule_explore",
            "ruleSearch": "rule_search",
            "ruleToc": "rule_toc",
            "searchUrl": "search_url",
        }

        # 转换属性名称
        for camel, snake in camel_to_snake.items():
            if camel in json_obj:
                json_obj[snake] = json_obj.pop(camel)

        # 处理缺失的字段（使用默认值）
        for field in cls.__annotations__:
            if field not in json_obj:
                json_obj[field] = None  # 可以根据需要设置默认值

        # 处理嵌套的 ExploreEntity 和 CategoryEntity，加入检查
        if "rule_category" in json_obj and json_obj["rule_category"]:
            try:
                json_obj["rule_category"] = CategoryEntity.from_json(
                    json_obj["rule_category"]
                )
            except Exception as e:
                print(f"Error processing rule_category: {e}")
                json_obj["rule_category"] = None

        if "rule_explore" in json_obj and json_obj["rule_explore"]:
            try:
                json_obj["rule_explore"] = ExploreEntity.from_json(
                    json_obj["rule_explore"]
                )
            except Exception as e:
                print(f"Error processing rule_explore: {e}")
                json_obj["rule_explore"] = None

        # 返回 SourceEntity 实例
        return cls(**json_obj)
