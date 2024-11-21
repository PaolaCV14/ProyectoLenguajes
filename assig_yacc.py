import ply.yacc as yacc
from assig_lex import tokens

def p_json(p):
    'json : LLAVE_ABRE contenido LLAVE_CIERRA'
    p[0] = p[1] + p[2] + p[3]

def p_contenido(p):
    'contenido: ROOT DOSPUNTOS COR_ABRE elementos COR_CIERRA'
    p[0] = p[1] + p[2] + p[3]

def p_elementos_varios(p):
    'elementos: LLAVE_ABRE estructura LLAVE_CIERRA COMA'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_elemento_final(p):
    'elementos: LLAVE_ABRE estructura LLAVE_CIERRA'
    p[0] = p[1] + p[2] + p[3]

def p_estructura(p):
    'estructura: competition_id season_id country competition_name gender youth international season_name match'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9]

def p_competition_id(p):
    'competition_id: COMPETITION_ID DOSPUNTOS NUMBER COMA'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_season_id(p):
    'season_id: SEASON_ID DOSPUNTOS NUMBER COMA'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_country(p):
    'country: COUNTRY DOSPUNTOS STRING COMA'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_competition_name(p):
    'competition_name: COMPETITION_NAME DOSPUNTOS STRING COMA'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_gender(p):
     'gender: GENDER DOSPUNTOS STRING COMA'
     p[0] = p[1] + p[2] + p[3] + p[4]

def p_youth(p):
     'youth: YOUTH DOSPUNTOS BOOLEAN COMA'
     p[0] = p[1] + p[2] + p[3] + p[4]

def p_international(p):
     'international: INTERNATIONAL DOSPUNTOS BOOLEAN COMA'
     p[0] = p[1] + p[2] + p[3] + p[4]

def p_season_name(p):
    'season_name: SEASON_NAME DOSPUNTOS STRING COMA'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_match(p):
    'match : MATCH DOSPUNTOS LLAVE_ABRE estructura_match LLAVE_CIERRA '
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_estructura_match(p):
    'estructura_match : updated updated360 available360 available'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_updated(p):
    'updated : UPDATED DOSPUNTOS TIMESTAMP COMA'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_updated_null(p):
    'updated : UPDATED DOSPUNTOS NULL COMA'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_updated360(p):
    'updated360 : UPDATED_360 DOSPUNTOS TIMESTAMP COMA'
    p[0] = p[1] + p[2] + p[3] + p[4]  

def p_updated360_null(p):
    'updated360 : UPDATED_360 DOSPUNTOS NULL COMA'
    p[0] = p[1] + p[2] + p[3] + p[4]    

def p_available360(p):
    'available360 : AVAILABLE_360 DOSPUNTOS TIMESTAMP COMA'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_available360_null(p):
    'available360 : AVAILABLE_360 DOSPUNTOS NULL COMA'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_available(p):
    'available : AVAILABLE DOSPUNTOS TIMESTAMP'
    p[0] = p[1] + p[2] + p[3] 

def p_available_null(p):
    'available : AVAILABLE DOSPUNTOS NULL'
    p[0] = p[1] + p[2] + p[3]

def p_error(p):
    print("Syntax error in input!")
    print(p)

parser = yacc.yacc()

while True: 
    try: 
        s = input('Validate expression: > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print("result: ", result)
