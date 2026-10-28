import httpx
import streamlit as st

API_URL = st.secrets.get("API_URL", "http://localhost:8000")
ESTIMATE_ENDPOINT = f"{API_URL}/api/v1/estimate"

def stream_estimation(transcription: str):
    """Llama al endpoint de estimaciones y emite la respuesta como stream."""
    try:
        response = httpx.post(
            ESTIMATE_ENDPOINT,
            json={"transcription": transcription},
            timeout=120,
        )
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 422:
            yield "La transcripción debe tener al menos 50 caracteres."
        else:
            yield f"Error del servidor ({e.response.status_code})."
        return
    except httpx.RequestError as e:
        yield f"No se pudo conectar con {ESTIMATE_ENDPOINT}: {e}"
        return

    yield response.json()["estimation"]


# Inicializar historial en session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Renderizar historial existente
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Aceptar input del usuario
if prompt := st.chat_input("Escribe tu mensaje"):
    # Mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Llamar al endpoint y mostrar la respuesta en el stream
    with st.chat_message("assistant"):
        response = st.write_stream(stream_estimation(prompt))
    st.session_state.messages.append({"role": "assistant", "content": response})
