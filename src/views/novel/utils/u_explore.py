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
from parsel import Selector
from src.views.novel.data.entities.explore_entity import ExploreEntity, CategoryEntity


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
        logging.error("category html 或 rule 为空")
        return []
    if not rule.category_list or not rule.category_name or not rule.category_url:
        logging.error("rule 规则不完整")
        return []

    # 保存原始规则字符串
    original_category_list = rule.category_list
    original_category_name = rule.category_name
    original_category_url = rule.category_url

    selector = Selector(html)
    category_list = []
    category_list_html = []

    # 处理列表规则
    if original_category_list.startswith("@css") or original_category_list.startswith(
        "@CSS"
    ):
        css_rule = original_category_list.replace("@css:", "").replace("@CSS:", "")
        category_list_html = selector.css(css_rule).getall()
    elif original_category_list.startswith(
        "@xpath"
    ) or original_category_list.startswith("@XPATH"):
        xpath_rule = original_category_list.replace("@xpath:", "").replace(
            "@XPATH:", ""
        )
        category_list_html = selector.xpath(xpath_rule).getall()

    for category_html in category_list_html:
        category_dict = {}
        category_selector = Selector(text=category_html)

        # 处理名称规则
        if original_category_name.startswith(
            "@css"
        ) or original_category_name.startswith("@CSS"):
            css_rule = original_category_name.replace("@css:", "").replace("@CSS:", "")
            category_dict["name"] = category_selector.css(css_rule).get()
        elif original_category_name.startswith(
            "@xpath"
        ) or original_category_name.startswith("@XPATH"):
            xpath_rule = original_category_name.replace("@xpath:", "").replace(
                "@XPATH:", ""
            )
            category_dict["name"] = category_selector.xpath(xpath_rule).get()

        # 处理URL规则
        if original_category_url.startswith("@css") or original_category_url.startswith(
            "@CSS"
        ):
            css_rule = original_category_url.replace("@css:", "").replace("@CSS:", "")
            category_dict["url"] = category_selector.css(css_rule).get()
        elif original_category_url.startswith(
            "@xpath"
        ) or original_category_url.startswith("@XPATH"):
            xpath_rule = original_category_url.replace("@xpath:", "").replace(
                "@XPATH:", ""
            )
            category_dict["url"] = category_selector.xpath(xpath_rule).get()

        category_list.append(category_dict)

    return category_list
