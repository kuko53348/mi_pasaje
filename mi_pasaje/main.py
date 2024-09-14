import telebot
import os

from core import library_telebot
from core import library_lenguage

# bot de prueba
bot = telebot.TeleBot(token="6636435110:AAEEbWZ9v_EhT_dDbzZvfTUX6gufLBEbVto")

# bot original
# bot = telebot.TeleBot(token="7519838417:AAEgpcGFQCbHjuVNP14i2V02Bm0Zfa0cI2A")

@bot.message_handler(func=lambda message:True)
def all_messages(message):
    data_buttons = {
                      'start': [
                                'Viajar en mi Ciudad',
                                'Fuera de mi Ciudad','',
                                # 'Confirmar salida', '',
                                # 'Bayamo',
                                # 'Transporte disponible para hoy',
                                'Principales dudas'],
                #========

           'Confirmar salida': [
                                'Confirmar para viajar',
                                'Cancelar botella',
                                'Atras','',
                                ],
                #========
                'Registrarse': [
                                'Registrarse como viajero',
                                'Registrarse como Conductor',
                                "Atras"
                                ],
                #========
        'Fuera de mi Ciudad': [
                                'Viajar hacia la Habana',
                                'Bayamo',
                                # 'Viajar en el Municipio',
                                # 'Bayamo',
                                # 'Alquiler de Vehiculos',
                                "Atras"
                                ],
        'Viajar en mi Ciudad': [
                                'Coche-tradicional',
                                'Coche-Guaguita',
                                'Coche-planchero',
                                'Bici-taxi',
                                'Moto-taxi',
                                'Motorina-taxi',
                                'Automobil',
                                'Camiones',
                                'Camionetas',
                                'Atras',
                                ],
         'Tipos de vehiculos': [
                                'Camiones',
                                'Camionetas',
                                'Guaguas',
                                'Otros',
                                'Volver','',
                                ],
                #========
'Transporte disponible para hoy': [
                                'Disponible en el Municipio',
                                'Disponible en la Provincia',
                                'Atras','',
                                ],
                     'Bayamo': [
                                'Bartolomé Masó',
                                'Buey Arriba',
                                'Campechuela',
                                'Cauto Cristo',
                                'Guisa',
                                'Jiguaní',
                                'Manzanillo',
                                'Media Luna',
                                'Pilón',
                                'Río Cauto',
                                'Yara',
                                'Atras'
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
    elif 'Confirmar salida' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Confirmar salida',
                    dict_buttons=data_buttons,
                    row_number=2,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )
    elif 'Fuera de mi Ciudad' == MESSAGE or 'Volver' ==  MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Fuera de mi Ciudad',
                    dict_buttons=data_buttons,
                    row_number=2,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )
    elif 'Transporte disponible para hoy' == MESSAGE or 'Volver' ==  MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Transporte disponible para hoy',
                    dict_buttons=data_buttons,
                    row_number=2,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )
    elif 'Viajar hacia la Habana' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Tipos de vehiculos',
                    dict_buttons=data_buttons,
                    row_number=2,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )

    elif 'Viajar en el Municipio' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Tipos de vehiculos',
                    dict_buttons=data_buttons,
                    row_number=2,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )
    elif 'Viajar en mi Ciudad' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Viajar en mi Ciudad',
                    dict_buttons=data_buttons,
                    row_number=3,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )
    elif 'Alquiler de Vehiculos' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Tipos de vehiculos',
                    dict_buttons=data_buttons,
                    row_number=2,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )
    elif 'Bayamo' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Bayamo',
                    dict_buttons=data_buttons,
                    row_number=3,
                    message=f'Bienvenido al menu de {MESSAGE}\n\nUsted puede volver a la pagina de inicio pulsando 👉<b>/atras</b> 👈',
                    # resize=True,
                    # show_keyboard=False,
                    )
    # =====================================================================
    elif '/unirse_al_grupo' == MESSAGE: # will capture text of press buttons
        message_formated = library_lenguage.read_header(data='GROUP')
        tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    elif '/califiar_app' == MESSAGE or 'califiar_app' == MESSAGE: # will capture text of press buttons
        tele_bot.congratulation( bot=bot,message_id=MESSAGE_ID,message='Formulario')

    elif '/total_votos' == MESSAGE: # will capture text of press buttons
        message_formated = f'Cantidad de votos: {"320"}\n\nVotos:\n\nPersonas que le gustan la App {"150"}\nPersonas que no les gusta: {"25"}\n\n'
        tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    else:
        message_formated = library_lenguage.read_header(data='NOTA')
        tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

        # print(f"""
        #     Telegram: @{message.json.get('from').get('username')}
        #     ID: {message.json.get('from').get('id')}
        #     usuario: {message.json.get('from').get('first_name')}
        #     texto: {message.json.get('text')}
        #     """)

        # print(message.json.get('chat'))

    # if 'B' == MESSAGE: # will capture text of press buttons
    #     message_formated = 'hello world'
    #     tele_bot.send_message( bot=bot,type_msg='reply',message_id=MESSAGE_ID,reply_message=REPLY_MESSAGE,message=message_formated)

    # if 'C' == MESSAGE: # will capture text of press buttons
    #     message_formated = 'All founds are deposited congratulation'
    #     tmp = tele_bot.congratulation( bot=bot,message_id=MESSAGE_ID,message=message_formated)
    #     print(tmp)

if __name__ == '__main__':
    tele_bot = library_telebot.tele_bot
    MenuCommand = library_telebot.tele_bot.MenuCommand
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