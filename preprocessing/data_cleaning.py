import re

class DataCleaner:
    def __init__(self):
        self.rules = [
            r':\s+:',
            r':#',
            r'#',
            r'\(\w{1}\)',
            r'\.$',
            r'ره',
            r'\[...\]',
            r'\.{2,}',
            r'[\،\؛\,\!\«\»\(\)\'\"\“\”\_]',
            r'\:\w+(_\w+)*\:',
            r'\\U[0-9a-zA-Z]{4,8}',
            r'\w\:',
            r'[a-zA-z]{3,}',
            r'(?<=تأیید|تایید)',
            r'(?=در)',
            r'(?<=\w)\.(?=\s+)',
            r'؟',
            r'(?<=%)'
        ]

        self.extra_rules = [
            r'(?=ها|های)'
        ]

    def clean_text(self, text):
        cleaned_text = text
        for rule in self.rules:
            cleaned_text = re.sub(rule, ' ', cleaned_text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text) 
        return cleaned_text.strip()

    def process_dataframe(self, df):
        df['data_clean'] = df['data_demojized'].replace(self.rules, ' ', regex=True)
        df['data_clean'] = df['data_clean'].replace(self.extra_rules, '\u200c', regex=True)
        df['data_clean'] = df['data_clean'].apply(self.clean_text)
        return df