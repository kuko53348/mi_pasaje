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

# all_citys = {

#     'Pinar_del_Rio':[
#             'Guanes',
#             'Mantua',
#             'Minas_Matahambre',
#             'Vinales',
#             'Pinar_San_Luis',
#             "S_Juan_Martinez",
#             'Pinar_del_Rio',
#             'Los_Palacios',
#             'Consolacion_Sur',
#             'La_Palma',
#             'Sandino',
#             'Atras',
#             ],
#     'Matanzas':[
#             'Matanzas ',
#             'Cárdenas',
#             'Martí',
#             'Colón',
#             'Perico',
#             'Jovellanos',
#             'Pedro_Betancourt',
#             'Limonar',
#             'Unión_Reyes',
#             'Ciénaga_Zapata',
#             'Jagüey_Grande',
#             'Calimete',
#             'Los_Arabos',
#             'Atras',
#             ],
#     'Ciego_Avila':[
#             'Bolivia',
#             'Majagua',
#             'Moron',
#             'Florencia',
#             'Ciego_Avila',
#             'Baragua',
#             'Venezuela',
#             'Ciro_Redondo',
#             'Primero_Enero',
#             'Chambas',
#             'Atras',
#             ],
#     'Artemisa':[
#             'Alquizar',
#             'Artemisa',
#             'S_Antonio_Banos',
#             'Caimito',
#             'Mariel',
#             'San_Cristobal',
#             'Guanajay',
#             'Bauta',
#             'Candelaria',
#             'Bahia_Honda',
#             'Guira_Melena',
#             'Atras',
#             ],
#     'Las_Tunas':[
#             'Jesus_Menendez',
#             'Manati',
#             'Colombia',
#             'Las_Tunas',
#             'Majibacoa',
#             'Puerto_Padre',
#             'Jobabo',
#             'Amancio',
#             'Atras',
#             ],
#     'La_Habana':[
#             'Plaza_Revolucion',
#             'Marianao',
#             'Cotorro',
#             'Cerro',
#             'Centro_Habana',
#             'Regla',
#             'S_Miguel_Padron',
#             'Boyeros',
#             'Habana_Vieja',
#             'Arrojo_Naranjo',
#             'Diez_Octubre',
#             'La_Lisa',
#             'Guanabacoa',
#             'Habana_del_Este',
#             'Playa',
#             'Atras',
#             ],
#     'Cienfuegos':[
#             'Cienfuegos',
#             'Aguada_Pasajeros',
#             'Abreus',
#             'Lajas',
#             'Rodas',
#             'Cruces',
#             'Palmira',
#             'Cumanayagua',
#             'Atras',
#             ],
#     'Holguin':[
#             'Frank_Pais',
#             'Cacocum',
#             'Rafael_Freyre',
#             'Banes',
#             'Mayari',
#             'Moa',
#             'Cueto',
#             'Holguin',
#             'Gibara',
#             'Sagua_Tanamo',
#             'Calixto_Garcia',
#             'Urbano_Noris',
#             'Antilla',
#             'Baguanos'
#             'Atras',
#             ],
#     'Santi_Spiritus':[
#             'Jatibonico',
#             'Santi_Spiritus',
#             'Cabaiguan',
#             'La_Sierpe',
#             'Yaguajay',
#             'Fomento',
#             'Taguasco',
#             'Trinidad',
#             'Atras',
#             ],
#     'Camaguey':[
#             'C_Jatibonico',
#             'Santa_Cruz_Sur',
#             'Camaguey',
#             'C_Manuel_Cespedes',
#             'Esmeralda',
#             'Najasa',
#             'Sierra_Cubitas',
#             'Minas',
#             'Nuevitas',
#             'Florida',
#             'Vertientes',
#             'Sibanicu',
#             'Atras',
#             ],
#     'Santiago_Cuba':[
#             'Pinar_San_Luis',
#             'Palma_Soriano',
#             'Segundo_Frente',
#             'Tercer_Frente',
#             'Contramaestre',
#             'Guama',
#             'Santiago_Cuba',
#             'Songo_la_Maya',
#             'Mella',
#             'Atras',
#             ],
#     'Granma':[
#             'Manzanillo',
#             'Buey_Arriba',
#             'Campechuela',
#             'Bartolome_Maso',
#             'Bayamo',
#             'Media_Luna',
#             'Pilón',
#             'Yara',
#             'Cauto_Cristo',
#             'Guisa',
#             'Río_Cauto',
#             'Jiguaní',
#             'Niquero',
#             'Atras',
#             ],
#     'Guantanamo':[
#             'Yateras',
#             'El_Salvador',
#             'Imias',
#             'Caimanera',
#             'Baracoa',
#             'Guantanamo',
#             'San_Antonio_Sur',
#             'Manuel_Tames',
#             'Maisi',
#             'Niceto_Perez',
#             'Atras',
#             ],
#     'Mayabeque':[
#             'Jaruco',
#             'Quivican',
#             'San_Jose_Lajas',
#             'Madruga',
#             'Guines',
#             'Santa_Cruz_Norte',
#             'Batabano',
#             'Nueva_Paz',
#             'Bejucal',
#             'Melena_del_Sur',
#             'San_Nicolas',
#             'Atras',
#             ],
#     'Villa_Clara':[
#             'Corralillo',
#             'Encrucijada',
#             'Santo_Domingo',
#             'Ranchuelo',
#             'Caibarien',
#             'Manicaragua',
#             'Cifuentes',
#             'Sagua_la_Grande',
#             'Atras',
#             ],
#     'Atras':['Atras'],
#         }

client_registered: dict ={}

#=========================== CLIENT
def client_number(message):
    tmp_message = message.text
    print(f'El numero ingresado es: {tmp_message}:')
    client_registered[message.chat.id]['number']=tmp_message

    print(f'datos completados\n\n{client_registered}')

    del client_registered[message.chat.id]


def client_name(message):
    tmp_message = message.text
    print(f'El nombre ingresado es: {tmp_message}:')

    client_registered[message.chat.id]={'type':'client'}
    client_registered[message.chat.id]['nombre']=tmp_message

    bot.send_chat_action(message.chat.id, 'typing')
    var_tmp = bot.send_message(message.chat.id, "\n\nIngrese su numero:")
    bot.register_next_step_handler(var_tmp,
                                    client_number)

#=========================== DRIVER
def driver_capacity(message):
    tmp_message = message.text
    print(f'show capaticy: {tmp_message}:')

    client_registered[message.chat.id]['capacity']=tmp_message

    bot.send_chat_action(message.chat.id, 'typing')
    tmp_data = client_registered.get(message.chat.id)
    message_formated = f"""

NOTA:
Usted esta punto de registrarse como un cuenta real, los datos ingresados deben estar correctos ya que al precionar acceptar se registrara toda la informacion y no podra modificar acto seguido de haber acceptado, porfavor lea, revise, y confirme.

Registrado como:\t\t{tmp_data.get('type')}
Nombre:\t\t{tmp_data.get('name')}
Movil:\t\t{tmp_data.get('number')}
Modelo de transporte:\t\t{tmp_data.get('car')}
Capacidad de transporte:\t\t{tmp_data.get('capacity')} Clientes


    """

    var_tmp = bot.send_message(message.chat.id, message_formated)

    # bot.register_next_step_handler(var_tmp,
    print(f'datos completados\n\n{client_registered}')
    #                                 driver_number)


def driver_number(message):
    tmp_message = message.text
    print(f'show number: {tmp_message}:')

    client_registered[message.chat.id]['number']=tmp_message

    message_formated = library_lenguage.read_header(data='DRIVER_CAPACITY')
    bot.send_chat_action(message.chat.id, 'typing')
    var_tmp = bot.send_message(message.chat.id, message_formated)
    bot.register_next_step_handler(var_tmp,
                                    driver_capacity)

def driver_cars(message):
    tmp_message = message.text
    print(f'show car: {tmp_message}:')

    client_registered[message.chat.id]['car']=tmp_message

    message_formated = library_lenguage.read_header(data='DRIVER_NUMBER')
    bot.send_chat_action(message.chat.id, 'typing')
    var_tmp = bot.send_message(message.chat.id, message_formated)
    bot.register_next_step_handler(var_tmp,
                                    driver_number)

def driver_name(message):
    tmp_message = message.text

    print(f'show name: {tmp_message}:')

    client_registered[message.chat.id]={'type':'driver'}
    client_registered[message.chat.id]['name']=tmp_message

    message_formated = library_lenguage.read_header(data='DRIVER_CAR')
    bot.send_chat_action(message.chat.id, 'typing')
    var_tmp = bot.send_message(message.chat.id, message_formated)
    bot.register_next_step_handler(var_tmp,
                                    driver_cars)
#=========================== DRIVER


@bot.message_handler(func=lambda message:True)
def all_messages(message):
    data_buttons = {
                      'start': [
                                'Mi informacion', 'Actualizar Posicion','',
                                'Viajar ahora','','',
                                'Configuracion','Ayuda del Usuario','',
                               ],
                #========
        'Actualizar Posicion': [
                                'Mi informacion','','',
                                'Donde estoy ahora?','Hacia donde voy?','',
                                'Viajar ahora','','',
                                'Ayuda del usuario','Atras','',
                                ],
                'Registrarse': [
                                'Registrarse como viajero',
                                'Registrarse como Conductor',
                                "Atras"
                                ],
    'Registrarse como viajero': [
                                'Guardar configuracion','Cancelar',
                                'Mi informacion','Ayuda Viajero','',
                                'Atras','','',
                                ],
  'Registrarse como Conductor': [
                                'Guardar configuracion','Cancelar',
                                'Mi informacion','Ayuda Conductor','',
                                'Atras','','',
                                ],
              'Configuracion': [
                                'Calificame','','',
                                'Unirse al grupo','Total de votos','',
                                'Modelos vehiculos','Version App','',
                                'Atras','','',

                               ],
                        }

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
    elif 'Actualizar Posicion' == MESSAGE: # will capture text of press buttons
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
    # ================================================= ADMIN
    elif '/set_help' == MESSAGE: # will capture text of press buttons
        if MESSAGE.startswith('/set_help'):
            message_formated = library_lenguage.read_header(data='SET_HELP')
            tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    elif '/set_client' == MESSAGE.split(':')[0]: # will capture text of press buttons
        bot.send_chat_action(message.chat.id, 'typing')
        var_tmp = bot.send_message(message.chat.id, "\n\nIngrese su nombre:")
        bot.register_next_step_handler(var_tmp,
                                        client_name)

    elif '/set_driver' == MESSAGE.split(':')[0]: # will capture text of press buttons
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

    # ================================================= ADMIN

    elif 'Modelos vehiculos' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        message_formated = library_lenguage.read_header(data='DRIVER_CAR')
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

            # elif check_name == 'known':
            #     message_formated = library_lenguage.read_header(data='NOTA')
            #     tele_bot.send_message( bot=bot, type_msg='message' ,message_id=MESSAGE_ID, message=message_formated )

            # else:
            #     tele_bot.tele_buttons(
            #                 bot = bot,
            #                 message_id=MESSAGE_ID,
            #                 key_dict_buttons=MESSAGE,
            #                 dict_buttons=all_citys,
            #                 row_number=3,
            #                 message=f"Bienvenido al menu de {MESSAGE}",
            #                 )

if __name__ == '__main__':
    tele_bot = library_telebot.tele_bot
    MenuCommand = library_telebot.tele_bot.MenuCommand

    # Create connction to dataase
    mysqlite_db = library_sqlite.mysqlite_db
    connection_db = mysqlite_db.sqlite_connection(namedatabase=os.path.join('mi_pasaje/database','.mi_botella_database.db'))

    list_all_commands = {
                        'start':'Lobby de bienvenida a Mi pasaje App',
                        'registrarse':'Registrarse como usuario o conductor',
                        'unirse_al_grupo':'Grupo creado para compartir ideas',
                        'califiar_app':'Calificame su opinion de la App',
                        'total_votos':'Ver cantidad de votos y aceptacion de la app chofe_parada',
                        'registrarse':'Registrarse en mi pasaje App',
                        'ayuda':'Principales dudas',
                        'donacion':'Puede contruir con la App',
                        }
    try:
        MenuCommand(bot,list_all_commands)
        bot.infinity_polling(skip_pending=True)
        # bot.infinity_polling()
    except Exception as e:
        os.system('clear')
        line = "="*30
        print(f'\n\n{line}\n\PORFAVOR VERIFIQUE SU INTERNET\n\n{line}\n\n{e}\n\n{line}\n\n\n')