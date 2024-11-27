import json
from dataclasses import dataclass
from typing import Optional, List
from src.data.model.analyze_rule.rule_data_interface import RuleDataInterface


@dataclass
class BaseBook(RuleDataInterface):
    name: str
    author: str
    book_url: str
    kind: Optional[str]
    word_count: Optional[str]
    variable: Optional[str]

    info_html: Optional[str]
    toc_html: Optional[str]

    def put_variable(self, key, value: Optional[str]):
        if super().put_variable(key, value):
            self.variable = json.dumps(self.variable_map)
        return True

    def put_custom_variable(self, value: Optional[str]):
        self.put_variable("custom", value)

    def get_custom_variable(self):
        return self.get_variable("custom")

    def get_kind_list(self) -> List[str]:
        kind_list = []
        if self.word_count and self.word_count.strip():
            kind_list.append(self.word_count)
        if self.kind:
            kinds = [kind.strip() for kind in self.kind.split(",") if kind.strip()]
            kind_list.extend(kinds)
        return kind_list
