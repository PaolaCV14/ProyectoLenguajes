import ply.lex as lex

tokens = (
    'LLAVE_ABRE',
    'LLAVE_CIERRA',
    'DOSPUNTOS',
    'COMA',
    'STRING',
    'NUMBER',
    'BOOLEAN',
    'NULL',
    'PARE_ABRE',
    'PARE_CIERRA'
)

t_LLAVE_ABRE = r'{'
t_LLAVE_CIERRA = r'}'
t_DOSPUNTOS = r':'
t_COMA = r','
t_STRING = r'[^<>]+' 
t_BOOLEAN = r''
t_NULL = r'NULL|null'
t_PARE_ABRE = r'\('
t_PARE_CIERRA = r'\)'

def t_NUMBER(t):
    r'[1-9][0-9]*'  
    t.value = int(t.value)
    return t

t_ignore = ' '


def t_error(t):
    print('Illegal character:', t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()