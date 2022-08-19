import telebot #разобраться с установкой
import random


token = '5465880199:AAGZjiHZKwcR57yQQ4dClRxZOiYkNyeuN20'


HELP = """
/help - напечатать справку по программе.
/add - добавить задачу в список (название задачи запрашиваем у пользователя).
/show(/print) - напечатать все добавленные задачи.
/random - добавить случайную задачу."""

bot = telebot.TeleBot(token)

tasks = {
    }
random_tasks = ['Погулять', 'Выпить', 'что-то еще']

def command_input(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add", "random"])
def add(message):
    if 'add' in message.text:
        date = message.text.split()[1].lower()
        task = message.text.split(maxsplit=2)[2]
    elif 'random' in message.text:
        date = message.text.split()[1]
        task = random.choice(random_tasks)

    command_input(date, task)
    bot.send_message(message.chat.id, f'задача <{task}> принята на дату <{date}>')

@bot.message_handler(commands=["show"])
def show(message):
    if 'show' in message.text:
        date = message.text.split()[1]
        if date in tasks:
            bot.send_message(message.chat.id, f'На дату <{date}> запланированно:')
            for task in tasks[date]:
                bot.send_message(message.chat.id, f'-- {task}')
        else:
            bot.send_message(message.chat.id, f'На дату: {date} пока нет задач')
@bot.message_handler(commands=["showall"])
def showall(message):
    bot.send_message(message.chat.id, f'все задачи:')
    for key in tasks:
        bot.send_message(message.chat.id, f'на дату <{key}>  у вас следущие дела:')
        for task in tasks[key]:
             bot.send_message(message.chat.id, f'-- {task}')

bot.polling(none_stop=True)