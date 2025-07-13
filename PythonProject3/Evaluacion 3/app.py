from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/procesar1', methods=['POST'])
def procesar1():
    # Validación: todos los campos deben estar llenos
    if not all([request.form['nota1'], request.form['nota2'], request.form['nota3'], request.form['asistencia']]):
        return "Todos los campos son obligatorios para el Ejercicio 1", 400

    nota1 = float(request.form['nota1'])
    nota2 = float(request.form['nota2'])
    nota3 = float(request.form['nota3'])
    asistencia = float(request.form['asistencia'])

    promedio = round((nota1 + nota2 + nota3) / 3, 2)
    estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

    return render_template('resultado1.html', promedio=promedio, estado=estado)

@app.route('/procesar2', methods=['POST'])
def procesar2():
    # Validación: todos los campos deben estar llenos
    if not all([request.form['nombre1'], request.form['nombre2'], request.form['nombre3']]):
        return "Todos los campos son obligatorios para el Ejercicio 2", 400

    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    nombre3 = request.form['nombre3']

    nombres = [nombre1, nombre2, nombre3]
    nombre_largo = max(nombres, key=len)
    cantidad_caracteres = len(nombre_largo)

    return render_template('resultado2.html', nombre=nombre_largo, caracteres=cantidad_caracteres)

if __name__ == '__main__':
    app.run(debug=True)
