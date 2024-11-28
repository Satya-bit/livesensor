#It has the ouput of all modules like data ingestion, data validation etc for making the artifacts to pass to next component
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str
    
@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_file_path: str
    
@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str

@dataclass
class ClassificationMetricArtifact:
    f1_score: float
    precision_score: float
    recall_score: float

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
    train_metric_artifact: ClassificationMetricArtifact
    test_metric_artifact: ClassificationMetricArtifact



@dataclass
class ModelEvaluationArtifact:

    is_model_accepted: bool
    improved_accuracy: float
    best_model_path: str
    trained_model_path: str
    train_model_metric_artifact: ClassificationMetricArtifact
    best_model_metric_artifact: ClassificationMetricArtifact
    
@dataclass
class ModelPusherArtifact:
    saved_model_path:str   #FOR LONG TERM BACKUP
    model_file_path:str    #FOR SHORT TERM USE FOR THE ARTIFACT FOR DEPLOYMENT OR PASS TO EXT COMPONENT