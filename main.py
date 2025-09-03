from Tables import Professor
from Tables import Disciplina
from Tables import DisXProf
from DB import database

hasConnected = 0

run = input("Deseja iniciar o programa? (s-sim/n-não)\n").lower().strip()
while run not in ["s","n","sim","nao","não"]:
        run = input("\nOpção inválida, deseja fazer outra ação no banco de dados? (s-sim/n-não)\n")
if run in ["s","sim"]:
    table = ""
    while table != "4":
        if hasConnected == 0:
            database.Connect()
            hasConnected = 1


        print("\nQual tabela deseja acessar?")
        print("[1] Professores")
        print("[2] Disciplinas")
        print("[3] Professores para Disciplinas")
        print("[4] Fechar o programa\n")
        table = input().strip()
        while table not in ["1","2","3","4"]:
            print("Opção inválida, selecione uma das seguintes:").strip()
            print("[1] Professores")
            print("[2] Disciplinas")
            print("[3] Professores para Disciplinas")
            print("[4] Fechar o programa\n")
            table = input().strip()
        print('-='*62)
        
        if table == "1":
            while True:
                print("\nO que deseja fazer na tabela professores?\n")
                print("[1] Inserir")
                print("[2] Consultar todos os cadastros")
                print("[3] Consultar por registro")
                print("[4] Alterar registro")
                print("[5] Excluir registro")
                print("[6] Sair da tabela\n")
                action = input().strip()

                while action not in ["1","2","3","4","5","6"]:
                    print("\nOpção inválida, selecione uma das seguintes:")
                    print("[1] Inserir")
                    print("[2] Consultar todos os cadastros")
                    print("[3] Consultar por registro")
                    print("[4] Alterar registro")
                    print("[5] Excluir registro")
                    print("[6] Sair da tabela\n")
                    action = input().strip() 
                    
                if action == "1":
                    Professor.Create(
                        int(input("Qual o registro?: ")),
                        input("Qual o nome completo?: ").strip().title(),
                        input("Qual o telefone?: ").strip(),
                        int(input("Qual a idade?: ")),
                        float(input("Qual o salário?: "))
                    )
                        
                elif action == "2":
                    print("\n")
                    Professor.ReadAll()
                        
                elif action == "3":
                    registro = input("\nQual o registro do professor que deseja consultar?\n")
                    while  registro.isnumeric() == False:
                        registro = input("O registro inserido não é valido, por favor insira um registro válido:\n")
                    registro = int(registro)
                    Professor.ReadByRg(registro)
                        
                elif action == "4":
                    Professor.Update(int(input("Qual o registro do professor que deseja atualizar?: ")),
                    input("Qual o nome completo?: ").strip().title(),
                    input("Qual o telefone?: ").strip(),
                    int(input("Qual a idade?: ")),
                    float(input("Qual o salário?: ")))
                        
                elif action == "5":
                    Professor.Delete(int(input("\nQual o registro que deseja excluir o cadastro?\n")))
                        
                elif action == "6":
                    break

                print('-='*62)
            
        elif table == "2":
            while True:
                print("\nO que deseja fazer na tabela disciplinas?\n")
                print("[1] Inserir")
                print("[2] Consultar todos os cadastros")
                print("[3] Consultar por código")
                print("[4] Alterar cadastro")
                print("[5] Excluir cadastro")
                print("[6] Sair da tabela\n")
                action = input().strip()

                while action not in ["1","2","3","4","5","6"]:
                    print("\nOpção inválida, selecione uma das seguintes:")
                    print("[1] Inserir")
                    print("[2] Consultar todos os cadastros")
                    print("[3] Consultar por código")
                    print("[4] Alterar cadastro")
                    print("[5] Excluir cadastro")
                    print("[6] Sair da tabela\n")
                    action = input().strip() 
                    
                if action == "1":
                        Disciplina.Create(
                            int(input("Qual o registro?: ")),
                            input("Qual o nome da Disciplina?: "),
                        )
                        
                elif action == "2":
                    print("\n")
                    Disciplina.ReadAll()
                        
                elif action == "3":
                    codigo = input("\nQual o código da disciplina que deseja consultar?\n")
                    while  codigo.isnumeric() == False:
                        codigo = input("O código inserido não é valido, por favor insira um código válido:\n")
                    codigo = int(codigo)
                    Disciplina.ReadByCdg(codigo)
                        
                elif action == "4":
                    Disciplina.Update(int(input("Qual o código da disciplina que deseja atualizar?: ")),
                    input("Qual o nome da disciplina?: "),
                    )
                        
                elif action == "5":
                    Disciplina.Delete(int(input("\nQual o código da disciplina que deseja excluir?\n")))
                        
                elif action == "6":
                    break

                print('-='*62)

        elif table == "3":
            while True:
                print("\nO que deseja fazer na tabela Professores para Disciplinas ?\n")
                print("[1] Inserir")
                print("[2] Consultar todos os cadastros")
                print("[3] Consultar por registro")
                print("[4] Alterar registro")
                print("[5] Excluir registro")
                print("[6] Sair da tabela\n")
                action = input().strip()

                while action not in ["1","2","3","4","5","6"]:
                    print("\nOpção inválida, selecione uma das seguintes:")
                    print("[1] Inserir")
                    print("[2] Consultar todos os cadastros")
                    print("[3] Consultar por registro")
                    print("[4] Alterar registro")
                    print("[5] Excluir registro")
                    print("[6] Sair da tabela\n")
                    action = input().strip() 
                    
                if action == "1":
                    DisXProf.Create(
                        (input("Qual o código da disciplina no curso?: ")),
                        int(input("Qual o código do professor?: ")),
                        int(input("Qual o código da disciplina?: ")),
                        int(input("Qual o curso?: ")),
                        int(input("Qual a carga horária?: ")),
                        int(input("Qual o ano letivo?: "))
                    )
                        
                elif action == "2":
                    DisXProf.ReadAll()
                        
                elif action == "3":
                    CdgDC = input("\nQual o código da disciplina no curso que deseja consultar?\n")
                    DisXProf.ReadByCdgDC(CdgDC)
                        
                elif action == "4":
                    DisXProf.Update(input("Qual o código da disciplina no curso que deseja atualizar?: "),
                    int(input("Qual o código do professor?: ")),
                    int(input("Qual o código da disciplina?: ")),
                    int(input("Qual o curso?: ")),
                    int(input("Qual a carga horária?: ")),
                    int(input("Qual o ano letivo?: ")))
                        
                elif action == "5":
                    DisXProf.Delete(input("Qual o código da disciplina no curso que deseja excluir o cadastro?\n"))
                        
                elif action == "6":
                    break

        print('-='*62)

if hasConnected == 1:
    database.connection.close()
print("Programa finalizado!")