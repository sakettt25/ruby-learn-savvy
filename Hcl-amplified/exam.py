import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

data_dir = "c215051c-6-Archive 4"
train = pd.read_csv(f"{data_dir}/train.csv")
test = pd.read_csv(f"{data_dir}/test.csv")

train["Reviews"] = train["Reviews"].fillna("")
test["Reviews"] = test["Reviews"].fillna("")

print(f"Train shape: {train.shape}, Test shape: {test.shape}")
print(f"Unique courses: {train['Course'].nunique()}")

def remove_course_name(row):
    review = row["Reviews"]
    course = row["Course"]
    review_clean = review.replace(course, "")
    return review_clean

train["Reviews_clean"] = train.apply(remove_course_name, axis=1)

tfidf_clf = TfidfVectorizer(
    max_features=50000,
    ngram_range=(1, 2),
    stop_words="english",
    sublinear_tf=True,
)

all_reviews_for_clf = pd.concat(
    [train["Reviews_clean"], test["Reviews"]], ignore_index=True
)
tfidf_clf.fit(all_reviews_for_clf)

X_train_clf = tfidf_clf.transform(train["Reviews_clean"])
X_test_clf = tfidf_clf.transform(test["Reviews"])

le = LabelEncoder()
y_train = le.fit_transform(train["Course"])

clf = SGDClassifier(loss="modified_huber", max_iter=200, random_state=42, n_jobs=-1)
clf.fit(X_train_clf, y_train)

test_predictions = clf.predict(X_test_clf)
test_courses = le.inverse_transform(test_predictions)

print(f"\nPredicted course distribution for test:")
pred_series = pd.Series(test_courses)
print(pred_series.value_counts().head(10))

course_to_indices = {}
for course in train["Course"].unique():
    course_mask = train["Course"] == course
    course_to_indices[course] = train[course_mask]["Index"].values

tfidf_sim = TfidfVectorizer(
    max_features=50000,
    ngram_range=(1, 2),
    stop_words="english",
    sublinear_tf=True,
)

all_reviews_for_sim = pd.concat([train["Reviews"], test["Reviews"]], ignore_index=True)
tfidf_sim.fit(all_reviews_for_sim)

train_tfidf_sim = tfidf_sim.transform(train["Reviews"])
test_tfidf_sim = tfidf_sim.transform(test["Reviews"])

results = []

for i in range(len(test)):
    predicted_course = test_courses[i]
    course_mask = (train["Course"] == predicted_course).values
    course_train_indices = np.where(course_mask)[0]  # positional indices in DataFrame
    course_actual_indices = train["Index"].values[course_train_indices]  # actual Index values
    
    test_vec = test_tfidf_sim[i]
    course_vecs = train_tfidf_sim[course_train_indices]
    
    sims = cosine_similarity(test_vec, course_vecs).flatten()
    
    top_10_pos = np.argsort(sims)[::-1][:10]
    top_10_actual = course_actual_indices[top_10_pos].tolist()
    
    results.append(top_10_actual)
    
    if (i + 1) % 2000 == 0:
        print(f"Processed {i+1}/{len(test)} test samples")

print(f"Processed {len(test)}/{len(test)} test samples")

submission = pd.DataFrame({
    "Index": test["Index"].values,
    "Index_list": [str(r) for r in results],
})

submission.to_csv("submission.csv", index=False)

print(f"\nSubmission shape: {submission.shape}")
print(f"First few rows:")
print(submission.head())

correct = 0
for i in range(min(100, len(test))):
    predicted_course = test_courses[i]
    recommended = results[i]
    course_indices_set = set(course_to_indices[predicted_course])
    all_in_course = all(idx in course_indices_set for idx in recommended)
    if all_in_course:
        correct += 1
