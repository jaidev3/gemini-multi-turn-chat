# gemini-multi-turn-chat

## Gemini Multi-Turn Chat

This project demonstrates a multi-turn chat session with the Gemini API.

### Prerequisites

- Python 3.x
- Google Generative AI SDK: `pip install google-generativeai`

### Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd gemini-multi-turn-chat
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure API Key:**
    Open `gemini_chat.py` and replace `"AIzaSyBQV........."` with your actual Gemini API key in the following line:
    ```python
    genai.configure(api_key="YOUR_API_KEY")
    ```

### Running the Chat

To start the chat session, run the following command in your terminal:

```bash
python gemini_chat.py
```

The script will then prompt you for the following:

1.  **Temperature:** (Optional) Enter a value between 0.0 and 1.0 (e.g., 0.7). Leave blank to use the default (0.9).
2.  **Your first message:** Enter your initial message to Gemini.
3.  **Your second message:** Enter your follow-up message.

The script will then print Gemini's final response to your second message, taking into account the context of the first message.
