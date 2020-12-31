from flask import Flask
import time

#variable para pruebas flask
lectura = 0

app = Flask('LOLE APP')

@app.route('/')
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
                    return 'Herramienta robada'