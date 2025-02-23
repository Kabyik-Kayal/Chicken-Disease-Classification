from Chicken_disease_classifier import logger
from Chicken_disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Chicken_disease_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed Successfully <<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f'>>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e