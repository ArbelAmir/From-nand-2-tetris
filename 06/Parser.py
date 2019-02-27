import re

SEMICOLON = ';'

EQUAL = '='

C_COMMAND = 'C_COMMAND'

L_COMMAND = 'L_COMMAND'

A_COMMAND = 'A_COMMAND'

L_PREFIX = '('
R_PREFIX = ')'

A_PREFIX = '@'

PATH_INDEX = 1

NEW_LINE_TRAIL = '\n'

START_OF_COMMENT = '//'
READ_MODE = 'r'
EMPTY_TRAILS = {'\n', '\r\n'}


class Parser:

    @staticmethod
    def is_comment(line):
        """
        Checks if given line is a comment.
        :param line: Line to check.
        :return: True iff line is a comment.
        """
        return line[0:2] == START_OF_COMMENT or (line in EMPTY_TRAILS)

    @staticmethod
    def strip_comments(line):
        """
        Strips comments off line of code.
        :param line: Given line of code.
        :return: New, comment-stripped line.
        """
        return line.split('//')[0]

    def __init__(self, path):
        """
        Opens the input file and gets ready to parse it.
        :param path: Path of the assembly code.
        """

        self.lines = self.first_run(path)
        self.index = 0

    def first_run(self, filepath):
        """
        Makes first run over code and removes comments and white spaces.
        In addition
        :param filepath: Path of the asm code.
        :return: List of all lines without comments and blank lines.
        """
        with open(filepath) as file:
            code_lines = []
            for line in file:
                line = (line.split('//', 1)[0].replace(' ', '').replace('\t', '').replace('\n', ''))
                if line != "":
                    code_lines.append(line)

            return code_lines

    def has_more_commands(self):
        """
        Checks if there any more commands in the input.
        :return:
        """
        return self.index < len(self.lines) - 1

    def advance(self):
        """
        Reads the next command from the input and makes it the current command.
        Should be called only if  hasMoreCommands() is true.
        Initially the is no current command.
        :return: True iff there are more commands to parse.
        """
        if self.has_more_commands():
            self.index += 1

    def reset(self):
        """
        Resets the Parser to the beginning of the code file.
        """
        self.index = 0

    def command_type(self):
        """
        :return: The type of the current 	command:
        - A_COMMAND for @Xxx where Xxx is either a symbol or a	decimal number
        - C_COMMAND for	dest=comp;jump
        - L_COMMAND (actually, pseudocommand) for (Xxx) where Xxx is a symbol.
        """
        first_char = self.lines[self.index][0]
        return {
            A_PREFIX: 'A_COMMAND',
            L_PREFIX: 'L_COMMAND'
        }.get(first_char, 'C_COMMAND')

    def symbol(self):
        """
        :return: The symbol or decimal Xxx of the current command @Xxx or (Xxx). Should be called
        only when commandType() is A_COMMAND or L_COMMAND.
        """
        assert self.command_type() in [A_COMMAND, L_COMMAND]

        symbol = self.lines[self.index].lstrip(A_PREFIX + L_PREFIX)
        return symbol.rstrip(R_PREFIX) if (self.command_type() == L_COMMAND) else symbol

    def dest(self):
        """
        :return: The dest mnemonic in the current C-command (8 possiblities).
        Should be called only when commandType() is C_COMMAND.
        """
        assert (self.command_type() == C_COMMAND)
        return self.lines[self.index].rpartition(EQUAL)[0]  # if there is no '=' it returns ''

    def comp(self):
        """
        :return: The comp mnemonic in the current C-command (28 possibilities).
        Should be called only when commandType() is C_COMMAND.
        """
        assert (self.command_type() == C_COMMAND), 'your line is: ' + str(self.lines[self.index])
        comp = self.lines[self.index].rpartition(EQUAL)[-1]
        # if there is '=' we get the right side of it, else we got the string
        comp = comp.partition(SEMICOLON)[0]
        # if there is ';' we get the left side of it, else we got the same string
        return comp

    def jump(self):
        """
        :return: The jump mnemonic in the current C-command (8 possibilities).
        Should be called only when commandType() is C_COMMAND.
        """
        assert (self.command_type() == C_COMMAND)
        return self.lines[self.index].partition(SEMICOLON)[-1]

# def main(argv):
# 	parser = Parser(argv[PATH_INDEX])
# 	for line in parser.lines:
# 		print(line)
# 		print("Com type is:", parser.command_type())
# 		print("Symbol is:", parser.symbol())
# 		print("Dest is:", parser.dest())
# 		print("Comp is:", parser.comp())
# 		print("Jump is:", parser.jump())
# 		parser.advance()
# 		print("****")
#
#
# if __name__ == "__main__":
# 	main(sys.argv)
