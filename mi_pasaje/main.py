import telebot
import os

from core import library_telebot
from core import library_lenguage
from core import library_sqlite

# bot de prueba
bot = telebot.TeleBot(token="6636435110:AAEEbWZ9v_EhT_dDbzZvfTUX6gufLBEbVto")

# bot original
# bot = telebot.TeleBot(token="7519838417:AAEgpcGFQCbHjuVNP14i2V02Bm0Zfa0cI2A")

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
        'Mi informacion', 'Establecer Ruta', '',
        'Viajar ahora', '', '',
        'Configuracion', 'Ayuda del Usuario', ''
    ],
    # ========
    'Registrarse': [
        'Registrarse como Viajero',
        'Registrarse como Conductor',
        'Atras',
    ],
    'Registrarse como Viajero': [
        'Comenzar Registro Viajero', '', '',
        'Atras'
    ],
    'Registrarse como Conductor': [
        'Comenzar Registro Conductor', '', '',
        'Atras'
    ],
    'Establecer Ruta': [
        'Mostrar informacion de mi Ruta', '', '',
        'Ruta salida ?', 'Ruta destino ?', '',
        'Ruta En mi localidad', '', '',
        'Atras',
    ],
    'Configuracion': [
        'Calificame', '', '',
        'Unirse al grupo', 'Modelos vehiculos', '',
        'Total de votos', 'Version App', 'Registrarse',
        'Atras'
    ],
    'Viajar ahora': [
        'Coche_tradicional',
        'Coche_Guaguita',
        'Coche_planchero',
        'Bici_taxi',
        'Moto_taxi',
        'Motorina_taxi',
        'Automobil',
        'Camiones',
        'Camionetas',
        'Atras',
    ],
}


#=========================== CLIENT
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
    print('CLIENT: ',client_registered[message.chat.id])

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

#=========================== DRIVER
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
    print('DRIVER: ',client_registered[message.chat.id])

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

#=========================== START BOT
@bot.message_handler(func=lambda message:True)
def all_messages(message):
    MESSAGE_ID = message.chat.id
    MESSAGE    = message.text

    # ===================================== MENU ================================
    if '/start' ==  MESSAGE or 'Atras' ==  MESSAGE or  '/atras' == MESSAGE: # will capture text of press buttons
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

    elif '/registrarse' == MESSAGE or 'Registrarse' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Registrarse',
                    dict_buttons=data_buttons,
                    row_number=2,
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
    elif 'Configuracion' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Configuracion',
                    dict_buttons=data_buttons,
                    row_number=3,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )
    elif 'Viajar ahora' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Viajar ahora',
                    dict_buttons=data_buttons,
                    row_number=3,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )
    elif 'Registrarse como Conductor' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Registrarse como Conductor',
                    dict_buttons=data_buttons,
                    row_number=3,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )
    elif 'Registrarse como Viajero' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''


        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Registrarse como Viajero',
                    dict_buttons=data_buttons,
                    row_number=3,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )

    elif 'Establecer Ruta' == MESSAGE or '/cual_es_mi_ruta' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Establecer Ruta',
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

    elif '/set_client' == MESSAGE.split(':')[0] or 'Comenzar Registro Viajero' == MESSAGE: # will capture text of press buttons
        bot.send_chat_action(message.chat.id, 'typing')
        message_formated = library_lenguage.read_header(data='CLIENT_NAME')

        var_tmp = bot.send_message(message.chat.id, message_formated)
        bot.register_next_step_handler(var_tmp,
                                        client_name)

    elif '/set_driver' == MESSAGE.split(':')[0] or 'Comenzar Registro Conductor' == MESSAGE: # will capture text of press buttons
        bot.send_chat_action(message.chat.id, 'typing')
        message_formated = library_lenguage.read_header(data='DRIVER_NAME')

        var_tmp = bot.send_message(message.chat.id, message_formated)
        bot.register_next_step_handler(var_tmp,
                                        driver_name)
    # ================================================= PLACE OR LOCATION
    elif 'Donde estoy ahora?' == MESSAGE:
        message_formated = library_lenguage.read_header(data='ORIGIN_PLACE')
        tele_bot.send_message( bot=bot, type_msg='message' ,message_id=MESSAGE_ID, message=message_formated )
        # SET LOCATION

    elif 'Hacia donde voy?' == MESSAGE:
        message_formated = library_lenguage.read_header(data='FINISH_PLACE')
        tele_bot.send_message( bot=bot, type_msg='message' ,message_id=MESSAGE_ID, message=message_formated )
        # SET LOCATION

    elif 'Ruta salida ?' == MESSAGE or 'Ruta En mi localidad' == MESSAGE:
        message_formated = library_lenguage.read_header(data='ORIGIN_PLACE')
        tele_bot.send_message( bot=bot, type_msg='message' ,message_id=MESSAGE_ID, message=message_formated )
        # SET LOCATION

    elif 'Ruta destino ?' == MESSAGE:
        message_formated = library_lenguage.read_header(data='FINISH_PLACE')
        tele_bot.send_message( bot=bot, type_msg='message' ,message_id=MESSAGE_ID, message=message_formated )
        # SET LOCATION

    # ================================================= ADMIN

    elif 'Modelos vehiculos' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        message_formated = library_lenguage.read_header(data='DRIVER_CAR')
        tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    elif 'Version App' == MESSAGE or '/app_version' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        with open('CHANGELOG.md' , 'r') as f:
            message_formated = f.read()
            tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    elif '/unirse_al_grupo' == MESSAGE or 'Unirse al grupo'  == MESSAGE: # will capture text of press buttons
        message_formated = library_lenguage.read_header(data='GROUP')
        tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    elif '/califiar_app' == MESSAGE or 'Calificame' == MESSAGE: # will capture text of press buttons
        tele_bot.congratulation( bot=bot,message_id=MESSAGE_ID,message='Formulario')

    elif '/total_votos' == MESSAGE: # will capture text of press buttons
        message_formated = f'Cantidad de votos: {"320"}\n\nVotos:\n\nPersonas que le gustan la App {"150"}\nPersonas que no les gusta: {"25"}\n\n'
        tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    else:
        # check_name = all_citys.get(MESSAGE,'known')

        if MESSAGE.startswith('/__'):

            message_formated = library_lenguage.read_header(data='CHECK_CITYS')
            original_string = MESSAGE.strip('/__')

            if original_string in message_formated:
                tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=f"Se ha actualizado en la base de datos lugar destino donde va a viajar: \n\nUsted esta viajando desde: {original_string} \n\nUsted puede consultar en datos, que tenga un buen viaje...")
                print(f"""
                    Telegram: @{message.json.get('from').get('username')}
                    ID: {message.json.get('from').get('id')}
                    usuario: {message.json.get('from').get('first_name')}
                    texto: {message.json.get('text')}
                    """)
            else:
                tele_bot.send_message( bot=bot, type_msg='message' ,message_id=MESSAGE_ID, message='/ayuda_usuario' )

        else:
            if MESSAGE.startswith('/_'):
                message_formated = library_lenguage.read_header(data='CHECK_CITYS')
                original_string = MESSAGE.strip('/__')

                if original_string in message_formated:

                    tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=f"Se ha actualizado en la base de datos lugar actual donde se encuentra: \n\nUsted esta viajando desde: {original_string} \n\nUsted puede consultar en datos, que tenga un buen viaje...")
                    print(f"""
                        Telegram: @{message.json.get('from').get('username')}
                        ID: {message.json.get('from').get('id')}
                        usuario: {message.json.get('from').get('first_name')}
                        texto: {message.json.get('text')}
                        """)
                else:
                    tele_bot.send_message( bot=bot, type_msg='message' ,message_id=MESSAGE_ID, message='/ayuda_usuario' )

if __name__ == '__main__':
    tele_bot = library_telebot.tele_bot
    MenuCommand = library_telebot.tele_bot.MenuCommand

    # Create connction to dataase
    mysqlite_db = library_sqlite.mysqlite_db
    connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))

    list_all_commands = {
                        'registrarse':'Registrarse como usuario o conductor',
                        'start':'Lobby de bienvenida a Mi pasaje App',
                        'unirse_al_grupo':'Grupo creado para compartir ideas',
                        'califiar_app':'Calificame su opinion de la App',
                        'donacion':'Puede contruir con la App',
                        'app_version':'Version de la App Actualmente',
                        'ayuda':'Principales dudas',
                        }
    try:
        MenuCommand(bot,list_all_commands)
        bot.infinity_polling(skip_pending=True)
        # bot.infinity_polling()
    except Exception as e:
        os.system('clear')
        line = "="*30
        print(f'\n\n{line}\n\PORFAVOR VERIFIQUE SU INTERNET\n\n{line}\n\n{e}\n\n{line}\n\n\n')