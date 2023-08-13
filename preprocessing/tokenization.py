from hazm import word_tokenize as HazmWordTokenizer

class Tokenizer:
    def __init__(self):
        self.tokenizer = HazmWordTokenizer()

    def tokenize(self, text):
        tokens = self.tokenizer.tokenize(text)
        return tokens

    def process_dataframe(self, df):
        df['data_tokenized'] = df['data_normalized'].apply(lambda x: self.tokenize(x))
        return df