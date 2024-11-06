The goal of this project is to manage the lifecycle of our models using MLflow. 

Part 0

    Install locally MLFlow on your setup. For that you can use the method you want (manual install or using docker official image : https://mlflow.org/docs/latest/docker.html)
    Make sure you can access the web UI of ML flow

Part 1 - Tracking a model training

1.1 Using the MLflow documentation (here for instance), make a model training script on a simple dataset of your choice. 

The model training script should track : 

    the model hyper-parameters
    the model metric (mse, accuracy or whatever)

No need to version the model for now

1.2 Run the script and check that the tracked data are available in mlflow UI

1.3 Change one hyper parameter of the model and rerun the training script. Check that both this run and the previous one are availables.

1.4 Make sure that the model is also save in MLFlow. Rerun the training script and access it in the interface

Part 2 - Deploying model from MLFlow  

We now want to have a web service service to serve our machine learning model.

The web service should 

    load the model model from the MLFlow server upon start of the server
    a /predict endpoint to return predictions upon a Post request
     a /update-model endpoint  allowing to  update the model with a webflow model version

    Build such service with fastAPI or flask, or any other service
    make a script to test automatically test your /predict endpoint 
    update the script so that it also test that /update-model works well
    Dockerise your webservice 
