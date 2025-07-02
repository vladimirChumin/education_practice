from matplotlib import pyplot as plt
from DataFrameOerations import DataFrameOperations

def main():
    df = DataFrameOperations("dataset_marks.csv")
    df.ethnical_diagram(result_score=179)
    df.ethnicaly_gender_diagram()
    df.exam_score_histogram(step=5)
    df.gender_parents_education_histogram()

if __name__ == "__main__":
    main()

