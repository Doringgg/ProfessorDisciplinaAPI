from DB import database
from Verifys import DiscVerify
from prettytable import PrettyTable

def Create (codigodisc = 0, nomedisc = ''):
    try:

        if DiscVerify.CdgExists(codigodisc) == False:
            if DiscVerify.Verifys(nomedisc):
                query = database.connection.cursor()
                query.execute(f'INSERT INTO disciplinas (codigodisc, nomedisc) VALUES ({codigodisc}, "{nomedisc}") ;')

                database.connection.commit()
                query.close()

                print('Inserção feita com sucesso!!')
        else:
            print("\nEste registro já existe no banco!!\n")

    except Exception as error:

        print(f'Error: {error}')
        query.close()

def ReadAll():
    try:

        grid = PrettyTable(['Código','Nome da disciplina'])

        query = database.connection.cursor()
        query.execute('SELECT * FROM disciplinas ;')
        table = query.fetchall()
        if query.rowcount > 0:
            for row in table:
                grid.add_row([row[0],row[1]])
            print(grid)
        else:
            print("\nNão existe registros no banco!!\n")
        
        query.close()

    except Exception as error:

        print(f'Error: {error}')
        query.close()

def ReadByCdg(codigodisc = 0):
    try:

        grid = PrettyTable(['Código','Disciplina'])

        query = database.connection.cursor()
        query.execute(f'SELECT * FROM disciplinas WHERE codigodisc = {codigodisc} ;')
        table = query.fetchall()
        if query.rowcount > 0:
            for row in table:
                grid.add_row([row[0],row[1]])
            print(grid)
        else:
            print('Não existe cadastros no banco com esse código!')

        query.close()

    except Exception as error:
        print(f'Error: {error}')
        query.close()

def Update(codigodisc = 0, nomedisc = ''):
    try:

        if DiscVerify.CdgExists(codigodisc):
            if DiscVerify.Verifys(nomedisc):
                query = database.connection.cursor()
                query.execute(f'UPDATE disciplinas SET nomedisc = "{nomedisc}" WHERE codigodisc = {codigodisc} ;')
                database.connection.commit()
                print("Cadastro atualizado com sucesso!!")
                query.close()
        else:
            print('Não existe nenhum cadastro no banco com esse código!')


    except Exception as error:
        print(f'Error: {error}')
        query.close()

def Delete(codigodisc = 0):
    try:
        if DiscVerify.IsInDisxProf(codigodisc):
            print('\nExiste um cadastro com esse código na tabela "Professores para Disciplinas", exclua-o antes de prosseguir\n')
        
        else:
            verify = input("Tem certeza que deseja fazer a exclusão? s-sim/n-não\n").strip().lower()
            while verify not in ["s","n","sim","nao","não"]:

                verify = input("Opção inválida, deseja realmente excluir o cadastro? s-sim/n-não\n")

            if verify in ["s","sim"]:
                query = database.connection.cursor()
                query.execute(f"DELETE FROM disciplinas WHERE codigodisc = {codigodisc} ; ")
                database.connection.commit()
                print("Cadastro excluido com sucesso!!")

                query.close()
            
            else:
                print("\nO cadastro não foi deletado\n")

    except Exception as error:
        print(f"Error: {error}")
        query.close()