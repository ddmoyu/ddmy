#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
书源之「分类、发现」工具类

Author: ddmoyu
Email: daydaymoyu@gmail.com
Date: 2024-11-30
"""

from typing import List
from src.views.novel.data_class.category import RuleCategory, DataCategory
from src.views.novel.data_class.explore import RuleExplore, DataExplore
from src.views.novel.utils.utils import parse_content_list


def get_category_list(html: str, rule: RuleCategory) -> List[DataCategory]:
    return parse_content_list(html, rule, DataCategory)

def get_explore_list(html: str, rule: RuleExplore) -> List[DataExplore]:
    return parse_content_list(html, rule, DataExplore)