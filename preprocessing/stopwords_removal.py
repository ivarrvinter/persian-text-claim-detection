from collections import Counter

class StopwordsRemover:
    def __init__(self, stopwords_list):
        self.stopwords = set(stopwords_list)

    def remove_stopwords(self, tokens):
        filtered_tokens = [token for token in tokens if token not in self.stopwords]
        return filtered_tokens

    def process_dataframe(self, df):
        df['data_no_stopwords'] = df['data_tokenized'].apply(self.remove_stopwords)
        return df