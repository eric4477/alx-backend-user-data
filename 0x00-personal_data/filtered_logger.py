#!/usr/bin/env python3
import logging
from typing import List
from re import sub, escape


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    pattern = rf"({'|'.join(map(escape, fields))})=.*?{escape(separator)}"
    return sub(
        pattern,
        lambda match: f"{match.group(1)}={redaction}{separator}",
        message
    )


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original_message = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, original_message, self.SEPARATOR
        )
