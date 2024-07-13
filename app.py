import streamlit as st
from multiapp import MultiApp
import home
import predict
import data_visualization
import information
import about
import health_recommendations
import pollutant_breakdown

app = MultiApp()

app.add_app("Home", home.app)
app.add_app("AQI Prediction", predict.app)
app.add_app("Data Visualization", data_visualization.app)
app.add_app("Information", information.app)

app.run()
