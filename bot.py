import telebot
import threading
from config import BOT_TOKEN, keyboard1, keyboard2, keyboard3, keyboard4, keyboard5
from config import hello_message, help_message
from client import SendMessage




bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, hello_message, reply_markup=keyboard1)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, help_message, reply_markup=keyboard1)



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'добавить получателей':
        bot.send_message(message.chat.id, 'Ввидите айди нужных получаталей, когда закончите нажимите кнопку \'Готово\'', reply_markup=keyboard2)
        bot.register_next_step_handler(message, add_adres)

    elif message.text.lower() == 'ввести сообщение':
        bot.send_message(message.chat.id, 'Следующее введеное сообщение будет отправлено:', reply_markup=keyboard4)
        bot.register_next_step_handler(message, send_message)

    elif message.text.lower() == 'просмотреть получаталей':
        chats = []
        f = open('user_id.txt', 'r')
        for us in f:
            try:
                chats.append(us[0:-1])
            except:
                bot.send_message(message.chat.id, 'Получаталей на данный момент нет', reply_markup=keyboard1)
                bot.register_next_step_handler(message, send_text)
        f.close()
        send_users = ""
        for us in chats:
            send_users += us + '\n'
        try:
            bot.send_message(message.chat.id, send_users, reply_markup=keyboard1)
        except:
            bot.send_message(message.chat.id, 'Получаталей на данный момент нет', reply_markup=keyboard1)
        bot.register_next_step_handler(message, send_text)

    elif message.text.lower() == 'удалить получаталей':
        bot.send_message(message.chat.id, 'Ввидите имя получателя, которого хотите удалить', reply_markup=keyboard5)
        bot.register_next_step_handler(message, delete_adres)
        pass




def delete_adres(message):
    target_user = message.text.lower()
    if message.text.lower() != 'назад':
        if message.text.lower() == 'удалить всех':
            f = open('user_id.txt', 'w')
            f.write('')
            f.close()
            bot.send_message(message.from_user.id, 'Все получатели удалены:', reply_markup=keyboard1)
            bot.register_next_step_handler(message, send_text)
        elif message.text.lower() == 'готово':
            bot.send_message(message.from_user.id, 'Введеные пользователи удалены', reply_markup=keyboard1)
            bot.register_next_step_handler(message, send_text)
        else:
            chats = []
            f = open('user_id.txt', 'r')
            for user_id in f:
                try:
                    chats.append(user_id[0:-1])
                except:
                    bot.send_message(message.chat.id, 'Получаталей на данный момент нет', reply_markup=keyboard1)
                    bot.register_next_step_handler(message, send_text)
            f.close()

            del_index = -1
            for i in range(len(chats)):
                if chats[i] == target_user:
                    del_index = i

            try:
                chats.pop(del_index)
            except:
                bot.send_message(message.from_user.id, 'Такого пользователя нет в списке получаталей', reply_markup=keyboard5)

            f = open('user_id.txt', 'w')
            for user in chats:
                f.write(user + '\n')
            f.close()
            bot.register_next_step_handler(message, delete_adres)

    else:
        bot.send_message(message.from_user.id, 'Меню:', reply_markup=keyboard1)
        bot.register_next_step_handler(message, send_text)


def add_adres(message):

    all_users = []
    f = open('user_id.txt', 'r')
    for user_id in f:
        try:
            all_users.append(user_id[0:-1])
        except:
            print('pusto')
    f.close()

    target_user = message.text.lower()
    if message.text.lower() == 'готово':
        bot.send_message(message.from_user.id, 'Пользователи добавлены', reply_markup=keyboard1)
        bot.register_next_step_handler(message, send_text)
    else:
        f = open('user_id.txt', 'a')
        if target_user[0] == '@':
            if target_user not in all_users:
                f.write(target_user + '\n')
        else:
            if ('@' + target_user) not in all_users:
                f.write('@' + target_user + '\n')
        f.close()
        bot.register_next_step_handler(message, add_adres)


def send_message(message):
    f = open('user_id.txt', 'r')
    test_users = f.read()
    f.close()
    if len(test_users) == 0:
        bot.send_message(message.from_user.id, 'Вначале добавьте получаталей', reply_markup=keyboard1)
        bot.register_next_step_handler(message, send_text)
    else:
        if message.text.lower() != 'назад':
            f = open('message.txt', 'a')
            f.write(message.text + '\n')
            f.close()

            thread1 = threading.Thread(target=SendMessage().pliz_do_mes())
            thread1.start()


            check = []
            f = open('result.txt', 'r')
            for line in f:
                check.append(line)
            f.close()

            bot.send_message(message.from_user.id, 'Идет отправка..', reply_markup=keyboard4)

            result_text = ""

            for i in range(len(check)-1):
                if check[i][0:-1] == '0' or check[i][0:-1] == '1':
                    pass
                else:
                    if check[i+1][0:-1] == '1':
                        sucess = check[i][0:-1] + ' Доставленно ✅ \n'
                        result_text += sucess
                    else:
                        bad = check[i][0:-1] + ' Ошибка ❌ \n'
                        result_text += bad



            bot.send_message(message.from_user.id, 'Рассылка завершена: \n' + result_text, reply_markup=keyboard1)
            bot.register_next_step_handler(message, send_text)

            f = open('result.txt', 'w')
            f.write('')
            f.close()

        else:
            bot.send_message(message.from_user.id, 'Меню:', reply_markup=keyboard1)
            bot.register_next_step_handler(message, send_text)



bot.polling()