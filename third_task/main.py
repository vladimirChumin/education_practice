from third_task.data_frame_functions import (
    load_dataframe,
    ethnical_diagram,
    ethnicaly_gender_diagram,
    exam_score_histogram,
    gender_parents_education_histogram
)

def all_task():
    df = load_dataframe("dataset_marks.csv")
    ethnical_diagram(df, result_score=179)
    ethnicaly_gender_diagram(df)
    exam_score_histogram(df, step=5)
    gender_parents_education_histogram(df)
    print(1)

def main():
    choice = input("Выберите задачу (1-5): \n")
    df = load_dataframe("dataset_marks.csv")

    match choice:
        case "1":
            print("Создание DataFrame")
            print(df)
        case "2":
            print("Задача 2: Круговая диаграмма соотношения этнической принадлежности и результатов экзаменов")
            ethnical_diagram(df, result_score=179)
        case "3":
            print("Задача 3: Диаграмма зависимости пола и этнической принадлежности")
            ethnicaly_gender_diagram(df)
        case "4":
            print("Задача 4: Гистограмма результатов экзаменов")
            exam_score_histogram(df, step=5)
        case "5":
            print("Задача 5: Гистограмма зависимости пола и образования родителей")
            gender_parents_education_histogram(df)
        case _:
            print("Неверный выбор задачи. Пожалуйста, выберите от 1 до 5.")


if __name__ == "__main__":
    all_task()