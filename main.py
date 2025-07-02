from first_task.main import main as first_main, all_task as first_all_task
from second_task.main import main as second_main, all_task as second_all_task
from third_task.main import  main as third_main, all_task as third_all_task

def main():
    choice = input("Выберите задачу (2-4): \n")

    match choice:
        case "2":
            print("Задача 2: Работа с матрицами и NumPy")
            first_main()
        case "3":
            print("Задача 3: Работа с DataFrame")
            second_main()
        case "4":
            print("Задача 4: Визуализация данных с помощью Matplotlib")
            third_main()
        case _:
            print("Неверный выбор задачи. Пожалуйста, выберите от 2 до 4.")

def all_task():
    print("Выполнение всех задач:")
    print("Задача 2: Работа с матрицами и NumPy")
    first_all_task()
    print("Задача 3: Работа с DataFrame")
    second_all_task()
    print("Задача 4: Визуализация данных с помощью Matplotlib")
    third_all_task()
    print("Все задачи выполнены.")

if __name__ == "__main__":
    all_task()
