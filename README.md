# AI Chat API with Ollama

A simple Flask web API that provides chat functionality using Ollama's LLaMA 3.1 model.

## Features

- RESTful API endpoint for chat interactions
- Integration with Ollama's LLaMA 3.1:8b model
- Error handling and JSON responses
- Direct script usage example

## Requirements

- Python 3.7+
- Flask
- ollama-python
- Ollama installed and running locally

## Installation

1. **Install Ollama** (if not already installed):
   - Download and install Ollama from [https://ollama.ai](https://ollama.ai)
   - Pull the LLaMA model: `ollama pull llama3.1:8b`

2. **Install Python dependencies**:
   ```bash
   pip install flask ollama
   ```

3. **Clone or download this project**

## Usage

### Running the API Server

Start the Flask server:

```bash
python api.py
```

The API will be available at `http://localhost:5000`

### API Endpoint

#### GET /chat

Send a chat message to the AI model.

**Parameters:**
- `prompt` (required): The message/question to send to the AI

**Example Request:**
```bash
curl "http://localhost:5000/chat?prompt=Hello, how are you?"
```

**Example Response:**
```json
{
  "response": "Hello! I'm doing well, thank you for asking. How can I help you today?"
}
```

**Error Response:**
```json
{
  "error": "Prompt não fornecido"
}
```

### Direct Script Usage

You can also use the chat functionality directly by running:

```bash
python script.py
```

This will execute a predefined prompt about Isaac Asimov's "I, Robot" and display the AI's response.

## Project Structure

```
├── api.py          # Flask web API server
├── script.py       # Direct usage example
└── README.md       # This file
```

## API Details

- **Server**: Flask development server
- **Port**: 5000
- **Debug Mode**: Enabled
- **Model**: llama3.1:8b
- **Method**: GET requests only

## Error Handling

The API includes basic error handling for:
- Missing prompt parameter
- General exceptions during chat processing

## Dependencies

- `flask`: Web framework for the API
- `ollama`: Python client for Ollama

## Notes

- Make sure Ollama is running before starting the API
- The LLaMA 3.1:8b model needs to be pulled locally
- The API runs in debug mode for development purposes

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under standard terms. 
