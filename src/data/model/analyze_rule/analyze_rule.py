import re
import json
from enum import Enum
from typing import Dict, Any, Optional
from urllib.parse import urlparse
from src.data.model.analyze_rule.analyze_by_json_path import AnalyzeByJsonPath
from src.data.entities.base_book import BaseBook


class Mode(Enum):
    XPATH = "xpath"
    JSON = "json"
    DEFAULT = "default"
    JS = "js"
    REGEX = "regex"


class SourceRule:
    def __init__(self, rule_str, mode=Mode.Default):
        self.rule = rule_str
        self.mode = mode
        self.replace_regex = ""
        self.replacement = ""
        self.replace_first = False
        self.put_map = {}
        self.rule_param = []
        self.rule_type = []
        self.get_rule_type = -2
        self.js_rule_type = -1
        self.default_rule_type = 0

        self.rule = self.parse_rule(rule_str)
        self.rule = self.split_put_rule(self.rule, self.put_map)
        self.parse_eval_pattern(self.rule)

    def parse_rule(self, rule_str):
        if self.mode == Mode.Js or self.mode == Mode.Regex:
            return rule_str
        if rule_str.startswith("@CSS:"):
            self.mode = Mode.Default
            return rule_str
        if rule_str.startswith("@@"):
            self.mode = Mode.Default
            return rule_str[2:]
        if rule_str.startswith("@XPath:"):
            self.mode = Mode.XPath
            return rule_str[7:]
        if rule_str.startswith("@Json:"):
            self.mode = Mode.Json
            return rule_str[6:]
        if self.is_json or rule_str.startswith("$.") or rule_str.startswith("$["):
            self.mode = Mode.Json
            return rule_str
        if rule_str.startswith("/"):
            self.mode = Mode.XPath
            return rule_str
        return rule_str

    def split_put_rule(self, rule_str, put_map):
        v_rule_str = rule_str
        put_matcher = re.compile(r"@put:(\{[^}]+?\})", re.IGNORECASE)
        while True:
            match = put_matcher.search(v_rule_str)
            if not match:
                break
            v_rule_str = v_rule_str.replace(match.group(), "")
            put_map.update(json.loads(match.group(1)))
        return v_rule_str

    def parse_eval_pattern(self, rule_str):
        start = 0
        eval_pattern = re.compile(r"@get:\{[^}]+?\}|\{\{[\w\W]*?\}\}", re.IGNORECASE)
        for match in eval_pattern.finditer(rule_str):
            if match.start() > start:
                tmp = rule_str[start : match.start()]
                self.split_regex(tmp)
            tmp = match.group()
            if tmp.startswith("@get:"):
                self.rule_type.append(self.get_rule_type)
                self.rule_param.append(tmp[6:-1])
            elif tmp.startswith("{{"):
                self.rule_type.append(self.js_rule_type)
                self.rule_param.append(tmp[2:-2])
            else:
                self.split_regex(tmp)
            start = match.end()
        if start < len(rule_str):
            tmp = rule_str[start:]
            self.split_regex(tmp)

    def split_regex(self, rule_str):
        start = 0
        regex_pattern = re.compile(r"\$\d{1,2}")
        for match in regex_pattern.finditer(rule_str):
            if match.start() > start:
                tmp = rule_str[start : match.start()]
                self.rule_type.append(self.default_rule_type)
                self.rule_param.append(tmp)
            tmp = match.group()
            self.rule_type.append(int(tmp[1:]))
            self.rule_param.append(tmp)
            start = match.end()
        if start < len(rule_str):
            tmp = rule_str[start:]
            self.rule_type.append(self.default_rule_type)
            self.rule_param.append(tmp)

    def make_up_rule(self, result):
        info_val = []
        if self.rule_param:
            for index in reversed(range(len(self.rule_param))):
                reg_type = self.rule_type[index]
                if reg_type > self.default_rule_type:
                    if isinstance(result, list) and len(result) > reg_type:
                        info_val.insert(0, result[reg_type])
                    else:
                        info_val.insert(0, self.rule_param[index])
                elif reg_type == self.js_rule_type:
                    if self.is_rule(self.rule_param[index]):
                        info_val.insert(0, self.get_string([self]))
                    else:
                        js_eval = self.eval_js(self.rule_param[index], result)
                        if js_eval is not None:
                            info_val.insert(0, str(js_eval))
                elif reg_type == self.get_rule_type:
                    info_val.insert(0, self.get(self.rule_param[index]))
                else:
                    info_val.insert(0, self.rule_param[index])
            self.rule = "".join(info_val)
        rule_str_s = self.rule.split("##")
        self.rule = rule_str_s[0].strip()
        if len(rule_str_s) > 1:
            self.replace_regex = rule_str_s[1]
        if len(rule_str_s) > 2:
            self.replacement = rule_str_s[2]
        if len(rule_str_s) > 3:
            self.replace_first = True

    def is_rule(self, rule_str):
        return (
            rule_str.startswith("@")
            or rule_str.startswith("$.")
            or rule_str.startswith("$[")
            or rule_str.startswith("//")
        )

    def get_param_size(self):
        return len(self.rule_param)


class AnalyzeRule:
    def __init__(self, rule_data=None, source=None):
        self.rule_data = rule_data
        self.source = source

        self.book = rule_data if isinstance(rule_data, BaseBook) else None

        self.chapter = None
        self.next_chapter_url = None
        self.content = None
        self.base_url = None
        self.redirect_url = None

        self.is_json = False
        self.is_regex = False

        self.analyze_by_xpath = None
        self.analyze_by_jsoup = None
        self.analyze_by_jsonpath = None

        self.string_rule_cache: Dict[str, str] = {}
        self.coroutine_context = None

    def set_content(self, content: Any, base_url: None):
        if content is None:
            return None

        self.content = content
        self.is_json = isinstance(content, (dict, list))

        self.set_base_url(base_url)
        self.analyze_by_xpath = None
        self.analyze_by_jsoup = None
        self.analyze_by_jsonpath = None
        return self

    def set_coroutine_content(self, context):
        self.coroutine_context = context
        return self

    def set_base_url(self, base_url: Optional[str]):
        if base_url:
            self.base_url = base_url
        return self

    def set_redirect_url(self, url: str):
        try:
            self.redirect_url = urlparse(url)
        except Exception as e:
            print("Error parsing URL:", e)
        return self.redirect_url

    def get_analyze_by_xpath(self, obj: Any):
        if obj != self.content:
            return AnalyzeByXPath(obj)
        if self.analyze_by_xpath is None:
            self.analyze_by_xpath = AnalyzeByXPath(self.content)
        return self.analyze_by_xpath

    def get_analyze_by_jsoup(self, obj: Any):
        if obj != self.content:
            return AnalyzeByJSoup(obj)
        if self.analyze_by_jsoup is None:
            self.analyze_by_jsoup = AnalyzeByJSoup(self.content)
        return self.analyze_by_jsoup

    def get_analyze_by_jsonpath(self, obj: Any):
        if obj != self.content:
            return AnalyzeByJsonPath(obj)
        if self.analyze_by_jsonpath is None:
            self.analyze_by_jsonpath = AnalyzeByJsonPath(self.content)
        return self.analyze_by_jsonpath

    def get_string_list(self, rule, content, is_url: False):
        if not rule:
            return None
        rule_list = self.split_source_rule_cache_string(rule)
        return self.get_string_list_from_rule_list(rule_list, content, is_url)

    def get_string_list_from_rule_list(self, rule_list, content, is_url=False):
        result = content or self.content
        if result and rule_list:
            for source_rule in rule_list:
                pass
        ## Todo

    def apply_rule(self, source_rule, result):
        if source_rule.rule:
            if source_rule.mode == Mode.JS:
                result = self.eval_js(source_rule.rule, result)
            if source_rule.mode == Mode.JSON:
                result = self.get_analyze_by_json_path(result).get_string_list(
                    source_rule.rule
                )
            elif source_rule.mode == Mode.XPATH:
                result = self.get_analyze_by_xpath(result).get_string_list(
                    source_rule.rule
                )
            else:
                result = self.get_analyze_by_jsoup(result).get_string_list(
                    source_rule.rule
                )
        if source_rule.replace_regex and isinstance(result, list):
            result = [self.replace_regex(item, source_rule) for item in result]
        elif source_rule.replace_regex:
            result = self.replace_regex(result, source_rule)
        return result

    def get_analyze_by_xpath(self, content):
        return AnalyzeByXPath(content)

    def get_analyze_by_jsoup(self, content):
        return AnalyzeByJSoup(content)

    def get_analyze_by_json_path(self, content):
        return AnalyzeByJsonPath(content)

    def put_rule(self, map):
        for key, value in map.items():
            self.put(key, self.get_string(value))

    def split_put_rule(self, rule_str, put_map):
        v_rule_str = rule_str
        put_matcher = re.compile(r"@put:(\{[^}]+?\})", re.IGNORECASE)
        while True:
            match = put_matcher.search(v_rule_str)
            if not match:
                break
            v_rule_str = v_rule_str.replace(match.group(), "")
            put_map.update(json.loads(match.group(1)))
        return v_rule_str

    def replace_regex(self, result, rule):
        if not rule.replace_regex:
            return result
        if rule.replace_first:
            pattern = re.compile(rule.replace_regex)
            match = pattern.search(result)
            if match:
                return match.group(0).replace(rule.replace_regex, rule.replacement, 1)
            return ""
        else:
            return result.replace(rule.replace_regex, rule.replacement)

    def split_source_rule_cache_string(self, rule_str):
        if not rule_str:
            return []
        return self.string_rule_cache.setdefault(
            rule_str, self.split_source_rule(rule_str)
        )

    def split_source_rule(self, rule_str, all_in_one=False):
        if not rule_str:
            return []
        rule_list = []
        m_mode = Mode.Default
        start = 0
        if all_in_one and rule_str.startswith(":"):
            m_mode = Mode.Regex
            self.is_regex = True
            start = 1
        elif self.is_regex:
            m_mode = Mode.Regex

        js_pattern = re.compile(r"<js>(.*?)</js>", re.IGNORECASE)
        for match in js_pattern.finditer(rule_str):
            if match.start() > start:
                tmp = rule_str[start : match.start()].strip()
                if tmp:
                    rule_list.append(SourceRule(tmp, m_mode))
            rule_list.append(SourceRule(match.group(1), Mode.Js))
            start = match.end()

        if start < len(rule_str):
            tmp = rule_str[start:].strip()
            if tmp:
                rule_list.append(SourceRule(tmp, m_mode))

        return rule_list

    def get_string(self, rule_str, m_content=None, is_url=False):
        if not rule_str:
            return ""
        rule_list = self.split_source_rule_cache_string(rule_str)
        return self.get_string_from_rule_list(rule_list, m_content, is_url)

    def get_string_from_rule_list(
        self, rule_list, m_content=None, is_url=False, unescape=True
    ):
        result = None
        content = m_content if m_content is not None else self.content
        if content and rule_list:
            result = content
            for source_rule in rule_list:
                self.put_rule(source_rule.put_map)
                source_rule.make_up_rule(result)
                result = self.apply_rule(source_rule, result)
        if result is None:
            result = ""
        result_str = str(result)
        if unescape and "&" in result_str:
            result_str = html.unescape(result_str)
        if is_url:
            return (
                self.base_url
                if not result_str
                else urljoin(self.redirect_url, result_str)
            )
        return result_str

    def get_element(self, rule_str):
        if not rule_str:
            return None
        result = None
        content = self.content
        rule_list = self.split_source_rule(rule_str, True)
        if content and rule_list:
            result = content
            for source_rule in rule_list:
                self.put_rule(source_rule.put_map)
                source_rule.make_up_rule(result)
                result = self.apply_rule(source_rule, result)
        return result

    def get_elements(self, rule_str):
        result = None
        content = self.content
        rule_list = self.split_source_rule(rule_str, True)
        if content and rule_list:
            result = content
            for source_rule in rule_list:
                self.put_rule(source_rule.put_map)
                result = self.apply_rule(source_rule, result)
        return result if isinstance(result, list) else []

    def put(self, key, value):
        if self.chapter:
            self.chapter.put_variable(key, value)
        elif self.book:
            self.book.put_variable(key, value)
        elif self.rule_data:
            self.rule_data.put_variable(key, value)
        elif self.source:
            self.source.put(key, value)
        return value

    def get(self, key):
        if key == "bookName" and self.book:
            return self.book.name
        if key == "title" and self.chapter:
            return self.chapter.title
        return (
            self.chapter.get_variable(key)
            if self.chapter
            else self.book.get_variable(key)
            if self.book
            else self.rule_data.get_variable(key)
            if self.rule_data
            else self.source.get(key)
            if self.source
            else ""
        )

    def eval_js(self, js_str, result=None):
        # Implement JS evaluation using a JavaScript engine like PyExecJS
        pass
        # Todo

    def ajax(self, url):
        pass
        # TODO
        # url_str = url if isinstance(url, str) else url[0]
        # response = requests.get(url_str)
        # return response.text

    def re_get_book(self):
        # Implement book retrieval logic
        pass

    def refresh_book(self):
        # Implement book refresh logic
        pass

    def refresh_toc_url(self):
        # Implement TOC URL refresh logic
        pass
