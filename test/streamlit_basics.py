import streamlit as st

st.title("Streamlit Intro")
st.write("This is where we'll streamlit")

name = st.text_input("Whats your name?")
if name:
    st.write(f"Welcome, {name}! Ready to build something amazing")
    
age = st.slider("Your age", 0, 100)
gender = st.radio("Gender", {"Male", "Female", "Other"})
interest = st.selectbox("Interested in ", {"CV", "ML", "Both"})
if st.button("Create proile"):
    st.write(f"Age: {age}, Gender: {gender}, Interest: {interest}")
    
# all_profile = []
# new_profile = {"Age": age, 
#                 "Gender": gender, 
#                 "Interest": interest}

# all_profile.append(new_profile)

# if(st.button("Show all profile")):
#     st.write(all_profile)

if "profiles" not in st.session_state:
    st.session_state.profiles = []
    
new_profile = {"Age": age, 
                "Gender": gender, 
                 "Interest": interest}

if st.button("Save and Show profile"):
    st.session_state.profiles.append(new_profile)
    st.write("All profiles", st.session_state.profiles)