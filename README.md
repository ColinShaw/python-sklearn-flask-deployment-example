# SKLearn Flask Deployment



This is an example of deploying an SKLearn model using Flask.  Endpoints are for both training
and prediction.  A convenient sheel script is provided to launch the Flask app.  You can
submit training from command line:

```
 curl -X POST -d '@data/train.json' http://localhost:5000/train
```

You can make a prediction from command line:

```
 curl -X POST -d '@data/predict.json' http://localhost:5000/predict
```

