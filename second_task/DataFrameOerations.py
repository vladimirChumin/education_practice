import pandas as pd


class DataFrameOperations:
    def __init__(self, data_frame):
        if isinstance(data_frame, str):
            self.df = pd.read_csv(data_frame)
        elif isinstance(data_frame, pd.DataFrame):
            self.df = data_frame
        else:
            raise TypeError("data_frame must be a pandas DataFrame or a file path to a CSV.")

    def get_result_sort(self, value):
        mask = self.df.iloc[:, [4, 5, 6]].sum(axis=1) >= value
        return self.df[mask].reset_index(drop=True)

    def get_low_scores_after_course(self):
        passed_mask = self.df.iloc[:, 3] != "none"
        prepared = self.df[passed_mask]
        mask = (
                (prepared["math score"] < 60) |
                (prepared["reading score"] < 60) |
                (prepared["writing score"] < 60)
        )
        return prepared[mask].reset_index(drop=True)

    def get_gender_counts_by_ethnicity(self):
        group = self.df.groupby([self.df.columns[1], self.df.columns[0]])
        size = group.size()
        gender_ethnicity_count = size.unstack()
        return gender_ethnicity_count

    def get_exam_pass_counts(self):
        passed_mask = self.df.iloc[:, 3] != "none"
        unpassed_mask = self.df.iloc[:, 3] == "none"
        result = {
            "Category": ["Passed", "Not Passed"],
            "Cout": [self.df[passed_mask].shape[0], self.df[unpassed_mask].shape[0]]
        }
        return pd.DataFrame(result)

    def get_exam_avarage_and_sum(self):
        scores = self.df.iloc[:, 4:7]
        result = self.df.copy()
        result["sum_result"] = scores.sum(axis=1)
        result["avg_result"] = result["sum_result"] / 3
        return DataFrameOperations(result)

    def write_to_csv(self, file_name):
        if not file_name.endswith('.csv'):
            raise ValueError("File name must end with '.csv'.")
        self.df.to_csv(file_name, index=False)
