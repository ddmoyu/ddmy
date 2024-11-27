import re
from typing import List, Optional


class AnalyzeByRegex:
    @staticmethod
    def get_element(res: str, regs: List[str], index: int = 0) -> Optional[List[str]]:
        v_index = index
        res_m = re.finditer(regs[v_index], res)
        match = next(res_m, None)
        if not match:
            return None
        if v_index + 1 == len(regs):
            info = []
            for group_index in range(len(match.groups()) + 1):
                info.append(match.group(group_index))
            return info
        else:
            result = []
            for match in res_m:
                result.append(match.group())
            return AnalyzeByRegex.get_element("".join(result), regs, v_index + 1)

    @staticmethod
    def get_elements(res: str, regs: List[str], index: int = 0) -> List[List[str]]:
        v_index = index
        res_m = re.finditer(regs[v_index], res)
        match = next(res_m, None)
        if not match:
            return []
        if v_index + 1 == len(regs):
            books = []
            for match in res_m:
                info = []
                for group_index in range(len(match.groups()) + 1):
                    info.append(match.group(group_index) or "")
                books.append(info)
            return books
        else:
            result = []
            for match in res_m:
                result.append(match.group())
            return AnalyzeByRegex.get_elements("".join(result), regs, v_index + 1)
