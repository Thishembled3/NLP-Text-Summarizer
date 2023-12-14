import argparse
from summarizer.abstractive import AbstractiveSummarizer
from summarizer.extractive import ExtractiveSummarizer
import os

def main():
    parser = argparse.ArgumentParser(description="NLP Text Summarizer")
    parser.add_argument("--text_file", type=str, help="Path to the input text file")
    parser.add_argument("--text_input", type=str, help="Direct text input for summarization")
    parser.add_argument("--summary_type", type=str, choices=["abstractive", "extractive"], default="abstractive",
                        help="Type of summarization to perform (abstractive or extractive)")
    parser.add_argument("--max_length", type=int, default=150, help="Maximum length for abstractive summary")
    parser.add_argument("--num_sentences", type=int, default=3, help="Number of sentences for extractive summary")
    parser.add_argument("--model_name", type=str, default="facebook/bart-large-cnn",
                        help="Model name for abstractive summarization (Hugging Face model ID)")

    args = parser.parse_args()

    input_text = ""
    if args.text_file:
        if not os.path.exists(args.text_file):
            print(f"Error: Text file not found at {args.text_file}")
            return
        with open(args.text_file, "r", encoding="utf-8") as f:
            input_text = f.read()
    elif args.text_input:
        input_text = args.text_input
    else:
        print("Error: Please provide either --text_file or --text_input.")
        return

    if not input_text.strip():
        print("Error: Input text is empty.")
        return

    print(f"\n--- Performing {args.summary_type.capitalize()} Summarization ---")

    if args.summary_type == "abstractive":
        summarizer = AbstractiveSummarizer(model_name=args.model_name)
        summary = summarizer.summarize(input_text, max_length=args.max_length)
    else: # extractive
        summarizer = ExtractiveSummarizer()
        summary = summarizer.summarize(input_text, num_sentences=args.num_sentences)

    print("\nOriginal Text (first 200 chars):\n", input_text[:200], "...")
    print("\nGenerated Summary:\n", summary)
    print("----------------------------------------")

if __name__ == "__main__":
    # Create a dummy text file for testing if it doesn't exist
    dummy_text_path = "sample_article.txt"
    if not os.path.exists(dummy_text_path):
        with open(dummy_text_path, "w", encoding="utf-8") as f:
            f.write("""
            Artificial intelligence (AI) is intelligence demonstrated by machines, unlike the natural intelligence
            displayed by humans and animals. Leading AI textbooks define the field as the study of 
// Update on 2023-05-31 00:00:00 - 86
// Update on 2023-12-14 00:00:00 - 151
