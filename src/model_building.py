import logging
from abc import ABC, abstractmethod
from typing import Any

import pandas as pd 
from sklearn.base import RegressorMixin
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class ModelBuildingStrategy(ABC):
    @abstractmethod
    def build_and_train_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> RegressorMixin:
        pass


class LinearRegressionStrategy(ModelBuildingStrategy):
    def build_and_train_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
        if not isinstance(X_train, pd.DataFrame):
            raise TypeError("X_train must be a pandas DataFrame.")
        if not isinstance(y_train, pd.Series):
            raise TypeError("y_train must be a pandas Series.")

        logging.info("Initializing Linear Regression model with scaling.")
        
        pipeline = Pipeline(
            [
                ("scaler", StandardScaler()), # Feature scaling
                ("model", LinearRegression()) # Linear regression model
            ]
        )

        logging.info("Training Linear Regression model.")
        pipeline.fit(X_train, y_train) # Fitting the model

        logging.info("Model training completed.")
        return pipeline


class ModelBuilder:
    def __init__(self, strategy: ModelBuildingStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: ModelBuildingStrategy):

        logging.info("Switching model building strategy.")
        self._strategy = strategy


        def build_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> RegressorMixin:

            logging.info("Building and training the model using the strategy.")
            return self._strategy.build_and_train_model(X_train, y_train)
        



# Example usage
if __name__ == "__main__":
    # Example DataFrame (replace with actual data loading)
    # df = pd.read_csv('your_data.csv')
    # X_train = df.drop(columns=['target_column'])
    # y_train = df['target_column']

    # Example usage of Linear Regression Strategy
    # model_builder = ModelBuilder(LinearRegressionStrategy())
    # trained_model = model_builder.build_model(X_train, y_train)
    # print(trained_model.named_steps['model'].coef_)  # Print model coefficients

    pass