import json
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any, Union
from src.views.novel.data_class.category import RuleCategory
from src.views.novel.data_class.explore import RuleExplore

@dataclass
class BaseSource:
    book_source_group: Optional[str] = None
    book_source_name: Optional[str] = None
    book_source_url: Optional[str] = None

    enabled: Optional[bool] = True
    enabled_explore: Optional[bool] = True
    last_update_time: Optional[str] = None

    rule_book_info: Optional[str] = None
    rule_content: Optional[str] = None
    rule_category: Optional[RuleCategory] = None
    rule_explore: Optional[RuleExplore] = None
    rule_search: Optional[str] = None
    rule_toc: Optional[str] = None

    search_url: Optional[str] = None

@dataclass
class RuleSource(BaseSource):
    @classmethod
    def from_json(cls, json_data: Union[str, Dict[str, Any]]) -> "RuleSource":
        if isinstance(json_data, str):
            json_obj = json.loads(json_data)
        else:
            json_obj = json_data
        converted_data = {}
        for key, value in json_obj.items():
            snake_key = ''.join(['_' + char.lower() if char.isupper() else char for char in key]).lstrip('_')
            if snake_key == 'rule_category' and isinstance(value, dict):
                converted_data[snake_key] = RuleCategory.from_json(value)
            elif snake_key == 'rule_explore' and isinstance(value, dict):
                converted_data[snake_key] = RuleExplore.from_json(value)
            else:
                converted_data[snake_key] = value
        return cls(**converted_data)

@dataclass
class DataSource(BaseSource):
    def to_json(self) -> str:
        """将数据转换为JSON字符串"""
        # 将蛇形命名转换为驼峰命名
        data = {}
        for key, value in asdict(self).items():
            components = key.split('_')
            camel_key = components[0] + ''.join(x.title() for x in components[1:])
            if key == 'rule_category' and isinstance(value, RuleCategory):
                data[camel_key] = asdict(value)
            elif key == 'rule_explore' and isinstance(value, RuleExplore):
                data[camel_key] = asdict(value)
            else:
                data[camel_key] = value
        wrapped_data = {"data_explore": data}
        return json.dumps(wrapped_data, ensure_ascii=False, indent=2)

    def to_dict(self) -> Dict[str, Any]:
        """将数据转换为字典"""
        data = {}
        for key, value in asdict(self).items():
            if key == 'rule_category' and isinstance(value, RuleCategory):
                data[key] = asdict(value)
            elif key == 'rule_explore' and isinstance(value, RuleExplore):
                data[key] = asdict(value)
            else:
                data[key] = value
        return {"data_explore": data}
