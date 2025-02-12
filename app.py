import streamlit as st
import pickle 
import pandas as pd
import requests

def fetch_poster(movie_id):
   response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=69440cafb37fcd7ec9c8d1ed1359b133&language=en-US".format(movie_id))
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse = True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from api

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies , recommended_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('D:\B-tech\Machine-Learning\Movies Recommendation System\similarity.pkl','rb'))

st.title ('MOVIE RECOMENDER SYSTEM')
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    names,poster = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.header(names[0])
        st.image(poster[0])

    with col2:
        st.header(names[1])
        st.image(poster[1])

    with col3:
        st.header(names[2])
        st.image(poster[2])

    with col4:
        st.header(names[3])
        st.image(poster[3])

    with col5:
        st.header(names[4])
        st.image(poster[4])

