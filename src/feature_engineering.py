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



class OneHotEncoding(FeatureEngineeringStrategy):
    def __init__(self, features):
        self.features = features
        self.encoder = OneHotEncoder(sparse=False, drop="first")


    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        """
        logging.info(f"Applying One Hot Encoding to features: {self.features}")
        df_transformed = df.copy()
        encoded_df = pd.DataFrame(
            self.encoder.fit_transform(df[self.features]),
            columns=self.encoder.get_feature_names_out(self.features)
        )
        df_transformed = df_transformed.drop(columns=self.features)
        df_transformed = pd.concat([df_transformed, encoded_df],)
        logging.info("One Hot Encoding completed.")
        return df_transformed
    


class FeatureEngineer:
    def __init__(self, strategy: FeatureEngineeringStrategy):
        """
        
        """
        logging.info("Switching features engineering strategy.")
        self._strategy = strategy

    def apply_feature_engineering(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Applying feature engneering strategy.")
        return self._strategy.apply_transformation(df)



# Example usage
if __name__ == "__main__":
    # Example dataframe
    df = pd.read_csv('/home/marwane/mlops-projects/Prices-Priedictor-System/extracted_data/AmesHousing.csv')
    
    # Log Transformation Example
    #log_transformer = FeatureEngineer(LogTransformation(features=['SalePrice', 'Gr Liv Area']))
    #df_log_transformed = log_transformer.apply_feature_engineering(df) 

    # Standard Scaling Example
    #standard_scaler = FeatureEngineer(StandardScaling(features=['SalePrice', 'Gr Liv Area']))
    #df_standard_scaled = standard_scaler.apply_feature_engineering(df)
    #print(df_standard_scaled.head())
    pass

