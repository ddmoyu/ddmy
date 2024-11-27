from parsel import Selector
from src.data.model.analyze_rule.analyze_rule import AnalyzeRule


class AnalyzeByXPath:
    def __init__(self, doc):
        self.selector = self.parse(doc)

    def parse(self, doc):
        if isinstance(doc, str):
            return Selector(text=doc)
        elif hasattr(doc, "xpath"):
            return doc
        else:
            raise ValueError("Unsupported document type")

    def get_result(self, xpath):
        return self.selector.xpath(xpath).getall()

    def get_elements(self, xpath):
        if not xpath:
            return None

        rule_analyzer = AnalyzeRule(xpath)
        rules = rule_analyzer.split_rule("&&", "||", "%%")

        if len(rules) == 1:
            return self.get_result(rules[0])
        else:
            results = []
            for rl in rules:
                temp = self.get_elements(rl)
                if temp:
                    results.append(temp)
                    if temp and rule_analyzer.elements_type == "||":
                        break

            if results:
                if "%%" == rule_analyzer.elements_type:
                    combined_results = []
                    for i in range(len(results[0])):
                        for temp in results:
                            if i < len(temp):
                                combined_results.append(temp[i])
                    return combined_results
                else:
                    return [item for sublist in results for item in sublist]
            return []

    def get_string_list(self, xpath):
        rule_analyzer = AnalyzeRule(xpath)
        rules = rule_analyzer.split_rule("&&", "||", "%%")

        if len(rules) == 1:
            return self.get_result(xpath)
        else:
            results = []
            for rl in rules:
                temp = self.get_string_list(rl)
                if temp:
                    results.append(temp)
                    if temp and rule_analyzer.elements_type == "||":
                        break

            if results:
                if "%%" == rule_analyzer.elements_type:
                    combined_results = []
                    for i in range(len(results[0])):
                        for temp in results:
                            if i < len(temp):
                                combined_results.append(temp[i])
                    return combined_results
                else:
                    return [item for sublist in results for item in sublist]
            return []

    def get_string(self, rule):
        rule_analyzer = AnalyzeRule(rule)
        rules = rule_analyzer.split_rule("&&", "||")

        if len(rules) == 1:
            result = self.get_result(rule)
            return "\n".join(result) if result else None
        else:
            text_list = []
            for rl in rules:
                temp = self.get_string(rl)
                if temp:
                    text_list.append(temp)
                    if rule_analyzer.elements_type == "||":
                        break
            return "\n".join(text_list)
