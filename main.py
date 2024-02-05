from CNNClassifier import logger
from CNNClassifier.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_2_prepare_model import PrepareBaseModelTrainingPipeline


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