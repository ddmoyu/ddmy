from parsel import Selector

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