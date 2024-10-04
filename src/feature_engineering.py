from abc import ABC, abstractmethod
import pandas as pd
import logging
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, StandardScaler


 





class FeatureEngineeringStrategy(ABC):
    @abstractmethod
    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        
        """
        pass
class LogTransformation(FeatureEngineeringStrategy):
    def __init__(self, features):
        """
        
        """
        self.features = features
    
    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Applying lo tranfsormation to features: {self.features}")
        df_transformed = df.copy()
        for feature in self.features:
            df_transformed[feature] = np.log1p(
                df[feature]
            )
        logging.info("Log transformation completed.")

        return df_transformed


class StandardScaling(FeatureEngineeringStrategy):
    
    def __init__(self, features):
        """
    
        """
        self.features = features
        self.scaler = StandardScaler()

    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        
        """ 
        logging.info(f"Applying StandardScaler tranfsormation to features: {self.features}")
        df_transformed = df.copy()
        df_transformed[self.features] = self.scaler.fit_transform(df[self.features])
        logging.info("Standard scaling completed.")
        return df_transformed
    

class MinMaxScaling(FeatureEngineeringStrategy):
    def __init__(self, features, feature_range=(0,1)):
        """
    
        """
        self.features = features
        self.scaler = MinMaxScaler(feature_range=feature_range)

    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        
        """ 
        logging.info(f"Applying MinMaxScaler tranfsormation to features: {self.features}")
        df_transformed = df.copy()
        df_transformed[self.features] = self.scaler.fit_transform(df[self.features])
        logging.info("Min-Max scaling completed.")
        return df_transformed