# Algerian Forest Fire Prediction Using Machine Learning

## Project Overview

This project focuses on predicting the Fire Weather Index (FWI) using meteorological and environmental factors from the Algerian Forest Fires dataset. The objective is to analyze the relationship between weather conditions and fire risk while building an accurate regression model for prediction.

The project follows a complete machine learning workflow, including data preprocessing, feature engineering, exploratory data analysis, model training, evaluation, and model serialization for future deployment.

## Dataset Description

The dataset contains weather and fire-related measurements collected from regions in Algeria. Key features include:

* Temperature
* Relative Humidity (RH)
* Wind Speed (Ws)
* Rain
* Fine Fuel Moisture Code (FFMC)
* Duff Moisture Code (DMC)
* Initial Spread Index (ISI)
* Fire Class
* Region

Target Variable:

* Fire Weather Index (FWI)

## Project Workflow

### Data Preprocessing

* Loaded and explored the dataset
* Removed unnecessary date-related columns
* Cleaned and encoded categorical variables
* Performed train-test splitting
* Applied feature scaling using StandardScaler

### Exploratory Data Analysis

* Statistical summary of the dataset
* Correlation matrix analysis
* Heatmap visualization
* Multicollinearity assessment

### Machine Learning Models

The following regression models were implemented and compared:

1. Linear Regression
2. Ridge Regression (RidgeCV)
3. Lasso Regression (LassoCV)
4. Elastic Net Regression (ElasticNetCV)

### Model Evaluation Metrics

The models were evaluated using:

* Mean Absolute Error (MAE)
* R² Score

## Results

| Model             | MAE    | R² Score |
| ----------------- | ------ | -------- |
| Linear Regression | 0.5468 | 0.9848   |
| RidgeCV           | 0.5642 | 0.9843   |
| ElasticNetCV      | 0.5782 | 0.9839   |
| LassoCV           | 0.7085 | 0.9783   |

### Best Performing Model

Linear Regression achieved the best overall performance:

* MAE: 0.5468
* R² Score: 0.9848

The results indicate that the model can accurately predict Fire Weather Index values while maintaining a low prediction error.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Pickle

## Model Deployment Preparation

The trained model and scaler were serialized using Pickle to enable future deployment and integration into web applications.

## Author

Rithick M
