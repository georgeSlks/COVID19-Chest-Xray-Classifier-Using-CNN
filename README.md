# COVID-19 Chest X-ray Classifier Using CNN (DenseNet-121)

A deep learning project that classifies chest X-ray images as **COVID-19** or **Normal** (binary classification) using a Convolutional Neural Network based on the DenseNet-121 architecture. The project contains dataset foldering management, data preprocessing, training, testing and performance analysis.

## Dataset

- **Source:** [COVID-19 Radiography Database – Kaggle](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database)
- **Classes Used:** 
  - COVID
  - Normal
- The other classes(folders) in the dataset (Viral Pneumonia, Lung Opacity) were excluded to focus on binary classification.
- Also i didn't use metadata and Masks folder which contains segmentation masks that show the regions of the lung affected by pneumonia or COVID-19.
- I just simply used the xray images from the Covid and Normal folders.

## Dataset Management

This Python script (DatasetRepositoriesManagement.py) was created to:
- Select COVID and Normal images.
- Split into `train`, `val`, and `test` sets.
- Organize directories and move images accordingly.
- I used the 80/10/10 split rule.

## Model Architecture

- **Base Model:** DenseNet-121 (pre-trained on ImageNet)
- **Transfer Learning:** Final classifier layers modified for binary classification
- **Loss Function:** CrossEntropyLoss
- **Evaluation:** Accuracy & loss tracked per epoch

## Results

## Performance Analysis
- **Test Accuracy:** 97%
