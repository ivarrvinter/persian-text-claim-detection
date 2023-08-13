from hazm import Normalizer as HazmNormalizer

class Normalizer:
    def __init__(self):
        self.normalizer = HazmNormalizer()

    def normalize(self, text):
        normalized_text = self.normalizer.normalize(text)
        return normalized_text

    def process_dataframe(self, df):
        df['data_normalized'] = df['data_clean'].apply(self.normalize)
        return df