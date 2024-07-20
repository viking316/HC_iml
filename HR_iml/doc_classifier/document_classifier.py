
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
import sys

# Read training data
x = []
y = []

with open('trainingdata.txt') as f:
    n_cases = int(f.readline().strip())
    for line in f:
        temp = line.split()
        y.append(int(temp[0]))
        x.append(" ".join(temp[1:]))

# Create and train the pipeline
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

pipeline.fit(x, y)

# Read input from stdin (HackerRank style)
input_data = sys.stdin.read().strip().split('\n')

# The first line of input data contains the number of documents
n = int(input_data[0].strip())

# The following lines contain the documents to classify
x_new = input_data[1:n+1]

# Predict categories for new documents
results = pipeline.predict(x_new)

# Output the predictions
for result in results:
    print(result)
