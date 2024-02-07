from CNNClassifier import logger
from CNNClassifier.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_2_prepare_model import PrepareBaseModelTrainingPipeline
from CNNClassifier.pipeline.stage_3_model_trainer import ModelTrainingPipeline
from CNNClassifier.pipeline.stage_4_model_evaluation import EvaluationPipeline
STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<<")
    obj =DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Prepare base model"
try:
    logger.info(f"***********")
    logger.info(f">>>>>>>>>>{STAGE_NAME} started <<<<<<<<<")
    obj=PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Evaluation stage"

try:
    logger.info(f"***********")
    logger.info(f">>>>>>>>>>>stage {STAGE_NAME} started <<<<<<")
    obj=EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>. stage {STAGE_NAME} completed ")
except Exception as e:
    logger.exception(e)
    raise e