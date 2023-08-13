import emoji

class Demojizer:
    def __init__(self):
        self.emojis_to_replace = {
            '💨': ' ',
            '😌': ' ',
            '▪️': ' '
        }

    def replace_emojis(self, text):
        for emoji, replacement in self.emojis_to_replace.items():
            text = text.replace(emoji, replacement)
        return text

    def demojize_text(self, text):
        return emoji.demojize(text)

    def process_dataframe(self, df):
        df['data'] = df['data'].apply(self.replace_emojis)
        df['data_demojized'] = df['data'].apply(self.demojize_text)
        return df