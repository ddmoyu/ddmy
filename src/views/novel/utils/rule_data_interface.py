class RuleDataInterface:
    def __init__(self):
        self.variable_map = {}

    def put_variable(self, key: str, value: str) -> bool:
        if value is None:
            del self.variable_map[key]
            return True
        if len(value) < 10000:
            self.variable_map[key] = value
            return True
        else:
            self.put_big_variable(key, value)
            return False

    def put_big_variable(self, key: str, value: str):
        pass

    def get_variable(self, key: str) -> str:
        return self.variable_map.get(key, self.get_big_variable(key) or "")

    def get_big_variable(self, key: str) -> str:
        pass
