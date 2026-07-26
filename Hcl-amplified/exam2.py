import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# ==========================
# Load Data
# ==========================

data_dir = "c215051c-6-Archive 4"

train = pd.read_csv(f"{data_dir}/train.csv")
test = pd.read_csv(f"{data_dir}/test.csv")

train["Reviews"] = train["Reviews"].fillna("")
test["Reviews"] = test["Reviews"].fillna("")
train["Course"] = train["Course"].fillna("")

# ==========================
# Text Cleaning
# ==========================

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"www\S+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"[^a-z0-9 ]", " ", text)
    text = " ".join(text.split())
    return text

train["Reviews"] = train["Reviews"].apply(clean_text)
test["Reviews"] = test["Reviews"].apply(clean_text)
train["Course"] = train["Course"].apply(clean_text)

# ==========================
# Combined Text
# ==========================

train["combined"] = train["Reviews"] + " " + train["Course"] + " " + train["Course"]
test["combined"] = test["Reviews"]

# ==========================
# TF-IDF
# ==========================

word_vectorizer = TfidfVectorizer(
    lowercase=True,
    strip_accents="unicode",
    stop_words="english",
    analyzer="word",
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.95,
    sublinear_tf=True,
    norm="l2"
)

char_vectorizer = TfidfVectorizer(
    analyzer="char_wb",
    ngram_range=(3, 5),
    min_df=2,
    sublinear_tf=True,
    norm="l2"
)

word_vectorizer.fit(train["combined"])
char_vectorizer.fit(train["combined"])

train_word = word_vectorizer.transform(train["combined"])
test_word = word_vectorizer.transform(test["combined"])

train_char = char_vectorizer.transform(train["combined"])
test_char = char_vectorizer.transform(test["combined"])

print("Word TF-IDF:", train_word.shape)
print("Char TF-IDF:", train_char.shape)

batch_size = 1000
TOP_K = 100

results = []
train_indices = train["Index"].values

# ==========================
# Retrieval
# ==========================

for start in range(0, test_word.shape[0], batch_size):
    end = min(start + batch_size, test_word.shape[0])

    print(f"Processing {start} -> {end}")

    word_sim = linear_kernel(test_word[start:end], train_word).astype(np.float32)
    char_sim = linear_kernel(test_char[start:end], train_char).astype(np.float32)

    sim = 0.60 * word_sim + 0.40 * char_sim

    top_candidates = np.argpartition(sim, -TOP_K, axis=1)[:, -TOP_K:]

    for row in range(sim.shape[0]):
        candidate_idx = top_candidates[row]
        candidate_scores = sim[row][candidate_idx]

        ranked_idx = candidate_idx[np.argsort(-candidate_scores)]

        final = []
        seen = set()

        for idx in ranked_idx:
            actual = int(train_indices[idx])
            if actual not in seen:
                final.append(actual)
                seen.add(actual)
            if len(final) == 10:
                break

        if len(final) < 10:
            for idx in np.argsort(-sim[row]):
                actual = int(train_indices[idx])
                if actual not in seen:
                    final.append(actual)
                    seen.add(actual)
                if len(final) == 10:
                    break

        results.append(final)

# ==========================
# Submission
# ==========================

submission = pd.DataFrame({
    "Index": test["Index"].astype(int),
    "Index_list": ["[" + ", ".join(map(str, x)) + "]" for x in results]
})

submission.to_csv("submission.csv", index=False)

print(submission.head())
print("Saved submission.csv successfully.")
