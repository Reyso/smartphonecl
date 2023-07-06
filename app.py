from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# diretorio do modelo.pkl
with open('/data/modelo.pkl','rb') as file:
    modelo = pickle.load(file)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obter os dados enviados pelo formulário
    battery_power = int(request.form['battery_power'])
    blue = 1 if request.form.get('blue') == 'on' else 0
    clock_speed = float(request.form['clock_speed'])
    dual_sim = 1 if request.form.get('dual_sim') == 'on' else 0
    fc = float(request.form['fc'])
    four_g = 1 if request.form.get('four_g') == 'on' else 0
    int_memory = float(request.form['int_memory'])
    m_dep = float(request.form['m_dep'])
    mobile_wt = float(request.form['mobile_wt'])
    n_cores = int(request.form['n_cores'])
    pc = float(request.form['pc'])
    px_height = int(request.form['px_height'])
    px_width = int(request.form['px_width'])
    ram = int(request.form['ram'])
    sc_h = int(request.form['sc_h'])
    sc_w = int(request.form['sc_w'])
    talk_time = int(request.form['talk_time'])
    three_g = 1 if request.form.get('three_g') == 'on' else 0
    touch_screen = 1 if request.form.get('touch_screen') == 'on' else 0
    wifi = 1 if request.form.get('wifi') == 'on' else 0
       
    # Criando um dataFrame para o modelo
    input_data = {
        "battery_power": [battery_power],
        "blue": [blue],        
        "clock_speed": [clock_speed],
        "dual_sim": [dual_sim],
        "fc": [fc],
        "four_g": [four_g],
        "int_memory": [int_memory],
        "m_dep": [m_dep],
        "mobile_wt": [mobile_wt],
        "n_cores": [n_cores],
        "pc": [pc],
        "px_height": [px_height],
        "px_width": [px_width],
        "ram": [ram],
        "sc_h": [sc_h],
        "sc_w": [sc_w],
        "talk_time": [talk_time],
        "three_g": [three_g],
        "touch_screen": [touch_screen],
        "wifi": [wifi]
        }
    data = pd.DataFrame(input_data)
    prediction = modelo.predict(data)


    # Retornar o resultado da previsão
    #return str(prediction[0])
    return render_template('result.html', prediction=prediction[0])





if __name__ == '__main__':
    app.run(debug=True,threaded=True)
