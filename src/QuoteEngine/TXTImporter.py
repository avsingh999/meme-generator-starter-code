from typing import List

from .ImportInterface import ImportInterface
from .QuoteModel import QuoteModel

class TXTImporter(ImportInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, 'r') as f:
            for line in f.readlines():
                body, author = line.split(" - ")
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
