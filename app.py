from flask import Flask, request, render_template_string

app = Flask(__name__)

# Base de datos falsa para almacenar publicaciones
publicaciones = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener datos del formulario
        usuario = request.form.get('usuario', 'Anónimo')
        titulo = request.form.get('titulo', 'Sin título')
        descripcion = request.form.get('descripcion', '')
        xss_code = request.form.get('xss', '')  # Campo vulnerable a XSS

        # Inyección predefinida (atajo: !inject)
        if xss_code.strip() == "!inject":
            xss_code = """
            <style>
                .post {
                    background: #f0f0f0;
                    border: 1px solid #ddd;
                    padding: 15px;
                    margin-bottom: 15px;
                }
                .post h3 { color: #ff5722; }
            </style>
            <script>alert('XSS inyectado con éxito!')</script>
            """

        # Guardar en la "base de datos"
        publicaciones.append({
            'usuario': usuario,
            'titulo': titulo,
            'descripcion': descripcion,
            'xss': xss_code  # ¡Campo sin sanitizar!
        })

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>XSS Lab - Foro de Seguridad</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 1000px;
                    margin: 0 auto;
                    padding: 20px;
                    line-height: 1.6;
                }
                .menu {
                    background-color: #333;
                    overflow: hidden;
                    margin-bottom: 20px;
                    border-radius: 5px;
                }
                .menu a {
                    float: left;
                    color: white;
                    text-align: center;
                    padding: 14px 16px;
                    text-decoration: none;
                    font-size: 17px;
                }
                .menu a:hover {
                    background-color: #ddd;
                    color: black;
                }
                .info-box {
                    background-color: #f8f9fa;
                    border-left: 5px solid #ff9800;
                    padding: 15px;
                    margin-bottom: 20px;
                }
                form {
                    margin-bottom: 20px;
                    padding: 20px;
                    background: #f5f5f5;
                    border-radius: 5px;
                }
                input, textarea {
                    width: 100%;
                    margin-bottom: 10px;
                    padding: 8px;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                }
                button {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 15px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                .post {
                    margin-bottom: 20px;
                    padding: 15px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    background: white;
                }
                .modal {
                    display: none;
                    position: fixed;
                    z-index: 1;
                    left: 0;
                    top: 0;
                    width: 100%;
                    height: 100%;
                    background-color: rgba(0,0,0,0.4);
                }
                .modal-content {
                    background-color: #fefefe;
                    margin: 15% auto;
                    padding: 20px;
                    border: 1px solid #888;
                    width: 80%;
                    max-width: 600px;
                    border-radius: 5px;
                }
                .close {
                    color: #aaa;
                    float: right;
                    font-size: 28px;
                    font-weight: bold;
                }
                .close:hover {
                    color: black;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <!-- Menú superior -->
            <div class="menu">
                <a href="/">Inicio</a>
                <a href="#" onclick="document.getElementById('infoModal').style.display='block'">Información</a>
                <a href="https://github.com/infernoidpl4y/XSSLab/" target="_blank">GitHub</a>
                <a href="https://cybersecurityproject.freeforums.net/">Foro</a>
            </div>

            <!-- Modal de Información -->
            <div id="infoModal" class="modal">
                <div class="modal-content">
                    <span class="close" onclick="document.getElementById('infoModal').style.display='none'">&times;</span>
                    <h2>Información del Creador</h2>
                    <p><strong>Nombre:</strong> InfernoidPl4y</p>
                    <p><strong>Contacto:</strong> infernoidpl4y@gmail.com</p>
                    <p><strong>Propósito:</strong> Esta es una aplicación para aprender y practicar en comunidad la vulnerabilidad XSS. Quizas todo no sea destruir.</p>
                    <p><strong>Advertencia:</strong> No ingresar información sensible. Los datos se reiniciarán cada 48 horas.</p>
                </div>
            </div>

            <!-- Información principal -->
            <div class="info-box">
                <h1>Laboratorio XSS - Foro de Seguridad</h1>
                <p>Bienvenido a nuestro laboratorio de pruebas XSS. Aquí puedes experimentar con vulnerabilidades de Cross-Site Scripting en un entorno controlado.</p>
                <p><strong>Importante:</strong> Este sitio se reinicia automáticamente cada 48 horas. Todos los datos serán eliminados periódicamente.</p>
            </div>

            <!-- Formulario -->
            <h2>Crear nueva publicación</h2>
            <form method="POST">
                <input type="text" name="usuario" placeholder="Tu usuario" required>
                <input type="text" name="titulo" placeholder="Título de la publicación" required>
                <textarea name="descripcion" placeholder="Descripción" rows="4"></textarea>
                <input type="text" name="xss" placeholder="Código XSS (campo vulnerable)">
                <button type="submit">Publicar</button>
            </form>

            <!-- Lista de publicaciones -->
            <h2>Publicaciones recientes:</h2>
            {% for pub in publicaciones %}
                <div class="post">
                    <h3>{{ pub.titulo }}</h3>
                    <p><strong>Autor:</strong> {{ pub.usuario }}</p>
                    <p>{{ pub.descripcion }}</p>
                    <div>{{ pub.xss|safe }}</div>  <!-- ¡Solo este campo es vulnerable! -->
                </div>
            {% endfor %}

            <script>
                document.querySelector('.close').onclick = function() {
                    document.getElementById('infoModal').style.display = 'none';
                }

                window.onclick = function(event) {
                    if (event.target == document.getElementById('infoModal')) {
                        document.getElementById('infoModal').style.display = 'none';
                    }
                }
            </script>
        </body>
        </html>
    ''', publicaciones=publicaciones)

if __name__ == '__main__':
    app.run(debug=True)
