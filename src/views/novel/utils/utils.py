import logging
from dataclasses import asdict
from typing import Any, Optional, Tuple, List, Type, TypeVar
from src.views.novel.utils.content_parse import ContentParser


def find_list_rule(rule: Any) -> Tuple[Optional[str], Optional[str]]:
    """
    查找规则中包含 'list' 的键
    Args:
        rule: 规则对象
    Returns:
        Tuple[str, str]: (list_key, list_value) 或 (None, None)
    """
    if not rule:
        return None, None

    rule_dict = vars(rule) if not isinstance(rule, dict) else rule
    for key, value in rule_dict.items():
        if "list" in key.lower():
            return key, value

    return None, None


def clean_and_get_last_text(texts):
    cleaned_texts = [text.strip() for text in texts if text.strip()]
    return cleaned_texts[-1] if cleaned_texts else ""


T = TypeVar("T")
R = TypeVar("R")


def parse_content_list(content: str, rule: R, model: Type[T]) -> Optional[List[T]]:
    """
    解析列表内容

    Args:
        content: HTML内容
        rule: 解析规则（BaseRule的子类实例）
        model: BaseData的子类

    Returns:
        Optional[List[T]]: 解析结果列表，解析失败返回None
    """
    if not content or not rule:
        logging.error("parse_content_list: 内容或规则为空")
        return None

    result_list = []
    try:
        # 查找列表规则
        list_key, list_value = find_list_rule(rule)
        if not list_key or not list_value:
            logging.error("parse_content_list: 未找到列表规则")
            return None

        # 解析列表项
        list_strategy = ContentParser(list_value)
        item_list = list_strategy.parse(content, list_value, "getall")
        if not item_list:
            logging.warning("parse_content_list: 未解析到列表项")
            return None

        # 获取规则字典
        rule_dict = asdict(rule)

        # 遍历解析每个列表项
        for item_content in item_list:
            try:
                # 创建数据对象
                item_data = model()
                parsed_any_field = False

                # 解析每个字段
                for field_name, field_rule in rule_dict.items():
                    # 跳过列表规则和空规则
                    if (
                        field_name == list_key
                        or not field_rule
                        or not field_rule.startswith("@")
                    ):
                        continue

                    try:
                        if field_name == "prev_url" or field_name == "next_url":
                            strategy = ContentParser(field_rule)
                            value = strategy.parse(content, field_rule)
                        else:
                            strategy = ContentParser(field_rule)
                            value = strategy.parse(item_content, field_rule)
                            if value is not None:
                                value = value.strip()

                            if value is None:
                                value = strategy.parse(
                                    item_content, field_rule, "getall"
                                )
                                value = clean_and_get_last_text(value)

                        # 只在成功解析到值时设置属性
                        if value is not None and value != "":
                            setattr(item_data, field_name, value)
                            parsed_any_field = True

                    except Exception as e:
                        logging.warning(f"解析字段 {field_name} 失败: {str(e)}")
                        continue

                # 只有成功解析了至少一个字段才添加到结果列表
                if parsed_any_field:
                    result_list.append(item_data)

            except Exception as e:
                logging.warning(f"解析列表项失败: {str(e)}")
                continue

    except Exception as e:
        logging.error(f"解析列表内容失败: {str(e)}")
        return None

    # 只在成功解析到数据时返回结果
    return result_list if result_list else None


def parse_content(content: str, rule: R, model: Type[T]) -> Optional[T]:
    """
    解析内容

    Args:
        content: 内容
        rule: 解析规则（BaseRule的子类实例）
        model: BaseData的子类

    Returns:
        Optional[T]: 解析结果，解析失败返回None
    """
    if not content or not rule:
        logging.error("parse_content_list: 内容或规则为空")
        return None

    try:
        data = model()
        for field_name, field_rule in asdict(rule).items():
            if not field_rule or not field_rule.startswith("@"):
                continue

            strategy = ContentParser(field_rule)
            value = strategy.parse(content, field_rule)
            if value is not None:
                setattr(data, field_name, value)
        return data

    except Exception as e:
        logging.error(f"解析内容失败: {str(e)}")
        return
