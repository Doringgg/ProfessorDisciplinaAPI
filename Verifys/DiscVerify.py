from DB import database

def IsInDisxProf(coddisc = 0):
    
    query = database.connection.cursor()
    query.execute(f'SELECT * FROM disciplinasxprofessores WHERE coddisciplina = {coddisc} ;')
    table = query.fetchall()
    if query.rowcount > 0:
        query.close()
        return True
    else:
        query.close()
        return False

def CdgExists(codigodisc):
    query = database.connection.cursor()
    query.execute(f'SELECT * FROM disciplinas WHERE codigodisc = {codigodisc} ;')
    table = query.fetchall()
    if query.rowcount > 0:
        query.close()
        return True
    else:
        query.close()
        return False
    
def Verifys(nomedisc = ''):
    if nomedisc.isspace() or len(nomedisc)<2 or nomedisc.replace(' ','').isalnum() == False:
        print("Nome inserido inválido")
        return False
    else:
        return True