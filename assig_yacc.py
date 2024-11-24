import ply.yacc as yacc
from assig_lex import tokens

data_dict = {
    'COMPETITION_ID': [],
    'SEASON_ID': [],
    'COUNTRY': [],
    'COMPETITION_NAME': [],
    'GENDER': [],
    'YOUTH': [],
    'INTERNATIONAL': [],
    'SEASON_NAME': [],
    'MATCH': [],
    'UPDATED': [],
    'UPDATED_360': [],
    'AVAILABLE_360': [],
    'AVAILABLE': []
}


def p_json(p):
    'json : LLAVE_ABRE contenido LLAVE_CIERRA'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])

def p_contenido(p):
    'contenido : ROOT DOSPUNTOS COR_ABRE elementos COR_CIERRA'
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4]) + str(p[5])

def p_elementos_multiple(p):
    'elementos : elementos COMA elemento'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])

def p_elementos_single(p):
    'elementos : elemento'
    p[0] = str(p[1])

def p_elemento(p):
    'elemento : LLAVE_ABRE estructura LLAVE_CIERRA'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])

def p_estructura(p):
    'estructura : competition_id season_id country competition_name gender youth international season_name match'
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4]) + str(p[5]) + str(p[6]) + str(p[7]) + str(p[8]) + str(p[9])

def p_competition_id(p):
    'competition_id : COMPETITION_ID DOSPUNTOS NUMBER COMA'
    data_dict['COMPETITION_ID'].append(p[3])
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_season_id(p):
    'season_id : SEASON_ID DOSPUNTOS NUMBER COMA'
    data_dict['SEASON_ID'].append(p[3])
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_country(p):
    'country : COUNTRY DOSPUNTOS STRING COMA'
    data_dict['COUNTRY'].append(p[3])
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_competition_name(p):
    'competition_name : COMPETITION_NAME DOSPUNTOS STRING COMA'
    data_dict['COMPETITION_NAME'].append(p[3])
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_gender(p):
    'gender : GENDER DOSPUNTOS STRING COMA'
    data_dict['GENDER'].append(p[3])
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_youth(p):
    'youth : YOUTH DOSPUNTOS BOOLEAN COMA'
    data_dict['YOUTH'].append(p[3])
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_international(p):
    'international : INTERNATIONAL DOSPUNTOS BOOLEAN COMA'
    data_dict['INTERNATIONAL'].append(p[3])
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_season_name(p):
    'season_name : SEASON_NAME DOSPUNTOS STRING COMA'
    data_dict['SEASON_NAME'].append(p[3])
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_match(p):
    'match : MATCH DOSPUNTOS LLAVE_ABRE estructura_match LLAVE_CIERRA'
    data_dict['MATCH'].append(p[4])
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4]) + str(p[5])

def p_estructura_match(p):
    'estructura_match : updated updated360 available360 available'
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_updated(p):
    'updated : UPDATED DOSPUNTOS TIMESTAMP COMA'
    data_dict['UPDATED'].append(p[3])
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_updated_null(p):
    'updated : UPDATED DOSPUNTOS NULL COMA'
    data_dict['UPDATED'].append(None)
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_updated360(p):
    'updated360 : UPDATED_360 DOSPUNTOS TIMESTAMP COMA'
    data_dict['UPDATED_360'].append(p[3])
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_updated360_null(p):
    'updated360 : UPDATED_360 DOSPUNTOS NULL COMA'
    data_dict['UPDATED_360'].append(None)
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_available360(p):
    'available360 : AVAILABLE_360 DOSPUNTOS TIMESTAMP COMA'
    data_dict['AVAILABLE_360'].append(p[3])
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_available360_null(p):
    'available360 : AVAILABLE_360 DOSPUNTOS NULL COMA'
    data_dict['AVAILABLE_360'].append(None)
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_available(p):
    'available : AVAILABLE DOSPUNTOS TIMESTAMP'
    data_dict['AVAILABLE'].append(p[3])
    p[0] = str(p[1]) + str(p[2]) + str(p[3])

def p_available_null(p):
    'available : AVAILABLE DOSPUNTOS NULL'
    data_dict['AVAILABLE'].append(None)
    p[0] = str(p[1]) + str(p[2]) + str(p[3])




def p_error(p):
    if p:
        print(f"Syntax error at token: {p.type} ({p.value})")
    else:
        print("Syntax error at EOF")

def insert_sql():
    with open("sql_insert_instructions.txt", "w") as f:
        f.write("INSERT INTO competitions (\n")
        f.write("    competition_id, \n")
        f.write("    season_id, \n")
        f.write("    country_name, \n")
        f.write("    competition_name, \n")
        f.write("    competition_gender, \n")
        f.write("    competition_youth, \n")
        f.write("    competition_international, \n")
        f.write("    season_name\n")
        f.write(") VALUES\n")

        for i in range(len(data_dict['COMPETITION_ID'])):
            competition_values = (
                str(data_dict['COMPETITION_ID'][i]),
                str(data_dict['SEASON_ID'][i]),
                str(data_dict['COUNTRY'][i]),
                str(data_dict['COMPETITION_NAME'][i]),
                str(data_dict['GENDER'][i]),
                str(data_dict['YOUTH'][i]),
                str(data_dict['INTERNATIONAL'][i]),
                str(data_dict['SEASON_NAME'][i])
            )
            f.write(f"({', '.join(competition_values)}),\n")

        f.seek(f.tell() - 2, 0)
        f.write(";\n\n")
        
        f.write("INSERT INTO matches (\n")
        f.write("    competition_id, \n")
        f.write("    season_id, \n")
        f.write("    updated, \n")
        f.write("    updated_360, \n")
        f.write("    available_360, \n")
        f.write("    available\n")
        f.write(") VALUES\n")

        for i in range(len(data_dict['COMPETITION_ID'])):
            match_values = (
                str(data_dict['COMPETITION_ID'][i]),
                f"'{data_dict['UPDATED'][i]}'" if data_dict['UPDATED'][i] != None else 'NULL',
                f"'{data_dict['UPDATED_360'][i]}'" if data_dict['UPDATED_360'][i] != None else 'NULL',
                f"'{data_dict['AVAILABLE_360'][i]}'" if data_dict['AVAILABLE_360'][i] != None else 'NULL',
                f"'{data_dict['AVAILABLE'][i]}'" if data_dict['AVAILABLE'][i] != None else 'NULL'
            )
            f.write(f"({', '.join(match_values)}),\n")

        f.seek(f.tell() - 2, 0)
        f.write(";\n")

    print("Las instrucciones SQL han sido escritas en 'sql_insert_instructions.txt'")

parser = yacc.yacc()


while True: 
    try: 
        s = input('Validate expression: > ')
    except EOFError:
        break
    if not s: 
        continue
    print(f"Input: {s}")
    try:
        result = parser.parse(s)
        if result:
            print("Resultado:", result)
            print("Validación correcta.")
            print(data_dict['COMPETITION_ID'][0])
            insert_sql()

        else:
            print("Validación fallida.")
    except Exception as e:
        print(f"Error al analizar: {e}")