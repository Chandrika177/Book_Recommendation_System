import streamlit as st 
import pickle
import pandas as pd
import os
import numpy as np
import requests

#Function to recommend similar books based on input book title

def recommend(book):
    
    if book in collaborative_filtering_pivot.index:
     
        index = np.where(collaborative_filtering_pivot.index==book)[0][0]
    #Get the similarity scores of all books compared to the input book
    
        similar_book_items = sorted(list(enumerate(similarities[index])), key=lambda x: x[1], reverse=True)[1:11]
        data = []
    
    # Retrieve information of similar books from the dataset
    
        for i in similar_book_items:
                item = []
                temp_df = books_data[books_data['Book-Title']==  collaborative_filtering_pivot.index[i[0]]]
                item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
                item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
                item.extend(list(temp_df.drop_duplicates('Book-Title')['Year-Of-Publication'].values))
                data.append(item)
    
        return data


#Main streamlit app
  
st.header('Book Recommendation System')

#Load data & models
popular_recommendations = pickle.load(open('PopularBookRecommendation.pkl', 'rb'))
collaborative_filtering_pivot = pickle.load(open('pivot.pkl', 'rb'))
books_data = pickle.load(open('Books.pkl', 'rb'))
similarities = pickle.load(open('similarities.pkl', 'rb'))


book_list = collaborative_filtering_pivot.index.values
book_Title =popular_recommendations['Book-Title'].tolist()
book_Author =popular_recommendations['Book-Author'].tolist()
Year_Of_Publication =popular_recommendations['Year-Of-Publication'].tolist()

# Sidebar for displaying Top 100 books
st.sidebar.title('Top 10 Popular Books')
if st.sidebar.button('SHOW'):
    
    st.subheader("Top 10 Popular Books")
    
    colms = st.columns(3)
    fields = ['Book-Title', 'Book-Author', 'Year-Of-Publication']
    
    for col, field_name in zip(colms, fields):
           # header
           col.write(field_name)
            
            #Display top 100 books
    col1,col2,col3 = st.columns(3)
    with col1:
                       
                        st.text(book_Title[0])
                        st.text(book_Title[1])
                        st.text(book_Title[2])
                        st.text(book_Title[3])
                        st.text(book_Title[4])
                        st.text(book_Title[5])
                        st.text(book_Title[6])
                        st.text(book_Title[7])
                        st.text(book_Title[8])
                        st.text(book_Title[9])
              
    with col2:
                         st.text(book_Author[0])
                         st.text(book_Author[1])
                         st.text(book_Author[2])
                         st.text(book_Author[3])
                         st.text(book_Author[4])
                         st.text(book_Author[5])
                         st.text(book_Author[6])
                         st.text(book_Author[7])
                         st.text(book_Author[8])
                         st.text(book_Author[9])
                         
    with col3:
                         
                        st.text(str(Year_Of_Publication[0]))
                        st.text(str(Year_Of_Publication[1]))
                        st.text(str(Year_Of_Publication[2]))
                        st.text(str(Year_Of_Publication[3]))
                        st.text(str(Year_Of_Publication[4]))
                        st.text(str(Year_Of_Publication[5]))
                        st.text(str(Year_Of_Publication[6]))
                        st.text(str(Year_Of_Publication[7]))
                        st.text(str(Year_Of_Publication[8]))
                        st.text(str(Year_Of_Publication[9]))
                        
                    
st.sidebar.title('Recommend Books')

selected_book = st.sidebar.selectbox("Type or Select a book from the dropdown",book_list)        
        
if st.sidebar.button('Search'):
    
    st.subheader("Recommended Books")
    
    #Retrieve and display similar book based on the selected book
    fetch_books =recommend(selected_book)
    
    
    #Displaying Recommended books
    col1,col2,col3,col4,col5 =st.columns(5)
    with col1:
        st.text(fetch_books[0][0])
        st.text(fetch_books[0][1])
    
    with col2:
         st.text(fetch_books[1][0])
         st.text(fetch_books[1][1])
     
    with col3:
         st.text(fetch_books[2][0])
         st.text(fetch_books[2][1])
     
    with col4:
          st.text(fetch_books[3][0])
          st.text(fetch_books[3][1])
      
    with col5:
          st.text(fetch_books[4][0])
          st.text(fetch_books[4][1])
          
    col6, col7,col8,col9,col10 = st.columns(5, vertical_alignment="bottom")
    with col6:
        st.text(fetch_books[5][0])
        st.text(fetch_books[5][1])
    
    with col7:
         st.text(fetch_books[6][0])
         st.text(fetch_books[6][1])
     
    with col8:
         st.text(fetch_books[7][0])
         st.text(fetch_books[7][1])
     
    with col9:
          st.text(fetch_books[8][0])
          st.text(fetch_books[8][1])
      
    with col10:
          st.text(fetch_books[9][0])
          st.text(fetch_books[9][1])
 
    