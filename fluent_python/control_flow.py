import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


class LazySentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'LazySentence({reprlib.repr(self.text)})'

    def __iter__(self):
        # for match in RE_WORD.finditer(self.text):
        #     yield match.group()
        # lazy generator
        return (match.group() for match in RE_WORD.finditer(self.text))
