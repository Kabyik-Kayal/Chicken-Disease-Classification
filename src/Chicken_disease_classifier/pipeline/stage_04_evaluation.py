from Chicken_disease_classifier.config.configuration import ConfigurationManager
from Chicken_disease_classifier.components.evaluation import Evaluation
from Chicken_disease_classifier import logger

STAGE_NAME = 'Model Evaluation'

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
    
    except Exception as e:
        logger.exception(e)
        raise e