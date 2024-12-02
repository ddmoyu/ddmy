import json
import logging
from typing import Any, Type
from parsel import Selector
from jsonpath_ng import parse as jsonpath_parse

# Base class for parsing strategies
class BaseParseStrategy:
    @staticmethod
    def parse(content: str, rule: str, method: str = "get") -> Any:
        """
        Base method to parse content with a given rule.
        This method should be overridden by subclasses.

        :param content: The content to parse (HTML, JSON, etc.)
        :param rule: The parsing rule (CSS, JSONPath, etc.)
        :param method: The method to extract ('get' or 'getall')
        :return: Parsed result
        """
        raise NotImplementedError("Subclasses must implement the parse method")

# CSS Parsing strategy
class CSSParseStrategy(BaseParseStrategy):
    @staticmethod
    def parse(content: str, rule: str, method: str = "get") -> Any:
        """
        CSS Selector parsing strategy
        """
        try:
            selector = Selector(text=content)
            css_rule = rule.replace("@css", "").replace("@CSS", "")
            method_map = {
                "get": selector.css(css_rule).get,
                "getall": selector.css(css_rule).getall,
            }
            result = method_map.get(method, selector.css(css_rule).get)()
            return result if result else None
        except Exception as e:
            logging.error(f"Error while parsing CSS: {e} with rule: {rule}")
            return None

# JMESPath parsing strategy
class JMESPathParseStrategy(BaseParseStrategy):
    @staticmethod
    def parse(content: str, rule: str, method: str = "get") -> Any:
        """
        JMESPath parsing strategy
        """
        try:
            selector = Selector(text=content)
            jmespath_rule = rule.replace("@jmespath", "").replace("@JMESPath", "")
            method_map = {
                "get": selector.jmespath(jmespath_rule).get,
                "getall": selector.jmespath(jmespath_rule).getall,
            }
            result = method_map.get(method, selector.jmespath(jmespath_rule).get)()
            return result if result else None
        except Exception as e:
            logging.error(f"Error while parsing JMESPath: {e} with rule: {rule}")
            return None

# JSON parsing strategy using JSONPath
class JSONParseStrategy(BaseParseStrategy):
    @staticmethod
    def parse(content: dict, rule: str, method: str = "get") -> Any:
        """
        JSON parsing strategy using jsonpath-ng
        """
        try:
            # Clean rule
            json_rule = rule.replace("@json", "").replace("@JSON", "")

            # Parse the content if it's a string
            if isinstance(content, str):
                content = json.loads(content)

            jsonpath_expr = jsonpath_parse(json_rule)
            matches = [match.value for match in jsonpath_expr.find(content)]

            if method == "get":
                return matches[0] if matches else None
            elif method == "getall":
                return matches
            return None
        except json.JSONDecodeError as e:
            logging.error(f"JSON decode error: {e} for rule: {rule}")
        except Exception as e:
            logging.error(f"Error while parsing JSONPath: {e} for rule: {rule}")
        return None

# JS parsing strategy (currently not implemented)
class JSParseStrategy(BaseParseStrategy):
    @staticmethod
    def parse(content: str, rule: str, method: str = "get") -> Any:
        """
        JS parsing strategy
        """
        logging.warning(f"JS parsing strategy not implemented for rule: {rule}")
        return None

# XPath parsing strategy
class XPathParseStrategy(BaseParseStrategy):
    @staticmethod
    def parse(content: str, rule: str, method: str = "get") -> Any:
        """
        XPath parsing strategy
        """
        try:
            selector = Selector(text=content)
            xpath_rule = rule.replace("@xpath", "").replace("@XPATH", "")
            method_map = {
                "get": selector.xpath(xpath_rule).get,
                "getall": selector.xpath(xpath_rule).getall,
            }
            result = method_map.get(method, selector.xpath(xpath_rule).get)()
            return result if result else None
        except Exception as e:
            logging.error(f"Error while parsing XPath: {e} with rule: {rule}")
            return None

# ContentParser class using strategy pattern
class ContentParser:
    _strategy_map = {
        "@css": CSSParseStrategy,
        "@CSS": CSSParseStrategy,
        "@jmespath": JMESPathParseStrategy,
        "@JMESPath": JMESPathParseStrategy,
        "@js": JSParseStrategy,
        "@JS": JSParseStrategy,
        "@javascript": JSParseStrategy,
        "@Javascript": JSParseStrategy,
        "@json": JSONParseStrategy,
        "@JSON": JSONParseStrategy,
        "@xpath": XPathParseStrategy,
        "@XPATH": XPathParseStrategy,
    }

    def __init__(self, rule: str):
        """
        Initialize the parser with the rule prefix, and select the appropriate strategy.
        """
        self.strategy = self._get_strategy(rule)
        if not self.strategy:
            logging.error(f"Unsupported parsing rule: {rule}")
            raise ValueError(f"Unsupported parsing rule: {rule}")

    def _get_strategy(self, rule: str) -> Type[BaseParseStrategy] | None:
        """
        Get the parsing strategy based on the rule prefix.
        """
        for prefix, strategy in self._strategy_map.items():
            if rule.startswith(prefix):
                return strategy
        return None

    def parse(self, content: str, rule: str, method: str = "get") -> Any:
        """
        Delegate the parsing task to the selected strategy.
        """
        try:
            return self.strategy.parse(content, rule, method)
        except Exception as e:
            logging.error(f"Error occurred while parsing with rule: {rule}. Error: {e}")
            return None