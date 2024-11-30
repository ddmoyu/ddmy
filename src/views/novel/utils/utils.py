import re
import json
import httpx
from parsel import Selector
from urllib.parse import urljoin
from src.views.novel.utils.jsoup_to_parsel import apply_advanced_rules

from src.common.tools import save_json, load_json
from src.common.request import fetch_json_async


def clean_value(value):
    if isinstance(value, str):
        return re.sub(r"#.*", "", value).strip()
    return value


def clean_hash_value(data):
    if isinstance(data, dict):
        return {key: clean_hash_value(data[key]) for key, value in data.items()}
    elif isinstance(data, list):
        return [clean_hash_value(item) for item in data]
    else:
        return clean_value(data)


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


def filter_book_source_type(json_data, _type=0):
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data
    filtered_data = [item for item in data if item.get("bookSourceType") == _type]
    return filtered_data


def filter_rule_content(json_data):
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data
    filtered_data = [
        item
        for item in data
        if "ruleContent" in item
        and item["ruleContent"]
        and "content" in item["ruleContent"]
        and item["ruleContent"]["content"]
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


def check_rule_type(rule):
    if rule.startswith("@css"):
        return "Css"
    elif rule.startswith("@json") or rule.startswith("$."):
        return "JsonPath"
    elif rule.startswith("@xpath") or rule.startswith("//"):
        return "Xpath"
    elif rule.startswith("<js>") or rule.startswith("@js"):
        return "Javascript"
    else:
        return "css"


async def fetch_search(url: str, source_url: str, keyword: str):
    if url.startswith("@js:") or url.startswith("{{"):
        return []

    if not url.startswith("http"):
        if source_url is not None:
            source_url = re.sub(r"##.*", "", source_url)
            url = urljoin(source_url, url)
        else:
            return []

    url = url.replace("{{key}}", keyword)
    url = url.replace("{{page}}", "1")

    if "," in url:
        url, json_config = url.split(",", 1)
        config = json.loads(json_config)
    else:
        config = {}

    headers = {}
    method = config.get("method", "GET")
    charset = config.get("charset", "utf-8")
    body = config.get("body", None)

    if body:
        if keyword in body:
            body = body.replace(keyword, keyword)
        body = body.encode(charset)

    if "headers" in config:
        headers.update(config["headers"])

    print(f"fetching {url}")
    async with httpx.AsyncClient(
        timeout=httpx.Timeout(10.0, connect=10.0), follow_redirects=True
    ) as client:
        if method == "POST":
            response = await client.post(url, headers=headers, content=body)
        else:
            response = await client.get(url, headers=headers)

        print(response.text)
        return response.text


async def fetch_search_test():
    item = await fetch_search(
        "https://www.zhuishushenqi.com/search?val={{key}}",
        "",
        "盘龙",
    )
    print(item)
    book_list = apply_advanced_rules(item, "class.book.all")
    print(book_list)
    # if not book_list:
    #     return []
    #
    # results = []
    # for book in book_list:
    #     book_info = {
    #         "author": apply_advanced_rules(book, "class.author@tag.span.0@text"),
    #         "bookUrl": apply_advanced_rules(book, "a@href"),
    #         "coverUrl": apply_advanced_rules(book, "img@src"),
    #         "kind": apply_advanced_rules(
    #             book, "class.author@tag.span.2@text&&class.popularity@text##\\|.*"
    #         ),
    #         "lastChapter": apply_advanced_rules(book, "class.popularity@text##.*\\|"),
    #         "name": apply_advanced_rules(book, "class.name@text"),
    #     }
    #     results.append(book_info)


# asyncio.run(fetch_search_test())
