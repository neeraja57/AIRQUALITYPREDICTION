import streamlit as st

def app():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://thumbs.dreamstime.com/b/green-grass-blue-sky-5728464.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center center;
            font-family: Arial, sans-serif;
            color: #333;
            text-align: center;
            padding: 20px;
            margin: 0;
            height: 100vh;
            overflow: hidden;
        }
        .container {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 8px;
            padding: 20px;
            display: inline-block;
            margin-top: 20px;
        }
        </style>
        <div class="container">
            <h1>Welcome to the AQI Prediction</h1>
            <p>This website predicts the Air Quality Index (AQI) for Ongole based on various meteorological parameters.</p>
            
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()
