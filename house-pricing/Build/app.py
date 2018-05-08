from flask import Flask
from flask import Response
from flask import request
import mlModel


app = Flask(__name__)


################# Train mlModel on start ###################
# TODO: put model training into a separate app and save/load the model weights
W, b, mean, maxDifference = mlModel.getTrainedWeights()


@app.route("/predict-by-size/<house_size>")
def predict_house_price(house_size):
    house_size = float(house_size)
    prediction = mlModel.predict(house_size, W, b, mean, maxDifference)
    return str(prediction)


@app.route("/")
def hello():
    print(W)
    return "Welcome to the house pricing prediction app!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
