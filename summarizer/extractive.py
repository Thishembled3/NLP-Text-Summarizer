from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import string

class ExtractiveSummarizer:
    """
    A class for performing extractive text summarization.
    """
    def __init__(self):
        self.stop_words = set(stopwords.words('english') + list(string.punctuation))
        print("Extractive Summarizer initialized.")

    def _calculate_sentence_scores(self, sentences, word_frequencies):
        """
        Calculates a score for each sentence based on word frequencies.
        """
        sentence_scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in word_frequencies:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_frequencies[word]
                    else:
                        sentence_scores[sentence] += word_frequencies[word]
        return sentence_scores

    def summarize(self, text, num_sentences=3):
        """
        Generates an extractive summary of the input text.

        Args:
            text (str): The input text to summarize.
            num_sentences (int): The number of sentences to include in the summary.

        Returns:
            str: The extractive summary.
        """
        print("Generating extractive summary...")
        sentences = sent_tokenize(text)
        words = word_tokenize(text.lower())
        words = [word for word in words if word not in self.stop_words]

        word_frequencies = Counter(words)
        sentence_scores = self._calculate_sentence_scores(sentences, word_frequencies)

        # Sort sentences by score and pick the top ones
        sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
        summary_sentences = [sentence for sentence, score in sorted_sentences[:num_sentences]]

        return " ".join(summary_sentences)


if __name__ == "__main__":
    sample_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, unlike the natural intelligence
    displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents":
    any device that perceives its environment and takes actions that maximize its chance of successfully
    achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines
    that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem-solving".
    The field was founded as an academic discipline in 1956, and in the years since has experienced several
    waves of optimism, followed by disappointment and the loss of funding (known as an "AI winter"),
    followed by new approaches, success, and renewed funding. For most of its history, AI research has been
    conducted in laboratories and universities, but in recent years, it has become a major topic of commercial interest.
    """

    summarizer = ExtractiveSummarizer()
    extractive_summary = summarizer.summarize(sample_text, num_sentences=2)
    print("\nOriginal Text:\n", sample_text)
    print("\nExtractive Summary:\n", extractive_summary)
