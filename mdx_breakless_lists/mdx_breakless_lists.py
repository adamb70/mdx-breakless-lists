import re
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class BreaklessLists(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(BreaklessListsProcessor(md.parser), 'breakless_lists', 27)
        md.registerExtension(self)


class BreaklessListsProcessor(Preprocessor):
    """ Simply add an extra line break before the list and let the other processors handle list creation. """

    def __init__(self, parser):
        super().__init__(parser)
        self.tab_length = parser.md.tab_length
        self.LI_RE = re.compile(r'^[ ]*((\d+\.)|[*+-])[ ]+.*')

    def run(self, lines):
        previous_was_li = False
        new_lines = []
        for line in lines:
            if self.LI_RE.match(line):
                if not previous_was_li:
                    # Add new blank line
                    new_lines.append('')
                previous_was_li = True
            elif line == '':
                previous_was_li = False

            new_lines.append(line)
        return new_lines


def makeExtension(**kwargs):
    return BreaklessLists(**kwargs)
