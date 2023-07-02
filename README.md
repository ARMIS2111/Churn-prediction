# Customer Churn Classification Project
This project aims to predict customer churn using Artificial Neural Networks (ANN) implemented with Keras. Customer churn refers to the phenomenon where customers discontinue their business relationship with a company or service. By accurately identifying customers who are likely to churn, companies can take proactive measures to retain them.

# Project Structure
The project structure is as follows: <br/>

This dataset used for training and testing the model is named Customer-Churn-Records.<br/>
This the trained model files are attached.<br/>
app.py: This file contains the Flask web application.<br/>
README.md: This file provides an overview of the project.<br/>
churn_data.csv: The main dataset file containing customer information and churn labels.<br/>


# Model Training
The customer churn classification model is implemented using Artificial Neural Networks (ANN) and Keras. The model is trained using the Customer-Churn-Records.csv dataset. The notebook Customer-churn_classification.ipynb in the root directory contains the code for loading the dataset, preprocessing the data, building the model, and training it. The trained model is saved.<br/>

# Flask App
The Flask web application is implemented to provide a user interface for predicting customer churn based on the trained model. <br/>
app.py: The main Flask application file that handles routing and prediction.<br/>
templates/index.html: The landing page of the web application, which is Bootstrap enabled and provides a form for inputting customer information.<br/>

Feel free to explore the code, dataset, and make use of the Flask app to make predictions and analyze customer churn in your own business context.
