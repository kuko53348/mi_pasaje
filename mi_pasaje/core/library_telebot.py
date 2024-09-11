from telebot.types import *
import telebot


class tele_bot():
    """docstring for tele_bot"""

    def __init__(self, token="6818512371:AAGYLNQSPI7Rg3sZQFuu0lxirUdK4aCIKI0"):
        super(tele_bot, self).__init__()
        # self.bot = telebot.TeleBot(token)
        sel.data = ''

    def run_telebot(self):
        self.bot.infinity_polling()

    def tele_buttons(bot, dict_buttons, key_dict_buttons='', message_id='', message='HELLO WORLD', row_number=0, resize=True, show_keyboard=False):
        """
        EXEMPLE:
        =======================================================================

        import library_telebot
        import telebot

        bot = telebot.TeleBot(token="6818512371:AAGYLNQSPI7Rg3sZQFuu0lxirUdK4aCIKI0")


        @bot.message_handler(func=lambda message:True)
        def all_messages(message):
            data_buttons = {
                            'start': ['button_1','button_2'],

                            'button_1': ['A','B',"start"],
                            'button_2': ['D','E',"start"],
                            }

            MESSAGE_ID = message.chat.id
            MESSAGE    = message.text

            if 'start' in MESSAGE: # will capture text of press buttons
                ''' We create a start button '''
                tele_bot.tele_buttons(
                            bot = bot,
                            message_id=MESSAGE_ID,
                            key_dict_buttons='start',
                            dict_buttons=data_buttons,
                            row_number=3,
                            message=f"Welcome to {MESSAGE} menu:",
                            # resize=True,
                            # show_keyboard=False,
                            )

            if 'button_1' in MESSAGE: # will capture text of press buttons
                ''' We create a start button '''
                tele_bot.tele_buttons(
                            bot = bot,
                            message_id=MESSAGE_ID,
                            key_dict_buttons='button_1',
                            dict_buttons=data_buttons,
                            row_number=3,
                            message=f"Welcome to {MESSAGE} menu:",
                            # resize=True,
                            # show_keyboard=False,
                            )


            if 'A' in MESSAGE: # will capture text of press buttons
                message_formated = 'hello world'
                tele_bot.send_message(  bot=bot,type_msg='message',message_id=MESSAGE_ID,message=message_formated)

            if 'B' in MESSAGE: # will capture text of press buttons
                message_formated = 'hello world'
                tele_bot.send_message( bot=bot,type_msg='reply',message_id=MESSAGE_ID,reply_message=REPLY_MESSAGE,message=message_formated)

            if 'C' in MESSAGE: # will capture text of press buttons
                message_formated = 'All founds are deposited congratulation'
                tmp = tele_bot.congratulation( bot=bot,message_id=MESSAGE_ID,message=message_formated)
                print(tmp)

        if __name__ == '__main__':
            tele_bot = library_telebot.tele_bot
            bot.infinity_polling()

        =======================================================================

        NOTE:

            "Is necessary make a dictionary that will have inside a list with more buttons"

            'key_buttons': ['buttons'...]

            1. get dict of button from dict_buttons
            2. our chat id to send message
            3. Body message will be filtered to make a function or action
            4. key_dict_buttons = id of our box that will have all button inside

        """
        boxLayout = telebot.types.ReplyKeyboardMarkup(
            row_width=row_number, resize_keyboard=resize, one_time_keyboard=show_keyboard)
        boxLayout.add(* dict_buttons.get(key_dict_buttons))
        bot.send_message(message_id, message,
                         reply_markup=boxLayout, parse_mode='html')

        return boxLayout

    # --------------------------------------  Reply all Text
    def send_message(bot, message_id='', reply_message='', type_msg='message', message='', file=''):

        CHAT_ID = message_id
        # our message id
        bot.send_chat_action(CHAT_ID, 'typing')  # print like typing

        # filter by type_msg ='message','photo','document','audio'
        if type_msg == 'message':
            # <= SEND MESSAGE
            bot.send_message(CHAT_ID, message, parse_mode='html')

        elif type_msg == 'reply':
            bot.reply_to(reply_message, message)

        elif type_msg == 'photo':
            photo = open(file, 'rb')
            bot.send_photo(CHAT_ID, photo, caption=message, parse_mode='html')
            photo.close()

        elif type_msg == 'document':
            document = open(file, 'rb')
            bot.send_document(CHAT_ID, document,
                              caption=message, parse_mode='html')
            document.close()

        elif type_msg == 'audio':
            audio = open(file, 'rb')
            bot.send_audio(CHAT_ID, photo, caption=message, parse_mode='html')
            audio.close()

        elif type_msg == 'video':
            video = open(file, 'rb')
            bot.send_audio(CHAT_ID, video, caption=message, parse_mode='html')
            video.close()

    def congratulation(bot, message_id, message=''):

        # bot.send_message(message.chat.id, "You win lottery day have a nice lucky day ")
        answer_options = ["Le gusta la App @mi_pasaje_bot","No sirve la App"]
        print(message)

        data = bot.send_poll(
            chat_id=message_id,
            question="Comparta su opinion hacerca de la App",
            options=answer_options,
            type="quiz",
            correct_option_id=0,
            is_anonymous=False,
            # is_anonymous=True,
        )
        # print(data)
        @bot.poll_answer_handler()
        def handle_poll(poll):
            # This handler can be used to log User answers and to send next poll
            polling = poll
            # 'option_ids', 'poll_id', 'to_dict', 'to_json', 'user', 'voter_chat'
            print(f"[+] A escogido respuesta: {answer_options[polling.option_ids[0]]}")
            print(f"[+] Usuario: @{polling.user.first_name} ID: {polling.poll_id}")
            print(f"[+] Login: @{polling.user.username}")
            # print(polling['option_ids'])

        return True

    def listen_message(message_id, reply_message, type_msg='message', message='', file=''):
        CHAT_ID = message_id

    def MenuCommand(bot, dict_commands=dict()):
        bot.delete_my_commands(scope=None, language_code=None)
        commands_list = list()

        for tmp in dict_commands.keys():
            commands_list.append(telebot.types.BotCommand(
                tmp, dict_commands.get(tmp)))

        bot.set_my_commands(commands=commands_list, )


if __name__ == '__main__':
    telebot = tele_bot()
