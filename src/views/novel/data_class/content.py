from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any, Union
import json


@dataclass
class BaseContent:
    content: Optional[str] = None


@dataclass
class RuleContent(BaseContent):
    @classmethod
    def from_json(cls, json_data: Union[str, Dict[str, Any]]) -> "RuleContent":
        if isinstance(json_data, str):
            json_obj = json.loads(json_data)
        else:
            json_obj = json_data
        converted_data = {}
        for key, value in json_obj.items():
            snake_key = "".join(
                ["_" + char.lower() if char.isupper() else char for char in key]
            ).lstrip("_")
            converted_data[snake_key] = value
        return cls(**converted_data)


@dataclass
class DataContent(BaseContent):
    def to_json(self) -> str:
        """将数据转换为JSON字符串"""
        # 将蛇形命名转换为驼峰命名
        data = {}
        for key, value in asdict(self).items():
            # 转换为驼峰命名
            components = key.split("_")
            camel_key = components[0] + "".join(x.title() for x in components[1:])
            data[camel_key] = value
        wrapped_data = {"data_content": data}
        return json.dumps(wrapped_data, ensure_ascii=False, indent=2)

    def to_dict(self) -> Dict[str, Any]:
        """将数据转换为字典"""
        return {"data_content": asdict(self)}
