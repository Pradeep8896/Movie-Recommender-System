from ctypes import cast
from urllib import response
import streamlit as st
import pickle
import pandas as pd
import requests
import ast

movies=pickle.load(open('movies.pkl','rb'))
st.title("Movie Recommender System")
#Importany Files
movies_list=movies['title'].values
similarity=pickle.load(open('similarity.pkl','rb'))
info=pickle.load(open('info.pkl','rb'))



#Movie name selectbox selector
selected_movie_name = st.selectbox('Movie Name',movies_list)


#Function for fetching recommended movie poster
def fetch_poster(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=57662ceb02223d144755d61d447e148b&language=en-US')
    data=response.json
    path='https://image.tmdb.org/t/p/w500'+data()['poster_path']
    return path


# Movie recommend 
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    recommend_movie=[]
    recommend_movie_poster=[]
    for i in movies_list:
        id=movies.iloc[i[0]][0]
        
        #fetch poster from API
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_movie_poster.append(fetch_poster(id))
    return recommend_movie, recommend_movie_poster
        
# Cast name and id
def detail_fetcher(movie_name):
    cast_name=[]
    cast_id=[]
    detail=info[info['title']==movie_name]['cast']
    for val in detail:
        val=ast.literal_eval(val)
        for dic in val:
            for key, val in dic.items():
                if key=='name':
                    cast_name.append(val)
                elif key=='id':
                    cast_id.append(val)
                else:
                    pass
    df=pd.DataFrame({'name':cast_name,'id':cast_id})
    return df.head(12)



#Cast waigera ke liye

def recommended_info(movie_name):
    detail_fetcher(movie_name)
    id=detail_fetcher(movie_name)['id']
    return id.values

def recommended_info_name(movie_name):
    detail_fetcher(movie_name)
    name=detail_fetcher(movie_name)['name']
    return name.values

#recommended_info(selected_movie_name)
#recommended_info_name(selected_movie_name)

def char_photo(person_id):
    response=requests.get(f'https://api.themoviedb.org/3/person/{person_id}?api_key=57662ceb02223d144755d61d447e148b&language=en-US')
    data=response.json
    path=data()['profile_path']
    return 'https://image.tmdb.org/t/p/w500/'+path

def photo_photo():
    photo=[]
    for val in recommended_info(selected_movie_name):
        photo.append(char_photo(val))
    return photo

def char_name():
    char_name=[]
    for val in recommended_info_name(selected_movie_name):
        char_name.append(val)
    return char_name

# Streamlit User Interface



def details(movie_name):
    poster=[]
    movie_index=movies[movies['title']==movie_name]['movie_id'].values[0]
    poster.append(fetch_poster(movie_index))
    return poster

if selected_movie_name==selected_movie_name:
    name, poster =recommend(selected_movie_name)
    photo=photo_photo()
    char=char_name()
    col1, col2=st.columns(2)

    with col1:
        st.image(details(selected_movie_name))
    with col2:
        st.title(selected_movie_name)
    
#Cast Photos
    st.header('Top Cast')
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.text(char[0])
        st.image(photo[0])
        
    with col2:
        st.text(char[1])
        st.image(photo[1])
        
    with col3:
        st.text(char[2])
        st.image(photo[2])
        
    with col4:
        st.text(char[3])
        st.image(photo[3])
        
    with col5:
        st.text(char[4])
        st.image(photo[4])

    with col6:
        st.text(char[5])
        st.image(photo[5])
    
#Recommendations
    st.header('Recommendations')
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])
        
    with col2:
        st.text(name[1])
        st.image(poster[1])
        
    with col3:
        st.text(name[2])
        st.image(poster[2])
        
    with col4:
        st.text(name[3])
        st.image(poster[3])
        
    with col5:
        st.text(name[4])
        st.image(poster[4])

    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[5])
        st.image(poster[5])
        
    with col2:
        st.text(name[6])
        st.image(poster[6])
        
    with col3:
        st.text(name[7])
        st.image(poster[7])
        
    with col4:
        st.text(name[8])
        st.image(poster[8])
        
    with col5:
        st.text(name[9])
        st.image(poster[9])
