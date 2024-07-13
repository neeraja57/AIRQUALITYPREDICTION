import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.title("Data Visualization")
    
    if "predictions" not in st.session_state or not st.session_state.predictions:
        st.warning("No predictions made yet. Please go to the AQI Prediction page to make some predictions.")
        return
    
    predictions_df = pd.DataFrame(st.session_state.predictions)
    
    st.subheader("Predicted AQI Data")
    st.dataframe(predictions_df)

    st.subheader("AQI Over Time")
    plt.figure(figsize=(10, 5))
    plt.plot(predictions_df.index, predictions_df["AQI"], marker='o')
    plt.xlabel("Prediction Index")
    plt.ylabel("AQI")
    plt.title("AQI Predictions Over Time")
    plt.grid(True)
    st.pyplot(plt)

    st.subheader("Average Temperature vs. AQI")
    plt.figure(figsize=(10, 5))
    plt.scatter(predictions_df["Average_Temperature"], predictions_df["AQI"], c=predictions_df["AQI"], cmap='viridis', s=100)
    plt.colorbar(label='AQI')
    plt.xlabel("Average Temperature")
    plt.ylabel("AQI")
    plt.title("Average Temperature vs. AQI")
    st.pyplot(plt)

    # You can add more visualizations as needed

if __name__ == "__main__":
    app()
