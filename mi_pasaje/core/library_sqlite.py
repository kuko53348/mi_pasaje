# import pymysql
import sqlite3


class mysqlite_db():
    """
    EXEMPLE:

    =========================================== creation database ===========================================
    Instance_mysqlite_db.CreateTableDatabase(connected=connection_db,tableName="book_orders",column=data_write)
    =========================================== find all data table
    find_all = Instance_mysqlite_db.sqlite_find_all(connected=connection_db,tableName='book_orders')
    =========================================== find by name
    name = Instance_mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='book_orders',columnName='user_name',fetch='all') #fetch=5,all                                 #by tabl+column
    name = Instance_mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='book_orders',columnName='user_name',name='street') #fetch=5,all                               #by tabl+column
    name = Instance_mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='book_orders',columnName='user_name',name='xxxx',match=['to_wallet','']) #fetch=5,all     #by tbl+column+match(column,name)
    =========================================== write data
    write_data = Instance_mysqlite_db.sqlite_write_data(connected=connection_db,tableName='book_orders',columnValue=('pedro','pedro','pedro','pedro','pedro','pedro','pedro','pedro'))
    =========================================== update data
    update_data = Instance_mysqlite_db.sqlite_update_data(connected=connection_db,tableName='book_orders',changeData=('user_name','data'),byData=('user_name','data'))
    update_data = Instance_mysqlite_db.sqlite_update_data(connected=connection_db,tableName='book_orders',changeData=('user_name','sas'),byData=('user_name','xxxx'),match=['block_hash',''])
    =========================================== remove data
    remove_data = Instance_mysqlite_db.sqlite_remove_data(connected=connection_db,tableName='book_orders',columnName='user_name',name='pedro')
    remove_data = Instance_mysqlite_db.sqlite_remove_data(connected=connection_db,tableName='book_orders',columnName='user_name',name='pedro',match=['block_hash','200'])
    ===========================================================================================================
    """

    def __init__(self,hosting=''):
        super().__init__()
        self.title='data'



    def sqlite_connection(namedatabase):

        """
        Is necesary open database giving direction to open this return a object of sqlite3 that is the database

        EXEMPLE:

            connection_db = Instance_mysqlite_db.sqlite_connection(namedatabase=".book_orders.db")
        """
        conn = sqlite3.connect(namedatabase)
        return conn

    def CreateTableDatabase(connected,tableName='',column={}):
        """
        Will return a new database

        EXEMPLE:

            connection_db = Instance_mysqlite_db.sqlite_connection(namedatabase=".book_orders.db")
            Instance_mysqlite_db.CreateTableDatabase(connected=connection_db,tableName="book_orders",column=data_write)
        """
        conn = connected
        tmp=''

        for _ in zip(column.keys(),column.values()):
            tmp+=f"""{_[0]} {_[1]},"""

        data = f"""{tmp}"""
        data = data[:-1]

        command = f"""CREATE TABLE {tableName}(
                                                {data}
                                                )
                    """
        try:
            cursor = conn.cursor()
            createDatabase = cursor.execute(command)
            print('DATABASE WAS CREATED')

        except Exception as e:
            print('PLESASE REMOVE OLD DATABASE TO CREATE NEW DATABASE',e)


    def sqlite_find_by_name(connected,tableName,columnName='',name='',fetch='all',match=[]):
        """
        Find by name if exist

        EXEMPLE:
            connection_db = Instance_mysqlite_db.sqlite_connection(namedatabase=".book_orders.db")

            Instance_mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='Employers',columnName='ColumnAdress',name='street') #fetch=5,all                               #by tabl+column
            Instance_mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='Employers',columnName='ColumnAdress',name='street',match=['ColumnPaymen','500']) #fetch=5,all  #by tbl+column+match(column,name)
        """
        # conn = sqlite3.connect(db_address)
        conn = connected
        cursor = conn.cursor()
        try:
            cursor.execute(f'SELECT * FROM {tableName} WHERE {columnName}="{name}" AND {match[0]}="{match[1]}"') if match else  cursor.execute(f"SELECT * FROM {tableName} WHERE {columnName}='{name}'")
        except Exception as e:
            print(f"ERROR: {e}")
            return False

        if fetch == 'all':
            data_finded = cursor.fetchall()
        elif fetch == 'one':
            data_finded = cursor.fetchone()


        conn.commit(),cursor.close(),conn.close()

        if data_finded:
            return data_finded
        else:
            return False

    def sqlite_find_all(connected,tableName='noExist'):
        """
        Return all datatable name in database

        EXEMPLE:

            find_all = Instance_mysqlite_db.sqlite_find_all(connected=connection_db,tableName='book_orders')

        """
        # conn = sqlite3.connect(db_address)
        conn = connected
        cursor = conn.cursor()
        # sql=f"SHOW FULL TABLES "
        # sql=f"SHOW TABLES "
        try:
            sql=f"SELECT * FROM {tableName} "
            cursor.execute(sql)
        except Exception as e:
            print(f"ERROR: {e}")
            return False

        data_finded = cursor.fetchall()
        conn.commit(),cursor.close(),conn.close()

        if data_finded:
            return data_finded
        else:
            return False

    def sqlite_write_data(connected,tableName='',columnValue=()):
        """
        Return BOL True or False if not error writing data.

        EXEMPLE:

            write_data = Instance_mysqlite_db.sqlite_write_data(connected=connection_db,tableName='book_orders',columnValue=('pedro','pedro','pedro','pedro','pedro','pedro','pedro','pedro'))

        """
        conn = connected
        cursor = conn.cursor()
        try:
            sql=f"INSERT INTO {tableName} VALUES{columnValue}"
            wrote_data = cursor.execute(sql)
        except Exception as e:
            print(f"ERROR: {e}")
            return False
        conn.commit(),cursor.close(),conn.close()

        if wrote_data:
            return True
        else:
            return False


    def sqlite_update_data(connected,tableName='',byData='',changeData='',match=[]):
        """
        how work inside:

        1. find and Update data if data exist
        2. If no exist data return false
        3. if data exist and match exist return true else false

        EXEMPLE:

            update_data = Instance_mysqlite_db.sqlite_update_data(connected=connection_db,tableName='book_orders',changeData=('user_name','data'),byData=('user_name','data'))
            update_data = Instance_mysqlite_db.sqlite_update_data(connected=connection_db,tableName='book_orders',changeData=('user_name','sas'),byData=('user_name','xxxx'),match=['block_hash',''])
        """
        #### (modifica SET) (donde WHERE) y (AND condicional)
        conn = connected
        crusor = conn.cursor()

        try:
            """
            find exist name to be changed

            find_name = crusor.execute(f'SELECT * FROM {tableName} WHERE {changeData[0]}="{changeData[1]}"')
            equal_name = crusor.fetchone()

            """
            find_name = crusor.execute(f'SELECT * FROM {tableName} WHERE {changeData[0]}="{changeData[1]}"')
            equal_name = crusor.fetchone()

            if equal_name:

                if match:
                    '''if match is writed'''
                    try:
                        """
                        find exist name tin match o be changed

                        find_match = crusor.execute(f'SELECT * FROM {tableName} WHERE {match[0]}="{match[1]}"')
                        equal_match = crusor.fetchone()

                        """

                        find_match = crusor.execute(f'SELECT * FROM {tableName} WHERE {match[0]}="{match[1]}"')
                        equal_match = crusor.fetchone()

                        if equal_match:
                            '''if equal_match appear'''
                            sql=f"UPDATE {tableName} SET {byData[0]}='{byData[1]}' WHERE {changeData[0]}='{changeData[1]}' AND {match[0]}='{match[1]}' "
                        else:
                            return False

                    except Exception as e:
                        print(f"ERROR: {e}")
                        return False
                else:
                    sql=f"UPDATE {tableName} SET {byData[0]}='{byData[1]}' WHERE {changeData[0]}='{changeData[1]}' "
                try:
                    update_data = crusor.execute(sql)

                except Exception as e:
                    print(f"ERROR: {e}")
                    return False

                conn.commit(),crusor.close(),conn.close()

                if update_data:
                    return True
                else:
                    return False
            else:
                print('No exist')
                return False

        except Exception as e:
            print(f"ERROR: {e}")
            return False

    def sqlite_remove_all(connected,tableName=''):
        """
        EXEMPLE:

            connection_db = mysqlite_db.sqlite_connection(namedatabase = '.book_price.db')
            remove_data   = mysqlite_db.sqlite_remove_all(connected=connection_db,tableName='Employers')
        """
        try:
            conn   = connected
            crusor = conn.cursor()
            crusor.execute(f'DELETE from {tableName}').fetchall()
            conn.commit(),crusor.close(),conn.close()

        except Exception as e:
            print(f"ERROR: {e}")
            return False


    def sqlite_remove_data(connected,tableName='',columnName='',name='',match=[]):
        """
        EXEMPLE:

            sqlite_remove_data(tableName='Employers',columnName='ColumnName',name='pepito',db_address='./address_db.db')
            sqlite_remove_data(tableName='Employers',columnName='ColumnName',name='jonan',match=['ColumnPaymen','100'],db_address='./address_db.db')
        """

        conn   = connected
        crusor = conn.cursor()
        sql = ''

        if match:
            '''
            if match is writed

            find_name = crusor.execute(f'SELECT * FROM {tableName} WHERE {columnName}="{name}"')
            equal_name = crusor.fetchone()

            '''
            data = True
            try:
                find_name = crusor.execute(f'SELECT * FROM {tableName} WHERE {columnName}="{name}"')
                equal_name = crusor.fetchone()
                find_match = crusor.execute(f'SELECT * FROM {tableName} WHERE {match[0]}="{match[1]}"')
                equal_match = crusor.fetchone()

                if find_name and equal_match:
                    sql=f"DELETE from {tableName} WHERE {columnName}='{name}' AND {match[0]}='{match[1]}' "
                else:
                    sql=f"DELETE from {tableName} WHERE {columnName}='{name}' AND {match[0]}='{match[1]}' "
                    data = 'no exist match user'
                    return data
            except Exception as e:
                print(f"ERROR: {e}")
                return False
        else:
            try:
                """
                find exist name to be erase

                find_name = crusor.execute(f'SELECT * FROM {tableName} WHERE {columnName}="{name}"')
                equal_name = crusor.fetchone()
                """
                data = True

                find_name = crusor.execute(f'SELECT * FROM {tableName} WHERE {columnName}="{name}"')
                equal_name = crusor.fetchone()
                if equal_name:
                    sql=f"DELETE from {tableName} WHERE {columnName}='{name}'"
                else:
                    print('No exist')
                    data = 'no exist match user'
            except Exception as e:
                print(f"ERROR: {e}")
                return False
        try:
            """Always will be executed"""
            crusor.execute(sql)
            conn.commit(),crusor.close(),conn.close()
            return data
        except Exception as e:
            print(f"ERROR: {e}")
            return False

if __name__ == '__main__':
    Instance_mysqlite_db = mysqlite_db

    # Server = 'localhost'
    # Username = 'root'
    # Password = 'xavier007 '

    # data_write ={
    #             'user_name':'TEXT',
    #             'user_id':'TEXT',
    #             'date_time':'TEXT',
    #             'date_time':'TEXT',
    #             'amount_trx':'TEXT',
    #             'from_wallet':'TEXT',
    #             'to_wallet':'TEXT',
    #             'block_hash':'TEXT',
    #             'transaction_hash':'TEXT',
    #             }

    data_price ={
                'trx_price'     :'TEXT',
                'matic_price'   :'TEXT',
                'bnb_price'     :'TEXT',
                }
    data_write ={
                'date_time'     :'TEXT',
                'user_name'     :'TEXT',
                'user_id'       :'TEXT',
                # =========================
                'wallet_matic'  :'TEXT',
                'wallet_binance':'TEXT',
                'wallet_tron'   :'TEXT',

                # =========================
                'key_matic_bnb' :'TEXT',
                'key_tron'      :'TEXT',
                # =========================
                'amount_matic'  :'TEXT',
                'amount_tron'   :'TEXT',
                'amount_binance':'TEXT',
                # =========================
                'inernal_wallet_matic':'TEXT',
                'inernal_wallet_tron':'TEXT',
                'game_balance'  :'TEXT',

                }

    # open database
    connection_db    = Instance_mysqlite_db.sqlite_connection(namedatabase=".book_user.db")
    connection_price = Instance_mysqlite_db.sqlite_connection(namedatabase=".book_price.db")

    #=========================================== creation database ===========================================
    Instance_mysqlite_db.CreateTableDatabase(connected=connection_db,tableName="register_user",column=data_write)
    Instance_mysqlite_db.CreateTableDatabase(connected=connection_price,tableName="coin_price",column=data_price)
    #=========================================== find all data table
    # find_all = Instance_mysqlite_db.sqlite_find_all(connected=connection_db,tableName='book_orders')
    #=========================================== find by name
    # name = Instance_mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='book_orders',columnName='user_name',fetch='all') #fetch=5,all                                 #by tabl+column
    # name = Instance_mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='book_orders',columnName='user_name',name='street') #fetch=5,all                               #by tabl+column
    # name = Instance_mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='book_orders',columnName='user_name',name='xxxx',match=['to_wallet','']) #fetch=5,all     #by tbl+column+match(column,name)
    #=========================================== write data
    # write_data = Instance_mysqlite_db.sqlite_write_data(connected=connection_db,tableName='book_orders',columnValue=('pedro','pedro','pedro','pedro','pedro','pedro','pedro','pedro'))
    #=========================================== update data
    # update_data = Instance_mysqlite_db.sqlite_update_data(connected=connection_db,tableName='book_orders',changeData=('user_name','data'),byData=('user_name','data'))
    # update_data = Instance_mysqlite_db.sqlite_update_data(connected=connection_db,tableName='book_orders',changeData=('user_name','sas'),byData=('user_name','xxxx'),match=['block_hash',''])
    #=========================================== remove data
    # remove_data = Instance_mysqlite_db.sqlite_remove_data(connected=connection_db,tableName='book_orders',columnName='user_name',name='pedro')
    # remove_data = Instance_mysqlite_db.sqlite_remove_data(connected=connection_db,tableName='book_orders',columnName='user_name',name='pedro',match=['block_hash','200'])
    #===========================================================================================================

    # print(name)
    # print(len(find_all)) #< to know all data in
    # print(write_data)
    # print(update_data)
    # print(remove_data)