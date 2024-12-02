from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any, Union
import json

@dataclass
class BaseCategory:
    url: Optional[str] = None
    category_list: Optional[str] = None
    category_name: Optional[str] = None
    category_url: Optional[str] = None

@dataclass
class RuleCategory(BaseCategory):
    @classmethod
    def from_json(cls, json_data: Union[str, Dict[str, Any]]) -> "RuleCategory":
        if isinstance(json_data, str):
            json_obj = json.loads(json_data)
        else:
            json_obj = json_data
        converted_data = {}
        for key, value in json_obj.items():
            snake_key = ''.join(['_' + char.lower() if char.isupper() else char for char in key]).lstrip('_')
            converted_data[snake_key] = value
        return cls(**converted_data)

@dataclass
class DataCategory(BaseCategory):
    def to_json(self) -> str:
        """将数据转换为JSON字符串"""
        # 将蛇形命名转换为驼峰命名
        data = {}
        for key, value in asdict(self).items():
            # 转换为驼峰命名
            components = key.split('_')
            camel_key = components[0] + ''.join(x.title() for x in components[1:])
            data[camel_key] = value
        wrapped_data = {"data_category": data}
        return json.dumps(wrapped_data, ensure_ascii=False, indent=2)

    def to_dict(self) -> Dict[str, Any]:
        """将数据转换为字典"""
        return {"data_category": asdict(self)}
