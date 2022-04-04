[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=pdemeulenaer_iris-flask-example&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=pdemeulenaer_iris-flask-example)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=pdemeulenaer_iris-flask-example&metric=coverage)](https://sonarcloud.io/summary/new_code?id=pdemeulenaer_iris-flask-example)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=pdemeulenaer_iris-flask-example&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=pdemeulenaer_iris-flask-example)

[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/summary/new_code?id=pdemeulenaer_iris-flask-example)

Simple Flask demo, copied and modified from https://github.com/GhostUser/IRIS-classification-flask-api

What has been added:

* Strongly modified Flask app structure, following tutorial here: https://pythonise.com/series/learning-flask/flask-application-structure

* predict_api_file in the flask app, so that now we can predict a whole CSV file

* fixed version of packages

* added CI/CD pipeline (github actions)

TODO

* add a deployment in the CD

* add unit tests

* use mock in tests?

* add mlflow tracking and model registration

* containarize the flask app: follow https://pythonise.com/series/learning-flask/building-a-flask-app-with-docker-compose (seems more advanced than usual containarized Flask setups)
