from flask import Flask, render_template
import time
import sys
import importlib.util

#Pruebas
spec = importlib.util.spec_from_file_location("archivo", "./rfid.MFRC522-python.Read.py")
archivo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(archivo)



#variable para pruebas flask
lectura = 0

app = Flask('LOLE APP')

"""@app.route('/')
def herramienta():
        if lectura == 1:
            return 'Herramienta en su sitio'
        else:
            return 'Devuelve la herramienta en 8 horas'

@app.route('/tiempo')
def tiempo():
        if lectura == 0:
            for i in range(8, -1, -1):
                time.sleep(1)
                if i > 0:
                    return 'El tiempo restante es: ' + str(i) + ' horas'
                else:
                    return 'Herramienta robada'"""

@app.route('/')
def herramienta():
    return render_template('index.html')