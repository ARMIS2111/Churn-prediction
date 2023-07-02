# Customer Churn Classification Project
This project aims to predict customer churn using Artificial Neural Networks (ANN) implemented with Keras. Customer churn refers to the phenomenon where customers discontinue their business relationship with a company or service. By accurately identifying customers who are likely to churn, companies can take proactive measures to retain them.

# Project Structure
The project structure is as follows:

This dataset used for training and testing the model is named Customer-Churn-Records.
This the trained model files are attached.
app.py: This file contains the Flask web application.
README.md: This file provides an overview of the project.
churn_data.csv: The main dataset file containing customer information and churn labels.


# Model Training
The customer churn classification model is implemented using Artificial Neural Networks (ANN) and Keras. The model is trained using the churn_data.csv dataset. The notebook churn_classification.ipynb in the root directory contains the code for loading the dataset, preprocessing the data, building the model, and training it. The trained model is saved in the models folder.

# Flask App
The Flask web application is implemented to provide a user interface for predicting customer churn based on the trained model. 
app.py: The main Flask application file that handles routing and prediction.
templates/index.html: The landing page of the web application, which is Bootstrap enabled and provides a form for inputting customer information.

Feel free to explore the code, dataset, and make use of the Flask app to make predictions and analyze customer churn in your own business context.
