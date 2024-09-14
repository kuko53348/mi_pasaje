# import pymysql
import sqlite3
import time


all_citys = {

    'Granma':[
            'Bayamo',
            'Bartolome_Maso',
            'Buey_Arriba',
            'Campechuela',
            'Cauto_Cristo',
            'Guisa',
            'Jiguaní',
            'Manzanillo',
            'Media_Luna',
            'Pilón',
            'Río_Cauto',
            'Yara',
            ],
'Matanzas':[
            'Matanzas',
            'Cárdenas',
            'Martí',
            'Colón',
            'Perico',
            'Jovellanos',
            'Pedro_Betancourt',
            'Limonar',
            'Unión_de_Reyes',
            'Ciénaga_de_Zapata',
            'Jagüey_Grande',
            'Calimete',
            'Los_Arabos',
            ]

        }


def CreateTableDatabase( hosting='', namedatabase='', user='', password='', tableName='',colums={}):
    """let create database in web host"""
    # createDatabase = cursor.execute("CREATE TABLE my_tabla_1 ( tabla TEXT, tipo TEXT, datos TEXT )")
    # conn = pymysql.connect(
    # conn = sqlite3.connect(
    #                         host=hosting,
    #                         database=namedatabase,
    #                         user=user,
    #                         password=password,
    #                         charset='utf8mb4',
    #                         )
    conn = sqlite3.connect(f".{namedatabase}.db")
    tmp=''
    for _ in zip(colums.keys(),colums.values()):
        tmp+=f"""{_[0]} {_[1]},"""

    data = f"""{tmp}"""
    data = data[:-1]
    command = f"""CREATE TABLE {tableName}(
                                            {data}
                                            )"""
    try:
        cursor = conn.cursor()
        createDatabase = cursor.execute(command)

    # except pymysql.err.OperationalError:
    except sqlite3.err.OperationalError:
        print('database complete')

def eraseTableDatabase(hosting='', namedatabase='', user='', password='', tableName=''):

    # conn = pymysql.connect(
    conn = sqlite3.connect(
                            host=hosting,
                            database=namedatabase,
                            user=user,
                            password=password,
                            charset='utf8mb4',
                            )

    sql=f"DROP TABLE {tableName}"
    cursor = conn.cursor()
    cursor.execute(sql)

    pass

if __name__ == '__main__':
    ####################################### pymysql
    # Server="sql10.freemysqlhosting.net"
    # NameDataBase='sql10628548'
    # Username='sql10628548'
    # Password='FZbUVBKtiI'
    # number=3306

    # Server = '127.0.0.1'
    Server = 'localhost'
    Username = 'root'
    Password = 'xavier007 '

    NameDataBase = 'database.db'
    TableName='Bayamo'
    # CreateTableDatabase(
    #                 hosting=Server,
    #                 namedatabase=NameDataBase,
    #                 user=Username,
    #                 password=Password,

    #                 tableName='luckyNumber',
    #                 colums={
    #                         'name_game':'TEXT',
    #                         'date_time':'TEXT',
    #                         'evening_number':'TEXT',
    #                         'midday_number':'TEXT',
    #                         })



    for tmp_municipios in all_citys.keys():
        # time.sleep(1)

        for tmp_city in all_citys.get(tmp_municipios):
            CreateTableDatabase(
                            hosting=Server,
                            namedatabase=NameDataBase,
                            user=Username,
                            password=Password,

                            tableName= f"{tmp_city}" ,

                            colums={
                                     'id_acc':'TEXT',
                                  'user_name':'TEXT',
                                   'telegram':'TEXT',
                                      'phone':'TEXT',
                                  'transport':'TEXT',
                                'origin_city':'TEXT',
                                'photo_trans':'TEXT',
                                   'time_acc':'TEXT'
                                    }
                            )

    CreateTableDatabase(
                    hosting=Server,
                    namedatabase=NameDataBase,
                    user=Username,
                    password=Password,

                    tableName='Client',

                    colums={
                             'id_acc':'TEXT',
                          'user_name':'TEXT',
                           'telegram':'TEXT',
                              'phone':'TEXT',
                           'time_acc':'TEXT'
                            }
                    )
    # eraseTableDatabase(
    #                 hosting=Server,
    #                 namedatabase=NameDataBase,
    #                 user=Username,
    #                 password=Password,
    #                 tableName='clientesConectados',
    #                 )