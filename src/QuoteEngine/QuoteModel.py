class QuoteModel:
    def __init__(self, body, author):
        self.author = author.strip()
        self.body = body.strip()

    def __repr__(self):
        return "{0} from {1}".format(self.body, self.author)
