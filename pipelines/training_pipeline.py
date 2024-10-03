from steps.data_ingestion_step import data_ingestion_step
from steps.data_splitter_step import data_splitter_step
from steps.handle_missing_values_step import handle_missing_values_step

from zenml import Model, pipeline, step


@pipeline(
    model = Model(
        name="prices_predictor"
    ),
)

def ml_pipeline():
    raw_data = data_ingestion_step(
        file_path = "/home/ubuntu/mlops-projects/Prices-Priedictor-System/extracted_data/AmesHousing.csv"
    )

    filled_data = handle_missing_values_step(raw_data)