'''
Module to find predictions of housin prices of California districts
'''
# import libraries
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
import os
from utils import HOUSING_PATH

class Housing:
    def __init__(self, ratio=0.2) -> None:
        self.load_housing_data(HOUSING_PATH)
        self.analyse_data()
        self.plot_histogram()
        self.split_dataset(ratio)
    # Convert the data to a format you can easily manipulate 
    # (without changing the data itself)

    # This function returns a Pandas DataFrame object containing all the data
    def load_housing_data(self, housing_path):
        csv_path = os.path.join(housing_path, "housing.csv")
        self.housing = pd.read_csv(csv_path)
    
    # Check the size and type of data (time series, sample, geographical, etc.)
    def analyse_data(self):
        # The method shows a summary of the describe() numerical attributes
        self.housing.describe()

        # info() method is useful to get a quick description of the data
        self.housing.info()

        # find out what categories exist and how many districts belong to
        #  each category by using the value_counts() method
        self.housing['ocean_proximity'].value_counts()

    # this function plots the histogram for all the features 
    def plot_histogram(self):
        self.housing.hist(bins=50, figsize= (20,15))
        plt.show()

    # distribute the dataset into train and test
    def split_dataset(self, ratio):
        self.train_set, self.test_set = train_test_split(self.housing, test_size=ratio, random_state=42)
    
    # since the target variable is not evenly distributed,
    # make sure the split ensures a stratified sampling
    # to avoid sampling bias

    # for that first create a new feature with income category attribute
    def income_category(self):
        self.housing['income_cat'] = pd.cut(self.housing, 
                                            bins=[0.0, 1.5])
    def stratified_split(self):
