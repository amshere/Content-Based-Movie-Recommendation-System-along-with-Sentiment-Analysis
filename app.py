#
#
# #******SHC*******
# import requests
# import pickle
# import pandas as pd
# import streamlit as st
# import json
# import re
# from nltk.corpus import stopwords
#
# from sklearn.feature_extraction.text import CountVectorizer
# from streamlit_lottie import st_lottie
# st.set_page_config(initial_sidebar_state="collapsed")
# def load_lottiefile(filepath: str):
#     with open(filepath, "r") as f:
#         return json.load(f)
#
# lottie_coding = load_lottiefile("animation1.json")
#
# #st.set_page_config(initial_sidebar_state="collapsed")
#
# # Initialize shared variable
# selected_movie_name_shared = st.empty()
#
#
# def fetch_poster(movie_id):
#     response = requests.get()
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     recommended_movies_posters = []
#
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         # fetch poster from api
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_posters
#
#
# # Load data
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# movies_detail_dict = pickle.load(open('movies_detail_dict.pkl', 'rb'))
# movies_detail_pd = pd.DataFrame(movies_detail_dict)
#
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# model = pickle.load(open('model.pkl','rb'))
# scaler = pickle.load(open('scaler.pkl','rb'))
#
#
#
#
#
# # Initialize session state
# if 'selected_movie_name' not in st.session_state:
#     st.session_state.selected_movie_name = None
# # Streamlit app
# #st.title('Movie Recommender System')
#
# movie_icon, movie_title = st.columns((0.25, 1.25))
# with movie_icon:
#     st_lottie(lottie_coding, height=200, key="movie")
# with movie_title:
#     st.markdown(
#         '<div class="st-emotion-cache-10trblm" style="padding-top:55px; font-size:40px; font-weight:bold;">Movie Recommendation System</div>',
#         unsafe_allow_html=True
#     )
#     #st.title('Movie Recommender System')
# selected_movie_name_value = None
#
# selected_movie_name = st.selectbox(
#     'Select a Movie?',
#     movies['title'].values)
#
# showdata = False
#
# button_clicked = st.button('Recommend')
#
# if "clicked" not in st.session_state:
#     st.session_state["clicked"] = False
#
# if "show_data" not in st.session_state:
#     st.session_state["show_data"] = False
#
# if "selected_movie_data" not in st.session_state:
#     st.session_state["selected_movie_data"] = None
#
# if button_clicked:
#     st.session_state["clicked"] = True
#
# if st.session_state["clicked"]:
#     names, posters = recommend(selected_movie_name)
#
#     col1, col2, col3, col4, col5 = st.columns(5)
#
#     for i in range(5):
#         with locals()[f"col{i + 1}"]:
#             st.text(names[i])
#             st.image(posters[i])
#             # st.button(names[i])
#             # Check if any button is clicked
#             if st.button(f"Details for {names[i]}"):
#                 selected_movie_name_value = names[i]
#
#                 st.session_state["show_data"] = True
#                 st.session_state["selected_movie_data"] = names[i]
#
# if st.session_state["show_data"]:
#
#     selected_movie_name_value = st.session_state["selected_movie_data"]
#
#     st.write("You selected:", selected_movie_name_value)
#
#     # Access the shared variable outside Streamlit
#     if selected_movie_name_value:
#         with st.container():
#             st.write("#")
#             st.write("This is inside the container")
#
#             details = movies_detail_pd[movies_detail_pd['title'] == selected_movie_name_value]
#             if not details.empty:
#                 details = details.iloc[0]
#                 #st.write(f'<span style="font-size:20px; color:blue; font-family:Arial, sans-serif;">Details for {selected_movie_name_value}:')
#                 st.write(
#                     f'<span style="font-size:30px; color:dark-grey; font-family:Arial, sans-serif; font-weight:bold;">{selected_movie_name_value}:</span>',
#                     unsafe_allow_html=True)
#                 movies_id = details['movie_id']
#                 movie_poster = fetch_poster(movies_id)
#                 st.image(movie_poster, width=200)
#
#                 st.write(f'<span style="font-size:15px; color:blue; font-weight:bold;">Overview:   </span><i>{details["overview"]}</i>', unsafe_allow_html=True)
#                 st.markdown(f'<span style="font-size:15px; color:blue; font-weight:bold;">Genres: </span><span style="font-size:15px; color:grey; font-weight:bold;">{details["genres"]}</span>', unsafe_allow_html=True)
#                 st.markdown(f'<span style="font-size:15px; color:blue; font-weight:bold;">Cast: </span><i>{details["cast"]}</i>', unsafe_allow_html=True)
#                 st.markdown(f'<span style="font-size:15px; color: blue; font-weight:bold;">Crew:  </span><i>{details["crew"]}', unsafe_allow_html=True)
#             else:
#                 print(f'Detailssssssssssss not found {selected_movie_name_value}')
#
#
#             def clean_review(review):
#                 str = ' '.join(word for word in review.split() if word.lower() not in stopwords.words('english'))
#                 return str
#
#
#             def clean_html(text):
#                 clean = re.compile('<.*?>')
#                 return re.sub(clean, '', text)
#
#
#             def remove_special(text):
#                 x = ''
#                 for i in text:
#                     if i.isalnum():
#                         x = x + i
#                     else:
#                         x = x + ' '
#                 return x
#
#             review = st.text_input('Write review here')
#             if st.button('Submit'):
#                 review_clean = clean_review(review)
#                 review_clean = clean_html(review)
#                 review_clean = remove_special(review)
#                 #scaler = CountVectorizer(max_features=5000)
#                 review_scale = scaler.transform([review_clean]).toarray()
#
#                 review_scale = scaler.transform([review_lowercase]).toarray()
#                 result = model.predict(review_scale)
#                 if result[0] == 0:
#                     st.write("Negative")
#                 else:
#                     st.write("Positive")
#
#
#
#
#
#
#
#
#
#
import requests
import pickle
import pandas as pd
import streamlit as st
import json
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import sqlite3
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile("animation1.json")

def fetch_poster(movie_id):
    response = requests.get(''.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

movies_detail_dict = pickle.load(open('movies_detail_dict.pkl', 'rb'))
movies_detail_pd = pd.DataFrame(movies_detail_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Initialize session state
if 'selected_movie_name' not in st.session_state:
    st.session_state.selected_movie_name = None

# Create SQLite database connection
conn = sqlite3.connect('movie_reviews.db')

# Function to add a review to the database
def add_review(movie_id, movie_title, review_text, sentiment):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO reviews (movie_id, movie_title, review, sentiment) VALUES (?, ?, ?, ?)',
                   (movie_id, movie_title, review_text, sentiment))
    conn.commit()

# Function to get reviews for a specific movie
def get_reviews(movie_id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reviews WHERE movie_id = ?', (movie_id,))
    return cursor.fetchall()

# Streamlit app
st.set_page_config(initial_sidebar_state="collapsed")

movie_icon, movie_title = st.columns((0.25, 1.25))
with movie_icon:
    st_lottie(lottie_coding, height=200, key="movie")
with movie_title:
    st.markdown(
        '<div class="st-emotion-cache-10trblm" style="padding-top:55px; font-size:40px; font-weight:bold;">Movie Recommendation System</div>',
        unsafe_allow_html=True
    )

selected_movie_name_value = None
selected_movie_name = st.selectbox(
    'Select a Movie?',
    movies['title'].values)

show_data = False
button_clicked = st.button('Recommend')

if "clicked" not in st.session_state:
    st.session_state["clicked"] = False

if "show_data" not in st.session_state:
    st.session_state["show_data"] = False

if "selected_movie_data" not in st.session_state:
    st.session_state["selected_movie_data"] = None

if button_clicked:
    st.session_state["clicked"] = True

if st.session_state["clicked"]:
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    for i in range(5):
        with locals()[f"col{i + 1}"]:
            st.text(names[i])
            st.image(posters[i])
            if st.button(f"Details for {names[i]}"):
                selected_movie_name_value = names[i]
                st.session_state["show_data"] = True
                st.session_state["selected_movie_data"] = names[i]
                st.session_state["review_text"] = ""

if st.session_state["show_data"]:
    selected_movie_name_value = st.session_state["selected_movie_data"]
    st.write("You selected:", selected_movie_name_value)

    def clean_review(review):
        str = ' '.join(word for word in review.split() if word.lower() not in stopwords.words('english'))
        return str

    def clean_html(text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def remove_special(text):
        x = ''
        for i in text:
            if i.isalnum():
                x = x + i
            else:
                x = x + ' '
        return x

    # Access the shared variable outside Streamlit
    if selected_movie_name_value:
        with st.container():
            st.write("#")
            #st.write("This is inside the container")

            details = movies_detail_pd[movies_detail_pd['title'] == selected_movie_name_value]
            if not details.empty:
                details = details.iloc[0]
                st.write(
                    f'<span style="font-size:35px; color:dark-grey; font-family:Arial, sans-serif; font-weight:bold;">{selected_movie_name_value}:</span>',
                    unsafe_allow_html=True)
                movies_id = details['movie_id']
                st.image(fetch_poster(movies_id), width=200)
                st.write(
                    f'<span style="font-size:20px; color:#FF4B4B; font-weight:bold;">Overview: </span><i>{details["overview"]}</i>',
                    unsafe_allow_html=True)
                st.markdown(
                    f'<span style="font-size:20px; color:#FF4B4B; font-weight:bold;">Genres: </span><span style="font-size:15px; color:#ffad33; font-weight:bold;text-shadow: 0 0 5px #ffad33, 0 0 10px #ffad33, 0 0 15px #ffad33; ">{details["genres"]}</span>',
                    unsafe_allow_html=True)
                st.markdown(
                    f'<span style="font-size:20px; color:#FF4B4B; font-weight:bold;">Cast: </span><i>{details["cast"]}</i>',
                    unsafe_allow_html=True)
                st.markdown(
                    f'<span style="font-size:20px; color: #FF4B4B; font-weight:bold;">Crew: </span><i>{details["crew"]}</i>',
                    unsafe_allow_html=True)
                with st.form(key='review_form', clear_on_submit=True):
                    review_input = st.text_area("Write review here")

                    # Handle the form submission
                    submit_button = st.form_submit_button(label='Submit')

                    if submit_button:
                        review = review_input.strip()  # Get the review text and remove leading/trailing whitespace
                        if review:
                            review_clean = clean_review(review)
                            review_clean = clean_html(review_clean)
                            review_clean = remove_special(review_clean)
                            review_scale = scaler.transform([review_clean]).toarray()
                            result = model.predict(review_scale)
                            sentiment = "Positive" if result[0] == 1 else "Negative"
                            add_review(movies_id, selected_movie_name_value, review, sentiment)
                            st.write(f"Review submitted! Sentiment: {sentiment}")
                            st.write(f"Review submitted! Review text: {review}")
                            # Clear the review input box using JavaScript
                            st.write(
                                "<script>"
                                "document.getElementById('review_form').reset();"
                                "</script>",
                                unsafe_allow_html=True
                            )
                        else:
                            st.write("Please enter a review.")
                # review = st.text_input('Write review here', value=st.session_state.review_text)
                # if st.button('Submit'):
                #     st.session_state.review_text = review
                #     review_clean = clean_review(review)
                #     review_clean = clean_html(review_clean)
                #     review_clean = remove_special(review_clean)
                #     review_scale = scaler.transform([review_clean]).toarray()
                #     result = model.predict(review_scale)
                #     sentiment = "Positive" if result[0] == 1 else "Negative"
                #     add_review(movies_id, selected_movie_name_value, review, sentiment)
                #     st.write(f"Review submitted! Sentiment: {sentiment}")
            else:
                st.write(f'Details not found for {selected_movie_name_value}')

            reviews = get_reviews(movies_id)
            if reviews:
                st.write(f"Reviews for {selected_movie_name_value}:")
                for review in reviews:
                   #st.write(f"Review: {review[2]}, Sentiment: {review[3]}")
                   st.markdown(
                       f"""
                                <div style="border: 1px solid #e6e6e6; border-radius: 5px; padding: 10px; box-shadow: 2px 2px 5px #888888; margin-bottom: 10px;">
                                    <p><b>Review:</b> {review[2]}</p>
                                    <p><b>Sentiment:</b> {review[3]}</p>
                                </div>
                                """,
                       unsafe_allow_html=True
                   )
            else:
                st.write(f"No reviews found for {selected_movie_name_value}")















