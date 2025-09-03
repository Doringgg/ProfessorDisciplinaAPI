from DB import database
from Verifys import ProfVerify
from prettytable import PrettyTable

def Create (registro = 0, nomeprof = '', telefoneprof = '', idadeprof = 0, salarioprof = 0.0):
    try:

        if ProfVerify.RgExists(registro) == False:
            if ProfVerify.Verifys(nomeprof, telefoneprof, idadeprof, salarioprof):
            
                query = database.connection.cursor()
                query.execute(f'insert into professores (registro, nomeprof, telefoneprof, idadeprof, salarioprof) values ({registro}, "{nomeprof}","{telefoneprof}",{idadeprof},{salarioprof}) ; ')

                database.connection.commit()
                query.close()

                print('\nInserção feita com sucesso!!\n')
        else:
            print("\nEste registro já existe no banco!!\n")
    
    except Exception as error:
        
        print(f'Error: {error}')
        query.close()

def ReadAll():
    try:

        grid = PrettyTable(['Registro','Nome do Professor','Telefone','Idade','Salario'])

        query = database.connection.cursor()
        query.execute('SELECT * FROM professores ;')
        table = query.fetchall()
        if query.rowcount > 0:
            for row in table:
                grid.add_row([row[0],row[1],row[2],row[3],row[4]])
            print(grid)
        else:
            print("\nNão existe registros no banco!!\n")
        
        query.close()
        

    except Exception as error:

        print(f'Error: {error}')
        query.close()

def ReadByRg(rg = 0):
    try:

        grid = PrettyTable(['Registro','Nome do professor','Telefone','Idade','Salario'])
        
        query = database.connection.cursor()
        query.execute(f'SELECT * FROM professores WHERE registro = {rg} ;')
        table = query.fetchall()
        if query.rowcount > 0:
            for row in table:
                grid.add_row([row[0],row[1],row[2],row[3],row[4]])
            print(grid)
        else:
            print('Não existe cadastros no banco com esse registro!')

        query.close()

    except Exception as error:
        print(f'Error: {error}')
        query.close()

def Update(registro = 0, nomeprof = '', telefoneprof = '', idadeprof = 0, salarioprof = 0.0):
    try:

        if ProfVerify.RgExists(registro):
            if ProfVerify.Verifys(nomeprof, telefoneprof, idadeprof, salarioprof):
                query = database.connection.cursor()
                query.execute(f'UPDATE professores SET nomeprof = "{nomeprof}", telefoneprof = "{telefoneprof}", idadeprof = "{idadeprof}", salarioprof = "{salarioprof}" WHERE registro = {registro} ;')
                database.connection.commit()
                print("\nCadastro atualizado com sucesso!!\n")

                query.close()
        else:
            print('Não existe nenhum cadastro no banco com esse registro!')

    except Exception as error:
        print(f'Error: {error}')
        query.close()

def Delete(registro = 0):
    try:

        if ProfVerify.IsInDisxProf(registro):
            print('\nExiste um cadastro com esse registro na tabela "Professores para Disciplinas", exclua-o antes de prosseguir\n')
        
        else:
            verify = input("Tem certeza que deseja fazer a exclusão? s-sim/n-não\n").strip().lower()
            while verify not in ["s","n","sim","nao","não"]:

                verify = input("Opção inválida, deseja realmente excluir o cadastro? s-sim/n-não\n")

            if verify in ["s","sim"]:
                query = database.connection.cursor()
                query.execute(f"DELETE FROM professores WHERE registro = {registro} ; ")
                database.connection.commit()
                print("\nCadastro excluido com sucesso!!\n")

                query.close()

            else:
                print("\nO cadastro não foi deletado\n")

    except Exception as error:
        print(f"Error: {error}")
        query.close()
