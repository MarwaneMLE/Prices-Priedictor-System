import logging
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class OutlierDetectionStretegy(ABC):
    def outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        
        """
        pass


class ZScoreOutlierDetection(OutlierDetectionStretegy):
    def __init__(self, threshold=3):
        self.threshold = threshold

    def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Detecting outliers using the Z-score method.")
        z_scores = np.abs((df - df.mean()) / df.std())
        outliers = z_scores > self.threshold
        logging.info(f"Outliers detected with Z-scores threshold : {self.threshold}")
        return outliers



class IQROutlierDetection(OutlierDetectionStretegy):
    def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Detecting outliers using the IQR method.")
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        outliers = (df < (Q1 - 1.5 * IQR)) | (df > (Q3 - 1.5 * IQR))
        logging.info(f"Outliers detected with IQR threshold : {self.threshold}")
        return outliers


class OutlierDetector:
    def __init__(self, strategy: OutlierDetectionStretegy):
        self._strategy = strategy

    def set_strategy(self, strategy: OutlierDetectionStretegy):
        logging.info("Switching outlier detection strategy.")
        self._strategy= strategy

    def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Executing outlier detection strategy.")
        return self._strategy.detect_outliers(df)

    def handle_outliers(self, df: pd.DataFrame, method='remove'):
        outliers = self.detect_outliers(df)
        if method == "remove":
            logging.info("Removing outliers from the dataset.")
            df_cleaned = df[(~outliers).all(axis=1)]
        elif method == "cap":
            logging.info("Capping outliers in the dataset.")
            df_cleaned = df.clip(lower=df.quantile(0.01), upper=df.quantile(0.99), axis=1)
        else:
            logging.warning(f"Unknown method '{method}'. No outliers handling performed.")
            return df
    
    def visualize_outliers(self, df: pd.DataFrame, features: list):
        logging.info(f"Visualizing outliers for features: {features}")
        for feature in features:
            plt.figure(figsize=(10,6))
            sns.boxplot(x=df[feature])
            plt.title(f"Boxplot of {feature}")
            plt.show()
        