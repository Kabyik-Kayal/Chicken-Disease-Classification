from Chicken_disease_classifier import logger
from Chicken_disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed Successfully <<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e

