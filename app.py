import os
from flask import Flask, render_template, request
import numpy as np
import joblib
import pandas as pd

# Fixed path
fullpath = r"hdp_model.pkl"


app = Flask(__name__)
model = joblib.load(fullpath)


@app.route(
    "/",
)
def hello():
    return render_template("index.html")


@app.route("/detail", methods=["POST"])
def submit():
    # Html to py
    if request.method == "POST":
        name = request.form["Username"]

    return render_template("detail.html", n=name)


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            # Collect and convert form inputs
            age = int(request.form["age"])
            sex = int(request.form["sex"])
            cp = int(request.form["cp"])
            trestbps = int(request.form["trestbps"])
            chol = int(request.form["chol"])
            fbs = int(request.form["fbs"])
            restecg = int(request.form["restecg"])
            thalach = int(request.form["thalach"])
            exang = int(request.form["exang"])
            oldpeak = float(request.form["oldpeak"])
            slope = int(request.form["slope"])
            ca = int(request.form["ca"])
            thal = int(request.form["thal"])

            # Prepare data for model prediction
            import pandas as pd

            columns = [
                "age",
                "sex",
                "cp",
                "trestbps",
                "chol",
                "fbs",
                "restecg",
                "thalach",
                "exang",
                "oldpeak",
                "slope",
                "ca",
                "thal",
            ]
            values = pd.DataFrame(
                [
                    [
                        age,
                        sex,
                        cp,
                        trestbps,
                        chol,
                        fbs,
                        restecg,
                        thalach,
                        exang,
                        oldpeak,
                        slope,
                        ca,
                        thal,
                    ]
                ],
                columns=columns,
            )

            # Predict
            prediction = model.predict(values)[0]  # get first item from array
            result = (
                "Positive (Heart Disease Detected)"
                if prediction == 1
                else "Negative (No Heart Disease)"
            )

            return render_template("predict.html", prediction=result)

        except Exception as e:
            return f"An error occurred during prediction: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
