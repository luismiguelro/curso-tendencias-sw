from os import abort

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Hola, Mundo desde flask"

# Mostrar variables
@app.route("/saludar")
def saludar():
    nombre = "pedro"
    edad = '58'
    return f'saludos: {nombre}, tu edad es: {edad}'

# Retornar nombre
@app.route('/mostrar/<nombre>',methods=['GET','POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html',nombre_llave=nombre)

#pagina error
@app.route('/salir')
def salir():
    return  abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return  render_template('error404.html',llaveerror=error),404

# sign up
@app.route("/signup",methods=['GET','POST'])
def show_signup_form():
    if request.method == 'POST':
        name = request.form['name']
        first_name = request.form.get("name")
        email = request.form['email']
        password = request.form['password']
        next = request.args.get('next',None)
        if next:
            return redirect(next),{first_name},name
        return redirect(url_for('respuestaform'))
    return  render_template("signup_form.html")
