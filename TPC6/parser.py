import ply.yacc as yacc
from lexer import tokens

# Grammar Rules
# <expression> ::= <term> | <expression> "+" <term> | <expression> "-" <term>
# <term>       ::= <factor> | <term> "*" <factor> | <term> "/" <factor>
# <factor>     ::= <number> | "(" <expression> ")"

def p_expression_term(p):
    """
    expression : term
    """
    p[0] = p[1]

def p_expression_operator(p):
    """
    expression : expression PLUS term
               | expression MINUS term
    """
    if p[2] == '+':
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1] - p[3]
        
def p_term_factor(p):
    """
    term : factor
    """
    p[0] = p[1]
    
def p_term_operator(p):
    """
    term : term TIMES factor
         | term DIVIDE factor
    """
    if p[2] == '/':
        p[0] = p[1] / p[3]
    else:
        p[0] = p[1] * p[3]
        
def p_factor_number(p):
    """
    factor : NUMBER
    """
    p[0] = p[1]

def p_factor_expression(p):
    """
    factor : LPAREN expression RPAREN
    """
    p[0] = p[2]
        
def p_error(p):
    print(f"Syntax error at {p}")

parser = yacc.yacc()