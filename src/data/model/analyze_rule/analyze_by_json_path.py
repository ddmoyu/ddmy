import json


class AnalyzeByJsonPath:
    def __init__(self, json_data):
        if isinstance(json_data, str):
            self.data = json.loads(json_data)
        else:
            self.data = json_data

    def get_string(self, rule):
        if not rule:
            return None
        result = ""
        try:
            rule = self.replace_inner_rules(rule)
            value = self.ctx.find(rule)
            if value:
                if isinstance(value, list):
                    result = "\n".join([str(item.value) for item in value])
                else:
                    result = str(value[0].value)
        except Exception as e:
            print("error:", e)

        return result

    def get_string_list(self, rules):
        results = []
        for rule in rules:
            result = self.get_string(rule)
            if result:
                results.append(result)

        return results

    def replace_inner_rules(self, rule):
        result = []
        if not rule:
            return result
        try:
            rule = self.replace_inner_rules(rule)
            values = self.ctx.find(rule)
            if values:
                if isinstance(values, list):
                    for item in values:
                        result.append(str(item.value))
                else:
                    result.append(str(values[0].value))
        except Exception as e:
            print("error:", e)
        return result

    def get_list(self, rule):
        result = []
        if not rule:
            return result
        try:
            rule = self.replace_inner_rules(rule)
            values = self.ctx.find(rule)
            if values:
                if isinstance(values, list):
                    for item in values:
                        result.append(item.value)
        except Exception as e:
            print("error:", e)
        return result
