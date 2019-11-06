import asyncio
import threading

from telethon import TelegramClient
from config import API_ID, API_HASH


# Изначально попросит телефон и код. Далее не будет, пока не сменим session_name




class SendMessage(threading.Thread):
    def pliz_do_mes(self):

        all_users = []
        f = open('user_id.txt', 'r')
        for user_id in f:
            try:
                all_users.append(user_id[0:-1])
            except:
                print('pusto')
        f.close()

        print(all_users)

        f = open('message.txt', 'r')
        message = f.read()
        f.close()

        print(message)



        asyncio.set_event_loop(asyncio.new_event_loop())
        client = TelegramClient('session_name', API_ID, API_HASH)
        def do_mes():

            client.start()
            for user in all_users:
                try:
                    client.send_message(user, message)
                    f = open('result.txt', 'a')
                    f.write(user+'\n'+'1'+'\n')
                    f.close()
                except:
                    f = open('result.txt', 'a')
                    f.write(user+'\n'+'0'+'\n')
                    f.close()

        # От сюда идет запуск клиента
        client.start()

        do_mes()

        # Будет работать, пока не отрубится=)
        client.disconnect()

        f = open('message.txt', 'w')
        f.write('')
        f.close()

