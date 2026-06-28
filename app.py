import streamlit as st
import time
from main import run_pipeline
from core.rag_engine import ask_question

# App Title & Configuration
st.set_page_config(page_title="AI Video Assistant", page_icon="🤖", layout="wide")
st.title("🤖 AI Video Assistant")
st.caption("Analyze YouTube videos or local audio files and chat with the transcript.")

# Initialize Session State variables to manage terminal flow
if "pipeline_run" not in st.session_state:
    st.session_state.pipeline_run = False
if "result" not in st.session_state:
    st.session_state.result = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for Inputs (Simulating initial terminal questions)
st.sidebar.header("📁 Source Settings")
source_input = st.sidebar.text_input("Enter YouTube URL or local file path:", placeholder="https://...")
language_input = st.sidebar.selectbox("Select Language:", ["english", "hinglish"], index=0)

run_btn = st.sidebar.button("🚀 Start AI Video Assistant", use_container_width=True)

# 1. Pipeline Execution Flow
if run_btn and source_input:
    with st.status("Starting AI Video Assistant...", expanded=True) as status:
        st.write("📥 Processing audio source...")
        
        # Simulating terminal pipeline execution with session state
        try:
            res = run_pipeline(source_input.strip(), language_input)
            st.session_state.result = res
            st.session_state.pipeline_run = True
            status.update(label="Analysis Complete!", state="complete", expanded=False)
        except Exception as e:
            status.update(label="Error processing video", state="error")
            st.error(f"Error: {str(e)}")

# 2. Main Terminal Dashboard (Displaying Results if pipeline ran successfully)
if st.session_state.pipeline_run and st.session_state.result:
    res = st.session_state.result
    
    st.subheader(f"📌 Title: {res['title']}")
    
    # Left column for Summary, Right for extracted entities
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Summary")
        st.write(res['summary'])
        
    with col2:
        st.markdown("### ✅ Action Items")
        if res['action_items'] and "No action items found" not in str(res['action_items']):
            st.write(res['action_items'])
        else:
            st.info("No action items found.")
            
        st.markdown("### 🔑 Key Decisions")
        if res['key_decisions'] and "No key decisions found" not in str(res['key_decisions']):
            st.write(res['key_decisions'])
        else:
            st.info("No key decisions found.")
            
        st.markdown("### ❓ Open Questions")
        if res['open_questions'] and "No open questions found" not in str(res['open_questions']):
            st.write(res['open_questions'])
        else:
            st.info("No open questions found.")

    # 3. Dedicated Interactive Chat Section
    st.subheader("💬 Chat with your meeting")
    st.caption("Ask questions about the video content below (Type 'exit' or click clear to reset)")

    # Render complete conversation history dynamically from session state
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Handle user query inputs properly
    if user_query := st.chat_input("You: Ask something about the video..."):
        
        # Immediate display of user prompt
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.write(user_query)

        # Handle exit condition like terminal
        if user_query.lower() in ["exit", "quit", "q"]:
            st.session_state.messages.append({"role": "assistant", "content": "👋 Goodbye! Please refresh or clear inputs to start over."})
            with st.chat_message("assistant"):
                st.write("👋 Goodbye! Please refresh or clear inputs to start over.")
        
        # Regular RAG Response processing
        else:
            with st.chat_message("assistant"):
                with st.spinner("Assistant is thinking..."):
                    # Check if knowledge is within the transcript or fallback
                    # Note: You can parse the '⚠️ This answer is not available in the video' log logic inside ask_question or display here
                    answer = ask_question(res["rag_chain"], user_query)
                    st.write(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})

else:
    if not st.session_state.pipeline_run:
        st.info("👈 Please enter a valid video source in the sidebar and trigger the pipeline to explore insights.")