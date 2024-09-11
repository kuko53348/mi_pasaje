from core import library_telebot
import telebot

bot = telebot.TeleBot(token="7288813327:AAGmz6f2MJa-X_SP8ECLtcTwGE_naSIogU4")


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
