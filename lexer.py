 # ------------------------------------------------------------
 # calclex.py
 #
 # tokenizer for a simple expression evaluator for
 # numbers and +,-,*,/
 # ------------------------------------------------------------
import lex as lex
import parsetab

reserved = {
    'if' : 'if',
    'then' : 'then',
    'else' : 'else',
    'while' : 'while',
    'for' : 'for',
    'bool' : 'bool',
    'true' : 'true',
    'false' : 'false',
    }
 
# List of token names.   This is always required
tokens = [
    'NUM', 'ID', 'NE', 'GE', 'LE', 'ASSIGN', 'PLUS', 'MINUS',
    'TIMES','DIVIDE', 'LPAREN','RPAREN',
] + list(reserved.values())



# Token regexes
t_NE = r'!='
t_GE = r'>='
t_LE = r'<='
t_ASSIGN = r':='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'


# Function for determinign character position on a line
# fileContents = fileHandle.read() is the input text string
# t is a token instance

def find_column(fileContents, t):
    line_start = fileContents.rfind('\n', 0, t.lexpos) + 1
    return (t.lexpos - line_start) + 1

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Ignore comments 
def t_comment(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass

#Detecting integers
def t_NUM(t):
    r'-?[0-9]+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Acceptable Identifiers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9|_]*' 
    t.type = reserved.get(t.value, 'ID')   # Checking for reserved words
    return t

# Error handling rule
def t_error(t):
    print("\nERROR: Illegal character '{0}' at line {1} position {2}".format(
       t.value[0], t.lexer.lineno, find_column(fileContents, t)))    #t.lexer.skip(1)
    exit(1)

# Building the lexer and optimizing
lexer = lex.lex(optimize=1)
 
# Give the lexer some input
inputFile = input("Enter file name: ")
fileHandle = open(inputFile)
fileContents = fileHandle.read()
lexer.input(fileContents)

# Closing file
fileHandle.close() 

# Tokenize
print("Position \t\t\tKind \t\t Value")

def next():
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input

        def kind():
            return tok.type

        def value():
            return tok.value

        def position():
            return "(line " + str(tok.lineno) + ", char " + str(find_column(fileContents, tok)) + ")"

        print(position(), "\t\t", kind(), "\t\t", value())

#Calling the next token
next() 
