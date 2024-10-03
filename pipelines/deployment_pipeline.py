import click
from pipelines.training_pipeline import ml_pipeline
from zenml.integrations.mlflow_utils import get_tracking
@click.command()
def main():
    """
    
    """
    run = ml_pipeline()