from DB import database
from Verifys import ProfVerify
from Verifys import DiscVerify

def CdgDCExists(CdgDC = ''):
    
    query = database.connection.cursor()
    query.execute(f'SELECT * FROM disciplinasxprofessores WHERE codigodisciplinanocurso = {CdgDC} ;')
    table = query.fetchall()
    if query.rowcount > 0:
        query.close()
        return True
    else:
        query.close()
        return False

def Verify(codprof = 0, coddisc = 0):
    if ProfVerify.RgExists(codprof) == False or DiscVerify.CdgExists(coddisc) == False:
        print("O professor e/ou disciplina não está cadastrado no banco!")
        return False
    else:
        return True
