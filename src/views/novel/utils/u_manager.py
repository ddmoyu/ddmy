#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
书源之「管理」工具类

Author: ddmoyu
Email: daydaymoyu@gmail.com
Date: 2024-11-30
"""

import json
import logging
from src.common.tools import load_json, save_json
from src.common.request import fetch_json_async


def get_local_book_sources():
    return load_json("novel_sources.json")


def import_local_source(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as e:
                logging.error(f"Failed to decode JSON from {file_path}: {e}")
                return []
    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}. Error: {e}")
        return []
    except PermissionError as e:
        logging.error(f"Permission denied: {file_path}. Error: {e}")
        return []
    except IsADirectoryError as e:
        logging.error(f"Expected a file but found a directory: {file_path}. Error: {e}")
        return []
    except Exception as e:
        logging.error(f"An unexpected error occurred while reading {file_path}: {e}")
        return []


async def fetch_book_sources(url, save=False):
    resources = await fetch_json_async(url)
    if not resources:
        return []

    book_sources = get_local_book_sources()
    existing_urls = {source["bookSourceUrl"]: source for source in book_sources}
    for resource in resources:
        url = resource["bookSourceUrl"]
        if url not in existing_urls:
            existing_urls[url] = resource
    book_sources = list(existing_urls.values())

    if save:
        save_json(book_sources, "novel_sources.json")
    return book_sources


def merge_sources(sources):
    book_sources = get_book_sources()
    existing_urls = {source["bookSourceUrl"]: source for source in book_sources}
    for resource in sources:
        url = resource["bookSourceUrl"]
        if url not in existing_urls:
            existing_urls[url] = resource
    book_sources = list(existing_urls.values())
    save_json(book_sources, "novel_sources.json")
    return book_sources
