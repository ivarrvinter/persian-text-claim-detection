from data_loader import DataHandler
from preprocessing.demojizing import Demojizer
from preprocessing.data_cleaning import DataCleaner
from preprocessing.normalization import Normalizer
from preprocessing.tokenization import Tokenizer
from preprocessing.stopwords_removal import StopwordsRemover
from preprocessing.lemmatization import Lemmatizer
from embeddings.embedding import EmbeddingGenerator
from model.neural_network import NeuralNetworkTrainer
from sklearn.model_selection import train_test_split

def main():
    data = DataHandler('dataset/2.train_data_text.csv')
    df = data.read_dataset()

    demojizer = Demojizer()
    df = demojizer.process_dataframe(df)

    data_cleaner = DataCleaner()

    df = data_cleaner.process_dataframe(df)

    normalizer = Normalizer()
    df = normalizer.process_dataframe(df)

    tokenizer = Tokenizer()
    df = tokenizer.process_dataframe(df)

    stopwords = [
        "از", "به", "که", "در", "با", "این", "برای", "را", "هم", "تا", "آن", "یا", "است", "یک", "نیز", "اما",
        "هر", "بود", "باشد", "ما", "شما", "او", "آنها", "تو", "من", "اگر", "بی", "اون", "رو", "بودم", "نه", "باشه",
        "شده", "اونا", "هست", "هستم", "خود", "خودش", "خودم", "ای", "منم", "توی", "چه", "چرا", "کی", "چی", "همین",
        "حتی", "الان", "حالا", "تونسته", "همه", "همون", "کل", "قبل", "هرکسی", "هرچیزی", "همچنین", "همچون", "آیا",
        "اکنون", "باید", "بعد", "پس", "پیش", "توسط", "تمام", "تر", "ترین", "جز", "حتما", "خیلی", "دیگر", "راه",
        "زیاد", "سعی", "شد", "شماها", "کاملا", "کامل", "مثل", "مثلا", "می", "همچین", "واقعا", "ولی", "یکی", "یعنی",
        "یه", "یکم", "چون", "بعضی", "هموطن", "وی", "شو", "دو", "کرد", "کردم", "کرده", "کردن", "کردند", "کردی",
        "کردید", "کرده‌اند", "کردم‌", "کنم", "کنی", "کنند", "کنید", "کند", "کنیم", "کندم", "کنیم", "کنونی", "کنونی‌",
        "کردم ", "کردم‌ ", "کردیم‌ ", "کرده‌ ", "کرده‌اند ", "کرده‌ام ", "کرده‌ای ", "کرده‌ایم ", "کرده‌اند‌ ",
        "کنم‌ ", "کنیم‌ ", "کنیم‌‌ ", "کنید‌ ", "کنید‌‌ ", "کنند‌ ", "کرد‌ ", "کرد‌‌ ", "کردم‌‌ ", "کرده‌‌ ",
        "کرده‌‌‌‌ ", "کرده‌ام‌‌ ", "کرده‌ای‌‌‌ ", "کرده‌ایم‌ ", "کرده‌اند‌‌ ", "کنم‌‌ ", "کنی‌‌ ", "کنند‌‌ ",
        "کنید‌‌ ", "کنید‌‌‌‌ ", "کنیم‌‌‌‌ ", "کنونی‌‌ ", "کنو"
    ]
    stopwords_remover = StopwordsRemover(stopwords)
    df = stopwords_remover.process_dataframe(df)

    lemmatizer = Lemmatizer()
    df = lemmatizer.process_dataframe(df)

    model_name = 'HooshvareLab/bert-base-parsbert-uncased'
    max_length = 68
    batch_size = 16

    embedding_generator = EmbeddingGenerator(model_name, max_length, batch_size)
    embeddings = embedding_generator.generate_embeddings(df)

    nn_trainer = NeuralNetworkTrainer()
    nn_trainer.build_model()

    X = ...
    y = ...

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    nn_trainer.train_model(X_train, y_train, epochs=10, batch_size=64)

    nn_trainer.evaluate_model(X_test, y_test)

if __name__ == '__main__':
    main()