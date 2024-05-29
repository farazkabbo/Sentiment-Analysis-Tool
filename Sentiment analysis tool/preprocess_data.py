from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [w.lower() for w in tokens]
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    words = [word for word in stripped if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(word) for word in words]
    return stemmed

if __name__ == "__main__":
    sample = "Here is a sample tweet from Twitter."
    print(preprocess_text(sample))
