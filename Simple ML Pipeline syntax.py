
from kfp.v2 import dsl
from kfp.v2.dsl import component

#Component is containerized
@component(
    base_image="python:3.7",  # Default base image used if none is specified (here, it's explicitly mentioned)
    packages_to_install=["pandas"]  # Install the required package(s)
)
def data_prep(input_data: str) -> str:
    # This is where data preprocessing happens
    # Example: Load and clean the dataset using Pandas

#Component is containerized
@component(
    base_image="python:3.7",  # Default base image
    packages_to_install=["scikit-learn"]  # Install scikit-learn for training the model
)
def model_train(preprocessed_data: str) -> str:
    # This is where model training happens
    # Example: Train a machine learning model using scikit-learn
  
#Component is containerized
@component(
    base_image="python:3.7",  # Default base image
    packages_to_install=["scikit-learn"]  # Install scikit-learn for model evaluation
)
def model_eval(trained_model: str) -> str:
    # This is where model evaluation happens
    # Example: Evaluate the trained model using scikit-learn
    


@dsl.pipeline(
    name='Simple ML Pipeline',
    description='A very simple machine learning pipeline with data prep, train, eval, and deploy'
)
def simple_ml_pipeline(input_data: str):
    # Step 1: Data Preparation
    data_prep_task = data_prep(input_data=input_data)
    
    # Step 2: Model Training
    model_train_task = model_train(preprocessed_data=data_prep_task.output)
    
    # Step 3: Model Evaluation
    model_eval_task = model_eval(trained_model=model_train_task.output)


if __name__ == '__main__':
    from kfp.v2 import compiler
    compiler.Compiler().compile(simple_ml_pipeline, 'simple_ml_pipeline.yaml')
