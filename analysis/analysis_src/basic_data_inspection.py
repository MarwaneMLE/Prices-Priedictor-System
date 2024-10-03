from abc import ABC, abstractmethod
import pandas as pd



class DataInspectionStrategy(ABC):
    """
    Abstract class for Data Inspection
    """
    def inspect(self, df:pd.DataFrame):
        """
        inspect method to perform specific type of data inspection

        Args:
            df: dtaframe to inspect

        Returns: 
            None: this method print the inspection results
        """
        pass


class DataTypesInspectionStrategy(DataInspectionStrategy):
    """
    Abstract class for Data Inspection
    """
    def inspect(self, df:pd.DataFrame):
        """
        inspect method to perform specific type of data inspection

        Args:
            df(pd.DataFrame): dataframe to inspect

        Returns: 
            None: prints data Types and Non-null Counts
        """
        print("\nData Types and Non-null Counts:")
        print(df.info())


class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    """
    To check descriptive statistics
    """
    def inspect(self, df:pd.DataFrame):
        """
        Prints summary statistics for numerical and categoricaal data
        Args:
            df(pd.DataFrame): dataframe to inspect

        Returns: 
            None: prints summary statistics
        """
        print("\n Summary Statistics of (Numerical Features):")
        print(df.describe())

        print("\n Summary Statistics of (Categorical Features):")
        print(df.describe(include=["object"]))


class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Initializes the DataInspector with a specific inspection
        Args:
            strategy(DataInspectionStrateg): The strategy to be us
        Returns:
            None 
        """
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        """
        Sets a new strategy for the DataInspector

        Args:
            strategy(DataInspectionStrateg): The strategy to be us
        
        Returns:
            None
        """
        self._strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        """
        Executes the inspection using the current strategy.

        Args:
            df(pd.DataFrame): dataframe to inspect

        Returns: 
            None: Executes the strategy's inspection method
        """
        self._strategy.inspect(df)



# Example usage
if __name__ == "__main__": 
    # Example usage of the DataInspector with different strategies
    # Load the data
    #df = pd.read_csv("/home/ubuntu/mlops-projects/Prices-Priedictor-System/extracted_data/AmesHousing.csv")

    # INITIALIZE THE DATA INSPECTOR WITH A SPECIFIC STRATEGY
    #inspector  = DataInspector(DataTypesInspectionStrategy())
    #inspector.execute_inspection(df)

    # Change strategy to Summary Statistics and execute
    #inspector.set_strategy(SummaryStatisticsInspectionStrategy())
    #inspector.execute_inspection(df)
    pass