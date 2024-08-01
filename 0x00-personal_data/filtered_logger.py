#!/usr/bin/env python3
import re


def filter_datum(fields, redaction, message, separator):
    return re.sub(
        rf"({'|'.join(map(re.escape, fields))})=.*?{re.escape(separator)}",
        lambda match: f"{match.group(1)}={redaction}{separator}",
        message
    )
