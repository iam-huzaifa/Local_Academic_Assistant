
import streamlit as st

from model import get_response, MODEL, SYSTEM_PROMPT


# Page configuration
st.set_page_config(
    page_title="Personal Academic Assistant",
    page_icon="🎓",
    layout="centered"
)


# Initialize conversation history
if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]


# Sidebar
with st.sidebar:

    st.title("Developer Information")

    st.write("Name: Muhammad Huzaifa ")
    st.write("Roll No: 03-134232-070")

    st.divider()

    st.subheader("Model Information")
    st.write(f"Model: {MODEL}")
    st.write("Runtime: Ollama (Local)")

    st.divider()

    # Clear conversation
    if st.button("Clear Conversation", use_container_width=True):

        st.session_state.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        st.rerun()


# Main interface
st.title("🎓 Personal Academic Assistant")

st.caption("Your local AI assistant for university learning.")

st.write(f"Currently running: **{MODEL}**")


# Display previous conversation
for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Accept user input
user_input = st.chat_input("Ask your academic assistant...")


if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate model response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                answer = get_response(
                    st.session_state.messages
                )

                st.markdown(answer)

                # Save assistant response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:

                st.error(f"Error: {e}")
