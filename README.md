# NLP-Text-Summarizer

A Python-based NLP project for abstractive and extractive text summarization using state-of-the-art models and techniques.

## Features
- **Abstractive Summarization**: Generates new sentences to summarize text using transformer models.
- **Extractive Summarization**: Identifies and extracts key sentences from the original text.
- **Multiple Models**: Supports various pre-trained models (e.g., BART, T5 for abstractive; TextRank, LexRank for extractive).
- **Evaluation Metrics**: Includes ROUGE score calculation for summarization quality assessment.

## Getting Started

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```python
from summarizer.abstractive import AbstractiveSummarizer
from summarizer.extractive import ExtractiveSummarizer

text = """Your long input text here..."""

# Abstractive Summarization
abstractive_summarizer = AbstractiveSummarizer(model_name="facebook/bart-large-cnn")
summary_abstractive = abstractive_summarizer.summarize(text, max_length=150)
print("Abstractive Summary:", summary_abstractive)

# Extractive Summarization
extractive_summarizer = ExtractiveSummarizer()
summary_extractive = extractive_summarizer.summarize(text, num_sentences=3)
print("Extractive Summary:", summary_extractive)
```

## Contributing

We welcome contributions! Please see `CONTRIBUTING.md` for details.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
