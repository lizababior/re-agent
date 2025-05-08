# HomeMatch - Personalized Real Estate Agent

HomeMatch is a real estate matching system that leverages Large Language Models (LLM) and vector databases to provide personalized property recommendations based on buyer preferences.

## Project Overview

HomeMatch creates a seamless experience for home buyers by:
1. Generating diverse and realistic real estate listings using LLM
2. Converting listings into semantic embeddings stored in a vector database
3. Matching buyer preferences with available properties through semantic search
4. Providing personalized property descriptions tailored to buyer preferences

## Features

### Synthetic Data Generation
- Generates at least 10 diverse real estate listings using LLM
- Each listing includes details like neighborhood, price, size, and detailed descriptions

### Semantic Search Capabilities
- Creates and maintains a vector database of property listings
- Stores semantic embeddings for efficient property matching
- Implements preference-based semantic search functionality

### Augmented Response Generation
- Personalizes property descriptions based on buyer preferences
- Maintains factual integrity while highlighting relevant features
- Uses LLM to generate appealing and tailored descriptions

## Setup and Installation

1. Create a virtual environment:
```bash
uv venv
source .venv/bin/activate
```

2. Install required dependencies:
```bash
uv pip install -r requirements.txt
```

## Usage

1. Run the main application:
```bash
python main.py
```

Or use the Jupyter notebook:
```bash
jupyter notebook HomeMatch.ipynb
```

2. Enter your preferences when prompted. The system will ask questions about:
- Desired house size
- Most important property features
- Preferred amenities
- Transportation requirements
- Neighborhood characteristics

3. Review the personalized property recommendations and descriptions

## Dependencies

- LangChain - For LLM integration
- Vector database (ChromaDB/LanceDB) - For semantic search
- OpenAI GPT or similar LLM
- Other dependencies listed in requirements.txt

## Project Structure

```
├── home_match.py          # Core matching functionality
├── HomeMatch.ipynb       # Jupyter notebook implementation
├── main.py              # Main application entry point
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Future Enhancements

Consider implementing CLIP for multimodal search capabilities:
- Generate embeddings for real estate images
- Enable search using both text and image embeddings
- Match visual property aspects with buyer preferences