import pandas as pd
import numpy as np
import random as rd
import os.path

def load_dataframe(file_path):
    if not isinstance(file_path, str) or not file_path.endswith('.csv') or not os.path.isfile(file_path):
        raise TypeError("file_path must be a string representing the path to the CSV file.")
    return pd.read_csv(file_path)

def get_result_sort(df, value=179):
    if not isinstance(value, int) or value < 0 or not isinstance(df, pd.DataFrame):
        raise ValueError("Value must be a non-negative integer.")
    mask = df.iloc[:, [4, 5, 6]].sum(axis=1) >= value
    return df[mask].reset_index(drop=True)

def get_nationality_head(df):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame.")
    return df["race/ethnicity"].head(10)

def get_low_scores_after_course(df, value=60):
    if not isinstance(value, int) or value < 0 or not isinstance(df, pd.DataFrame):
        raise ValueError("Value must be a non-negative integer.")
    passed_mask = df.iloc[:, 3] != "none"
    prepared = df[passed_mask]
    mask = (
            (prepared["math score"] < value) |
            (prepared["reading score"] < value) |
            (prepared["writing score"] < value)
    )
    return prepared[mask].reset_index(drop=True)

def get_gender_counts_by_ethnicity(df):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame.")
    group = df.groupby([df.columns[1], df.columns[0]])
    size = group.size()
    gender_ethnicity_count = size.unstack()
    return gender_ethnicity_count

def get_exam_pass_counts(df):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame.")
    passed_mask = df.iloc[:, 3] != "none"
    unpassed_mask = df.iloc[:, 3] == "none"
    result = {
        "Category": ["Passed", "Not Passed"],
        "Cout": [df[passed_mask].shape[0], df[unpassed_mask].shape[0]]
    }
    return pd.DataFrame(result)

def get_exam_avarage_and_sum(df):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame.")
    scores = df.iloc[:, 4:7]
    result = df.copy()
    result["sum_result"] = scores.sum(axis=1)
    result["avg_result"] = result["sum_result"] / 3
    return result

def write_to_csv(df, file_name):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame.")
    if not file_name.endswith('.csv'):
        raise ValueError("File name must end with '.csv'.")
    df.to_csv(file_name, index=False)

def generate_series(start=0, end=20, num=15):
    if not isinstance(start, (int, float)) or not isinstance(end, (int, float)) or not isinstance(num, int):
        raise ValueError("Start and end must be numbers, and num must be an integer.")
    uniform_values = np.linspace(start, end, num)
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
            start, end, num = 0, 20, 15
            series = generate_series(start, end, num)
            print(series)
        case "2":
            print("Задача 2: Создание DataFrame")
            df = load_dataframe("dataset_marks.csv")
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
            filter = input("Введите значение для фильтрации по сумме баллов (по умолчанию 179): ")
            if filter.isdigit():
                filter_value = int(filter)
            else:
                filter_value = 179
            df_result_sort = get_result_sort(df, filter_value)
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