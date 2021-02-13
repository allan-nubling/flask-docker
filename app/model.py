from joblib import load
import pandas as pd


def categorie_prediction(data: list):
    logreg = load('./models/cat_class_logreg.joblib')
    tfidf_vect = load('./models/cat_class_tfidf_vect.joblib')
    categories_df = pd.read_pickle('./models/cat_class_df.pkl')
    x_tfidf = tfidf_vect.transform(data).toarray()
    y_log = logreg.predict(x_tfidf)
    y_log_list = y_log.tolist()
    print(y_log_list)
    i = 0
    result = []
    while (i < len(data)):
        result.append({
            'text': data[i],
            'categorie': categories_df.loc[y_log_list[i], ][0]
        })
        i = i + 1
    return result
