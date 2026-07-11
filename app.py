import pickle
import streamlit as st

df=pickle.load(open("df.pkl",'rb'))
similarity=pickle.load(open("similarity.pkl",'rb'))
tfidf=pickle.load(open("tfidf.pkl",'rb'))

st.title("Bollywood music Recommender systeam")

user_input=st.text_input("Enter song name:")
st.markdown(
    """
    <style>
    /* Change background of the main content area */
    .stApp {
        background-color: #2596be;
        background-image:url("https://wallpapers.com/images/hd/table-of-music-4k-kapplvr0i9cj975e.jpg");
        background-size:cover;

    }
    

    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    h1 {
        color: #4F46E5 !important; /* Indigo color code */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    h2 {
        color: #4F46E5 !important; /* Indigo color code */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    header.stAppHeader {
        background-color: transparent !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def recommend(song):
  song=song.lower()

  try:
    index=df[df['song_name'].str.lower()==song].index[0]
  except:
    return []

  distance=similarity[index]
  songs_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

  recommended_songs=[]
  for i,score in songs_list:
    recommended_songs.append({
      "song":df.iloc[i]["song_name"],
      "artist":df.iloc[i]["artist"],
      "thumbnail":df.iloc[i]["thumbnail"] if
      "thumbnail" in df.columns else None
    })
  return recommended_songs

if st.button("Recommend"):
  try:
      
      idx=df[df["song_name"].str.lower()==user_input.lower()].index[0]
      st.subheader("You Searched For:")
      col1,col2=st.columns([1,3])


      with col1:


         
        if "thumbnail" in df.columns:


           
          st.image(df.iloc[idx]["thumbnail"],width="content")

      with col2:
        st.write("**Song:**",df.iloc[idx]["song_name"])
        st.write("**Artist:**",df.iloc[idx]["artist"])
     
  except:
    st.error("song not found")
    st.stop()

  st.subheader("Recommended Song")
  result=recommend(user_input)

  for item in result:
    col1,col2=st.columns([1,3])

    with col1:
      if item["thumbnail"]:
        st.image(item["thumbnail"],width="content")

    with col2:
      st.write("**Song:**",item["song"])
      st.write("**Artist:**",item["artist"])


  

  

