# Differential Privacy Interface

## Introduction
The goal of this project is to use the SmartNoise sdk in a MITM proxy that sits between a querier and a database.

* The user should be able to make basic aggregate queries as permitted
in SmartNoise such as count() and sum() but should reject other queries.
* The interface itself should use a simple config file which defines what queries are allowed and what the parameters should be for the interface.
  

## Technical Specification
Refer to this [link](https://docs.google.com/document/d/1Up2pG3Q17O37CDpZ5BMFxB0581DOfUUZDPI2Dqm_I_g/edit?usp=sharing) for technical specification.

## To Run the Project


1. Create a python virtual environment. Refer to this [link](https://stackoverflow.com/questions/13855463/bash-mkvirtualenv-command-not-found) for any errors.
    ```
    pip install virtualenv
    mkvirtualenv my-venv
    workon myenv
    ```
2. Clone the repo and cd into the directory
3. Install all dependencies 
    ``` 
    pip3 install -r requirements.txt
    ```
4. Run the app (Server is opened at: 'http://127.0.0.1:5000/' and is running in development env with debug on)
   ``` 
   flask run 
   ```
5. Do a GET call with the SQL queries:
   ```
    curl -d '{"query":"SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married"}' -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/
   ```