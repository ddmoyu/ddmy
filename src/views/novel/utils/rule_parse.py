from typing import Dict, Any, Callable
from parsel import Selector
import logging


class BaseCategoryParseStrategy:
    @staticmethod
    def parse(selector, rule: str, method: str = "get") -> Any:
        """
        基础解析策略

        :param selector: Scrapy选择器
        :param rule: 解析规则
        :param method: 提取方法（'get'或'getall'）
        :return: 解析结果
        """
        raise NotImplementedError("子类必须实现具体解析逻辑")


class CSSParseStrategy(BaseCategoryParseStrategy):
    @staticmethod
    def parse(selector, rule: str, method: str = "get") -> Any:
        """
        CSS选择器解析策略
        """
        css_rule = rule.replace("@css:", "").replace("@CSS:", "")
        method_map = {
            "get": selector.css(css_rule).get,
            "getall": selector.css(css_rule).getall,
        }
        return method_map.get(method, selector.css(css_rule).get)()


class XPathParseStrategy(BaseCategoryParseStrategy):
    @staticmethod
    def parse(selector, rule: str, method: str = "get") -> Any:
        """
        XPath解析策略
        """
        xpath_rule = rule.replace("@xpath:", "").replace("@XPATH:", "")
        method_map = {
            "get": selector.xpath(xpath_rule).get,
            "getall": selector.xpath(xpath_rule).getall,
        }
        return method_map.get(method, selector.xpath(xpath_rule).get)()


class JSONParseStrategy(BaseCategoryParseStrategy):
    @staticmethod
    def parse(selector, rule: str, method: str = "get") -> Any:
        """
        JSON解析策略
        """
        # TODO: 实现JSON解析逻辑
        raise NotImplementedError("JSON解析策略尚未实现")


class JSParseStrategy(BaseCategoryParseStrategy):
    @staticmethod
    def parse(selector, rule: str, method: str = "get") -> Any:
        """
        JS解析策略
        """
        # TODO: 实现JS解析逻辑
        raise NotImplementedError("JS解析策略尚未实现")


class CategoryParser:
    _strategy_map = {
        "@css": CSSParseStrategy,
        "@CSS": CSSParseStrategy,
        "@xpath": XPathParseStrategy,
        "@XPATH": XPathParseStrategy,
        "@json": JSONParseStrategy,
        "@js": JSParseStrategy,
    }

    @classmethod
    def get_strategy(cls, rule: str) -> BaseCategoryParseStrategy:
        """
        根据规则获取对应的解析策略
        """
        for prefix, strategy in cls._strategy_map.items():
            if rule.startswith(prefix):
                return strategy
        raise ValueError(f"未找到匹配的解析策略：{rule}")


def get_category_list(html: str, rule) -> list[Dict[str, Any]]:
    """
    使用策略模式解析类别列表

    :param html: HTML内容
    :param rule: 解析规则实体
    :return: 类别列表
    """
    if not html or not rule:
        logging.error("category html 或 rule 为空")
        return []

    required_attrs = ["category_list", "category_name", "category_url"]
    if not all(hasattr(rule, attr) for attr in required_attrs):
        logging.error("rule 规则不完整")
        return []

    selector = Selector(html)
    category_list = []

    try:
        # 解析类别列表
        list_strategy = CategoryParser.get_strategy(rule.category_list)
        category_list_html = list_strategy.parse(selector, rule.category_list, "getall")

        for category_html in category_list_html:
            category_dict = {}
            category_selector = Selector(text=category_html)

            # 解析类别名称
            name_strategy = CategoryParser.get_strategy(rule.category_name)
            category_dict["name"] = name_strategy.parse(
                category_selector, rule.category_name
            )

            # 解析类别URL
            url_strategy = CategoryParser.get_strategy(rule.category_url)
            category_dict["url"] = url_strategy.parse(
                category_selector, rule.category_url
            )

            category_list.append(category_dict)

    except Exception as e:
        logging.error(f"解析类别列表时发生错误：{e}")
        return []

    return category_list
