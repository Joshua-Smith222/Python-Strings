# task 1

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
keywords = ["good", "bad", "excellent", "poor", "average"]

def highlight_keywords(reviews, keywords):
    highlighted_reviews = []
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        highlighted_reviews.append(review)
    return highlighted_reviews
highlighted_reviews = highlight_keywords(reviews, keywords)
for review in highlighted_reviews:
    print(review)

#task 2
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(reviews, positive_words, negative_words):
    for review in reviews:
        positive_count = 0
        negative_count = 0
        words = review.lower().split()

        for word in words:
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1
        print(f"Review: {review}")
        print(f"Positive Words: {positive_count}, Negative Words: {negative_count}")

sentiment_tally(reviews, positive_words, negative_words)

#task 3
def review_summary(review, max_length=30):
    if len(review) > max_length:
        summary = review[:max_length]
        last_space_index = summary.rfind(" ")
        if last_space_index != -1:
            summary = summary[:last_space_index]
        summary += "..."
    else:
        summary = review
    return summary
for review in reviews:
    print(f"Original Review: {review}")
    print(f"Summary of Review: {review_summary(review)}\n")
