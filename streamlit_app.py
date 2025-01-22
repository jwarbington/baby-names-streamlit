# Import the necessary libraries
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

# Setup web page
st.set_page_config(
    page_title="Snowflake Summit 2025",
    menu_items={
        "Get Help": "https://developers.snowflake.com",
        "About": "The original source code for this application can be accessed on GitHub https://github.com/iamontheinet/data-cloud-summit-countdown",
    },
)

count = st_autorefresh(interval=1000, limit=1000, key="datacloudsummitcounter")

def date_diff_in_seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def dhms_from_seconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

data_cloud_summit_25_date = datetime.strptime('2025-06-02 08:00:00', '%Y-%m-%d %H:%M:%S')
to_day = datetime.now()

days, hours, minutes, seconds = dhms_from_seconds(date_diff_in_seconds(data_cloud_summit_25_date,to_day))

with open("app.css") as f:
     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container():
    st.image("snowflake_summit_25.png")
    # st.title("Snowflake Summit 2025")
    st.subheader(":black[BUILD THE FUTURE TOGETHER WITH AI AND APPS]")
    st.subheader("MOSCONE CENTER | SAN FRANCISCO | JUNE 2-5, 2025")

st.header(f"{days} Days")

with st.container():
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.metric("Hours", hours)
    with col2:
        st.metric("Mins", minutes)
    with col3:
        st.metric("Secs", seconds)

st.markdown("___")
spaces = "          "
# st.caption(f"[Register Now](https://www.snowflake.com/summit/) // [Join Us at Dev Day](https://www.snowflake.com/summit/devday/)")
st.button(f"[REGISTER NOW](https://www.snowflake.com/summit/)")

st.caption(f"Originally Developed by [Dash](https://www.linkedin.com/in/dash-desai/) // Dedicated to [Saqib](https://www.linkedin.com/in/saqibmustafa/)")

with st.container():
    col1, col2, col3 = st.columns([3,3,1])
    with col2:
        st.image('dash_boarding.png', width=75)