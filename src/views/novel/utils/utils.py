import json
import re
from parsel import Selector

from src.common.tools import save_json, load_json
from src.common.request import fetch_json_async

def clean_value(value):
    if isinstance(value, str):
        return re.sub(r'#.*', '', value).strip()
    return value

def clean_hash_value(data):
    if isinstance(data, dict):
        return {key: clean_hash_value(data[key]) for key, value in data.items()}
    elif isinstance(data, list):
        return [clean_hash_value(item) for item in data]
    else:
        return clean_value(data)

def parse_content(content, rule):
    if '@' not in rule:
        raise Exception('rule must be a valid xpath or css selector')
    selector_query, query_type = rule.split('@')
    selector = Selector(text=content)
    if query_type == 'html':
        result = selector.css(selector_query).get()
    elif query_type == 'text':
        result = selector.css(selector_query).xpath('string(.)').get()
    else:
        raise Exception('unknown query type')
    return result

def filter_book_source_type(json_data, _type=0):
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data
    filtered_data = [item for item in data if item.get('bookSourceType') == _type]
    return filtered_data

def filter_rule_content(json_data):
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data
    filtered_data = [
        item for item in data
        if 'ruleContent' in item
           and item['ruleContent']
           and 'content' in item['ruleContent']
           and item['ruleContent']['content']
    ]
    return filtered_data

def get_book_sources():
    return load_json("novel_sources.json")

async def fetch_book_sources(url, save=False):
    res = await fetch_json_async(url)
    if not res:
        return []
    resources = filter_book_source_type(res, 0)
    if not resources:
        return []
    resources = filter_rule_content(resources)
    if not resources:
        return []
    resources = clean_hash_value(resources)
    if not resources:
        return []
    book_sources = get_book_sources() or []

    existing_urls = {source["bookSourceUrl"]: source for source in book_sources}
    for resource in resources:
        url = resource["bookSourceUrl"]
        if url not in existing_urls:
            existing_urls[url] = resource
    book_sources = list(existing_urls.values())

    if save:
        save_json(book_sources, "novel_sources.json")
    return book_sources


