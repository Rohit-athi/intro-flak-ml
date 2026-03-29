from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

model = pickle.load(open("model1.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict')
def predict():
    data = request.args
    size = int(data.get("size", 0))
    age = int(data.get("age", 0))
    predicts = model.predict([[age, size]])
    return render_template("index.html", val=predicts[0])

if __name__ == "__main__":
    app.run(debug=True)