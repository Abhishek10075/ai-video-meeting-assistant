<img width="1916" height="962" alt="image" src="https://github.com/user-attachments/assets/a64a7441-4040-4737-99ad-a08962403b57" />



# 🤖 AI Video Meeting Assistant

An AI-powered Meeting Assistant that analyzes YouTube videos and local audio files. It transcribes speech, generates meeting summaries, extracts action items, key decisions, and open questions, and provides an intelligent chat interface using Retrieval-Augmented Generation (RAG).

## 🚀 Features

- 🎥 Process YouTube video URLs
- 🎵 Upload and analyze local audio files
- 📝 Speech-to-text transcription using Whisper
- 🌐 Hinglish to English transcription using Sarvam AI
- 📋 Automatic meeting summary generation
- ✅ Extract Action Items
- 🔑 Extract Key Decisions
- ❓ Extract Open Questions
- 💬 Chat with meeting transcripts using RAG
- 🧠 Semantic search with ChromaDB
- 🌐 Streamlit-based interactive web interface

## 🛠️ Tech Stack

- Python
- Streamlit
- Whisper
- Sarvam AI
- LangChain
- Mistral AI
- ChromaDB
- HuggingFace Embeddings
- yt-dlp
- FFmpeg
- PyDub

## 📂 Project Structure

```
AI-Video-Meeting-Assistant/
│── app.py
│── main.py
│── requirements.txt
│── .gitignore
│
├── core/
│   ├── extractor.py
│   ├── rag_engine.py
│   ├── summarizer.py
│   ├── transcriber.py
│   └── vector_store.py
│
├── utils/
│   └── audio_processor.py
```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Abhishek10075/ai-video-meeting-assistant.git
cd ai-video-meeting-assistant
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install FFmpeg

Download FFmpeg and add it to your system PATH.

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_api_key
SARVAM_API_KEY=your_api_key
WHISPER_MODEL=small
```

## ▶️ Run the Application

### Streamlit App

```bash
streamlit run app.py
```

### Command Line

```bash
python main.py
```

## 📌 Workflow

1. Input a YouTube URL or local audio file.
2. Extract audio and split it into chunks.
3. Transcribe speech using Whisper or Sarvam AI.
4. Generate a meeting title and summary.
5. Extract action items, key decisions, and open questions.
6. Store transcript embeddings in ChromaDB.
7. Ask questions about the meeting using RAG.

## 📸 Demo

_Add screenshots or a demo GIF here._

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Abhishek Nishad**

GitHub: https://github.com/Abhishek10075
