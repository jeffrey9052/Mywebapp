from flask import Flask, render_template

my_app = Flask(__name__)


@app.route('/')
def home():
    return render_template('inicio.html')


@app.route('/Servicios')
def servicio():
    return render_template('servicio.html')


@app.route('/Servicios/Websites')
def websites():
    return render_template('website.html')


@app.route('/Servicios/Redes')
def redes():
    return render_template('redes.html')


@app.route('/Servicios/CCTV')
def cctv():
    return render_template('cctv.html')


@app.route('/Servicios/Mantenimiento')
def mantenimiento():
    return render_template('mantenimiento.html')


@app.route('/Servicios/Productos')
def productos():
    return render_template('mantenimiento.html')


@app.route('/Acerca')
def about():
    return render_template('acerca.html')


@app.route('/Contacto')
def contacto():
    return render_template('contacto.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)