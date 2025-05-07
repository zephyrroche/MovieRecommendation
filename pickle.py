import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=889aa0c639b0c516375df633d9cd8b02&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  movie_list = sorted(list(enumerate(similarity[0])), reverse = True,key = lambda x:x[1])[1:6]

  recommend_movies = []
  recommended_movies_posters = []

  for i in movie_list:
    movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from API
    recommended_movies.append(movies.iloc[i[0]].title)
    recommended_movies_posters.append(fetch_poster(movie_id))
  return recommended_movies,recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommendation System')

selected_movie_name = st.selectbox("Enter the name of a movie", movies['title'].values)



option = st.selectbox(
'Enter movie name?',
    movies['title'].values)

if st.button('Recommend'):
    names,posters= recommend(option)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])


    with col5:
        st.text(names[4])
        st.image(posters[4])