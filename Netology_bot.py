import random

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = {}

while True:

    random_tasks = ['Погулять', 'Выпить', 'что-то еще']
    def command_input(date, task):      
      if date in tasks:        
        tasks[date].append(task)
      else:
        tasks[date] = []
        tasks[date].append(task)
      print(f"Задача <{task}> добавлена на дату {date}")


    command = input("Введите команду: ")
    if command.lower().strip() == "help":
        print(HELP)
    elif command.lower().strip() == "show":
      date = input('Введите дату: ')
      if date in tasks:
        print(f'На данную дату запланированно:')
        for task in tasks[date]:             
          print(f'-- {task}')
      else:
        print(f'На дату: {date} пока нет задач')         
    elif command.lower().strip() == "add": 
      date = input("Введите дату выполнения задачи: ")
      task = input ('Введите  задачу: ')
      command_input(date, task)      
      

      #elif date_task.lower().strip() == 'завтра':
        #tomorrow_tasks.append(task)
        #print(f'Задача <{task}> добавлена')
      #else:
        #tasks[date].append(task)
        #print(f'Задача <{task}> добавлена')    
    elif command.lower().strip() == "random":  
      date = input("Введите дату выполнения задачи: ")
      random_task = random.choice(random_tasks)
      command_input(date, random_task)
    elif command.lower().strip() == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else: 
        print("Неизвестная команда! Попробуйте еще раз")
        

print("До свидания!")