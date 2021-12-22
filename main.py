import telebot
token = '1079455577:AAFAVMfPr2jQlYPrZi6FiOkpBzVs53-X9zs'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('LogisticRegression', 'DecisionTreeClassifier')
    bot.send_message(message.chat.id,  'Привет. Выбери алгоритм машинного обучения, который тебя интересует.', \
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    lr = ['https://scikit-learn.org/stable/modules/linear_model.html', \
          'https://habr.com/ru/company/ods/blog/323890/#2-logisticheskaya-regressiya']
    dtc = ['https://habr.com/ru/company/ods/blog/322534/', \
           'https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier']
    if message.text.lower() == 'logisticregression':
        bot.send_message(message.chat.id, f'Парочка полезных ссылок:\n{lr[0]}')
        bot.send_message(message.chat.id, f'{lr[1]}')
    elif message.text.lower() == 'decisiontreeclassifier':
        bot.send_message(message.chat.id, \
                         f'Полезные ссылки:\nСтатья на хабре:{dtc[0]}')
        bot.send_message(message.chat.id, f'Документация к фреймворку catboost: {dtc[1]}')


bot.polling()
