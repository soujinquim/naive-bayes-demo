# naive-bayes-demo
Just a simple sentimet classifier demo

# 🤖 Sentiment Classifier

Simple AI that predicts if text is **POSITIVE 😊** or **NEGATIVE 😞**

**Made by:** [Your Name] | **Class:** [Your Class]

---

## How to Use

1. Click the link → **"Copy to Drive"**
2. Click **Play** ▶️
3. Type your review
4. See the result!

---

## How to Make It Smarter

Add more training examples to the `reviews` list:

```python
reviews = [
    "amazing great love",           # Positive
    "excellent best perfect",       # Positive
    "fantastic awesome wonderful",  # Positive
    "terrible awful bad",           # Negative
    "horrible worst hate",          # Negative
    "disappointing poor useless"    # Negative
]
```

**Rule:** Add equal numbers of positive and negative reviews!

Update the `labels` list to match:
```python
labels = [1, 1, 1, 0, 0, 0]  # 1=Positive, 0=Negative
```

---

## Try These Experiments

- Add 10 more reviews and see if accuracy improves
- Test with emojis: "This is great 😊"
- Try mixed reviews: "Good quality but expensive"
- Use longer sentences instead of just keywords


---

**Questions?** Ask [Your Name] in class!
