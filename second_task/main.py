from second_task.DataFrameOerations import DataFrameOperations

def all_task():
    cur_df = DataFrameOperations("dataset_marks.csv")
    nationality_head = cur_df.df.iloc[:, 0].head(10)
    df_count_exam_pass = cur_df.get_exam_pass_counts()
    df_result_sort = cur_df.get_result_sort(179)
    df_low_scores_after_course = cur_df.get_low_scores_after_course()
    df_gender_sort = cur_df.get_gender_counts_by_ethnicity()
    changed_df = cur_df.get_exam_avarage_and_sum()
    changed_df.write_to_csv("changed_dataset.csv")
    print(1)

def main():
    choice = input("Выберите задачу (1-5): \n")
    cur_df = DataFrameOperations("dataset_marks.csv")

    match choice:
        case "1":
            print("Задача 1: Создание DataFrame")
            print(cur_df.df)
        case "2":
            print("Задача 2: Вывод первых 10 значений столбца 'race/ethnicity'")
            nationality_head = cur_df.df.iloc[:, 0].head(10)
            print(nationality_head)
        case "3":
            print("Задача 3: Вычисление количества учеников, сдавших и не сдавших экзамены")
            df_count_exam_pass = cur_df.get_exam_pass_counts()
            print(df_count_exam_pass)
        case "4":
            print("Задача 4: Фильтрация DataFrame по сумме баллов")
            df_result_sort = cur_df.get_result_sort(179)
            print(df_result_sort)
        case "5":
            print("Задача 5: Функция для получения учеников с низкими баллами ниже 60 после курса")
            df_low_scores_after_course = cur_df.get_low_scores_after_course()
            print(df_low_scores_after_course)
        case "6":
            print("Задача 6: Подсчет количества учеников по полу и этнической принадлежности")
            df_gender_sort = cur_df.get_gender_counts_by_ethnicity()
            print(df_gender_sort)
        case "7":
            print("Задача 7: Вычисление средней и суммы баллов по экзаменам, создание нового DataFrame и запись в CSV")
            chanded_df = cur_df.get_exam_avarage_and_sum()
            print(chanded_df.df)
            chanded_df.write_to_csv("changed_dataset.csv")

if __name__ == "__main__":
    all_task()
