from steps.data_ingestion_step import data_ingestion_step
from steps.data_splitter_step import data_splitter_step
from steps.handle_missing_values_step import handle_missing_values_step
from steps.feature_engineering_step import feature_engineering_step
from steps.outlier_detection_step import outlier_detection_step
from zenml import Model, pipeline, step


@pipeline(
    model = Model(
        name="prices_predictor"
    ),
)

def ml_pipeline():
    raw_data = data_ingestion_step(
        file_path="/home/marwane/mlops-projects/Prices-Priedictor-System/data/archive.zip"
    )

    filled_data = handle_missing_values_step(raw_data)

    # Feature engineering step
    engineered_data = feature_engineering_step(
        filled_data, strategy="log", features=["Gr Liv Area", "SalePrice"]
    )
    
    # outlier detecting step
    clean_data = outlier_detection_step(engineered_data, column_name="SalePrice")

    # Split thhe data
    X_train, X_test, y_train, y_test = data_splitter_step(clean_data, target_column="SalePrice")