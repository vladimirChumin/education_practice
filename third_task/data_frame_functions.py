import pandas as pd
import matplotlib
import numpy as np
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

def load_dataframe(file_path):
    if isinstance(file_path, str):
        return pd.read_csv(file_path)
    elif isinstance(file_path, pd.DataFrame):
        return file_path
    else:
        raise TypeError("file_path must be a pandas DataFrame or a file path to a CSV.")

def get_result_sort(df, value):
    mask = df.iloc[:, [4, 5, 6]].sum(axis=1) >= value
    return df[mask].reset_index(drop=True)

def ethnical_diagram(df, result_score=0):
    filtered_df = get_result_sort(df, result_score)
    ethnicity_column = df.columns[1]
    diagram_data = filtered_df.groupby(ethnicity_column).size()
    diagram_data.plot.pie(autopct='%1.1f%%', startangle=90, ylabel='')
    plt.title(f"Распределение по этнической принадлежности (результат >= {result_score})")
    plt.show()

def ethnicaly_gender_diagram(df):
    ethinical_list = df[df.columns[1]].unique()
    data = pd.DataFrame(columns=["race/ethnicity", "Male count", "Female count"])
    for ethinic_group in ethinical_list:
        mask = df.iloc[:, 1] == ethinic_group
        ethinical_mask = df[mask]
        gender_info_in_ethnical = ethinical_mask.groupby(ethinical_mask.columns[0]).size()
        ethinical_data = pd.DataFrame({
            "race/ethnicity": [ethinic_group],
            "Male count": [gender_info_in_ethnical.iloc[1]],
            "Female count": gender_info_in_ethnical.iloc[0]
        })
        data = pd.concat([data, ethinical_data], ignore_index=True)

    indices = np.arange(data.shape[0])
    width = 0.2
    fig, ax = plt.subplots()
    ax.bar(indices - width / 2, data["Male count"], width, label="Male")
    ax.bar(indices + width / 2, data["Female count"], width, label="Female")

    ax.set_xlabel("Этническая принадлежность")
    ax.set_ylabel("Количество")
    ax.set_title("Зависимость пола и этнической принадлежности")
    ax.set_xticks(indices)
    ax.set_xticklabels(data["race/ethnicity"])
    ax.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def exam_score_histogram(df, step=5):
    bins = np.array([0] + [i for i in range(step, 101, step)])
    math_counts, _ = np.histogram(df.iloc[:, 4], bins=bins)
    reading_counts, _ = np.histogram(df.iloc[:, 5], bins=bins)
    writing_counts, _ = np.histogram(df.iloc[:, 6], bins=bins)

    centers = (bins[:-1] + bins[1:]) / 2
    bar_width = step / 3

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(centers - bar_width, math_counts, width=bar_width, label="Math")
    ax.bar(centers, reading_counts, width=bar_width, label="Reading")
    ax.bar(centers + bar_width, writing_counts, width=bar_width, label="Writing")

    ax.set_xlabel("Диапазон баллов")
    ax.set_ylabel("Количество студентов")
    ax.set_title("Гистограмма результатов экзаменов")
    ax.set_xticks(bins)
    ax.legend()

    plt.show()

def gender_parents_education_histogram(df):
    educations = df.iloc[:, 2].unique()
    data = pd.DataFrame(columns=["education", "Female count", "Male count"])

    for education in educations:
        mask = df.iloc[:, 2] == education
        sorted_df = df[mask]
        gender_info = sorted_df.groupby(sorted_df.iloc[:, 0]).size()
        education_data = pd.DataFrame({
            "education": [education],
            "Female count": gender_info.iloc[0],
            "Male count": gender_info.iloc[1]
        })
        data = pd.concat([data, education_data], ignore_index=True)

    width = 0.2
    female_count = data.iloc[:, 1]
    male_count = data.iloc[:, 2]
    indices = np.arange(data.shape[0])

    fig, ax = plt.subplots()
    ax.bar(indices - width / 2, female_count, width, label="Количество женищин")
    ax.bar(indices + width / 2, male_count, width, label="Количество мужчин")

    ax.set_xlabel("Категория образования у родителей")
    ax.set_ylabel("Количество")
    ax.set_title("Гистограмма зависимости пола и образования родителей")
    ax.legend()
    ax.set_xticks(indices)
    ax.set_xticklabels(data.iloc[indices, 0])
    plt.tight_layout()
    plt.show()