import streamlit as st 
import pickle 

# Loading Pickle Model
model = pickle.load(open('model.pkl', 'rb'))

# Create Title
st.title("Predicting if msg is Spam or not")

message = st.text_input("Enter a message")
submit = st.button('Predict')


if submit:
    prediction = model.predict([message])
    
    if prediction[0] == 'spam':
        st.warning("This message is SPAM")
    else:
        st.success("This message is Legit (HAM)")

st.balloons()
    