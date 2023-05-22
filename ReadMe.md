# Contract Review and Analysis
This project utilizes artificial intelligence to streamline the contract review process. It identifies key phrases, clauses, rights and obligations of an individual or company signing it and assessing the associated impact helping lawyers spot potential problems and make the review process more efficient.

## Introduction
The machine learning learn to automatically extract and identify key clauses from contracts, thus saving hundreds of hours of manual labour and cost. The system was trained and learns with the [CUAD DATASET](https://arxiv.org/abs/2103.06268).

The research work on the Contract Understanding Atticus Dataset (CUAD), consists of over 500 contracts, each carefully labelled by legal experts, to identify 41 different types of important clauses.

We have leveraged the pretrained model from the [Atticus Project](https://www.atticusprojectai.org/cuad) to make our predictions. A Flask-based frontend has been developed to interface with the model.

## Folder Structure
* static : Contains all the styling required for the Flask application.
* templates : Contains the HTML files required for the frontend of our Flask application.
* Contract_Review_PR.ipynb : The notebook file that runs the pretrained model with the questions and contract.
* index.py : The main file to run the Flask application. You will need to define the path to the model. The model can be gotten from https://zenodo.org/record/4599830#.ZGj8zXbML18
* predict.py : Contains the function to make predictions from the pretrained model.
* questions.txt : This file contains all 41 questions that the model was trained on.
* requirements.txt : Lists the Python libraries required for this project.

## How to Run the Project
* Clone the repository to your local machine.
* Navigate to the project directory.
* (Optional) Create a new virtual environment and activate it.
* Install the requirements using pip.
* Download the pretrained model from the following link and place it in your local project directory.
* Open index.py and change the model path variable to the path where you have stored the downloaded model.
* Run the Flask application. using "python index.py"
