from hazm import Lemmatizer as HazmLemmatizer

class Lemmatizer:
    def __init__(self):
        self.lemmatizer = HazmLemmatizer()

    def lemmatize(self, token):
        lemmatized_token = self.lemmatizer.lemmatize(token)
        return lemmatized_token

    def process_dataframe(self, df):
        df['data_lemmatized'] = df['data_no_stopwords'].apply(lambda tokens: [self.lemmatize(token) for token in tokens])
        return df