import nltk
from transformers import pipeline
from rake_nltk import Rake
from nltk.corpus import wordnet

# Download all necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Summarizer
def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Keyword Extractor
def extract_keywords(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases()[:5]  # Return top 5 keywords
    return keywords

# Sentence Tokenizer
def tokenize_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

# Sentence Mapper
def map_sentences_to_keywords(sentences, keywords):
    mapped = []
    for sentence in sentences:
        for keyword in keywords:
            if keyword.lower() in sentence.lower():
                mapped.append((sentence, keyword))
                break
    return mapped

# Distractor Generator
def generate_distractors(word, n=3):
    distractors = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.name().lower() != word.lower():
                distractors.append(lemma.name())
                if len(distractors) == n:
                    return distractors
    if not distractors:
        from random import sample
        all_words = list(set([w for s in wordnet.all_synsets() for w in s.lemma_names()]))
        distractors = sample([w for w in all_words if w.lower() != word.lower()], min(n, len(all_words)))
    return distractors

# Main MCQ Generation Function
def generate_mcqs(text):
    summary = summarize_text(text)
    keywords = extract_keywords(summary)
    sentences = tokenize_sentences(summary)
    mapped = map_sentences_to_keywords(sentences, keywords)
    
    mcqs = []
    for sentence, keyword in mapped:
        distractors = generate_distractors(keyword)
        if distractors:
            mcqs.append({
                'question': sentence.replace(keyword, "________"),
                'answer': keyword,
                'distractors': distractors
            })
    return mcqs

# Function to display MCQs
def display_mcqs(mcqs):
    if not mcqs:
        print("No MCQs were generated. This might be due to difficulties in finding suitable distractors.")
        return
    
    for i, mcq in enumerate(mcqs, 1):
        print(f"\nQuestion {i}:")
        print(mcq['question'])
        options = [mcq['answer']] + mcq['distractors']
        for j, option in enumerate(options):
            print(f"{chr(65 + j)}. {option}")
        print(f"Answer: {mcq['answer']}")

# Interactive input and output (for testing purposes)
if __name__ == "__main__":
    def run_interactive():
        print("MCQ Generator")
        print("Enter your text below (type 'END' on a new line when finished):")
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        
        text = '\n'.join(lines)
        
        if text:
            print("\nGenerating MCQs...\n")
            mcqs = generate_mcqs(text)
            display_mcqs(mcqs)
        else:
            print("No text entered. Please run the function again and enter some text.")
    
    run_interactive()
