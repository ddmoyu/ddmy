from parsel import Selector


class AnalyzeByJSoup:
    def __init__(self, doc):
        self.element = self.parse(doc)

    def parse(self, doc):
        if isinstance(doc, Selector):
            return doc
        if isinstance(doc, str):
            if doc.startswith("<?xml"):
                return Selector(text=doc, type="xml")
            return Selector(text=doc)
        raise ValueError("Unsupported document type")

    def get_elements(self, rule):
        return self._get_elements(self.element, rule)

    def get_string(self, rule_str):
        if not rule_str:
            return None
        string_list = self.get_string_list(rule_str)
        if not string_list:
            return None
        if len(string_list) == 1:
            return string_list[0]
        return "\n".join(string_list)

    def get_string0(self, rule_str):
        string_list = self.get_string_list(rule_str)
        return string_list[0] if string_list else ""

    def get_string_list(self, rule_str):
        text_list = []
        if not rule_str:
            return text_list

        source_rule = SourceRule(rule_str)
        if not source_rule.elements_rule:
            text_list.append(self.element.get() or "")
        else:
            rule_analyzes = RuleAnalyzer(source_rule.elements_rule)
            rule_str_list = rule_analyzes.split_rule("&&", "||", "%%")
            results = []
            for rule_str_x in rule_str_list:
                temp = (
                    self.get_result_list(rule_str_x)
                    if source_rule.is_css
                    else self.get_result_list(rule_str_x)
                )
                if temp:
                    results.append(temp)
                    if rule_analyzes.elements_type == "||":
                        break
            if results:
                if rule_analyzes.elements_type == "%%":
                    for i in range(len(results[0])):
                        for temp in results:
                            if i < len(temp):
                                text_list.append(temp[i])
                else:
                    for temp in results:
                        text_list.extend(temp)
        return text_list

    def _get_elements(self, temp, rule):
        if not temp or not rule:
            return []

        elements = []
        source_rule = SourceRule(rule)
        rule_analyzes = RuleAnalyzer(source_rule.elements_rule)
        rule_str_list = rule_analyzes.split_rule("&&", "||", "%%")
        elements_list = []
        if source_rule.is_css:
            for rule_str in rule_str_list:
                temp_elements = temp.css(rule_str)
                elements_list.append(temp_elements)
                if temp_elements and rule_analyzes.elements_type == "||":
                    break
        else:
            for rule_str in rule_str_list:
                rs_rule = RuleAnalyzer(rule_str)
                rs_rule.trim()
                rs = rs_rule.split_rule("@")
                if len(rs) > 1:
                    el = [temp]
                    for rl in rs:
                        es = []
                        for et in el:
                            es.extend(self._get_elements(et, rl))
                        el = es
                    elements_list.append(el)
                else:
                    elements_list.append(
                        ElementsSingle().get_elements_single(temp, rule_str)
                    )
                if elements_list[-1] and rule_analyzes.elements_type == "||":
                    break
        if elements_list:
            if rule_analyzes.elements_type == "%%":
                for i in range(len(elements_list[0])):
                    for es in elements_list:
                        if i < len(es):
                            elements.append(es[i])
            else:
                for es in elements_list:
                    elements.extend(es)
        return elements

    def get_result_list(self, rule_str):
        if not rule_str:
            return None
        elements = [self.element]
        rule = RuleAnalyzer(rule_str)
        rule.trim()
        rules = rule.split_rule("@")
        last = len(rules) - 1
        for i in range(last):
            es = []
            for elt in elements:
                es.extend(ElementsSingle().get_elements_single(elt, rules[i]))
            elements = es
        return self.get_result_last(elements, rules[last]) if elements else None

    def get_result_last(self, elements, last_rule):
        text_list = []
        for element in elements:
            if last_rule == "text":
                text = element.get()
                if text:
                    text_list.append(text)
            elif last_rule == "textNodes":
                tn = [
                    node.get().strip()
                    for node in element.xpath(".//text()")
                    if node.get().strip()
                ]
                if tn:
                    text_list.append("\n".join(tn))
            elif last_rule == "ownText":
                text = element.xpath("string()").get()
                if text:
                    text_list.append(text)
            elif last_rule == "html":
                for script in element.xpath(".//script"):
                    script.getparent().remove(script)
                for style in element.xpath(".//style"):
                    style.getparent().remove(style)
                html = element.get()
                if html:
                    text_list.append(html)
            elif last_rule == "all":
                text_list.append(element.get())
            else:
                url = element.attrib.get(last_rule)
                if url and url not in text_list:
                    text_list.append(url)
        return text_list
