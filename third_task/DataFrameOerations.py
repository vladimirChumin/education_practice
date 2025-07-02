import pandas as pd
import matplotlib
import numpy as np
matplotlib.use('TkAgg')  # или 'Qt5Agg'
from matplotlib import pyplot as plt
from matplotlib.ticker import FixedLocator

class DataFrameOperations:
    def __init__(self, data_frame):
        if isinstance(data_frame, str):
            self.df = pd.read_csv(data_frame)
        elif isinstance(data_frame, pd.DataFrame):
            self.df = data_frame
        else:
            raise TypeError("data_frame must be a pandas DataFrame or a file path to a CSV.")

        self.columns = self.df.columns.tolist()
        self.rows = self.df.shape[-1]

    def __sorted_df(selfs, column_name, value, operation, max_rows=10 ** 10):
        if column_name not in selfs.columns:
            raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

        match operation:
            case "=":
                result = selfs.df[selfs.df[column_name] == value][:max_rows]
                return result
            case ">":
                result = selfs.df[selfs.df[column_name] > value][:max_rows]
                return result
            case ">=":
                result = selfs.df[selfs.df[column_name] >= value][:max_rows]
                return result
            case "<":
                result = selfs.df[selfs.df[column_name] < value][:max_rows]
                return result
            case "<=":
                result = selfs.df[selfs.df[column_name] <= value][:max_rows]
                return result
            case "!=":
                result = selfs.df[selfs.df[column_name] != value][:max_rows]
                return result
            case _:
                raise ValueError(f"Invalid operation '{operation}'. Supported operations are: '=', '>', '>=', '<', '<=', '!='.")

    def get_result_sort(self, value):
        mask = self.df.iloc[:, [4, 5, 6]].sum(axis=1) >= value
        return self.df[mask].reset_index(drop=True)

    def get_low_scores_after_course(self):
        prepared = self.__sorted_df(self.df.columns[3], "none", "!=")
        mask = (
                (prepared["math score"] < 60) |
                (prepared["reading score"] < 60) |
                (prepared["writing score"] < 60)
        )
        return prepared[mask].reset_index(drop=True)

    def get_gender_counts_by_ethnicity(self):
        gender_ethnicity_count = self.df.groupby([self.df.columns[1], self.df.columns[0]]).size().unstack(fill_value=0)
        return gender_ethnicity_count

    def get_exam_pass_counts(self):
        pass_cout = self.__sorted_df(self.df.columns[3], "none", "!=")
        pass_not_cout = self.__sorted_df(self.df.columns[3], "none", "=")
        result = {
            "Category": ["Passed", "Not Passed"],
            "Cout": [pass_cout.shape[0], pass_not_cout.shape[0]]
        }
        return pd.DataFrame(result, index=[0, 1], )

    def get_exam_avarage_and_sum(self):
        scores = self.df.iloc[:, 4:7]
        result = self.df.copy()
        result["sum_result"] = scores.sum(axis=1)
        result["avg_result"] = result["sum_result"] / 3
        return result

    def write_to_csv(self, file_name, data_frame=None):
        if data_frame is None:
            data_frame = self.df
        if not file_name.endswith('.csv'):
            raise ValueError("File name must end with '.csv'.")
        data_frame.to_csv(file_name, index=False)

    def ethnical_diagram(self, result_score=0):
        filtered_df = self.get_result_sort(result_score)
        ethnicity_column = self.df.columns[1]
        diagram_data = filtered_df.groupby(ethnicity_column).size()
        diagram_data.plot.pie(autopct='%1.1f%%', startangle=90, ylabel='')
        plt.title(f"Распределение по этнической принадлежности (результат >= {result_score})")
        plt.show()

    def ethnicaly_gender_diagram(self):
        ethinical_list = self.df[self.df.columns[1]].unique()
        data = pd.DataFrame(columns=["race/ethnicity", "Male count", "Female count"])
        for ethinic_group in ethinical_list:
            mask = self.df.iloc[:, 1] == ethinic_group
            ethinical_mask = self.df[mask]
            gender_info_in_ethnical = ethinical_mask.groupby(ethinical_mask.columns[0]).size()
            ethinical_data = pd.DataFrame({"race/ethnicity": [ethinic_group],
            "Male count": [gender_info_in_ethnical.iloc[1]],
            "Female count": gender_info_in_ethnical.iloc[0]})

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

    def exam_score_histogram(self, step=5):
        bins = np.array([0] + [i for i in range(step, 101, step)])
        math_counts, _ = np.histogram(self.df.iloc[:, 4], bins=bins)
        reading_counts, _ = np.histogram(self.df.iloc[:, 5], bins=bins)
        writing_counts, _ = np.histogram(self.df.iloc[:, 6], bins=bins)

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

    def gender_parents_education_histogram(self):
        educations = self.df.iloc[:, 2].unique()
        data = pd.DataFrame(columns=["education", "Female count", "Male count"])

        for education in educations:
            mask = self.df.iloc[:, 2] == education
            sorted_df = self.df[mask]
            gender_info = sorted_df.groupby(sorted_df.iloc[:, 0]).size()
            education_data = pd.DataFrame({
                "education": [education],
                "Female count": gender_info.iloc[0],
                "Male count": gender_info.iloc[1]})
            data = pd.concat([data, education_data], ignore_index=True)
        width = 0.2
        female_count = data.iloc[:, 1]
        male_count = data.iloc[:, 2]
        indices = np.arange(data.shape[0])

        fig, ax = plt.subplots()
        ax.bar(indices - width / 2, female_count, width, label="Количество женищин")
        ax.bar(indices + width / 2, male_count, width, label="Количество мужчин")

        ax.set_xlabel("Этническая принадлежность")
        ax.set_ylabel("Количество")
        ax.set_title("Гистограмма зависимости пола и образования родителей")
        ax.legend()
        ax.set_xticks(indices)
        ax.set_xticklabels(data.iloc[indices, 0])
        fig.show()
