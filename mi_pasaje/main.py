import telebot
import os

from core import library_telebot
from core import library_lenguage

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
all_citys = {

    'Pinar_del_Rio':[
            'Guanes',
            'Mantua',
            'Minas_Matahambre',
            'Vinales',
            'San_Luis',
            "S_Juan_Martinez",
            'Pinar_del_Rio',
            'Los_Palacios',
            'Consolacion_Sur',
            'La_Palma',
            'Sandino',
            'Atras',
            ],
    'Matanzas':[
            'Matanzas ',
            'Cárdenas',
            'Martí',
            'Colón',
            'Perico',
            'Jovellanos',
            'Pedro_Betancourt',
            'Limonar',
            'Unión_Reyes',
            'Ciénaga_Zapata',
            'Jagüey_Grande',
            'Calimete',
            'Los_Arabos',
            'Atras',
            ],
    'Ciego_Avila':[
            'Bolivia',
            'Majagua',
            'Moron',
            'Florencia',
            'Ciego_Avila',
            'Baragua',
            'Venezuela',
            'Ciro_Redondo',
            'Primero_Enero',
            'Chambas',
            'Atras',
            ],
    'Artemisa':[
            'Alquizar',
            'Artemisa',
            'S_Antonio_Banos',
            'Caimito',
            'Mariel',
            'San_Cristobal',
            'Guanajay',
            'Bauta',
            'Candelaria',
            'Bahia_Honda',
            'Guira_Melena',
            'Atras',
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
            'Atras',
            ],
    'La_Habana':[
            'Plaza_Revolucion',
            'Marianao',
            'Cotorro',
            'Cerro',
            'Centro_Habana',
            'Regla',
            'S_Miguel_Padron',
            'Boyeros',
            'Habana_Vieja',
            'Arrojo_Naranjo',
            'Diez_Octubre',
            'La_Lisa',
            'Guanabacoa',
            'Habana_del_Este',
            'Playa',
            'Atras',
            ],
    'Cienfuegos':[
            'Cienfuegos',
            'Aguada_Pasajeros',
            'Abreus',
            'Lajas',
            'Rodas',
            'Cruces',
            'Palmira',
            'Cumanayagua',
            'Atras',
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
            'Sagua_Tanamo',
            'Calixto_Garcia',
            'Urbano_Noris',
            'Antilla',
            'Baguanos'
            'Atras',
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
            'Atras',
            ],
    'Camaguey':[
            'Jatibonico',
            'Santa_Cruz_Sur',
            'Camaguey',
            'C_Manuel_Cespedes',
            'Esmeralda',
            'Najasa',
            'Sierra_Cubitas',
            'Minas',
            'Nuevitas',
            'Florida',
            'Vertientes',
            'Sibanicu',
            'Atras',
            ],
    'Santiago_Cuba':[
            'San_Luis',
            'Palma_Soriano',
            'Segundo_Frente',
            'Tercer_Frente',
            'Contramaestre',
            'Guama',
            'Santiago_Cuba',
            'Songo_la_Maya',
            'Mella',
            'Atras',
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
            'Atras',
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
            'Atras',
            ],
    'Mayabeque':[
            'Jaruco',
            'Quivican',
            'San_Jose_Lajas',
            'Madruga',
            'Guines',
            'Santa_Cruz_Norte',
            'Batabano',
            'Nueva_Paz',
            'Bejucal',
            'Melena_del_Sur',
            'San_Nicolas',
            'Atras',
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
            'Atras',
            ],
    'Atras':['Atras'],
        }

@bot.message_handler(func=lambda message:True)
def all_messages(message):
    data_buttons = {
                      'start': [
                                # 'Mostrar Municipios','Registrarse','',
                                'Mis datos','Donde estoy?','',
                                'Viajar en mi Ciudad',
                                # 'Fuera de Ciudad','',
                                'Vijar en mi Municipio','',
                                # 'Fuera de Municipio','',

                                # 'Vijar en mi Municipio','',
                                # 'Confirmar salida', '',
                                # 'Granma',
                                # 'Transporte disponible para hoy',
                                'Mostrar Info','Principales dudas',
                                ],
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
        'Vijar en mi Municipio':  [
                                'Pinar_del_Rio',
                                'Matanzas',
                                'Ciego_Avila',
                                'Artemisa',
                                'Las_Tunas',
                                'La_Habana',
                                'Cienfuegos',
                                'Holguin',
                                'Santi_Spiritus',
                                'Camaguey',
                                'Santiago_Cuba',
                                'Granma',
                                'Guantanamo',
                                'Mayabeque',
                                'Villa_Clara',
                                'Atras',
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
    elif 'Vijar en mi Municipio' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''

        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Vijar en mi Municipio',
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
    elif 'Viajar en mi Ciudad' == MESSAGE or 'Bayamo' == MESSAGE: # will capture text of press buttons
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



    elif 'Granma' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        tele_bot.tele_buttons(
                    bot = bot,
                    message_id=MESSAGE_ID,
                    key_dict_buttons='Granma',
                    dict_buttons=data_buttons,
                    row_number=4,
                    message=f'Bienvenido al menu de {MESSAGE}\n\nUsted puede volver a la pagina de inicio pulsando 👉<b>/atras</b> 👈',
                    # resize=True,
                    # show_keyboard=False,
                    )

    elif 'Mostrar Municipios' == MESSAGE: # will capture text of press buttons
        ''' We create a start button '''
        message_formated = data_buttons.get("Vijar en mi Municipio")
        tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=','.join(message_formated).replace(',','\n'))

    elif '/unirse_al_grupo' == MESSAGE: # will capture text of press buttons
        message_formated = library_lenguage.read_header(data='GROUP')
        tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    elif '/califiar_app' == MESSAGE or 'califiar_app' == MESSAGE: # will capture text of press buttons
        tele_bot.congratulation( bot=bot,message_id=MESSAGE_ID,message='Formulario')

    elif '/total_votos' == MESSAGE: # will capture text of press buttons
        message_formated = f'Cantidad de votos: {"320"}\n\nVotos:\n\nPersonas que le gustan la App {"150"}\nPersonas que no les gusta: {"25"}\n\n'
        tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

    else:
        data = all_citys.get(MESSAGE,'known')
        # print(data)

        if data == 'known':
            message_formated = library_lenguage.read_header(data='NOTA')
            tele_bot.send_message( bot=bot, type_msg='message' ,message_id=MESSAGE_ID, message=message_formated )

        else:
            tele_bot.tele_buttons(
                        bot = bot,
                        message_id=MESSAGE_ID,
                        key_dict_buttons=MESSAGE,
                        dict_buttons=all_citys,
                        row_number=3,
                        message=f"Bienvenido al menu de {MESSAGE}",
                        )
        # print(f"""
        #     Telegram: @{message.json.get('from').get('username')}
        #     ID: {message.json.get('from').get('id')}
        #     usuario: {message.json.get('from').get('first_name')}
        #     texto: {message.json.get('text')}
        #     """)

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