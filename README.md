Ollama Streamlit Chat Bot 🤖
Una interfaz gráfica simple y efectiva para interactuar con modelos de lenguaje de Ollama usando Streamlit. Esta aplicación permite mantener conversaciones con el modelo LLaMA 2 a través de una interfaz web amigable.
🚀 Características

Interfaz web intuitiva con Streamlit
Respuestas en tiempo real (streaming)
Integración con Ollama API
Soporte para el modelo LLaMA 2 (7B)
Manejo de errores robusto
Interfaz responsiva y amigable

📋 Prerequisitos

Python 3.8 o superior
Ollama instalado en tu sistema
Modelo LLaMA 2 (7B) descargado en Ollama

🔧 Instalación

Clona el repositorio
Instala las dependencias desde requirements.txt
Asegúrate de tener Ollama iniciado y el modelo LLaMA 2 descargado

💻 Uso

Inicia el servidor de Ollama
Ejecuta la aplicación Streamlit
Abre tu navegador en http://localhost:8501

📁 Estructura del Proyecto
Copyollama-streamlit-bot/
├── app.py              # Aplicación principal
├── requirements.txt    # Dependencias del proyecto
└── README.md          # Este archivo
📝 Requirements.txt
Copystreamlit>=1.24.0
requests>=2.31.0
🤝 Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir qué te gustaría cambiar.
⚠️ Solución de Problemas
Si encuentras el error "404 Client Error: Not Found", verifica:

Que Ollama está corriendo
Que el modelo está instalado
Que el servidor está accesible en localhost:11434

📄 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE.md para más detalles.
👤 charly aguiar


GitHub: Charlesagui


⭐️ Muestra tu Apoyo
Si este proyecto te ha sido útil, considera darle una estrella en GitHub.
📝 Notas

Esta aplicación está diseñada para uso local y educativo
El rendimiento dependerá de tu hardware
Se recomienda tener al menos 16GB de RAM para un funcionamiento óptimo