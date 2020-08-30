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
        self.RE = re.compile(r'^[ ]{0,%d}((\d+\.)|[*+-])[ ]+.*' % (self.tab_length - 1))
        self.INDENT_RE = re.compile(r'^[ ]{%d,%d}((\d+\.)|[*+-])[ ]+.*' % (self.tab_length, self.tab_length * 2 - 1))

    def run(self, lines):
        inside_list = False
        new_lines = []
        for line in lines:
            if self.RE.match(line):
                if not inside_list:
                    inside_list = True
                    # Add new blank line
                    new_lines.append('')
            elif self.INDENT_RE.match(line):
                pass
            elif line == '':
                # Empty line, list has ended
                inside_list = False

            new_lines.append(line)
        return new_lines


def makeExtension(**kwargs):
    return BreaklessLists(**kwargs)
