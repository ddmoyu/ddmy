#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
书源之「目录、内容」工具类

Author: ddmoyu
Email: daydaymoyu@gmail.com
Date: 2024-12-04
"""

from typing import List
from parsel import Selector
from src.views.novel.data_class.toc import RuleToc
from src.views.novel.utils.utils import parse_content_list


def parse_content(content, rule):
    if "@" not in rule:
        raise Exception("rule must be a valid xpath or css selector")
    selector_query, query_type = rule.split("@")
    selector = Selector(text=content)
    if query_type == "html":
        result = selector.css(selector_query).get()
    elif query_type == "text":
        result = selector.css(selector_query).xpath("string(.)").get()
    else:
        raise Exception("unknown query type")
    return result


def get_toc_list(html: str, rule: RuleToc) -> List[RuleToc]:
    return parse_content_list(html, rule, RuleToc)
