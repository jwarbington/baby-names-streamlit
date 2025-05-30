# Import the necessary libraries
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import streamlit.components.v1 as components

# Setup web page
st.set_page_config(
   layout="wide",
    page_title="Baby Names Streamlit + Astrato",
    menu_items={
        "Get Help": "https://streamlit.io/",
        "About": "The original source code branched for this application can be accessed on GitHub https://github.com/iamontheinet/data-cloud-summit-countdown",
    },
)

count = st_autorefresh(interval=60000, limit=120, key="babyduedatecounter")

def date_diff_in_seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def dhms_from_seconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

baby_due_date = datetime.strptime('2025-04-11 19:22:00', '%Y-%m-%d %H:%M:%S')
to_day = datetime.now()

days, hours, minutes, seconds = dhms_from_seconds(date_diff_in_seconds(to_day,baby_due_date))

with open("app.css") as f:
     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container():
    # st.image("snowflake_summit_25.png")
    # st.title("Snowflake Summit 2025")
    st.header("**WELCOME BABY!**")
    st.subheader("🎂 APRIL 2025 🎂")
    st.balloons()
    
##st.header(f"{days} Days")
st.markdown("___")
spaces = "          "

with st.container():
    col1, col2, col3 = st.columns(3, gap="small", vertical_alignment='bottom')
    with col1:
        spaces = "          "
    with col2:
        #st.image('https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTRpZ3hseTZyNDQ0bTUwNHVzaHQxNHhtcjYyamVkdHhwZHk2emlucSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BDPuPAqI5rWCWXZp0f/giphy.gif')
        st.metric("Days", days)
    with col3:
        spaces = "          "

with st.container():
    col1, col2 = st.columns(2, gap="small", vertical_alignment='bottom')
    with col1:
        st.metric("Hours", hours)
    with col2:
        st.metric("Mins", minutes)

st.markdown("___")
spaces = "          "
# st.text("Astrato Analytics - Powered by Snowflake")
st.image('astrato-logo.svg')
components.iframe("https://app.astrato.io/embed/xvf1vvI", height=1000)

st.markdown("___")
spaces = "          " 
st.markdown(f"Built using [Streamlit](https://streamlit.io/) , [Snowflake](https://www.snowflake.com/), and [Astrato](https://www.astrato.io/) ")
