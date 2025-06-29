import pandas as pd

class DataFrame:
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        self.columns = self.data.columns

    def get_column(self, column_index):
        if column_index < 0 or column_index >= len(self.columns):
            raise IndexError("Column index out of range")
        return self.data.iloc[:, column_index]

    def sort_old_houses(self):
        return self.data.sort_values(by='YearBuilt', ascending=True)

    def get_average_price(self):
        return self.data['Price'].sum() / self.data.shape[0]

    def get_median_price(self):
        return self.data['Price'].median()

    def sort_by_price(self, price, reverse=False):
        if reverse:
            mask = self.data['Price'] < price
        else:
            mask = self.data['Price'] > price
        return self.data[mask]

    def group_by(self, column):
        if column not in self.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame")
        group = self.data["Bathrooms"].value_counts().reset_index()
        return group

    def normolize_df(self):
        mask = self.data['Price'] > 0
        self.data = self.data[mask].reset_index(drop=True)
        return self.data

    def get_room_count(self):
        counts = self.data.loc[:, ["Bedrooms", "Bathrooms"]].sum(axis=1)
        return counts

    def get_factor(self):
        factor = self.data.loc[:, ["Price", "SquareFeet"]].apply(lambda x: round(x['Price'] / x['SquareFeet'], 2), axis=1)
        return factor

    def change_price_format(self):
        self.data['Price'] = self.data['Price'].apply(lambda x: round(x))
        return self.data

    def new_column(self, column_name, data):
        if column_name in self.columns:
            raise ValueError(f"Column '{column_name}' already exists in the DataFrame")
        if len(data) != len(self.data):
            raise ValueError("Length of new data does not match the length of the DataFrame")
        self.data[column_name] = data
        self.columns = self.data.columns

    def change_df(self, path):
        self.normolize_df()
        self.new_column("num_rooms", self.get_room_count())
        self.change_price_format()
        self.new_column("factor", self.get_factor())
        self.data.to_csv(path)