import streamlit as st

def app():
    # Applying background color using a full-page layout
    st.markdown(
        """
        <style>
        .main {
            background-color: #d1d3d4; /* Light cyan background */
            padding: 20px;
        }
        .title {
            text-align: center;
            color: #ffffff;
            background-color: #666666; /* Light peach color for the title background */
            padding: 20px;
            border-radius: 10px;
        }
        .content {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }
        .section {
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Main container with light cyan background
    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.markdown('<h1 class="title">Air Quality Index (AQI) Information and Health Recommendations</h1>', unsafe_allow_html=True)

   

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write("""
    ## What is AQI?
    The Air Quality Index (AQI) is an index for reporting daily air quality. It tells you how clean or polluted your air is, and what associated health effects might be of concern.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write("""
    ## Health Impacts:
    - **Good**: Air quality is considered satisfactory, and air pollution poses little or no risk.
    - **Moderate**: Air quality is acceptable; however, there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.
    - **Unhealthy for Sensitive Groups**: Members of sensitive groups may experience health effects. The general public is less likely to be affected.
    - **Unhealthy**: Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.
    - **Very Unhealthy**: Health alert: everyone may experience more serious health effects.
    - **Hazardous**: Health warnings of emergency conditions. The entire population is more likely to be affected.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write("""
    ## Health Recommendations
    Based on the predicted AQI, here are some health recommendations:
    - **Good (0-50)**: Air quality is considered satisfactory, and air pollution poses little or no risk.
    - **Moderate (51-100)**: Air quality is acceptable; however, there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.
    - **Unhealthy for Sensitive Groups (101-150)**: Members of sensitive groups may experience health effects. The general public is less likely to be affected.
    - **Unhealthy (151-200)**: Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.
    - **Very Unhealthy (201-300)**: Health alert: everyone may experience more serious health effects.
    - **Hazardous (301-500)**: Health warnings of emergency conditions. The entire population is more likely to be affected.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
