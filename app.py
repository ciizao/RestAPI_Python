from flask import Flask, send_file  # Importamos send_file para devolver archivos específicos

app = Flask(__name__)  # Inicializamos la aplicación Flask

# Ruta para la API que sirve el archivo HTML
@app.route('/api/hello', methods=['GET'])  # Ruta que responde al método GET
def hello_world():
    # Usamos send_file para devolver el archivo HTML directamente desde la raíz
    return send_file('helloRestAPI.html')

if __name__ == '__main__':
    # Ejecutamos el servidor Flask en modo depuración, escuchando en el puerto 1000
    app.run(debug=True, port=1000)



    