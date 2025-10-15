from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Data
reviews = ["amazing great love", "excellent best perfect", "fantastic awesome wonderful",
           "terrible awful bad", "horrible worst hate", "disappointing poor useless"]
labels = [1, 1, 1, 0, 0, 0]  # 1=Positive, 0=Negative

# Train
vec = CountVectorizer()
X = vec.fit_transform(reviews)
model = MultinomialNB().fit(X, labels)

# Test
text = input("Your review: ")
prediction = model.predict(vec.transform([text]))[0]
print("POSITIVE 😊" if prediction == 1 else "NEGATIVE 😞")
