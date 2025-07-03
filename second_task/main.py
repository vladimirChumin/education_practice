import pandas as pd
import numpy as np
import random as rd

def load_dataframe(file_path):
    return pd.read_csv(file_path)

def get_result_sort(df, value=179):
    mask = df.iloc[:, [4, 5, 6]].sum(axis=1) >= value
    return df[mask].reset_index(drop=True)

def get_nationality_head(df):
    return df["race/ethnicity"].head(10)

def get_low_scores_after_course(df):
    passed_mask = df.iloc[:, 3] != "none"
    prepared = df[passed_mask]
    mask = (
            (prepared["math score"] < 60) |
            (prepared["reading score"] < 60) |
            (prepared["writing score"] < 60)
    )
    return prepared[mask].reset_index(drop=True)

def get_gender_counts_by_ethnicity(df):
    group = df.groupby([df.columns[1], df.columns[0]])
    size = group.size()
    gender_ethnicity_count = size.unstack()
    return gender_ethnicity_count

def get_exam_pass_counts(df):
    passed_mask = df.iloc[:, 3] != "none"
    unpassed_mask = df.iloc[:, 3] == "none"
    result = {
        "Category": ["Passed", "Not Passed"],
        "Cout": [df[passed_mask].shape[0], df[unpassed_mask].shape[0]]
    }
    return pd.DataFrame(result)

def get_exam_avarage_and_sum(df):
    scores = df.iloc[:, 4:7]
    result = df.copy()
    result["sum_result"] = scores.sum(axis=1)
    result["avg_result"] = result["sum_result"] / 3
    return result

def write_to_csv(df, file_name):
    if not file_name.endswith('.csv'):
        raise ValueError("File name must end with '.csv'.")
    df.to_csv(file_name, index=False)

def generate_series():
    uniform_values = np.linspace(0, 20, 15)
    factor = rd.random()
    result_series = pd.Series(uniform_values * factor)
    return result_series

def generate_changed_df(df, file_name="changed_dataset.csv"):
    changed_df = get_exam_avarage_and_sum(df)
    write_to_csv(changed_df, file_name)
    return changed_df

def all_task():
    df = load_dataframe("dataset_marks.csv")
    generate_series()
    nationality_head = get_nationality_head(df)
    df_count_exam_pass = get_exam_pass_counts(df)
    df_result_sort = get_result_sort(df, 179)
    df_low_scores_after_course = get_low_scores_after_course(df)
    df_gender_sort = get_gender_counts_by_ethnicity(df)
    changed_df = generate_changed_df(df)
    passed = df.iloc[:, 3] != "none"
    x = df_result_sort.groupby(df.columns[1]).size()
    df_y = df.groupby(df.columns[1]).size()
    print(1)

def main():
    choice = input("Выберите задачу (1-8): \n")
    df = load_dataframe("dataset_marks.csv")

    match choice:
        case "1":
            print("Вы выбрали задачу 1: Создание Siries из 15 чисел, разбивающих отрезок от 0 до 20 на равные части")
            series = generate_series()
            print(series)
        case "2":
            print("Задача 2: Создание DataFrame")
            print(df)
        case "3":
            print("Задача 3: Вывод первых 10 значений столбца 'race/ethnicity'")
            nationality_head = get_nationality_head(df)
            print(nationality_head)
        case "4":
            print("Задача 4: Вычисление количества учеников, сдавших и не сдавших экзамены")
            df_count_exam_pass = get_exam_pass_counts(df)
            print(df_count_exam_pass)
        case "5":
            print("Задача 5: Фильтрация DataFrame по сумме баллов")
            df_result_sort = get_result_sort(df, 179)
            print(df_result_sort)
        case "6":
            print("Задача 6: Функция для получения учеников с низкими баллами ниже 60 после курса")
            df_low_scores_after_course = get_low_scores_after_course(df)
            print(df_low_scores_after_course)
        case "7":
            print("Задача 7: Подсчет количества учеников по полу и этнической принадлежности")
            df_gender_sort = get_gender_counts_by_ethnicity(df)
            print(df_gender_sort)
        case "8":
            print("Задача 8: Вычисление средней и суммы баллов по экзаменам, создание нового DataFrame и запись в CSV")
            changed_df = generate_changed_df(df)
            print(changed_df)

if __name__ == "__main__":
    all_task()