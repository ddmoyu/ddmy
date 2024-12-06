#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
书源之「目录、内容」工具类

Author: ddmoyu
Email: daydaymoyu@gmail.com
Date: 2024-12-04
"""

from typing import List

from src.views.novel.data_class.content import RuleContent, DataContent
from src.views.novel.data_class.toc import RuleToc, DataToc
from src.views.novel.utils.utils import parse_content_list, parse_content


def get_toc_list(html: str, rule: RuleToc) -> List[DataToc]:
    return parse_content_list(html, rule, DataToc)


def get_content(content: str, rule: RuleContent) -> DataContent:
    return parse_content(content, rule, DataContent)
