import pandas as pd
import random as rd
import numpy as np
from DataFrameOerations import DataFrameOperations

def series_manipulation():
    list = np.linspace(0, 20, 15)
    series = pd.Series(list)
    series = series.apply(lambda x: x * rd.randint(0,1))
    return series


def main():
    print(f"Series manipulation:\n{series_manipulation().to_string()}\n")
    df = DataFrameOperations("dataset_marks.csv")
    cur_columns = df.columns
    nationality_head = df.df[cur_columns[0]].head(10)
    df_cout_exam_pass = df.get_exam_pass_counts()
    df_result_sort = df.get_result_sort(179)
    df_low_scores_after_course = df.get_low_scores_after_course()
    df_gender_sort = df.get_gender_counts_by_ethnicity()
    changed_df = df.get_exam_avarage_and_sum()
    df.write_to_csv("changed_dataset.csv", changed_df)

    print(2)

if __name__ == "__main__":
    main()


