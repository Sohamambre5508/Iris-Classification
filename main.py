from flask import Flask,request
import pickle
from sklearn.datasets import load_iris

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/Predict", methods = ["POST","GET"])
def predict():
    if request.method == "POST":
        data = request.json
        print(data)
        with open ('model.pkl','rb') as f:
            clf = pickle.load(f)

        test = [[data['sepal_length'],data['sepal_width'],data['petal_length'],['petal_width']]]
        output = clf.predict(test)
        class_flower = iris['target_names'][output]
        print(class_flower)


        return {'class':class_flower,'success':'True'}

app.run(debug = True)

