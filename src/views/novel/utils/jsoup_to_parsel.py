from parsel import Selector
from enum import Enum


class RuleType(Enum):
    JSOUP_Default = 1
    JSOUP_CSS = 2
    JSONPath = 3
    XPath = 4
    Javascript = 5
    RE_AllInOne = 6
    RE_OnlyOne = 7
    RE_Replace = 8
    Custom_symbol = 9


class RuleParser:
    def __init__(self, data):
        self.data = data
        self.data_type = "html"  # html, json, xml
        self.rule_type = RuleType.JSOUP_Default  # JSOUP_Default, JSOUP_CSS, JSONPath, XPath, Javascript, RE_AllInOne, RE_OnlyOne, RE_replace, Custom_symbol
        self.data_type = self.check_data_type(data)

    @staticmethod
    def check_data_type(data):
        if data.startswith("<!DOCTYPE html>"):
            return "html"
        elif data.startswith("{") or data.startswith("["):
            return "json"

    @staticmethod
    def check_rule_type(rule):
        if rule.startswith("@css"):
            return RuleType.JSOUP_CSS
        elif rule.startswith("@json") or rule.startswith("$."):
            return RuleType.JSONPath
        elif rule.startswith("@XPath") or rule.startswith("//"):
            return RuleType.XPath
        elif "@js" in rule or "<js>" in rule:
            return RuleType.Javascript
        elif rule.startswith(":"):
            return RuleType.RE_AllInOne
        elif rule.startswith("##") and rule.endswith("###"):
            return RuleType.RE_OnlyOne
        elif rule.startswith("##") and not rule.endswith("###"):
            return RuleType.RE_Replace
        elif rule in ["&&", "||", "%%"]:
            return RuleType.Custom_symbol
        else:
            return RuleType.JSOUP_Default

    def run(self, rule):
        pass


def parse_advanced_rule(rule, selector):
    parts = rule.split("@")
    current_selector = selector

    for part in parts:
        # 处理索引和切片
        if "[" in part and "]" in part:
            base_part = part.split("[")[0]
            index_part = part.split("[")[1].rstrip("]")

            # 处理基础选择器
            if base_part == "children":
                current_selector = current_selector.xpath("./*")
            elif base_part.startswith("."):
                current_selector = current_selector.css(base_part)
            elif base_part == "tag":
                current_selector = current_selector.css(index_part.split(".")[0])
            elif base_part == "class":
                current_selector = current_selector.css(f'.{index_part.split(".")[0]}')
            elif base_part == "text":
                current_selector = current_selector.xpath(
                    f'//*[contains(text(), "{index_part}")]'
                )

            # 处理索引和切片
            if ":" in index_part:
                # 切片处理
                start, end = map(lambda x: int(x) if x else None, index_part.split(":"))
                current_selector = current_selector[start:end]
            elif "!" in index_part:
                # 排除索引
                exclude_indices = list(map(int, index_part.split("!")[1].split(",")))
                current_selector = Selector(
                    root=[
                        el
                        for i, el in enumerate(current_selector.getall())
                        if i not in exclude_indices
                    ]
                )
            elif index_part.startswith("-"):
                # 负索引处理
                current_selector = current_selector[int(index_part) :]
            elif index_part.isdigit():
                # 正索引处理
                current_selector = current_selector[int(index_part)]

        # 处理属性和文本提取
        elif part in ["text", "textNodes", "ownText", "href", "src", "html", "all"]:
            if part == "text":
                return current_selector.css("::text").get()
            elif part == "textNodes":
                return current_selector.css("::text").getall()
            elif part == "ownText":
                return current_selector.xpath("text()").get()
            elif part in ["href", "src"]:
                return current_selector.attrib.get(part)
            elif part == "html":
                return current_selector.get()
            elif part == "all":
                return current_selector.getall()

        # 处理基础选择器
        elif part.startswith("class."):
            current_selector = current_selector.css(f'.{part.split(".")[1]}')
        elif part.startswith("tag."):
            current_selector = current_selector.css(part.split(".")[1])
        elif part.startswith("text."):
            current_selector = current_selector.xpath(
                f'//*[contains(text(), "{part.split(".")[1]}")]'
            )

    return current_selector.get()


def apply_advanced_rules(html, rule):
    selector = Selector(text=html)

    if "&&" in rule:
        sub_rules = rule.split("&&")
        result = " ".join(
            str(parse_advanced_rule(sub_rule, selector))
            for sub_rule in sub_rules
            if parse_advanced_rule(sub_rule, selector)
        )
    elif "||" in rule:
        sub_rules = rule.split("||")
        for sub_rule in sub_rules:
            result = parse_advanced_rule(sub_rule, selector)
            if result:
                break
        else:
            result = None
    else:
        result = parse_advanced_rule(rule, selector)
        print(result)

    # return result
