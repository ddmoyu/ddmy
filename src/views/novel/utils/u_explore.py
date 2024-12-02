#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
书源之「分类、发现」工具类

Author: ddmoyu
Email: daydaymoyu@gmail.com
Date: 2024-11-30
"""

import logging
from typing import Dict, Any
from src.views.novel.data.entities.explore_entity import ExploreEntity, CategoryEntity
from src.views.novel.utils.content_parse import ContentParser


def get_explore(source: Dict[str, Any]) -> ExploreEntity:
    if not isinstance(source, dict):
        logging.error("source 不是字典类型")
        raise TypeError("source 必须是字典类型")
    if not source.get("ruleExplore"):
        logging.error("source 字典中不包含 'ruleExplore' 键")
        raise ValueError("source 字典中必须包含 'ruleExplore' 键") 
    rule_explore = source.get("ruleExplore")
    explore = ExploreEntity.from_json(rule_explore)
    return explore


def get_category_list(html: str, rule: CategoryEntity) -> list[Dict[str, Any]]:
    if not html or not rule:
        logging.error("get_category_list html 或 rule 为空")
        return []
    if not rule.category_list or not rule.category_name or not rule.category_url:
        logging.error("get_category_list rule 规则不完整")
        return []

    category_list = []
    try:
        list_strategy = ContentParser(rule.category_list)
        category_list_html = list_strategy.parse(html, rule.category_list, "getall")

        for category_html in category_list_html:
            category_dict = {}

            name_strategy = ContentParser(rule.category_name)
            category_dict["name"] = name_strategy.parse(category_html, rule.category_name)

            url_strategy = ContentParser(rule.category_url)
            category_dict["url"] = url_strategy.parse(category_html, rule.category_url)

            category_list.append(category_dict)

    except Exception as e:
        logging.error(f"Error while parsing category list: {e}")

    return category_list
