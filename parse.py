import pyparsing as pp


class Parser:

    def __init__(self):
        opr = pp.one_of("and or")
        term = pp.Word(pp.alphas)
        spaces = pp.ZeroOrMore(' ')
        self.form_only_words = pp.ZeroOrMore(term + spaces + opr.suppress()) + spaces + term
        self.form = pp.ZeroOrMore(term + spaces + opr) + spaces + term
        self.form_free = pp.ZeroOrMore(term)

    def extract_words(self, query):
        return self.form_only_words.parse_string(query)

    def parse_query(self, query):
        return self.form.parse_string(query)

    def extract_free_style(self, query):
        return self.form_free.parse_string(query)
