import ply.lex as lex

tokens = (
    'NUMBER',   # for integers or floats
    'PLUS',     # "+"
    'MINUS',    # "-"
    'TIMES',    # "*"
    'DIVIDE',   # "/"
    'LPAREN',   # "("
    'RPAREN'   # ")"
)

t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'

def t_NUMBER(t):
    r'\d+[\.\d+]?'
    
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

t_ignore  = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()