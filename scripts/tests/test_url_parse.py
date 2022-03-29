import unittest
from src.md2tex import convert_md_str_to_tex

class UrlParseTestCase(unittest.TestCase):
    '''
    testing the conversion of markdown style hyperlinks to latex style
    '''

    def test_one(self):
        '''testing a string with no hyperlinks
        '''
        md_str = 'dude i love coffee'
        tex_str = convert_md_str_to_tex(md_str)

        expected_str = r'dude i love coffee'

        self.assertEqual(
            expected_str,
            tex_str,
        )

    def test_two(self):
        '''testing a string with one hyperlink that starts somewhere in the middle
        '''
        md_str = 'dude lets ask [google](https://www.google.com)'
        tex_str = convert_md_str_to_tex(md_str)

        expected_str = r'dude lets ask \href{https://www.google.com}{google}'

        self.assertEqual(
            expected_str,
            tex_str,
        )


    def test_three(self):
        '''testing a string with one hyperlink that is the entire string
        '''
        md_str = '[google](https://www.google.com)'
        tex_str = convert_md_str_to_tex(md_str)

        expected_str = r'\href{https://www.google.com}{google}'

        self.assertEqual(
            expected_str,
            tex_str,
        )

    def test_four(self):
        '''testing a string with one hyperlink that starts with the hyperlink and has additional chars at the end
        '''
        md_str = '[google](https://www.google.com) we should ask'
        tex_str = convert_md_str_to_tex(md_str)

        expected_str = r'\href{https://www.google.com}{google} we should ask'

        self.assertEqual(
            expected_str,
            tex_str,
        )

    def test_five(self):
        '''testing a string with two hyperlinks that occur in the middle
        '''
        md_str = 'question: to use [google](https://www.google.com) or [firefox](https://www.mozilla.org/en-US/firefox/new/) for search?'
        tex_str = convert_md_str_to_tex(md_str)

        expected_str = r'question: to use \href{https://www.google.com}{google} or \href{https://www.mozilla.org/en-US/firefox/new/}{firefox} for search?'

        self.assertEqual(
            expected_str,
            tex_str,
        )


