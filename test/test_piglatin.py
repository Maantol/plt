import unittest
from piglatin import PigLatin
from error import PigLatinError
class TestPigLatin(unittest.TestCase):

    #Python experience is 0, first time use is in this week even in testing. I don't know Python syntax or language rules.
    #I didn't understand the rules or logic (no bracelets, no type
    # declarations, importance of spacing, etc.) of Python language despite effort and learning via the web during
    #experience. (self) -> str: What does that even mean?
    #I normally use Java, C, React, Javascript.

    def test_input_take(self):
        pg = PigLatin("This is a phrase")
        self.assertEqual("This is a phrase", pg)


