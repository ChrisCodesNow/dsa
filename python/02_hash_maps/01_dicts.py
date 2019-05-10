import urllib.request
import random
from collections import defaultdict, OrderedDict
import re

def get_data(url):
    response = urllib.request.urlopen(url)
    binary_data = response.read()
    text = binary_data.decode(encoding='utf-8', errors='ignore')

    return text


def get_reviews(text):
    reviews = {}
    
    distinct_reviews = text.split("\n")

    for review in distinct_reviews:
        review_components = review.split("\t")
        score = review_components[0]
        url = review_components[1]
        title = review_components[2]
        body = review_components[3]

        reviews[url] = {'score': score, 'url': url, 'title': title, 'body': body}

    if validate_data(distinct_reviews, reviews):
        print('Data in get reviews is valid')

    return reviews


# Validate distinct input data sets are each saved in 
# a dictionary
def validate_data(input_data, created_dict):
    return len(input_data) == len(created_dict)


# Get urls of low scores
def get_low_scores(reviews):
    low_scores_urls = []

    for url, review in reviews.items():
        if float(review['score']) == 1.0:
            low_scores_urls.append(url)

    return low_scores_urls


# Create subset dict with the given array of keys
def subset_dict(input_dict, keys):
    subset = {}
    for key in keys:
        subset[key] = input_dict[key]

    if validate_data(keys, subset):
        print("Data in subset dicts is valid")

    return subset


# Dict with scores as keys, rather than urls as keys
def group_by_score(reviews):
    reviews_by_score = defaultdict(list)
    for url, review in reviews.items():
        score = review['score']
        review_dict = {'url': url, 'title': review['title'], 'body': review['body']}
        reviews_by_score[score].append(review_dict)
        
    return reviews_by_score


# Sentiment analysis: 
# Frequency of words associated with low scores
def word_sentiment_analysis(low_scores_reviews):
    word_frequency = defaultdict(int)
    for url in low_scores_reviews:
        review = reviews[url]['body']
        text = re.sub('<.*?>', '', review)              # remove HTML tags
        words = text.strip().lower().split()    # List of words in review
        for word in words:
            word_frequency[word] += 1

    return word_frequency
    

def sort_data(low_score_words):
    sorted_pairs = sorted(low_score_words.items(), key=lambda tup: tup[1], reverse=True)
    ordered_dict = OrderedDict(sorted_pairs)

    # ignore top 10%, mostly stop words
    top_ten = len(ordered_dict.keys()) // 10

    # first 100 from top 90%
    return list(ordered_dict.items())[top_ten: top_ten + 100]


if __name__ == "__main__":
    print("Reading data")

    url = "https://gist.githubusercontent.com/twielfaert/a0972bf366d9aaf6cb1206c16bf93731/raw/dde46ad1fa41f442971726f34ad03aaac85f5414/Donna-Tartt-The-Goldfinch.csv"

    text = get_data(url)
    reviews = get_reviews(text)
    low_scores_urls = get_low_scores(reviews)
    low_score_reviews = subset_dict(reviews, low_scores_urls)
    reviews_by_score = group_by_score(reviews)
    low_score_words = word_sentiment_analysis(low_score_reviews)
    top_low_scores = sort_data(low_score_words)

    print(top_low_scores)