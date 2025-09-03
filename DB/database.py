import mysql.connector

def Connect ():
    try:
        global connection

        connection = mysql.connector.Connect(
            host='localhost',
            database='univap',
            user='root',
            password=''
        )

        if connection.is_connected():

            global query
            
            query = connection.cursor()
            query.execute('select database();')
            dbname = query.fetchone()
            print("Conexão com banco realizada com sucesso")
            print(f'Banco conectado = {dbname}'.replace("(","").replace(")","").replace("'","").replace(",",""))
            print('='*80)
            query.close()
        else:
            print('A conexão não pode ser realizada')

    except Exception as error:
        print(f'Error : {error}')
