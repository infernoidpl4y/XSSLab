from flask import Flask, request, render_template_string

app = Flask(__name__)

publicaciones = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        usuario = request.form.get('usuario', 'Anónimo')
        titulo = request.form.get('titulo', 'Sin título')
        descripcion = request.form.get('descripcion', '')
        xss_code = request.form.get('xss', '')

        if xss_code.strip() == "!inject":
            xss_code = """
            <style>
                .xss-visual {
                    animation: glitch 1s infinite;
                    color: #ff0000;
                    text-shadow: 2px 2px #000000;
                }
                @keyframes glitch {
                    0% { text-shadow: 2px 2px #ff0000; }
                    25% { text-shadow: -2px -2px #ff0000; }
                    50% { text-shadow: 2px -2px #ff0000; }
                    75% { text-shadow: -2px 2px #ff0000; }
                }
            </style>
            <script>
                document.addEventListener('DOMContentLoaded', () => {
                    const glitchText = document.createElement('div');
                    glitchText.className = 'xss-visual';
                    glitchText.style.position = 'fixed';
                    glitchText.style.top = '10px';
                    glitchText.style.left = '10px';
                    glitchText.style.fontSize = '2rem';
                    glitchText.style.zIndex = '9999';
                    glitchText.textContent = 'XSS ACTIVADO';
                    document.body.appendChild(glitchText);
                });
            </script>
            """

        publicaciones.append({
            'usuario': usuario,
            'titulo': titulo,
            'descripcion': descripcion,
            'xss': xss_code
        })

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>XSS Lab - Laboratorio de Seguridad</title>
            <style>
                :root {
                    --primary: #ff0000;
                    --dark: #0a0a0a;
                    --light: #e0e0ff;
                    --background: #121212;
                    --card-bg: #1a1a1a;
                    --accent: #ff4444;
                }

                body {
                    background-color: var(--background);
                    color: var(--light);
                    font-family: 'Courier New', monospace;
                    margin: 0;
                    padding: 0;
                    min-height: 100vh;
                    display: flex;
                    flex-direction: column;
                    overflow-x: hidden;
                }

                .navbar {
                    background-color: var(--primary);
                    overflow: hidden;
                    margin-bottom: 20px;
                    position: relative;
                    z-index: 10;
                }

                .navbar a {
                    float: left;
                    color: #000;
                    text-align: center;
                    padding: 14px 16px;
                    text-decoration: none;
                    font-weight: bold;
                    transition: all 0.3s ease;
                }

                .navbar a:hover {
                    background-color: #000;
                    color: var(--primary);
                }

                .modal {
                    display: none;
                    position: fixed;
                    z-index: 1000;
                    left: 0;
                    top: 0;
                    width: 100%;
                    height: 100%;
                    background-color: rgba(0,0,0,0.85);
                }

                .modal-content {
                    background-color: var(--card-bg);
                    margin: 15% auto;
                    padding: 25px;
                    border: 2px solid var(--primary);
                    width: 80%;
                    max-width: 600px;
                    border-radius: 10px;
                    position: relative;
                    box-shadow: 0 0 20px var(--primary);
                }

                .close {
                    color: var(--primary);
                    float: right;
                    font-size: 28px;
                    font-weight: bold;
                    cursor: pointer;
                    position: absolute;
                    right: 15px;
                    top: 10px;
                }

                .close:hover {
                    color: #fff;
                    transform: scale(1.2);
                }

                .info-box {
                    background: var(--card-bg);
                    border-left: 5px solid var(--primary);
                    padding: 20px;
                    margin: 0 auto 30px;
                    max-width: 900px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px var(--primary);
                    animation: pulse 2s infinite;
                }

                @keyframes pulse {
                    0%, 100% { box-shadow: 0 0 10px var(--primary); }
                    50% { box-shadow: 0 0 20px var(--primary); }
                }

                form {
                    max-width: 700px;
                    margin: 0 auto 30px;
                    padding: 25px;
                    background: var(--card-bg);
                    border-radius: 10px;
                    box-shadow: 0 0 15px var(--primary);
                }

                input, textarea {
                    width: 100%;
                    margin-bottom: 15px;
                    padding: 10px;
                    border: 2px solid var(--primary);
                    border-radius: 5px;
                    background: #222;
                    color: var(--light);
                    font-family: inherit;
                }

                input:focus, textarea:focus {
                    outline: none;
                    border-color: var(--accent);
                    box-shadow: 0 0 5px var(--accent), 0 0 10px var(--primary);
                }

                button {
                    background-color: var(--primary);
                    color: #000;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold;
                    font-size: 1rem;
                    transition: all 0.3s ease;
                    position: relative;
                    overflow: hidden;
                }

                button::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: -100%;
                    width: 100%;
                    height: 100%;
                    background: var(--accent);
                    transition: all 0.5s ease;
                    z-index: -1;
                }

                button:hover::before {
                    left: 100%;
                }

                .container {
                    max-width: 900px;
                    margin: 0 auto;
                    padding: 0 15px;
                }

                .post {
                    margin-bottom: 25px;
                    padding: 20px;
                    background: var(--card-bg);
                    border-left: 4px solid var(--primary);
                    border-radius: 8px;
                    box-shadow: 0 0 10px var(--primary);
                    transition: transform 0.3s ease;
                    position: relative;
                    overflow: hidden;
                }

                .post:hover {
                    transform: translateY(-5px);
                    box-shadow: 0 0 15px var(--primary), 0 0 5px var(--accent);
                }

                .post::after {
                    content: 'XSS';
                    position: absolute;
                    top: 5px;
                    right: 5px;
                    color: var(--primary);
                    font-size: 0.8rem;
                    opacity: 0.3;
                }

                .xss-warning {
                    color: var(--primary);
                    font-style: italic;
                    margin-top: 5px;
                    display: block;
                    font-size: 0.9rem;
                }

                .post-list {
                    margin-bottom: 30px;
                }

                .logo {
                    font-size: 2.5rem;
                    color: var(--primary);
                    margin: 20px 0;
                    text-align: center;
                    text-shadow: 2px 2px #000;
                    animation: glitch 1s infinite;
                }

                @keyframes glitch {
                    0% { text-shadow: 2px 2px var(--primary); }
                    25% { text-shadow: -2px -2px var(--primary); }
                    50% { text-shadow: 2px -2px var(--primary); }
                    75% { text-shadow: -2px 2px var(--primary); }
                }

                .footer {
                    margin-top: 40px;
                    padding: 20px;
                    text-align: center;
                    color: #666;
                    font-size: 0.9rem;
                }

                .particle {
                    position: absolute;
                    width: 5px;
                    height: 5px;
                    background: var(--primary);
                    border-radius: 50%;
                    animation: float 10s infinite linear;
                    pointer-events: none;
                    z-index: 0;
                }

                @keyframes float {
                    0% { transform: translateY(0); opacity: 0.3; }
                    50% { opacity: 0.8; }
                    100% { transform: translateY(-100vh); opacity: 0.3; }
                }

                .xss-example {
                    display: block;
                    color: var(--primary);
                    cursor: pointer;
                    margin-top: -10px;
                    margin-bottom: 15px;
                    text-align: center;
                    font-weight: bold;
                    animation: glow 2s infinite alternate;
                }

                @keyframes glow {
                    from { color: var(--primary); }
                    to { color: #ff9999; }
                }

                .code-display {
                    background: #111;
                    padding: 10px;
                    border-radius: 5px;
                    font-family: monospace;
                    font-size: 0.9rem;
                    overflow-x: auto;
                    border: 1px solid var(--primary);
                    margin-top: 10px;
                }

                .post-count {
                    color: var(--primary);
                    font-weight: bold;
                    margin-top: 10px;
                    text-align: center;
                    font-size: 1.1rem;
                }

                .hack-animation {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    pointer-events: none;
                    background: repeating-linear-gradient(
                        45deg,
                        transparent,
                        transparent 10px,
                        var(--primary) 10px,
                        var(--primary) 20px
                    );
                    opacity: 0.05;
                    z-index: -1;
                }

                .xss-payload {
                    background: #222;
                    padding: 10px;
                    border-radius: 5px;
                    margin-top: 5px;
                    font-family: monospace;
                    font-size: 0.9rem;
                }

                .xss-label {
                    color: var(--primary);
                    font-size: 0.8rem;
                    margin-top: -15px;
                    margin-bottom: 10px;
                    display: block;
                }

                @media (max-width: 600px) {
                    .navbar a {
                        font-size: 14px;
                        padding: 10px 12px;
                    }

                    .logo {
                        font-size: 2rem;
                    }
                }
            </style>
        </head>
        <body>
            <div class="hack-animation"></div>
            <!-- Generar partículas -->
            <script>
                document.addEventListener('DOMContentLoaded', () => {
                    const body = document.body;
                    for (let i = 0; i < 30; i++) {
                        const particle = document.createElement('div');
                        particle.className = 'particle';
                        particle.style.left = `${Math.random() * 100}%`;
                        particle.style.top = `${Math.random() * 100}%`;
                        particle.style.width = particle.style.height = `${Math.random() * 5 + 2}px`;
                        particle.style.animationDuration = `${Math.random() * 5 + 5}s`;
                        body.appendChild(particle);
                    }
                });
            </script>

            <!-- Navbar -->
            <div class="navbar">
                <a href="/">Inicio</a>
                <a href="#" onclick="document.getElementById('infoModal').style.display='block'">Información</a>
                <a href="https://github.com/infernoidpl4y/XSSLab/"  target="_blank">GitHub</a>
                <a href="https://cybersecurityproject.freeforums.net/">Foro</a>
            </div>

            <!-- Modal de Información -->
            <div id="infoModal" class="modal">
                <div class="modal-content">
                    <span class="close">&times;</span>
                    <h2 style="color: var(--primary);">🛡️ Información del Creador</h2>
                    <p><strong>Nombre:</strong> InfernoidPl4y</p>
                    <p><strong>Portfolio:</strong> <a href="https://infernoidpl4y.netlify.app/"  style="color: var(--primary); text-decoration: underline;">infernoidpl4y.netlify.app</a></p>
                    <p><strong>Contacto:</strong> infernoidpl4y@gmail.com</p>
                    <p><strong>Propósito:</strong> Esta es una aplicación para aprender y practicar en comunidad la vulnerabilidad XSS. Quizás todo no sea destruir.</p>
                    <p><strong>Advertencia:</strong> No ingresar información sensible. Los datos se reiniciarán cada 48 horas.</p>
                </div>
            </div>

            <!-- Banner -->
            <div class="container">
                <h1 class="logo">XSS Lab Interactive</h1>

                <!-- Información principal -->
                <div class="info-box">
                    <h2>🚨 Laboratorio de Vulnerabilidades XSS</h2>
                    <p>Bienvenido al laboratorio de pruebas de seguridad web. Aquí puedes experimentar con vulnerabilidades de Cross-Site Scripting (XSS) en un entorno controlado.</p>
                    <p><strong>Importante:</strong> Este sitio se reinicia automáticamente cada 48 horas. Todos los datos serán eliminados periódicamente.</p>
                    <p><strong>Modo de uso:</strong> Ingresa un usuario, título y descripción, y prueba distintos payloads en el campo XSS.</p>
                </div>

                <!-- Formulario -->
                <h2 style="text-align: center; color: var(--primary); margin-bottom: 20px;">Crear nueva publicación</h2>
                <form method="POST">
                    <input type="text" name="usuario" placeholder="Tu usuario" required>
                    <input type="text" name="titulo" placeholder="Título de la publicación" required>
                    <textarea name="descripcion" placeholder="Descripción" rows="4"></textarea>

                    <label for="xss" class="xss-label">Código XSS (campo vulnerable)</label>
                    <input type="text" name="xss" placeholder="Ejemplo: <script>alert('xss')</script>" id="xss">
                    <div class="xss-warning">💡 Escribe "!inject" para ver un ejemplo de inyección</div>

                    <button type="submit" style="width: 100%; display: block;">Publicar</button>
                </form>

                <!-- Ejemplo de XSS -->
                <p class="xss-example" onclick="document.getElementById('xss').value='<script>alert(`XSS BÁSICO`)</script>';">
                    EJEMPLO: <span class="xss-payload">&lt;script&gt;alert('XSS BÁSICO')&lt;/script&gt;</span>
                </p>

                <!-- Lista de publicaciones -->
                <div class="post-list">
                    <h2 style="text-align: center; color: var(--primary); margin-bottom: 20px;">Publicaciones recientes:</h2>
                    {% if publicaciones %}
                        {% for pub in publicaciones %}
                            <div class="post">
                                <h3>{{ pub.titulo }}</h3>
                                <p><strong>Autor:</strong> {{ pub.usuario }}</p>
                                <p>{{ pub.descripcion }}</p>
                                <div>{{ pub.xss|safe }}</div>
                            </div>
                        {% endfor %}
                    {% else %}
                        <div style="text-align: center; color: #888; padding: 20px; background: #111; border-radius: 8px; margin: 20px 0;">
                            📝 No hay publicaciones aún. ¡Sé el primero en probar una inyección XSS!
                        </div>
                    {% endif %}
                </div>

                <!-- Contador -->
                <p class="post-count">📊 Publicaciones actuales: {{ publicaciones|length }}</p>

                <!-- Footer -->
                <div class="footer">
                    <p>Desarrollado por <strong>InfernoidPl4y</strong> | Laboratorio de Seguridad Web</p>
                    <p style="font-size: 0.8rem;">⚠️ Este entorno es para aprendizaje y debe usarse bajo tu propia responsabilidad</p>
                </div>
            </div>

            <!-- Scripts -->
            <script>
                // Manejar cierre de modal
                document.querySelector('.close').onclick = function() {
                    document.getElementById('infoModal').style.display = 'none';
                }

                window.onclick = function(event) {
                    if (event.target == document.getElementById('infoModal')) {
                        document.getElementById('infoModal').style.display = 'none';
                    }
                }

                // Animación de advertencia para campo XSS
                document.getElementById('xss').addEventListener('input', function() {
                    const value = this.value;
                    if (value.includes('<script>') || value.includes('javascript:')) {
                        this.style.borderColor = 'var(--primary)';
                        this.style.boxShadow = '0 0 5px var(--primary)';
                    } else {
                        this.style.borderColor = 'var(--primary)';
                        this.style.boxShadow = 'none';
                    }
                });
            </script>
        </body>
        </html>
    ''', publicaciones=publicaciones)

if __name__ == '__main__':
    app.run(debug=True)
