from transformers import pipeline

class AbstractiveSummarizer:
    """
    A class for performing abstractive text summarization using pre-trained models.
    """
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.summarizer = pipeline("summarization", model=model_name)
        print(f"Abstractive Summarizer initialized with model: {model_name}")

    def summarize(self, text, max_length=150, min_length=30):
        """
        Generates an abstractive summary of the input text.

        Args:
            text (str): The input text to summarize.
            max_length (int): The maximum length of the generated summary.
            min_length (int): The minimum length of the generated summary.

        Returns:
            str: The abstractive summary.
        """
        print("Generating abstractive summary...")
        summary = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]["summary_text"]


if __name__ == "__main__":
    sample_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, unlike the natural intelligence
    displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents":
    any device that perceives its environment and takes actions that maximize its chance of successfully
    achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines
    that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem-solving".
    """

    summarizer = AbstractiveSummarizer()
    abstractive_summary = summarizer.summarize(sample_text)
    print("\nOriginal Text:\n", sample_text)
    print("\nAbstractive Summary:\n", abstractive_summary)
