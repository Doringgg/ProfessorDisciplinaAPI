from Verifys import DisXProfVerify
from DB import database
from prettytable import PrettyTable
    

def Create (cdgdisccurso = '', codprof = 0, coddisc = 0, curso = 0, cargahoraria = 0, anoletivo = 0):
    try:
        
        if DisXProfVerify.CdgDCExists(cdgdisccurso) == False:
            if DisXProfVerify.Verify(codprof,coddisc):
                query = database.connection.cursor()
                query.execute(f'''INSERT INTO disciplinasxprofessores (codigodisciplinanocurso, codprofessor, coddisciplina, curso, cargahoraria, anoletivo) 
                            VALUES ("{cdgdisccurso}", {codprof}, {coddisc}, {curso}, {cargahoraria}, {anoletivo}) ;''')
                
                database.connection.commit()
                query.close()

                print("Inserção feita com sucesso!!")
        else:
            print("Este código de disciplina no curso já existe!!")

    except Exception as error:

        print(f'Error : {error}')
        query.close()

def ReadAll():
    try:

        grid = PrettyTable(['Código da disciplina no curso', 'Código do professor', 'Código da disciplina', 'Curso', 'Carga Horária', 'Ano Letivo'])

        query = database.connection.cursor()
        query.execute('SELECT * FROM disciplinasxprofessores ;')
        table = query.fetchall()
        if query.rowcount > 0:
            for row in table:
                grid.add_row([row[0],row[1],row[2],row[3],row[4],row[5]])
            print(grid)
        else:
            print("\nNão existe registros no banco!!\n")
        
        query.close()

    except Exception as error:

        print(f'Error: {error}')

def ReadByCdgDC(CdgDC = ''):
    try:

        grid = PrettyTable(['Código da disciplina no curso', 'Código do professor', 'Código da disciplina', 'Curso', 'Carga Horária', 'Ano Letivo'])

        query = database.connection.cursor()
        query.execute(f'SELECT * FROM disciplinasxprofessores WHERE codigodisciplinanocurso = "{CdgDC}" ;')
        table = query.fetchall()
        if query.rowcount > 0:
            for row in table:
                grid.add_row([row[0],row[1],row[2],row[3],row[4],row[5]])
            print(grid)
        else:
            print("\nNão existe registros no banco com esse código!!\n")
        
        query.close()

    except Exception as error:

        print(f'Error: {error}')

def Update(cdgdisccurso = '', codprof = 0, coddisc = 0, curso = 0, cargahoraria = 0, anoletivo = 0):

    try:

        if DisXProfVerify.CdgDCExists(cdgdisccurso):
            if DisXProfVerify.Verify(codprof,coddisc):
                query = database.connection.cursor()
                query.execute(f'''UPDATE disciplinasxprofessores SET 
                            codigodisciplinanocurso = '{cdgdisccurso}',
                            codprofessor = {codprof},
                            coddisciplina = {coddisc},
                            curso = {curso},
                            cargahoraria = {cargahoraria},
                            anoletivo = {anoletivo} ;''')
                    
                database.connection.commit()
                print("Cadastro atualizado com sucesso!!!")
                query.close()      
        else:
            print('Não existe nenhum cadastro no banco com esse registro!')
        
    except Exception as error:
        print(f'Error: {error}')
        query.close()

def Delete(CdgDC = ''):
    try:
        verify = input("Tem certeza que deseja fazer a exclusão? s-sim/n-não\n").strip().lower()
        while verify not in ["s","n","sim","nao","não"]:
            verify = input("Opção inválida, deseja realmente excluir o cadastro? s-sim/n-não\n")
        if verify in ["s","sim"]:
            query = database.connection.cursor()
            query.execute(f"DELETE FROM disciplinasxprofessores WHERE codigodisciplinanocurso = '{CdgDC}' ; ")
            database.connection.commit()
            print("Cadastro excluido com sucesso!!")

            query.close()
        else:
            print("O cadastro não foi deletado")

    except Exception as error:
        print(f"Error: {error}")
        query.close()