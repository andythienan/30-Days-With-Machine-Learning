# Import neccessary libraries
import nltk
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
from nltk.corpus import stopwords
import random

# Download the NLTK data files
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')

# Preprocess the movie reviews data
def extract_features(words):
    return {word: True for word in words}

# Load the movie reviews data from NLTK
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle the documents to randomize the order of the reviews
random.shuffle(documents)

# Preprocess the dataset for training and testing
featuresets = [(extract_features(d), c) for (d, c) in documents]
train_set, test_set = featuresets[:1600], featuresets[1600:]

# Train a Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Evaluate the classifier on the test set
acccuracy = nltk_accuracy(classifier, test_set)
print(f'Accuracy: {acccuracy * 100:.2f}%')

# Show the most informative features of the classifier
classifier.show_most_informative_features(10)

# Test on new input sentences
def analyze_sentiment(text):
    # Tokenize and remove stopwords
    words = nltk.word_tokenize(text)
    words = [word for word in words if word.lower() not in stopwords.words('english')]
    
    # Predict sentiment
    features = extract_features(words)
    return classifier.classify(features)

# Test the sentiment analysis function
test_sentences = [
    "This movie is absolutely fantastic! The acting, the story, everything was amazing!",
    "I hated this movie. It was a waste of time and money.",
    "The plot was a bit dull, but the performances were great.",
    "I have mixed feelings about this film. It was okay, not great but not terrible either."
]

for sentence in test_sentences:
    print(f"Sentence: {sentence}")
    print(f"Predicted sentiment: {analyze_sentiment(sentence)}")
    print()

