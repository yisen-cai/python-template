import unittest

from fluent_python.control_flow import Sentence, LazySentence


class TestControlFlow(unittest.TestCase):
    sentence = Sentence("word1 word2")
    lazy_sentence = LazySentence("word1 word2")

    def test_sentence(self):
        assert len(self.sentence) > 0

    def test_iterator(self):
        for word in self.sentence:
            assert word is not None

    def test_lazy_sentence(self):
        for word in self.lazy_sentence:
            assert word is not None
