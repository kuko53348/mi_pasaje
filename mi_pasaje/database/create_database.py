# import pymysql
import sqlite3
import time


all_citys = {

    'Pinar_del_Rio':[
            'Guanes',
            'Mantua',
            'Minas_de_Matahambre',
            'Vinales',
            'San_Luis',
            "San_Juan_y_Martinez",
            'Pinar_del_Rio',
            'Los_Palacios',
            'Consolacion_del_Sur',
            'La_Palma',
            'Sandino',
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
            ],
    'Ciego_de_Avila':[
            'Bolivia',
            'Majagua',
            'Moron',
            'Florencia',
            'Ciego_de_Avila',
            'Baragua',
            'Venezuela',
            'Ciro_Redondo',
            'Primero_de_Enero',
            'Chambas',
            ],
    'Artemisa':[
            'Alquizar',
            'Artemisa',
            'San_Antonio_Banos',
            'Caimito',
            'Mariel',
            'San_Cristobal',
            'Guanajay',
            'Bauta',
            'Candelaria',
            'Bahia_Honda',
            'Guira_de_Melena',
            ],
    'Las_Tunas':[
            'Jesus_Menendez',
            'Manati',
            'Colombia',
            'Las_Tunas',
            'Majibacoa',
            'Puerto_Padre',
            'Jobabo',
            'Amancio',
            ],
    'La_Habana':[
            'Plaza_de_la_Revolucion',
            'Marianao',
            'Cotorro',
            'Cerro',
            'Centro_Habana',
            'Regla',
            'San_Miguel_Padron',
            'Boyeros',
            'Habana_Vieja',
            'Arrojo_Naranjo',
            'Diez_de_Octubre',
            'La_Lisa',
            'Guanabacoa',
            'Habana_del_Este',
            'Playa',
            ],
    'Cienfuegos':[
            'Cienfuegos',
            'Aguada_de_Pasajeros',
            'Abreus',
            'Lajas',
            'Rodas',
            'Cruces',
            'Palmira',
            'Cumanayagua',
            ],
    'Holguin':[
            'Frank_Pais',
            'Cacocum',
            'Rafael_Freyre',
            'Banes',
            'Mayari',
            'Moa',
            'Cueto',
            'Holguin',
            'Gibara',
            'Sagua_de_Tanamo',
            'Calixto_Garcia',
            'Urbano_Noris',
            'Antilla',
            'Baguanos'
            ],
    'Santi_Spiritus':[
            'Jatibonico',
            'Santi_Spiritus',
            'Cabaiguan',
            'La_Sierpe',
            'Yaguajay',
            'Fomento',
            'Taguasco',
            'Trinidad',
            ],
    'Camaguey':[
            'Jatibonico',
            'Santa_Cruz_del_Sur',
            'Camaguey',
            'Carlos_Manuel_Cespedes',
            'Esmeralda',
            'Najasa',
            'Sierra_de_Cubitas',
            'Minas',
            'Nuevitas',
            'Florida',
            'Vertientes',
            'Sibanicu',
        ],
    'Santiago_de_Cuba':[
            'San_Luis',
            'Palma_Soriano',
            'Segundo_Frente',
            'Tercer_Frente',
            'Contramaestre',
            'Guama',
            'Santiago_de_Cuba',
            'Songo_la_Maya',
            'Mella',
        ],
    'Granma':[
            'Manzanillo',
            'Buey_Arriba',
            'Campechuela',
            'Bartolome_Maso',
            'Bayamo',
            'Media_Luna',
            'Pilón',
            'Yara',
            'Cauto_Cristo',
            'Guisa',
            'Río_Cauto',
            'Jiguaní',
            'Niquero',
            ],
    'Guantanamo':[
            'Yateras',
            'El_Salvador',
            'Imias',
            'Caimanera',
            'Baracoa',
            'Guantanamo',
            'San_Antonio_Sur',
            'Manuel_Tames',
            'Maisi',
            'Niceto_Perez',
            ],

    'Mayabeque':[
            'Jaruco',
            'Quivican',
            'San_Jose_Lajas',
            'Madruga',
            'Guines',
            'Santa_Cruz_del_Norte',
            'Batabano',
            'Nueva_Paz',
            'Bejucal',
            'Melena_Del_Sur',
            'San_Nicolas',
            ],
    'Villa_Clara':[
            'Corralillo',
            'Encrucijada',
            'Santo_Domingo',
            'Ranchuelo',
            'Caibarien',
            'Manicaragua',
            'Cifuentes',
            'Sagua_la_Grande',
            ],
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