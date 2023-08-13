import numpy as np
import pandas as pd
from transformers import AutoTokenizer, TFBertModel
import tensorflow as tf

class EmbeddingGenerator:
    def __init__(self, model_name, max_length, batch_size):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.bert_model = TFBertModel.from_pretrained(model_name)
        self.max_length = max_length
        self.batch_size = batch_size

    def generate_embeddings(self, df):
        num_samples = len(df)
        num_batches = int(np.ceil(num_samples / self.batch_size))
        embeddings_list = []

        for i in range(num_batches):
            start_index = i * self.batch_size
            end_index = min((i + 1) * self.batch_size, num_samples)
            batch = df['data_normalized'][start_index:end_index]

            tokenized_tensors = self.tokenizer.batch_encode_plus(
                batch.tolist(),
                add_special_tokens=True,
                truncation=True,
                padding='max_length',
                max_length=self.max_length,
                return_tensors='tf'
            )['input_ids']

            outputs = self.bert_model(tokenized_tensors)
            embeddings = outputs.last_hidden_state.numpy()
            embeddings_list.append(embeddings)

        embeddings = np.concatenate(embeddings_list, axis=0)
        return embeddings