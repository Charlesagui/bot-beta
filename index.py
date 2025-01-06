import streamlit as st
import requests
import json

# Configuración de la API de Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"

def stream_ollama_response(prompt: str):
    """
    Transmite la respuesta de Ollama en tiempo real usando llama2:7b
    """
    try:
        # Primero verificamos si el servidor está activo
        try:
            requests.get("http://localhost:11434/api/version")
        except requests.exceptions.ConnectionError:
            st.error("⚠️ No se puede conectar al servidor de Ollama. Por favor verifica que:")
            st.error("1. Ollama está instalado")
            st.error("2. El servidor está corriendo (ejecuta 'ollama serve' en la terminal)")
            st.error("3. El modelo llama2:7b está descargado (ejecuta 'ollama pull llama2:7b')")
            return False

        # Contenedor para la respuesta streaming
        response_container = st.empty()
        current_response = ""

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama2:7b",
                "prompt": prompt,
                "stream": True
            },
            stream=True
        )
        response.raise_for_status()

        for line in response.iter_lines():
            if line:
                try:
                    json_response = json.loads(line)
                    if 'response' in json_response:
                        current_response += json_response['response']
                        # Actualiza la respuesta en tiempo real
                        response_container.markdown(current_response + "▌")
                except json.JSONDecodeError:
                    continue

        # Muestra la respuesta final sin el cursor
        response_container.markdown(current_response)
        return True

    except Exception as e:
        st.error(f"Error: {str(e)}")
        return False

def main():
    st.set_page_config(
        page_title="Chat Bot con llama2:7b",
        page_icon="🤖",
    )
    
    st.title("🤖 Chat Bot con llama2:7b")
    
    # Instrucciones de uso
    with st.expander("ℹ️ Instrucciones de uso", expanded=True):
        st.markdown("""
        1. Asegúrate de que Ollama está instalado y corriendo:
           - Ejecuta `ollama serve` en una terminal
           - Si no tienes el modelo, ejecuta `ollama pull llama2:7b`
        2. Escribe tu pregunta en el campo de texto
        3. Presiona Enter o haz clic en Enviar
        """)
    
    # Entrada del usuario
    prompt = st.text_input(
        "Escribe tu pregunta aquí:",
        key="user_input",
        placeholder="Escribe tu pregunta y presiona Enter..."
    )
    
    # Procesar input cuando se presiona Enter o el botón
    if prompt:
        stream_ollama_response(prompt)
    
    # Footer informativo
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: gray; font-size: 0.8em;'>
        Usando llama2:7b en Ollama | Servidor local en localhost:11434
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()