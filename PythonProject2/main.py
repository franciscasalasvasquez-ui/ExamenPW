from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def calculoDescuento():
    if request.method == 'POST':
        resultado = ''
        desc = ''
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        cantidadTarros = int(request.form['cantidad'])
        total = cantidadTarros * 9000
        if 18 <= edad <= 30:
            resultado = total * 0.85
            desc = total - resultado
        elif edad > 30:
            resultado = total * 0.75
            desc = total - resultado
        else:
            resultado = total
            desc = 0
        return render_template('ejercicio1.html', nombre=nombre, resultado=resultado, desc=desc, total=total)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ingresoUsuario():
    if request.method == 'POST':
        mensaje = ''
        usuario = str(request.form['usuario'])
        contrasena = str(request.form['contraseña'])
        if usuario == 'juan' and contrasena == 'admin':
            mensaje = 'ADMINISTRADOR'
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = 'USUARIO'
        else:
            mensaje = 'INVALIDO'
        return render_template('ejercicio2.html',mensaje=mensaje)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run()