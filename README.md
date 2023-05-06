# Brain Tumor Classification

This repository contains code for training and testing a deep learning model for classifying brain tumors.

## Using

To use the

1. Clone this repo at the suitable directory
2. Install requirements
   ```
   pip install requirements.txt
   ```
3. Downloading the input data

   1. Download the dataset from [https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset/download?datasetVersionNumber=1]
   2. Extract the dataset and place the data into root of repository
   3. The dataset directory should have following structure:

   ```
      input/
      ├── training/
      │ ├── glioma/
      │ │ ├── glioma_001.jpg
      │ │ ├── glioma_002.jpg
      │ │ ├── ...
      ├── testing/
      │ ├── no_tumor/
      │ │ ├── no_tumor_101.jpg
      │ │ ├── ...
   ```

4. Open the directory in VSCode
5. Choose the desired model's 'use\_<model_name>.ipynb' file
   Specify the image path and storage path for the CAM image file
   Run all

## Training

1. Choose the desired model to train and opne '<model_name>\_training.ipynb'
2. Run All
3. Access the trained model at 'savedmodels/'
