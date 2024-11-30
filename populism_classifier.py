import re

import pandas as pd
from nltk.corpus import stopwords

from brazilian_populist_dictionary import brazilian_dictionary

df = pd.read_excel("base_principal_com_transcricoes.xlsx")


def remove_stopwords(text, languages=["spanish", "english", "portuguese"]):
    stop_words = set()
    for lang in languages:
        stop_words.update(stopwords.words(lang))
    text = re.sub(r"[^\w\s]", "", text.lower())
    filtered_words = [word for word in text.split() if word not in stop_words]
    return " ".join(filtered_words)


is_left = [
    "pco",
    "pstu",
    "pco",
    "up",
    "pt",
    "pcb",
    "rede",
    "pcdob",
    "psb",
    "pv",
    "pdt",
    "psol",
]


def left_classifier(df, left):
    df["Party"] = df["Party"].str.lower()
    df["is_left"] = df["Party"].apply(lambda party: 1 if party in left else 0)

    return df


def calculate_populism_level(data, terms):
    data["transcricao"] = data["transcricao"].astype(str)
    data["transcricao"] = data["transcricao"].apply(remove_stopwords)

    data["populist_count"] = 0
    data["word_count"] = data["transcricao"].apply(lambda x: len(x.split()))
    data = data[data["word_count"] >= 1000]
    data["said_populist_word"] = ""
    for index, row in data.iterrows():
        words = row["transcricao"].split()
        populist_words = [word for word in words if word in terms]
        populist_count = len(populist_words)
        data.at[index, "populist_count"] = populist_count
        data.at[index, "said_populist_word"] = ", ".join(populist_words)

    data["populist_level"] = data["populist_count"] / data["word_count"].replace(0, 1)
    data["populist_level"] = data["populist_level"] * 100
    data["populist_level"].fillna(0)
    return data


final_data = calculate_populism_level(df, brazilian_dictionary)
final_data = left_classifier(final_data, is_left)
# final_data.to_excel("final_data.xlsx", index=False)
