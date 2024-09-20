import telebot
import os

from core import library_telebot
from core import library_lenguage
from core import library_sqlite

# bot de original
# bot = telebot.TeleBot(token="7140060249:AAFt5XKfd4NY0U98y_FkaIjTSP75XlVf26U")

# bot prueba chat0gpt
bot = telebot.TeleBot(token="6481554552:AAFrjGgpIykDhzZLFcr0rGqqUb21xCLKC58")

# my_token
## 2m4xn2jNiqxdWoTpQI6yePycVtL_6QhVhZnn1ykjEVptKTKSD
#ngrok config add-authtoken 2m4xn2jNiqxdWoTpQI6yePycVtL_6QhVhZnn1ykjEVptKTKSD
#ngrok http http://localhost:8080
#
# 2fa
# ngrock HT3MVPEWGNABYMW3IS3CSOPOIUBCNTJG
#
#

client_registered: dict ={}

data_buttons = {
    'start': [
        '💼 Mi informacion', '📍 Establecer Ruta', '',
        '🏁 Viajar ahora 🏁', '', '',
        '⚙️ Configuracion', '👋 Ayuda', '',
        # '✍️ Registrarse'
    ],
    # ========
    '✍️ Registrarse': [
        '✍️ Registrarse como Viajero',
        '🛞 Registrarse como Conductor',
        '◀️ Atras',
    ],
    '✍️ Registrarse como Viajero': [
        '⏭ Registro Viajero', '', '',
        '◀️ Atras'
    ],
    '🛞 Registrarse como Conductor': [
        '⏭ Registro Conductor', '', '',
        '◀️ Atras'
    ],
    '📍 Establecer Ruta': [
        '💼 Mostrar informacion de mi Ruta', '', '',
        '↗️ Ruta de salida', '↘️ Ruta de destino', '',
        '🔄 Viajar en mi ciudad', '', '',
        '◀️ Atras',
    ],
    '⚙️ Configuracion': [
        '🌟 Calificame', '✍️ Registrarse', '',
        '👨‍👩‍👦‍👦 Unirse al grupo', '','',
        '🏁 Modelos vehiculos', '🔄 Version App', '',
        '🗳 Total de votos','◀️ Atras'
    ],
    '🏁 Viajar ahora 🏁': [
        '🐴 Coche Tradicional',
        '🐴 Coche Guaguita',
        '🐴 Coche Carretonero',
        '🚲 Bici Taxi',
        '🛺 Moto Taxi',
        '🛵 Motorina',
        '🚕 Automobil',
        '🛻 Camionetas',
        '🚚  Camiones',
        '💼 Mi informacion',
        '◀️ Atras',
    ],
    'modo_conductor':[
        '💼 Mostrar informacion de mi Ruta', '', '',
        '↗️ Ruta de salida', '↘️ Ruta de destino', '',
        '🔄 Viajar en mi ciudad', '', '',
        '◀️ Atras',
    ],
}

#============================================================================================ CHECK DATABASE

def check_data_exist(message,return_just_data: bool=False):
    data_returned = check_user_in_database(message=message)

    if data_returned:
        tmp_returned = data_returned[1][0]



        message_formated = library_lenguage.read_header(data='CLIENT_EXIT')
        message_formated = message_formated.replace('TYPE_USER',tmp_returned[0])
        message_formated = message_formated.replace('TYPE_NAME',tmp_returned[2])
        message_formated = message_formated.replace('TYPE_NUMBER',tmp_returned[5])
        message_formated = message_formated.replace('TYPE_ORIGIN',tmp_returned[7])
        message_formated = message_formated.replace('TYPE_DESTINY',tmp_returned[8])

        if tmp_returned[0] == "Conductor":
            new_connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
            fided_data = mysqlite_db.sqlite_find_by_name(
                                                        connected=new_connection_db,
                                                        tableName='Drivers_Users',
                                                        columnName='id_account', # <=== check by id
                                                        name=message
                                                        )

            if not fided_data:
                return False , "register route"

            tmp_returned_driver = fided_data[0]


            # Return just all real data to check
            if return_just_data:
                return tmp_returned_driver

            message_formated = library_lenguage.read_header(data='CLIENT_EXIT')

            message_formated = message_formated.replace('TYPE_USER',tmp_returned_driver[0])
            message_formated = message_formated.replace('TYPE_NAME',tmp_returned_driver[2])
            message_formated = message_formated.replace('TYPE_NUMBER',tmp_returned_driver[5])
            message_formated = message_formated.replace('TYPE_ORIGIN',tmp_returned_driver[7])
            message_formated = message_formated.replace('TYPE_DESTINY',tmp_returned_driver[8])


            return data_returned ,message_formated

        if tmp_returned[0] == "Cliente":
            new_connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
            fided_data = mysqlite_db.sqlite_find_by_name(
                                                        connected=new_connection_db,
                                                        tableName='Clients_Users',
                                                        columnName='id_account', # <=== check by id
                                                        name=message
                                                        )

            if not fided_data:
                return False , "register route"

            tmp_returned_driver = fided_data[0]

            # Return just all real data to check
            if return_just_data:
                return tmp_returned_driver

            message_formated = library_lenguage.read_header(data='CLIENT_EXIT')

            message_formated = message_formated.replace('TYPE_USER',tmp_returned_driver[0])
            message_formated = message_formated.replace('TYPE_NAME',tmp_returned_driver[2])
            message_formated = message_formated.replace('TYPE_NUMBER',tmp_returned_driver[5])
            message_formated = message_formated.replace('TYPE_ORIGIN',tmp_returned_driver[7])
            message_formated = message_formated.replace('TYPE_DESTINY',tmp_returned_driver[8])

            return data_returned ,message_formated

        return data_returned ,message_formated
    else:

        return data_returned , False

def check_user_in_database(message):
    connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database', '.mi_botella_database.db'))
    fided_data = mysqlite_db.sqlite_find_by_name(
                                                connected=connection_db,
                                                tableName='All_Users',
                                                columnName='id_account', # <=== check by id
                                                name=message
                                                )

    if fided_data:
        return True ,fided_data
    else:
        return False


def update_database(
                    table_name: str = "",
                    change_column: str = "",
                    data_old: str = "",
                    data_to_update: str = "",
                    ):

    connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database', '.mi_botella_database.db'))
    update_data = mysqlite_db.sqlite_update_data(
                                                    connected=connection_db,
                                                    tableName=table_name,
                                                    changeData=(change_column, data_old),   # get data
                                                    byData=(change_column, data_to_update), # change data
    )
    # print('====================')
    # print(f'[+] table_name: {table_name} change_column {change_column}')
    # print(f'[+] old {data_old} new {data_to_update}')
    # print('====================')

#============================================================================================ CLIENT


def client_number(message):
    tmp_message = message.text
    # print(f'El numero ingresado es: {tmp_message}:')
    client_registered[message.chat.id]['number'] = tmp_message
    # print(f'datos completados\n\n{client_registered}')

    tmp_data = client_registered.get(message.chat.id)
    message_formated = library_lenguage.read_header(data='CLIENT_REGISTER')
    message_formated = message_formated.replace('TYPE_USER',tmp_data.get('type'))
    message_formated = message_formated.replace('TYPE_NAME',tmp_data.get('name'))
    message_formated = message_formated.replace('TYPE_NUMBER',tmp_data.get('number'))

    var_tmp = bot.send_message(message.chat.id, message_formated)

    # SET DATA IN MYSQL
    """
    CONPOSITATION OF DATABASE:

                   'type_acc':'TEXT', # client / driver
                 'id_account':'TEXT',
                  'real_name':'TEXT',
               'name_account':'TEXT',
              'telegram_name':'TEXT',
               'phone_number':'TEXT',
              'time_creation':'TEXT',
               'origin_local':'TEXT',
              'destiny_route':'TEXT',
         'transport_capacity':'TEXT', # False True
            'photo_transport':'TEXT', # False True
    """
    connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
    mysqlite_db.sqlite_write_data(
                                    connected=connection_db,
                                    tableName='Clients_Users',
                                  columnValue=(
                                               tmp_data.get('type'), # type_acc             # client / driver
                                 message.json.get('from').get('id'), # id_account
                                               tmp_data.get('name'), # real_name
                           message.json.get('from').get('username'), # name_account
                         message.json.get('from').get('first_name'), # telegram_name
                                             tmp_data.get('number'), # phone_number
                                                            'False', # time_creation        # False True
                                                            'False', # origin_local         # False True
                                                            'False', # destiny_route        # False True
                                                            'False', # model transport       # False True
                                                            'False', # transport_capacity   # False True
                                                            'False', # photo_transport      # False True
                                    ))
    connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
    mysqlite_db.sqlite_write_data(
                                    connected=connection_db,
                                    tableName='All_Users',
                                  columnValue=(
                                               tmp_data.get('type'), # type_acc             # client / driver
                                 message.json.get('from').get('id'), # id_account
                                               tmp_data.get('name'), # real_name
                           message.json.get('from').get('username'), # name_account
                         message.json.get('from').get('first_name'), # telegram_name
                                             tmp_data.get('number'), # phone_number
                                                            'False', # time_creation        # False True
                                                            'False', # origin_local         # False True
                                                            'False', # destiny_route        # False True
                                                            'False', # model transport       # False True
                                                            'False', # transport_capacity   # False True
                                                            'False', # photo_transport      # False True
                                    ))
    # print('CLIENT: ',client_registered[message.chat.id])

    del client_registered[message.chat.id]

def client_name(message):
    tmp_message = message.text
    # print(f'show name: {tmp_message}:')

    client_registered[message.chat.id]={'type':'Cliente'}
    client_registered[message.chat.id]['name']=tmp_message

    message_formated = library_lenguage.read_header(data='CLIENT_NUMBER')
    bot.send_chat_action(message.chat.id, 'typing')
    var_tmp = bot.send_message(message.chat.id, message_formated)
    bot.register_next_step_handler(var_tmp,
                                    client_number)

#============================================================================================ DRIVERS

def driver_capacity(message):
    tmp_message = message.text
    # print(f'show capaticy: {tmp_message}:')

    client_registered[message.chat.id]['capacity']=tmp_message
    bot.send_chat_action(message.chat.id, 'typing')

    tmp_data = client_registered.get(message.chat.id)
    message_formated = library_lenguage.read_header(data='REGISTER')
    message_formated = message_formated.replace('TYPE_USER',tmp_data.get('type'))
    message_formated = message_formated.replace('TYPE_NAME',tmp_data.get('name'))
    message_formated = message_formated.replace('TYPE_NUMBER',tmp_data.get('number'))
    message_formated = message_formated.replace('TYPE_CAR',tmp_data.get('car'))
    message_formated = message_formated.replace('TYPE_CAPACITY',tmp_data.get('capacity'))

    var_tmp = bot.send_message(message.chat.id, message_formated)

    # SET DATA IN MYSQL
    connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
    mysqlite_db.sqlite_write_data(
                                            connected=connection_db,
                                            tableName='Drivers_Users',
                                          columnValue=(
                                               tmp_data.get('type'), # type_acc             # client / driver
                                 message.json.get('from').get('id'), # id_account
                                               tmp_data.get('name'), # real_name
                           message.json.get('from').get('username'), # name_account
                         message.json.get('from').get('first_name'), # telegram_name
                                             tmp_data.get('number'), # phone_number
                                                            'False', # time_creation        # False True
                                                            'False', # origin_local         # False True
                                                            'False', # destiny_route        # False True
                                                tmp_data.get('car'), # model transport       # False True
                                           tmp_data.get('capacity'), # transport_capacity   # False True
                                                            'False', # photo_transport      # False True
                                    ))

    connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
    mysqlite_db.sqlite_write_data(
                                            connected=connection_db,
                                            tableName='All_Users',
                                          columnValue=(
                                               tmp_data.get('type'), # type_acc             # client / driver
                                 message.json.get('from').get('id'), # id_account
                                               tmp_data.get('name'), # real_name
                           message.json.get('from').get('username'), # name_account
                         message.json.get('from').get('first_name'), # telegram_name
                                             tmp_data.get('number'), # phone_number
                                                            'False', # time_creation        # False True
                                                            'False', # origin_local         # False True
                                                            'False', # destiny_route        # False True
                                                tmp_data.get('car'), # model transport       # False True
                                           tmp_data.get('capacity'), # transport_capacity   # False True
                                                            'False', # photo_transport      # False True
                                    ))

    # print('DRIVER: ',client_registered[message.chat.id])

    del client_registered[message.chat.id]

def driver_number(message):
    tmp_message = message.text
    # print(f'show number: {tmp_message}:')

    client_registered[message.chat.id]['number']=tmp_message

    message_formated = library_lenguage.read_header(data='DRIVER_CAPACITY')
    bot.send_chat_action(message.chat.id, 'typing')
    var_tmp = bot.send_message(message.chat.id, message_formated)
    bot.register_next_step_handler(var_tmp,
                                    driver_capacity)

def driver_cars(message):
    tmp_message = message.text
    # print(f'show car: {tmp_message}:')

    client_registered[message.chat.id]['car']=tmp_message

    message_formated = library_lenguage.read_header(data='DRIVER_NUMBER')
    bot.send_chat_action(message.chat.id, 'typing')
    var_tmp = bot.send_message(message.chat.id, message_formated)
    bot.register_next_step_handler(var_tmp,
                                    driver_number)

def driver_name(message):
    tmp_message = message.text
    # print(f'show name: {tmp_message}:')

    client_registered[message.chat.id]={'type':'Conductor'}
    client_registered[message.chat.id]['name']=tmp_message

    message_formated = library_lenguage.read_header(data='DRIVER_VEHICUL')
    bot.send_chat_action(message.chat.id, 'typing')
    var_tmp = bot.send_message(message.chat.id, message_formated)
    bot.register_next_step_handler(var_tmp,
                                    driver_cars)
#=====================================================================================================================================================
#=================================================================== START BOT =======================================================================
#=====================================================================================================================================================

@bot.message_handler(func=lambda message:True)
def all_messages(message):
    MESSAGE_ID = message.chat.id
    MESSAGE    = message.text

    # ===================================== MENU ================================
    if '/start' ==  MESSAGE or '◀️ Atras' ==  MESSAGE or  '/atras' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        message_formated = library_lenguage.read_header(data='NOTA')
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='start',
                    dict_buttons=data_buttons,
                    row_number=3,
                    message=message_formated,
                    # resize=True,
                    # show_keyboard=False,
                    )

    elif '/registrarse' == MESSAGE or '✍️ Registrarse' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='✍️ Registrarse',
                    dict_buttons=data_buttons,
                    row_number=1,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )
    elif 'Actualizar Posicion' == MESSAGE or '/Actualizar_Posicion' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Actualizar Posicion',
                    dict_buttons=data_buttons,
                    row_number=3,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )
    elif '⚙️ Configuracion' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='⚙️ Configuracion',
                    dict_buttons=data_buttons,
                    row_number=3,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )
    elif '🏁 Viajar ahora 🏁' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''

        message_formated = check_data_exist(message=MESSAGE_ID,return_just_data=True)

        if not message_formated[1] == 'register route':

            # print(message_formated[1])
            if not bool(message_formated[0]):
                message_formated = library_lenguage.read_header(data='NOTA')
                tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

            else:
                if message_formated[7] == "False":
                    message_formated = library_lenguage.read_header(data='SEND_INFO')
                    tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)
                else:

                    # print(message_formated,'xxxxxxxxxxxxxxxxxxxxxxxxxx')
                    if message_formated[0] == 'Conductor':
                        tele_bot.tele_buttons(
                                bot = bot,
                                message_id=MESSAGE_ID,
                                key_dict_buttons='modo_conductor',
                                dict_buttons=data_buttons,
                                row_number=3,
                                message=f"Bienvenido al menu de {MESSAGE}",
                                # resize=True,
                                # show_keyboard=False,
                                )
                    else:
                        tele_bot.tele_buttons(
                                bot = bot,
                                message_id=MESSAGE_ID,
                                key_dict_buttons='🏁 Viajar ahora 🏁',
                                dict_buttons=data_buttons,
                                row_number=3,
                                message=f"Bienvenido al menu de {MESSAGE}",
                                # resize=True,
                                # show_keyboard=False,
                                )
        else:
            message_formated = library_lenguage.read_header(data='CLIENT_EXIT_LAS_CONFIG')
            tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    elif '🛞 Registrarse como Conductor' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''

        data_returned = check_user_in_database(message=MESSAGE_ID)
        if data_returned:
            message_formated = library_lenguage.read_header(data='CLIENT_EXIT_LAS_CONFIG')
            tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)
        else:
            tele_bot.tele_buttons(
                        bot = bot,
                        message_id=MESSAGE_ID,
                        key_dict_buttons='🛞 Registrarse como Conductor',
                        dict_buttons=data_buttons,
                        row_number=3,
                        message=f"Bienvenido al menu de {MESSAGE}",
                        # resize=True,
                        # show_keyboard=False,
                        )
    elif '✍️ Registrarse como Viajero' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        data_returned = check_user_in_database(message=MESSAGE_ID)
        if data_returned:
            message_formated = library_lenguage.read_header(data='CLIENT_EXIT_LAS_CONFIG')
            tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

        else:
            tele_bot.tele_buttons(
                        bot = bot,
                        message_id=MESSAGE_ID,
                        key_dict_buttons='✍️ Registrarse como Viajero',
                        dict_buttons=data_buttons,
                        row_number=3,
                        message=f"Bienvenido al menu de {MESSAGE}",
                        # resize=True,
                        # show_keyboard=False,
                        )

    elif '📍 Establecer Ruta' == MESSAGE or '/cual_es_mi_ruta' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='📍 Establecer Ruta',
                    dict_buttons=data_buttons,
                    row_number=3,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )
    # ================================================= ADMIN
    elif '/set_help' == MESSAGE: # will capture text of press buttons
        if MESSAGE.startswith('/set_help'):
            message_formated = library_lenguage.read_header(data='SET_HELP')
            tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    elif '/set_client' == MESSAGE or '⏭ Registro Viajero' == MESSAGE: # will capture text of press buttons

        # CHECK IF DATA EXIST
        data_returned , message_formated = check_data_exist(message=MESSAGE_ID)

        if data_returned:
            message_formated = f'Tiene una cuenta registrada en la plataforma:\n{message_formated}'
            tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

        else:
            bot.send_chat_action(message.chat.id, 'typing')
            message_formated = library_lenguage.read_header(data='CLIENT_NAME')

            var_tmp = bot.send_message(message.chat.id, message_formated)
            bot.register_next_step_handler(var_tmp,
                                            client_name)

    elif '/set_driver' == MESSAGE or '⏭ Registro Conductor' == MESSAGE: # will capture text of press buttons

        # CHECK IF DATA EXIST
        data_returned , message_formated = check_data_exist(message=MESSAGE_ID)

        if data_returned:
            message_formated = f'Tiene una cuenta registrada en la plataforma:\n{message_formated}'
            tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

        else:
            bot.send_chat_action(message.chat.id, 'typing')
            message_formated = library_lenguage.read_header(data='DRIVER_NAME')

            var_tmp = bot.send_message(message.chat.id, message_formated)
            bot.register_next_step_handler(var_tmp,
                                            driver_name)
    # ================================================= PLACE OR LOCATION
    elif '/app_version' == MESSAGE or '🔄 Version App' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        with open('CHANGELOG.md' , 'r') as f:
            message_formated = f.read()
            tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    elif '/unirse_al_grupo' == MESSAGE or '👨‍👩‍👦‍👦 Unirse al grupo'  == MESSAGE: # will capture text of press buttons
        message_formated = library_lenguage.read_header(data='GROUP')
        tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    elif '/califiar_app' == MESSAGE or '🌟 Calificame' == MESSAGE: # will capture text of press buttons
        tele_bot.congratulation( bot=bot,message_id=MESSAGE_ID,message='Formulario')

    elif '/total_votos' == MESSAGE: # will capture text of press buttons
        message_formated = f'Cantidad de votos: {"320"}\n\nVotos:\n\nPersonas que le gustan la App {"150"}\nPersonas que no les gusta: {"25"}\n\n'
        tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    elif '↗️ Ruta de salida' == MESSAGE or '🔄 Viajar en mi ciudad' == MESSAGE or '/ruta_origen' == MESSAGE:
        data_returned = check_user_in_database(message=MESSAGE_ID)

        if not data_returned:
            message_formated = library_lenguage.read_header(data='NOTA')
            tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

        else:
            message_formated = library_lenguage.read_header(data='ORIGIN_PLACE')
            tele_bot.send_message( bot=bot, type_msg='message' ,message_id=MESSAGE_ID, message=message_formated )
            # SET LOCATION

    elif '↘️ Ruta de destino' == MESSAGE or '/ruta_destino' == MESSAGE:
        data_returned = check_user_in_database(message=MESSAGE_ID)

        if not data_returned:
            message_formated = library_lenguage.read_header(data='NOTA')
            tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

        else:
            message_formated = library_lenguage.read_header(data='FINISH_PLACE')
            tele_bot.send_message( bot=bot, type_msg='message' ,message_id=MESSAGE_ID, message=message_formated )
            # SET LOCATION
    # ================================================= ADMIN
    elif '🏁 Modelos vehiculos' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        message_formated = library_lenguage.read_header(data='DRIVER_CAR')
        tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    elif '💼 Mi informacion' == MESSAGE or '💼 Mostrar informacion de mi Ruta' == MESSAGE: # will capture text of press buttons
        # CHECK IF DATA EXIST
        data_returned , message_formated = check_data_exist(message=MESSAGE_ID)

        if data_returned:
            message_formated = f'Tiene una cuenta registrada en la plataforma:\n{message_formated}'
            tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

        else:
            message_formated = library_lenguage.read_header(data='NOTA')
            tele_bot.send_message( bot=bot, type_msg='message' ,message_id=MESSAGE_ID, message=message_formated )

    elif '/users' == MESSAGE: # will capture text of press buttons
        data_returned = check_user_in_database(message=MESSAGE_ID)

        # print(data_returned,'<<<<<<<<<<<<<<<<<<<<<')

    elif '🐴 Coche Tradicional' == MESSAGE or \
         '🐴 Coche Guaguita' == MESSAGE or \
         '🐴 Coche Carretonero' == MESSAGE or \
         '🚲 Bici Taxi' == MESSAGE or \
         '🛺 Moto Taxi' == MESSAGE or \
         '🛵 Motorina' == MESSAGE or \
         '🚕 Automobil' == MESSAGE or \
         '🛻 Camionetas' == MESSAGE or \
         '🚚  Camiones' == MESSAGE or \
         '💼 Mi informacion' == MESSAGE:

        data_returned = check_user_in_database(message=MESSAGE_ID)

        if data_returned[0]:

            list_data = data_returned[1][0]
            type_client = list_data[0]
            id_client = list_data[1]


            #FIND CLIENT EXACTLY DESTINY ROUTE
            connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
            client_finded = mysqlite_db.sqlite_find_by_name(
                                                        connected=connection_db,
                                                        tableName='Clients_Users',
                                                        columnName='id_account',
                                                        name=id_client
                                                        )


            data_dict_returned = library_lenguage.read_header(data='MODEL_CAR')

            if client_finded:
                origin_route = client_finded[0][7]
                destiny_route = client_finded[0][8]
                model_car = data_dict_returned.get(MESSAGE)
                # FIND IN DRIVER TABLE EXACTLY CAR TYPE
                # if destiny is same
                #
                connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
                driver_finded = mysqlite_db.sqlite_find_by_name(
                                                            connected=connection_db,
                                                            tableName='Drivers_Users',
                                                            columnName='destiny_route',
                                                            name=destiny_route,
                                                            fetch='all',
                                                            # match=["model_car",model_car], # Uncoment to only apear model car <=======================
                                                            )

                # print(driver_finded)
                message_formated: str=""

                if driver_finded:

                    for _ in driver_finded:

                        # if find one existing driver return driver name and phone route
                        user_name=_[2]
                        phone_number=_[5]
                        source_route=_[7]
                        destiny_route=_[8]
                        model_car=_[9]
                        capacity_route=_[10]

                        # DRIVER DATA
                        # message_formated+=f"{user_name}\n{phone_number}\n{destiny_route}\n{model_car} \n{capacity_route}\n"
                        tmp_string=library_lenguage.read_header(data='DRIVER_DATA')
                        tmp_string=tmp_string.replace('USER_NAME',user_name)
                        tmp_string=tmp_string.replace('USER_PHONE',phone_number)
                        tmp_string=tmp_string.replace('TRANSPORT',model_car)
                        tmp_string=tmp_string.replace('CAPACITY',capacity_route)
                        # message_formated=message_formated.replace('SOURCE',source_route)
                        message_formated+=tmp_string.replace('DESTINY',destiny_route)
                        # message_formated+=message_formated.replace()

                    message_formated+="--------------------------------------------------------------------------------------------"
                    tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)
                else:
                    message_formated = library_lenguage.read_header(data='NO_EXIT_DATABASE')
                    tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

            else:
                message_formated = library_lenguage.read_header(data='NO_EXIT_DATABASE')
                tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)



    else:
        # check_name = all_citys.get(MESSAGE,'known')

        if MESSAGE.startswith('/__'):

            data_returned = check_user_in_database(message=MESSAGE_ID)

            if not data_returned:
                message_formated = library_lenguage.read_header(data='NOTA')
                tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

            else:

                message_formated = library_lenguage.read_header(data='CHECK_CITYS')
                original_string = MESSAGE.strip('/__')

                if original_string in message_formated:
                    tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=f"Se ha actualizado en la base de datos lugar destino donde va a viajar: \n\nUsted esta viajando desde: {original_string} \n\nUsted puede consultar en datos, que tenga un buen viaje...")

                    # UPDATE DESTINY ROUTE
                    connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
                    fided_data = mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='All_Users',columnName='id_account',name=MESSAGE_ID)

                    type_account  = fided_data[0][0] # CLient / Driver

                    # origin_route  = fided_data[0][7]
                    # destiny_route = fided_data[0][8]

                    # # cliente
                    # print('client: //////////////////// ',type_account,'<<<<<< stype')
                    # print('client: //////////////////// ',origin_route,"origin")
                    # print('client: //////////////////// ',destiny_route,"destiny")

                    if type_account == 'Cliente':
                        connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
                        fided_data = mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='CLients_Users',columnName='id_account',name=MESSAGE_ID)
                        destiny_route = fided_data[0][8]

                        update_database(
                                        table_name='Clients_Users',
                                        change_column='destiny_route',
                                        data_old=destiny_route,
                                        data_to_update=original_string,
                                        )
                    elif type_account == 'Conductor':
                        connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
                        fided_data = mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='Drivers_Users',columnName='id_account',name=MESSAGE_ID)
                        destiny_route = fided_data[0][8]

                        update_database(
                                        table_name='Drivers_Users',
                                        change_column='destiny_route',
                                        data_old=destiny_route,
                                        data_to_update=original_string,
                                        )


                else:
                    tele_bot.send_message( bot=bot, type_msg='message' ,message_id=MESSAGE_ID, message='/ayuda_usuario' )

        else:
            if MESSAGE.startswith('/_'):

                data_returned = check_user_in_database(message=MESSAGE_ID)

                if not data_returned:
                    message_formated = library_lenguage.read_header(data='NOTA')
                    tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

                else:

                    message_formated = library_lenguage.read_header(data='CHECK_CITYS')
                    original_string = MESSAGE.strip('/_')

                    if original_string in message_formated:

                        tele_bot.send_message(
                                                bot=bot,
                                                type_msg='message',
                                                message_id=MESSAGE_ID,
                                                message=f"Se ha actualizado en la base de datos lugar actual donde se encuentra: \n\nUsted esta viajando desde: {original_string} \n\nUsted puede consultar en datos, que tenga un buen viaje..."
                                                )

                        # UPDATE SOURCE ROUTE
                        connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
                        fided_data = mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='All_Users',columnName='id_account',name=MESSAGE_ID)

                        type_account  = fided_data[0][0] # CLient / Driver

                        # origin_route  = fided_data[0][7]
                        # destiny_route = fided_data[0][8]
                        # # cliente
                        # print('client: //////////////////// ',type_account,'<<<<<< stype')
                        # print('client: //////////////////// ',origin_route,"origin")
                        # print('client: //////////////////// ',destiny_route,"destiny")

                        if type_account == 'Cliente':
                            connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
                            fided_data = mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='CLients_Users',columnName='id_account',name=MESSAGE_ID)
                            type_account  = fided_data[0][0] # CLient / Driver
                            origin_route  = fided_data[0][7]
                            destiny_route = fided_data[0][8]

                            update_database(
                                            table_name='Clients_Users',
                                            change_column='origin_local',
                                            data_old=origin_route,
                                            data_to_update=original_string,
                                            )
                            update_database(
                                            table_name='Clients_Users',
                                            change_column='destiny_route',
                                            data_old=destiny_route,
                                            data_to_update=original_string,
                                            )
                        elif type_account == 'Conductor':
                            connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))
                            fided_data = mysqlite_db.sqlite_find_by_name(connected=connection_db,tableName='Drivers_Users',columnName='id_account',name=MESSAGE_ID)
                            type_account  = fided_data[0][0] # CLient / Driver
                            origin_route  = fided_data[0][7]
                            destiny_route = fided_data[0][8]

                            update_database(
                                            table_name='Drivers_Users',
                                            change_column='origin_local',
                                            data_old=origin_route,
                                            data_to_update=original_string,
                                            )
                            update_database(
                                            table_name='Drivers_Users',
                                            change_column='destiny_route',
                                            data_old=destiny_route,
                                            data_to_update=original_string,
                                            )
                        # print(f"""
                        #     Telegram: @{message.json.get('from').get('username')}
                        #     ID: {message.json.get('from').get('id')}
                        #     usuario: {message.json.get('from').get('first_name')}
                        #     texto: {message.json.get('text')}
                        #     """)
                    else:
                        tele_bot.send_message( bot=bot, type_msg='message' ,message_id=MESSAGE_ID, message='/ayuda_usuario' )

if __name__ == '__main__':
    tele_bot = library_telebot.tele_bot
    MenuCommand = library_telebot.tele_bot.MenuCommand

    # Create connction to dataase
    mysqlite_db = library_sqlite.mysqlite_db

    list_all_commands = {
                        'start':'👟 Comenzar cuenta',
                        'registrarse':'✍️ Registrar cuenta',
                        'unirse_al_grupo':'👥 Grupo Mi motella',
                        'califiar_app':'🤙 Su Calificacion',
                        'donacion':'💰 Gracias por su aporte',
                        'app_version':'🔄 Version de la App',
                        'ayuda':'🆘 Ayuda general',
                        }
    try:
        # MenuCommand(bot,list_all_commands)
        bot.infinity_polling(skip_pending=True)
        # bot.infinity_polling()
    except Exception as e:
        os.system('clear')
        line = "="*30
        print(f'\n\n{line}\n\PORFAVOR VERIFIQUE SU INTERNET\n\n{line}\n\n{e}\n\n{line}\n\n\n')