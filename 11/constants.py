"""
Useful constants.
"""

class Messages:
    INVALID_PATH_MSG = "Error: Invalid path."

class String:
    NEW_LINE = '\n'  # TODO what if we use 'os.linesep'?
    TAB = '\t'


class OS:
    WRITING_MODE = 'w'
    INVALID_PATH_MSG = 'Error: the supplied path is invalid.'
    JACK_EXTENSION = '.jack'
    VM_EXTENSION = '.vm'


class SymbolTable:
    # Symbol table indexing rules
    TYPE_IDX = 0
    KIND_IDX = 1
    COUNT_IDX = 2


class VMCommands:
    GENERAL_COMMAND = '{} {{}} {{}}'  # used for formatting in the specific command
    PUSH = GENERAL_COMMAND.format('push')  # used for formatting in the segment and index
    POP = GENERAL_COMMAND.format('pop')  # used for formatting in the segment and index
    OP2VM = {'+': 'add',
             '-': 'sub',
             '=': 'eq',
             '>': 'gt',
             '<': 'lt',
             '&': 'and',
             '|': 'or',
             '~': 'not'}  # TODO handles difference between neg and sub


class Kinds:
    CLASS_VAR_KINDS = {'static', 'field'}
    SUBROUTINE_VAR_KINDS = {'argument', 'var'}
    SUBROUTINE_KINDS = {'constructor', 'function', 'method'}


class SubroutineVarKinds:
    ARG = 'arg'
    VAR = 'var'


class SubroutineKinds:
    CONSTRUCTOR = 'constructor'
    FUNCTION = 'function'
    METHOD = 'method'


class Segments:
    CONST = 'constant'
    ARG = 'argument'
    LOCAL = 'local'
    STATIC = 'static'
    THIS = 'this'
    THAT = 'that'
    POINTER = 'pointer'
    TEMP = 'temp'


class Commands:
    ADD = 'add'
    SUB = 'sub'
    NEG = 'neg'
    EQ = 'eq'
    GT = 'gt'
    LT = 'lt'
    AND = 'and'
    OR = 'or'
    NOT = 'not'


class Keywords:
    CLASS = 'class'
    CONSTRUCTOR = 'constructor'
    FUNCTION = 'function'
    METHOD = 'method'
    FIELD = 'field'
    STATIC = 'static'
    VAR = 'var'
    INT = 'int'
    CHAR = 'char'
    BOOL = 'boolean'
    VOID = 'void'
    TRUE = 'true'
    FALSE = 'false'
    NULL = 'null'
    THIS = 'this'
    LET = 'let'
    DO = 'do'
    IF = 'if'
    ELSE = 'else'
    WHILE = 'while'
    RETURN = 'return'


class Symbols:
    L_CURLY_BRACKET = '{'
    R_CURLY_BRACKET = '}'
    L_ROUND_BRACKET = '('
    R_ROUND_BRACKET = ')'
    L_SQUARE_BRACKET = '['
    R_SQUARE_BRACKET = ']'
    L_ANGLE_BRACKET = '<'
    R_ANGLE_BRACKET = '>'
    PERIOD = '.'
    COMMA = ','
    SEMICOLON = ';'
    PLUS = '+'
    MINUS = '-'
    ASTERISK = '*'
    SLASH = '/'
    AMPERSAND = '&'
    PIPE = '|'
    EQUALS = '='
    TILDE = '~'

    OPS = {'+', '-', '*', '/', '&', '|', '<', '>', '='}


class TokenKinds:
    IDENTIFIER = 'IDENTIFIER'


class Types:
    VAR_TYPES = {'int', 'char', 'boolean'}
    SUBROUTINE_TYPES = VAR_TYPES.union({'void'})


class Statements:
    STATEMENTS = {'let', 'if', 'while', 'do', 'return'}
