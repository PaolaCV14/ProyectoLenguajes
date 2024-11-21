import ply.lex as lex

tokens = (
    'LLAVE_ABRE',
    'LLAVE_CIERRA',
    'DOSPUNTOS',
    'COMA',
    'COR_ABRE',
    'COR_CIERRA',
    'STRING',
    'NUMBER',
    'BOOLEAN',
    'NULL',
    'ROOT',
    'COMPETITION_ID',
    'SEASON_ID',
    'COUNTRY',
    'COMPETITION_NAME',
    'GENDER',
    'YOUTH',
    'INTERNATIONAL',
    'SEASON_NAME',
    'MATCH',
    'UPDATED',
    'UPDATED_360',
    'AVAILABLE_360',
    'AVAILABLE',
    'TIMESTAMP'
)

#Delimitadores
t_LLAVE_ABRE = r'{'
t_LLAVE_CIERRA = r'}'
t_DOSPUNTOS = r':'
t_COMA = r','
t_COR_ABRE = r'\['
t_COR_CIERRA = r'\]'

#Valores
t_STRING = r'\".*?\"'
#t_NUMBER = r'\d+'
t_BOOLEAN = r'(true|false)'
t_NULL = r'NULL|null'

#Campos
t_ROOT = r'\"root\"'
t_COMPETITION_ID = r'\"competition_id\"'
t_SEASON_ID = r'\"season_id\"'
t_COUNTRY = r'\"country_name\"'
t_COMPETITION_NAME = r'\"competition_name\"'
t_GENDER = r'\"competition_gender\"'
t_YOUTH = r'\"competition_youth\"'
t_INTERNATIONAL = r'\"competition_international\"'
t_SEASON_NAME = r'\"season_name\"'
t_MATCH = r'\"match\"'
t_UPDATED = r'\"updated\"'
t_UPDATED_360 = r'\"updated_360\"'
t_AVAILABLE_360 = r'\"available_360\"'
t_AVAILABLE = r'\"available\"'
t_TIMESTAMP = r'\"[0-9]{4}\-[0-9]{2}\-[0-9]{2}T[0-9]{2}\:[0-9]{2}:[0-9]{2}\.[0-9]*'

def t_NUMBER(t):
    r'[1-9][0-9]*'  
    t.value = int(t.value)
    return t

t_ignore = ' '


def t_error(t):
    print('Illegal character:', t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()