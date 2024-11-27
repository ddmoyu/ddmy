from typing import Optional


class RuleDataInterface:
    def __init__(self):
        self.variable_map = {}

    def put_variable(self, key, value: Optional[str]):
        if value is None:
            self.variable_map.pop(key, None)
        else:
            self.variable_map[key] = value
        return True

    def get_variable(self, key):
        return self.variable_map[key]
