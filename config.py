import telebot
# CLIENT PART
API_ID = 997646
API_HASH = '9ee9aa25b68b1cd36f77eaefef80a869'


API_ID2 = 1083112
API_HASH2 = '576067568e13c13a59c18f5a15214fc4'


# BOT PART
BOT_TOKEN = '817895824:AAE-zOtYiFzY3gLnRsfUUF3NpNNcQjNufcM'
# Приветственное сообщение
hello_message = 'Привет, я бот, который отправляет от твоего лица? сообщения заданным пользователям. \n' \
                'Если нужна помощь в использовании ввидите /help'
# Сообщение для помощи
help_message = 'Для того, что бы настроить список получателей нажимите кнопку:\'кнопканейм\' \n' \
               'Для того, что бы отправить сообщение получателям нажмите кнопку 2'

# Настраиваем кнопки для приложения
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard1.row('Ввести сообщение')
keyboard1.add('Добавить получателей', 'Просмотреть получаталей', 'Удалить получаталей')

keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard2.row('Готово')

keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard3.row('Отправить')

keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard4.row('Назад')

keyboard5 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard5.add('Готово')
keyboard5.add('Удалить всех')
keyboard5.add('Назад')



# OTHER
