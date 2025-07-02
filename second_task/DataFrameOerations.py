from matplotlib import pyplot as plt
import pandas as pd


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
