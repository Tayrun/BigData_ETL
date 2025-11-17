from flask import Flask, render_template

# Inicializa la aplicación Flask
app = Flask(__name__)

@app.route('/')
def inicio():
    """
    Ruta principal que carga la página del dashboard.
    """
    # Flask buscará automáticamente 'index.html' en la carpeta 'templates'
    return render_template('index.html')

# Inicia el servidor cuando se ejecuta el script
if __name__ == '__main__':
    app.run(debug=True)