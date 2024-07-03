import streamlit as st
import numpy as np
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Set page config
st.set_page_config(page_title="Mart Sales Prediction", layout="wide")

# Add custom CSS to style the page
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
            padding: 2rem;
        }
        .stTextInput, .stNumberInput {
            background-color: #ffffff;
            border: 1px solid #cccccc;
            border-radius: 4px;
            padding: 12px;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: box-shadow 0.3s ease-in-out;
            font-size: 16px;
        }
        .stTextInput:focus, .stNumberInput:focus {
            outline: none;
            box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
        }
        .stButton button {
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease-in-out;
        }
        .stButton button:hover {
            background-color: #0056b3;
        }
        .stTitle {
            color: #007BFF;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 1.5rem;
        }
        .stSubheader {
            color: #FF5733;
            font-size: 24px;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Set the title of the app
st.markdown("<h1 class='stTitle'> Mart Sales Prediction Using Machine Learning</h1>", unsafe_allow_html=True)

# Add a form to input all the features
with st.form("prediction_form"):
    st.markdown("<h2 class='stSubheader'>Input All Features Here</h2>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        Item_Identifier = st.text_input("Item Identifier")
    with col2:
        Item_weight = st.text_input("Item Weight")
    with col3:
        Item_Fat_Content = st.text_input("Item Fat Content")
    with col4:
        Item_visibility = st.text_input("Item Visibility")

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        Item_Type = st.text_input("Item Type")
    with col6:
        Item_MPR = st.text_input("Item MPR")
    with col7:
        Outlet_identifier = st.text_input("Outlet Identifier")
    with col8:
        Outlet_established_year = st.text_input("Outlet Established Year", value="1900")

    col9, col10, col11 = st.columns(3)
    with col9:
        Outlet_size = st.text_input("Outlet Size")
    with col10:
        Outlet_location_type = st.text_input("Outlet Location Type")
    with col11:
        Outlet_type = st.text_input("Outlet Type")

    # Submit button
    submit_button = st.form_submit_button("Predict")

# Function to validate numeric inputs
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# If the form is submitted, make the prediction
if submit_button:
    if not all([Item_Identifier, Item_weight, Item_Fat_Content, Item_visibility, Item_Type,
                Item_MPR, Outlet_identifier, Outlet_established_year, Outlet_size,
                Outlet_location_type, Outlet_type]):
        st.warning("Please fill in all the input fields.")
    elif not all([is_numeric(Item_weight), is_numeric(Item_visibility), is_numeric(Item_MPR), is_numeric(Outlet_established_year)]):
        st.error("Wrong input format. Please enter numeric values where appropriate.")
    else:
        try:
            features = np.array([[Item_Identifier, float(Item_weight), Item_Fat_Content, float(Item_visibility), Item_Type,
                                  float(Item_MPR), Outlet_identifier, int(Outlet_established_year), Outlet_size,
                                  Outlet_location_type, Outlet_type]], dtype=object)
            prediction = model.predict(features)[0]
            st.subheader(f"Predicted Sales: {prediction}")
        except ValueError:
            st.error("Wrong input format. Please enter the correct format.")
