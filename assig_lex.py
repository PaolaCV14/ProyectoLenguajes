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
t_LLAVE_ABRE = r'\{'
t_LLAVE_CIERRA = r'\}'
t_DOSPUNTOS = r'\:'
t_COMA = r'\,'
t_COR_ABRE = r'\['
t_COR_CIERRA = r'\]'


#Campos
# Campos
def t_ROOT(t):
    r'"root"'
    t.type = 'ROOT'
    return t

def t_COMPETITION_ID(t):
    r'"competition_id"'
    t.type = 'COMPETITION_ID'
    return t

def t_SEASON_ID(t):
    r'"season_id"'
    t.type = 'SEASON_ID'
    return t

def t_COUNTRY(t):
    r'"country_name"'
    t.type = 'COUNTRY'
    return t

def t_COMPETITION_NAME(t):
    r'"competition_name"'
    t.type = 'COMPETITION_NAME'
    return t

def t_GENDER(t):
    r'"competition_gender"'
    t.type = 'GENDER'
    return t

def t_YOUTH(t):
    r'"competition_youth"'
    t.type = 'YOUTH'
    return t

def t_INTERNATIONAL(t):
    r'"competition_international"'
    t.type = 'INTERNATIONAL'
    return t

def t_SEASON_NAME(t):
    r'"season_name"'
    t.type = 'SEASON_NAME'
    return t

def t_MATCH(t):
    r'"match"'
    t.type = 'MATCH'
    return t

def t_UPDATED(t):
    r'"updated"'
    t.type = 'UPDATED'
    return t

def t_UPDATED_360(t):
    r'"updated_360"'
    t.type = 'UPDATED_360'
    return t

def t_AVAILABLE_360(t):
    r'"available_360"'
    t.type = 'AVAILABLE_360'
    return t

def t_AVAILABLE(t):
    r'"available"'
    t.type = 'AVAILABLE'
    return t

def t_TIMESTAMP(t):
    r'"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]*"'
    t.type = 'TIMESTAMP'
    return t

# Valores
def t_STRING(t):
    r'"(\\.|[^"\\])*"'
    t.type = 'STRING'
    return t

def t_BOOLEAN(t):
    r'true|false'
    t.type = 'BOOLEAN'
    return t

def t_NULL(t):
    r'null|NULL'
    t.type = 'NULL'
    return t

# Números
def t_NUMBER(t):
    r'[1-9][0-9]*'
    t.value = int(t.value)
    t.type = 'NUMBER'
    return t



t_ignore = ' \n'



def t_error(t):
    print('Illegal character:', t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()



