import pandas as pd
from src.ingest_data import DataIngestFactory
from zenml import step


@step
def data_ingestion_step(file_path: str) -> pd.DataFrame:
    file_path = ".zip"

    data_ingestor = DataIngestFactory.get_data_ingest(file_path)

    df = data_ingestor.ingest(file_path)

    return df