# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('ASSIGN', 'DIVIDE', 'GE', 'ID', 'LE', 'LPAREN', 'MINUS', 'NE', 'NUM', 'PLUS', 'RPAREN', 'TIMES', 'bool', 'else', 'false', 'for', 'if', 'then', 'true', 'while'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_newline>\\n+)|(?P<t_comment>(/\\*(.|\\n)*?\\*/)|(//.*))|(?P<t_NUM>-?[0-9]+)|(?P<t_ID>[a-zA-Z_][a-zA-Z0-9|_]*)|(?P<t_NE>!=)|(?P<t_GE>>=)|(?P<t_LE><=)|(?P<t_ASSIGN>:=)|(?P<t_PLUS>\\+)|(?P<t_TIMES>\\*)|(?P<t_LPAREN>\\()|(?P<t_RPAREN>\\))|(?P<t_MINUS>-)|(?P<t_DIVIDE>/)', [None, ('t_newline', 'newline'), ('t_comment', 'comment'), None, None, None, ('t_NUM', 'NUM'), ('t_ID', 'ID'), (None, 'NE'), (None, 'GE'), (None, 'LE'), (None, 'ASSIGN'), (None, 'PLUS'), (None, 'TIMES'), (None, 'LPAREN'), (None, 'RPAREN'), (None, 'MINUS'), (None, 'DIVIDE')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
