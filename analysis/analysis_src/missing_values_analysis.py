from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class MissingValuesAnalysisTemplate(ABC):
    def analyze(self, df: pd.DataFrame):
        """
        Check if there are a missing values

        Args:
            df(pd.DataFrame): the dataframe to analyse
        
        Returns: 
            None: prints the analysis and visualization
        """
        self.identify_missing_values(df)
        self.visualize_missing_values(df)

    @abstractmethod
    def identify_missing_values(self, df: pd.DataFrame):
        """
        Identifies missing vales in the dataframe

        Args:
            df(pd.DataFrame): the dataframe to analyse
        
        Returns: 
            None: prints the analysis and visualization
        """
        pass

    @abstractmethod
    def visualize_missing_values(self, df: pd.DataFrame):
        pass


class SimpleMissingValuesAnalysis(MissingValuesAnalysisTemplate):
    def identify_missing_values(self, df: pd.DataFrame):
        """
        Prints the count of missing values for each column in the

        Args:
            df(pd.DataFrame): the dataframe to analyse
        
        Returns: 
            None: prints missings count to the  console
        """
        print("\n Missing Values Count by Column:")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])

    def visualize_missing_values(self, df: pd.DataFrame):
        """
        Prints the cout of missing vales for each column in the  
        
        Args:
            df(pd.DataFrame): the dataframe to analyse
        
        Returns: 
            None: Display Heatmap of missing values.
        """
        print("\n Visualizing Missing values:")
        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
        plt.title("Missing values Heatmap")
        plt.show()


# Example usage
if __name__ == "__main__": 
    # Example usage of the DataInspector with different strategies
    # Load the data 
    #df = pd.read_csv("/home/ubuntu/mlops-projects/Prices-Priedictor-System/extracted_data/AmesHousing.csv")

    # INITIALIZE THE DATA INSPECTOR WITH A SPECIFIC STRATEGY
    #missing_values_analysis  = SimpleMissingValuesAnalysis(MissingValuesAnalysis())
    #missing_values_analysis.analysis(df)

    # Change strategy to Summary Statistics and execute
    #inspector.set_strategy(SummaryStatisticsInspectionStrategy())
    #inspector.execute_inspection(df)
    pass