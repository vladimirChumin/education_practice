from third_task.DataFrameOerations import DataFrameOperations

def all_task():
    df = DataFrameOperations("dataset_marks.csv")
    df.ethnical_diagram(result_score=179)
    df.ethnicaly_gender_diagram()
    df.exam_score_histogram(step=5)
    df.gender_parents_education_histogram()
    print(1)

def main():
    choice = input("Выберите задачу (1-5): \n")
    cur_df = DataFrameOperations("dataset_marks.csv")

    match choice:
        case "1":
            print("Создание DataFrame")
            print(cur_df.df)
        case "2":
            print("Задача 2: Круговая диаграмма соотношения этнической принадлежности и результатов экзаменов")
            cur_df.ethnical_diagram(result_score=179)
        case "3":
            print("Задача 3: Диаграмма зависимости пола и этнической принадлежности")
            cur_df.ethnicaly_gender_diagram()
        case "4":
            print("Задача 4: Гистограмма результатов экзаменов")
            cur_df.exam_score_histogram(step=5)
        case "5":
            print("Задача 5: Гистограмма зависимости пола и образования родителей")
            cur_df.gender_parents_education_histogram()
        case _:
            print("Неверный выбор задачи. Пожалуйста, выберите от 1 до 5.")


if __name__ == "__main__":
    all_task()
