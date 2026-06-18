import pickle
from pathlib  import Path
import pandas as pd
from flask import Flask, request, render_template

application = Flask(__name__)
app = application
ROOT_DIR=Path(__file__).resolve().parent.parent
SRC_DIR=ROOT_DIR/'models'
with open(SRC_DIR / 'ridge.pkl', 'rb') as f:
    ridge_model = pickle.load(f)
with open(SRC_DIR / 'scaler.pkl', 'rb') as f:
    standard_scaler = pickle.load(f)
@app.route("/")
def index():
    '''Render the application's landing page.

    This function handles the root URL route ('/').
    When the user opens the main website URL, Flask calls this function
    and displays the index.html template.

    Returns:
        str: Rendered index.html page.'''
    return render_template('index.html')
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    '''
    Handle Forest Fire Weather Index prediction requests.

    This function supports both GET and POST requests.

    For a GET request:
        - Displays the prediction input form using home.html.

    For a POST request:
        - Reads user input values from the HTML form.
        - Converts the input values into float format.
        - Creates a pandas DataFrame with the same feature names used during model training.
        - Scales the input data using the saved StandardScaler.
        - Predicts the FWI value using the saved Ridge Regression model.
        - Rounds the prediction result to two decimal places.
        - Sends the prediction result back to home.html.

    Returns:
        str: Rendered home.html page with either the prediction form or prediction result.

    Raises:
        Exception: Catches and prints any error that occurs during input processing,
                   scaling, or prediction.'''
    if request.method == "POST":
        try:
            temperature_val = float(request.form.get("Temperature"))
            rh = float(request.form.get("RH"))
            ws = float(request.form.get("Ws"))
            rain = float(request.form.get("Rain"))
            ffmc = float(request.form.get("FFMC"))
            dmc = float(request.form.get("DMC"))
            isi = float(request.form.get("ISI"))
            classes = float(request.form.get("Classes"))
            region = float(request.form.get("Region"))

            input_data = pd.DataFrame([[temperature_val, rh, ws, rain, ffmc, dmc, isi, classes, region]],
                                      columns=["Temperature", "RH", "Ws", "Rain", "FFMC", "DMC", "ISI", "Classes", "Region"])
            scaled_data = standard_scaler.transform(input_data)
            prediction = ridge_model.predict(scaled_data)
            if hasattr(prediction, "__len__"):
                final = round(float(prediction[0]), 2)
            else:
                final = round(float(prediction), 2)
            return render_template('home.html', result=final)
        except Exception as e:
            import traceback
            traceback.print_exc()
            return render_template('home.html', error="Something went wrong. Please check input values.")
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)