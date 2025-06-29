import pandas as pd
import numpy as np
from DataFrame import DataFrame


def main():
    data = pd.read_csv("dataset_house_price1.csv")
    df = DataFrame(data)
    oldest_houses = df.sort_old_houses().head(10)
    more_median = df.sort_by_price(df.get_median_price())
    more_average = df.sort_by_price(df.get_average_price())
    less_average = df.sort_by_price(df.get_average_price(), reverse=True)
    grouped_by_bethrooms = df.group_by("Bedrooms")
    print(oldest_houses)
    print(more_median)
    print(more_average)
    print(less_average)
    print(grouped_by_bethrooms)
    df.change_df("new_dataset.csv")
    print(1)


if __name__ == "__main__":
    main()