# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# import requests

# #updater = Updater(token='1239441085:AAEVcQWv-Lmj9hexUSD76j2F3TjzDP0IpEI', use_context=True )



# def telegram_bot_sendtext(bot_token, bot_chatID, bot_message):
#         send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
#         response = requests.get(send_text)

# telegram_bot_sendtext('1239441085:AAEVcQWv-Lmj9hexUSD76j2F3TjzDP0IpEI','tweetyfabot', 'test')

import os 

os.system('telegram-send dsa')