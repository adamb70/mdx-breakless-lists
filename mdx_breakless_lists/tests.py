import unittest
from markdown import markdown

expected_html = "<p>This line is before the list starts</p>\n" \
                "<ul>\n<li>first list item</li>\n<li>second list item</li>\n</ul>"

expected_html_split = "<p>This line is before the list starts</p>\n<ul>\n<li>first list item</li>" \
                      "\n<li>second list item\n second item continued</li>\n<li>third list item</li>\n</ul>"

expected_html_nested = "<p>This line is before the list starts</p>\n<ol>\n<li>\n<p>List 1</p>" \
                       "\n<p>List 2 is here:</p>\n<ul>\n<li>nested item</li>\n<li>nested item</li>" \
                       "\n</ul>\n<p>subtitle</p>\n<ul>\n<li>new nested item</li>\n</ul>\n</li>\n</ol>"


class BreaklessListTestCase(unittest.TestCase):
    def test_no_break(self):
        text = "This line is before the list starts\n- first list item\n- second list item"
        html = markdown(text, extensions=['mdx_breakless_lists'])
        self.assertEqual(
            html,
            expected_html
        )

    def test_break(self):
        text = "This line is before the list starts\n\n- first list item\n- second list item"
        html = markdown(text, extensions=['mdx_breakless_lists'])
        self.assertEqual(
            html,
            expected_html
        )

    def test_split_line(self):
        text = "This line is before the list starts\n\n- first list item\n- second list item\n second item " \
               "continued\n- third list item"
        html = markdown(text, extensions=['mdx_breakless_lists'])
        self.assertEqual(
            html,
            expected_html_split
        )

    def test_split_line_no_break(self):
        text = "This line is before the list starts\n- first list item\n- second list item\n second item " \
               "continued\n- third list item"
        html = markdown(text, extensions=['mdx_breakless_lists'])
        self.assertEqual(
            html,
            expected_html_split
        )

    def test_nested_list(self):
        text = "This line is before the list starts" \
               "\n1. List 1" \
               "\n\n\tList 2 is here:" \
               "\n\n\t* nested item" \
               "\n\t* nested item" \
               "\n" \
               "\n\tsubtitle" \
               "\n\n\t- new nested item"
        html = markdown(text, extensions=['mdx_breakless_lists'])
        self.assertEqual(
            html,
            expected_html_nested
        )

    def test_nested_list_no_break(self):
        text = "This line is before the list starts" \
               "\n1. List 1" \
               "\n\n\tList 2 is here:" \
               "\n\t* nested item" \
               "\n\t* nested item" \
               "\n" \
               "\n\tsubtitle" \
               "\n\t- new nested item"
        html = markdown(text, extensions=['mdx_breakless_lists'])
        self.assertEqual(
            html,
            expected_html_nested
        )


if __name__ == '__main__':
    unittest.main()
