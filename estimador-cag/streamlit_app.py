import httpx
import streamlit as st

API_URL = st.secrets.get("API_URL", "http://localhost:8000")
ESTIMATE_STREAM_ENDPOINT = f"{API_URL}/api/v1/estimate/stream"

def stream_estimation(transcription: str):
    """Llama al endpoint de estimaciones y emite la respuesta como stream."""
    try:
        with httpx.stream(
            "POST",
            ESTIMATE_STREAM_ENDPOINT,
            json={"transcription": transcription},
            timeout=120,
        ) as response:
            response.raise_for_status()
            yield from response.iter_text()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 422:
            yield "La transcripción debe tener al menos 50 caracteres."
        else:
            yield f"Error del servidor ({e.response.status_code})."
    except httpx.RequestError as e:
        yield f"No se pudo conectar con {ESTIMATE_STREAM_ENDPOINT}: {e}"


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
