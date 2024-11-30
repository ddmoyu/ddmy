import json
from src.common.tools import load_json, save_json


def get_book_sources():
    return load_json("novel_sources.json")


def import_local_source(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


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
