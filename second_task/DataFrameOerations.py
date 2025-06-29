import numpy as np
import pandas as pd

class DataFrameOperations:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.columns = self.df.columns.tolist()
        self.rows = self.df.shape[-1]

    def display_column(self, column):
        if column not in self.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        return self.df[column]

    def sorted_df(selfs, column_name, value, operation, max_rows=10**10):
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


def main():
    operations = DataFrameOperations("dataset_marks.csv")
    cur_columns = operations.columns
    print(cur_columns)
    score_of_not_test_prepared = operations.sorted_df(cur_columns[3], "none", "=").shape[0]
    print(f"Number of students not prepared for the test: {score_of_not_test_prepared}")

if __name__ == "__main__":
    main()
