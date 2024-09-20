import os
import zipfile
from abc import ABC, abstractmethod

import pandas as pd


# Abstract class for Data Ingestor
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Abstract method to ingest data from given file."""
        pass


# Abstract class for Data Ingestor
class ZipDataIngestor(DataIngestor):
    #@abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Extract a .zip file and returns the content as a pandas files"""

        # Verify if the file is a .zip 
        if not file_path.endswith(".zip"):
            raise ValueError("The provided file is not a .zip file")
        
        # Extract a zip file
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall("extracted_data")

        # Get the CSV file
        extracted_files = os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]

        if len(csv_files) == 0:
            raise FileNotFoundError("There are no CSV file")
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files found, please select wich one you need to use")
        
        # Read CSV file into a DataFrame
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)

        return df
    

# Implement a factory to create bDataIngestors
class DataIngestFactory:
    @staticmethod
    def get_data_ingest(file_extension: str) -> DataIngestor:
        """ Returns the appropriate DataIngestor based on file extension."""
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f"No ingestor availabe for file extension: {file_extension}")


# Example usage
if __name__ == "__main__": 
    
    # File path
    file_path = "/home/ubuntu/mlops-projects/Prices-Priedictor-System/data/AmesHousing.zip"
     
    # Determine the file extension
    file_extension = os.path.splitext(file_path)[1]
     
    # Get the appropiete DataIngestor
    data_ingestor = DataIngestFactory.get_data_ingest(file_extension)

    df = data_ingestor.ingest(file_path)
    if not df.empty:
        print("Data ingested successfully!") 
        print(df.shape)
        print(df.head())
    else:
        print("No data in the DataFrame.")