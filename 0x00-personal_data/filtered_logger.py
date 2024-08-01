#!/usr/bin/env python3
import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    return re.sub(
        rf"({'|'.join(map(re.escape, fields))})=.*?{re.escape(separator)}",
        lambda match: f"{match.group(1)}={redaction}{separator}",
        message,
    )
