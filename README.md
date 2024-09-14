## Lungs Xray Classification with deep learning 


In this project, I developed an X-ray lung classification model using deep learning techniques to detect lung abnormalities. Leveraging the PyTorch framework, I trained a convolutional neural network (CNN) to classify chest X-rays as either healthy or showing signs of lung disease. The model was then integrated into a web API for real-time predictions and deployed using Docker for scalability and accessibility.


## worflow

- constants : Defines global constants used across the project, such as paths, configurations, and hyperparameters.
- config_entity : Contains configuration classes that manage various settings required for different stages of the workflow.
- artifact_entity : Defines classes to represent artifacts generated at each stage of the machine learning pipeline.
- components : Houses core modules for data ingestion, model training, evaluation, and prediction components.
- pipeline :  Orchestrates the entire workflow by connecting various components and executing the machine learning pipeline.
- main :  Entry point of the project that triggers the execution of the pipeline, handling end-to-end processing.

## How to setup

```bash
conda create -p env python=3.8 -y
```
```bash
conda activate env
```
```bash
git clone https://github.com/kunalshelke90/Xray_Image_Classification.git

```
```bash
cd Xray_Image_Classification

```
```bash
pip install -r requirements.txt
```
- setup AWS CLI

```bash
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```
```bash
aws configure
```

- setup this information

```bash
AWS Access Key ID=
AWS Secret Access Key=
Default region name=
```
- to run the code with streamlit

```bash
python app.py
```