from DB import database

def IsInDisxProf(codprof = 0):
    
    query = database.connection.cursor()
    query.execute(f'SELECT * FROM disciplinasxprofessores WHERE codprofessor = {codprof} ;')
    table = query.fetchall()
    if query.rowcount > 0:
        query.close()
        return True
    else:
        query.close()
        return False

def RgExists(rg):

    query = database.connection.cursor()
    query.execute(f'SELECT * FROM professores WHERE registro = {rg} ;')
    table = query.fetchall()
    if query.rowcount > 0:
        query.close()
        return True
    else:
        query.close()
        return False

def Verifys(nome = '', telefone = '', idade = '', salario = ''):
    tel = [0,1,2,3,4,5,6,7,8,9,'()','-',' ']
    symbols = ['!','@','#','$','%','&','*','()','-',]

    if len(nome)<3 or nome.replace(' ','').isalnum() != True or len(nome.split())<2:
        print("Nome inserido inválido")
        return False
    
    elif len(telefone)<11 or telefone in tel != True or telefone.count('-') > 1 or telefone.count(' ') > 2 or telefone.count('(') > 1 or telefone.count(')') > 1:
        print("Telefone inserido inválido")
        return False
    
    elif idade<18 or idade> 120:
        print("Idade inserida inválida")
        return False
    
    elif salario<1518 or salario>30000:
        print("Salário inserido inválido")
        return False
    
    else:
        return True
