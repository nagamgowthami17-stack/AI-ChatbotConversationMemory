
import streamlit as st
from llm import generate_response
from memory import (
    initialize_memory,
    save_memory,
    retrieve_memories,
    delete_all_memories,
    update_memory
)

st.set_page_config(page_title="AI Memory Chatbot", page_icon="🤖")

st.title("🤖 AI Memory Chatbot")
st.caption("AI assistant with short-term and long-term memory")

initialize_memory()

USER_ID = "user_1"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Retrieve long-term memory
    memories = retrieve_memories(USER_ID)

    memory_context = "\n".join(
        information for memory_id, information in memories
    )

    system_message = {
        "role": "system",
        "content": (
            "You are a helpful AI assistant. Use these saved memories "
            "when relevant. Do not invent personal information.\n"
            f"Saved memories:\n{memory_context}"
        )
    }

    # Short-term memory: latest 10 messages
    short_term_memory = st.session_state.messages[-10:]

    history = [system_message] + short_term_memory[:-1]

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = generate_response(user_input, history)
                st.write(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

                if user_input.lower().startswith("remember:"):
                   information = user_input.split(":", 1)[1].strip()

                   if information:
                         save_memory(USER_ID, information)

            except Exception as e:
                st.error(f"Error: {e}")

# Memory management sidebar
st.sidebar.title("🧠 Memory Management")

if st.sidebar.button("View Saved Memories"):
    saved_memories = retrieve_memories(USER_ID)

    if saved_memories:
        for memory_id, information in saved_memories:
            st.sidebar.write(f"ID: {memory_id} - {information}")
    else:
        st.sidebar.info("No memories saved.")

st.sidebar.subheader("Update Memory")

memory_id = st.sidebar.number_input(
    "Enter Memory ID",
    min_value=1,
    step=1
)

new_information = st.sidebar.text_input("Updated Information")

if st.sidebar.button("Update Memory"):
    if new_information:
        update_memory(memory_id, new_information)
        st.sidebar.success("Memory updated!")
    else:
        st.sidebar.warning("Enter new information.")

if st.sidebar.button("Delete All Memories"):
    delete_all_memories(USER_ID)
    st.sidebar.success("All memories deleted!")
