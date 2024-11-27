import json


class RuleDataInterface:
    def __init__(self):
        self.variable_map = {}

    def put_variable(self, key: str, value: str):
        if value is None:
            del self.variable_map[key]
        else:
            self.variable_map[key] = value

    @property
    def data(self):
        return json.loads(self.rule_data)
