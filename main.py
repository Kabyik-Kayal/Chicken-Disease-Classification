from Chicken_disease_classifier import logger
from Chicken_disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Chicken_disease_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Chicken_disease_classifier.pipeline.stage_03_training import ModelTrainingPipeline
from Chicken_disease_classifier.pipeline.stage_04_evaluation import EvaluationPipeline

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

STAGE_NAME = "Training"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e