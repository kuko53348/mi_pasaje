from core import library_telebot
import telebot
import os
bot = telebot.TeleBot(token="7288813327:AAGmz6f2MJa-X_SP8ECLtcTwGE_naSIogU4")


@bot.message_handler(func=lambda message:True)
def all_messages(message):
    data_buttons = {
                      'start': ['Registrarse',
                                'Confirmar salida', '',
                                'Transporte disponible para hoy ', '', '',
                                'Ruta & Destino',
                                'Ayuda del viajero'],
                #========
                'Registrarse': ['Registrarse como viajero',
                                'Registrarse como Conductor',
                                "Atras"
                                ],
                #========
             'Ruta & Destino': ['Destino Habana',
                                'Dentro del mismo Municipio',
                                'Alquiler de Vehiculos',
                                "Atras"
                                ],
         'Tipos de vehiculos': ['Camiones',
                                'Camionetas',
                                'Guaguas',
                                'Otros',
                                'Atras','',
                                ],

                #========
                    }

    MESSAGE_ID = message.chat.id
    MESSAGE    = message.text

    # ===================================== MENU ================================
    if '/start' ==  MESSAGE or 'Atras' ==  MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='start',
                    dict_buttons=data_buttons,
                    row_number=3,
                    message=f"Bienvenido al lobby de mi pasaje app donde usted puede hacer sus reservaciones de transporte o simplemente tener conocimiento del transporte publico en la ciudad de Cardenas.",
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
    elif 'Ruta & Destino' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Ruta & Destino',
                    dict_buttons=data_buttons,
                    row_number=1,
                    message=f"Bienvenido al menu de {MESSAGE}",
                    # resize=True,
                    # show_keyboard=False,
                    )

    elif 'Destino Habana' == MESSAGE: # will capture text of press buttons
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

    elif 'Dentro del mismo Municipio' == MESSAGE: # will capture text of press buttons
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

    # =====================================================================
    if '/califiar_app' == MESSAGE or 'califiar_app' == MESSAGE: # will capture text of press buttons
        tele_bot.congratulation( bot=bot,message_id=MESSAGE_ID,message='Formulario')


    else:
        message_formated = 'Comando desconocido por favor presione /Ayuda en caso de no saber.'
        tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

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
                        'califiar_app':'Calificame su opinion de la App',
                        'registrarse':'Registrarse en mi pasaje App',
                        'donacion':'Puede contruir con la App',
                        'ayuda':'Ayuda del viajero',
                        }
    try:
        MenuCommand(bot,list_all_commands)
        # bot.infinity_polling(skip_pending=True)
        bot.infinity_polling()
    except Exception as e:
        os.system('clear')
        line = "="*30
        print(f'\n\n{line}\n\PORFAVOR VERIFIQUE SU INTERNET\n\n{line}\n\n{e}\n\n{line}\n\n\n')