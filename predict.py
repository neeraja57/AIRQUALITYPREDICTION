import streamlit as st
import pickle

# Load the model
pickle_in = open("Random_forest_regressor.pkl", "rb")
random_forest_regressor = pickle.load(pickle_in)

def predict_AQI(Average_Temperature, Maximum_Temperature, Minimum_Temperature, Atm_pressure_at_sea_level, Average_wind_speed):
    prediction = random_forest_regressor.predict([[Average_Temperature, Maximum_Temperature, Minimum_Temperature, Atm_pressure_at_sea_level, Average_wind_speed]])
    return prediction[0]

def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good (0-50)", "#9ccc65", "Air quality is considered satisfactory, and air pollution poses little or no risk."
    elif aqi <= 100:
        return "Moderate (51-100)", "#ffeb3b", "Air quality is acceptable; however, there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups (101-150)", "#ff9800", "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
    elif aqi <= 200:
        return "Unhealthy (151-200)", "#f44336", "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
    elif aqi <= 300:
        return "Very Unhealthy (201-300)", "#9c27b0", "Health alert: everyone may experience more serious health effects."
    else:
        return "Hazardous (301-500)", "#795548", "Health warnings of emergency conditions. The entire population is more likely to be affected."

def app():
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
        }
        .stTextInput input {
            padding: 10px;
            border-radius: 5px;
        }
        .stTextInput input:focus {
            outline: none;
        }
        .title-container {
            background-color: #4CAF50; /* Green background for title */
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .title-container h2 {
            color: white; /* White text for the title */
            margin: 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title-container"><h2>AQI Prediction Website</h2></div>', unsafe_allow_html=True)
    
    st.title("Ongole AQI Prediction")

    if "predictions" not in st.session_state:
        st.session_state.predictions = []

    Average_Temperature = st.text_input("Average Temperature", "Type Here")
    Maximum_Temperature = st.text_input("Maximum Temperature", "Type Here")
    Minimum_Temperature = st.text_input("Minimum Temperature", "Type Here")
    Atm_pressure_at_sea_level = st.text_input("Atmospheric Pressure at Sea Level", "Type Here")
    Average_wind_speed = st.text_input("Average Wind Speed", "Type Here")
    
    result = ""
    aqi_category = ""
    color = ""
    health_message = ""
    
    if st.button("Predict"):
        # Convert inputs to floats
        Average_Temperature = float(Average_Temperature)
        Maximum_Temperature = float(Maximum_Temperature)
        Minimum_Temperature = float(Minimum_Temperature)
        Atm_pressure_at_sea_level = float(Atm_pressure_at_sea_level)
        Average_wind_speed = float(Average_wind_speed)
        
        result = predict_AQI(Average_Temperature, Maximum_Temperature, Minimum_Temperature, Atm_pressure_at_sea_level, Average_wind_speed)
        aqi_category, color, health_message = get_aqi_category(result)

        # Save the prediction to session state
        st.session_state.predictions.append({
            "Average_Temperature": Average_Temperature,
            "Maximum_Temperature": Maximum_Temperature,
            "Minimum_Temperature": Minimum_Temperature,
            "Atm_pressure_at_sea_level": Atm_pressure_at_sea_level,
            "Average_wind_speed": Average_wind_speed,
            "AQI": result
        })
        
        st.success(f'The predicted AQI is {result}')
        st.markdown(f'<div style="background-color:{color}; padding: 10px; border-radius: 5px; color: black;">AQI Category: {aqi_category}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="background-color:{color}; padding: 10px; border-radius: 5px; color: black;">Health Message: {health_message}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
