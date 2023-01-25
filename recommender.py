

import streamlit as st
import pickle

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

movie_df = pd.read_csv("movies.csv")
movie_keywords = pd.read_csv("keywords.csv")
movie_credits = pd.read_csv("credits.csv")



movie_df = movie_df[['id','original_title','overview','genres']]

movie_df["title"] = movie_df["original_title"].copy()
movie_df.reset_index(inplace=True, drop=True)

movie_df["id"] = movie_df["id"].astype(int)
df = pd.merge(movie_df, movie_keywords, on="id")

df = pd.merge(df, movie_credits, on="id")

df["overview"] = df["overview"].fillna("[]")

df["genres"] = df["genres"].apply(lambda x: [i["name"] for i in eval(x)])
df["genres"] = df["genres"].apply(lambda x: ' '.join([i.replace(" ","") for i in x]))

df["keywords"] = df["keywords"].apply(lambda x: [i["name"] for i in eval(x)])
df["keywords"] = df["keywords"].apply(lambda x: ' '.join([i.replace(" ","") for i in x]))

df["director"] = df["crew"].apply(literal_eval).apply(lambda x: [i["name"] for i in x if i["job"]=="Director"])
df["director"] = df["director"].apply(lambda x: ' '.join([i.replace(" ","") for i in x]))

df.drop("crew", axis=1, inplace=True)

df["cast"] = df["cast"].apply(lambda x: [i["name"][:5] for i in eval(x)])
df["cast"] = df["cast"].apply(lambda x: ' '.join([i.replace(" ","") for i in x]))

df["tags"] = df["overview"] + " " + df["genres"] + " " + df["original_title"] + " " + df["keywords"] + " " + df["cast"] + " " + df["director"] + " " +  df["director"] + " " + df["director"]

df.drop(columns=["overview", "original_title", "keywords", "cast"], axis=1, inplace=True)

df.drop_duplicates(inplace=True)

tfidf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
vectorized_df = tfidf.fit_transform(df["tags"])

cosine_sim = cosine_similarity(vectorized_df)

def recommendation_title(title):
    id_recom = df[df["title"]==title].index[0]
    distances = cosine_sim[id_recom]
    top_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10]
    movie_list = []
    ids = []
    for i in top_list:
        movie_list.append(df.iloc[i[0]].title)
        ids.append(df.iloc[i[0]].id)
    return movie_list

def recommendation_genre(genre):
    id_recom = df[df["genres"]==genre].index[0]
    distances = cosine_sim[id_recom]
    top_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10]
    movie_list = []
    ids = []
    for i in top_list:
        movie_list.append(df.iloc[i[0]].title)
        ids.append(df.iloc[i[0]].id)
    return movie_list

def recommendation_director(director):
    id_recom = df[df["director"]==director].index[0]
    distances = cosine_sim[id_recom]
    top_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10]
    movie_list = []
    ids = []
    for i in top_list:
        movie_list.append(df.iloc[i[0]].title)
        ids.append(df.iloc[i[0]].id)
    return movie_list


pickle.dump(df.to_dict(),open('movies.pkl','wb'))

pickle.dump(cosine_sim,open('similarity.pkl','wb'))

st.title('Movies Recommendation System')
movies=pickle.load(open('./movies.pkl','rb'))
movies=pd.DataFrame(movies)
similarity=pickle.load(open('./similarity.pkl','rb'))

criteria = st.selectbox('Select Criteria for Recommendation', options= ['Title','Genre','Director'],index=0)

if criteria == "Title":
    selected = st.selectbox('Select',df['title'].values)
    if st.button('Recommend'):
        names = recommendation_title(selected)
        st.write(''' ## Top Five Recommended Movies: ''')
        st.text(names[0])
        st.text(names[1])
        st.text(names[2])
        st.text(names[3])
        st.text(names[4])

elif criteria == "Genre":
     selected = st.selectbox('Select',df['genres'].unique())
     if st.button('Recommend'):
        names = recommendation_genre(selected)
        st.write(''' ## Top Five Recommended Movies: ''')
        st.text(names[0])
        st.text(names[1])
        st.text(names[2])
        st.text(names[3])
        st.text(names[4])

else:
     selected = st.selectbox('Select',df['director'].unique())
     if st.button('Recommend'):
        names = recommendation_director(selected)
        st.write(''' ## Top Five Recommended Movies: ''')
        st.text(names[0])
        st.text(names[1])
        st.text(names[2])
        st.text(names[3])
        st.text(names[4])

   



