from flask import Flask, render_template, request
from predict import model_predict
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        date_of_birth = request.form['date_of_birth']
        cycle = int(request.form['cycle'])
        weight_gain = bool(request.form['weight_gain'])
        hair_growth = bool(request.form['hair_growth'])
        skin_darkening = bool(request.form['skin_darkening'])
        fast_food = bool(request.form['fast_food'])
        follicle_no_l = int(request.form['follicle_no_l'])
        follicle_no_r = int(request.form['follicle_no_r'])

        processed_data = model_predict(cycle, weight_gain, hair_growth, skin_darkening, fast_food, follicle_no_l, follicle_no_r)
        return render_template('result.html', name=name, processed_data=processed_data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
