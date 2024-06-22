import streamlit as st
import requests
import pandas as pd
import json
import datetime as dt

def temp_convert(f):
    c = (f - 32) * 5/9
    return c

st.sidebar.title('Weather Checker')
title = st.sidebar.text_input("Enter city name")

input_style = """
<style>
input[type="text"] {
    background-color: transparent;
    color: #a19eae;
}
div[data-baseweb="base-input"] {
    background-color: transparent !important;
}
[data-testid="stAppViewContainer"] {
    background-color: transparent !important;
}
</style>
"""
st.markdown(input_style, unsafe_allow_html=True)

API_key = '0730b6f9f2d9fcc976b98ba4a611ddae'
weather_data: object = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={title}&units=imperial&appid={API_key}").json()

if st.sidebar.button('Check the weather'):
    st.title("The weather in " + title.capitalize() + ' is: ')
    description = weather_data['weather'][0]['description']

    if 'clear' in description:
        background_image = """
        <style>
        [data-testid="stAppViewContainer"] > .main {
            background-image: url("https://images.unsplash.com/photo-1622278647429-71bc97e904e8?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-size: 100vw 100vh;
            background-position: center;  
            background-repeat: no-repeat;
        }
        </style>
        """

        st.markdown(background_image, unsafe_allow_html=True)
    elif description == 'clouds' or description == 'scattered clouds' or description == 'overcast clouds' or description == 'few clouds' or description == 'broken clouds':

        background_image = """
                <style>
                [data-testid="stAppViewContainer"] > .main {
                    background-image: url("https://img.freepik.com/free-photo/beautiful-blue-sky-image_839833-16788.jpg?w=900&t=st=1718386872~exp=1718387472~hmac=8fb1c219b1bd3b4e398fab224c784f700a4293220dd5e9783e73ca9b6492c01a");
                    background-size: 100vw 100vh;
                    background-position: center;  
                    background-repeat: no-repeat;
                }
                </style>
                """

        st.markdown(background_image, unsafe_allow_html=True)

    elif description == 'moderate rain' or description == 'rain' or description == 'moderate rain' or description == 'light rain' or description == 'light intensity shower rain':
        background_image = """
                        <style>
                        [data-testid="stAppViewContainer"] > .main {
                            background-image: url("https://img.freepik.com/free-photo/urban-clear-scratched-window-cement_1123-101.jpg?t=st=1718389118~exp=1718392718~hmac=8ac0c82b57de5c53d82970516a6b211be65e5d6a75ea1c0ef7acd0bb0f3f77d1&w=740");
                            background-size: 100vw 100vh;
                            background-position: center;  
                            background-repeat: no-repeat;
                        }
                        </style>
                        """

        st.markdown(background_image, unsafe_allow_html=True)

    elif description == 'thunderstorm':
        background_image = """
                        <style>
                        [data-testid="stAppViewContainer"] > .main {
                            background-image: url("https://img.freepik.com/free-photo/view-apocalyptic-dark-clouds_23-2151065807.jpg?t=st=1718397294~exp=1718400894~hmac=beb24bed1c31ef57a3c93ca878cdecee7e48e6d24ef9346c4c83da25152bd8ea&w=900");
                            background-size: 100vw 100vh;
                            background-position: center;  
                            background-repeat: no-repeat;
                        }
                        </style>
                        """

        st.markdown(background_image, unsafe_allow_html=True)

    elif description == 'mist':
        background_image = """
                        <style>
                        [data-testid="stAppViewContainer"] > .main {
                            background-image: url("https://img.freepik.com/premium-photo/scenic-view-sea-against-sky_1048944-24561918.jpg?w=900");
                            background-size: 100vw 100vh;
                            background-position: center;  
                            background-repeat: no-repeat;
                        }
                        </style>
                        """

        st.markdown(background_image, unsafe_allow_html=True)

    elif description == 'snow':
        background_image = """
                        <style>
                        [data-testid="stAppViewContainer"] > .main {
                            background-image: url("https://img.freepik.com/premium-photo/winter-atmospheric-landscape-with-frost-covered-dry-plants-snowfall-winter-christmas-background_199743-8760.jpg?w=1060");
                            background-size: 100vw 100vh;
                            background-position: center;  
                            background-repeat: no-repeat;
                        }
                        </style>
                        """

        st.markdown(background_image, unsafe_allow_html=True)


    if weather_data.get('cod') != 404:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric('Temperature', f"{temp_convert(weather_data['main']['temp']):.0f}°C")
            st.metric('Feels like', f"{temp_convert(weather_data['main']['feels_like']):.0f}°C")
        with col2:
            st.metric('Min temperature', f"{temp_convert(weather_data['main']['temp_min']):.0f}°C")
            st.metric('Max temperature', f"{temp_convert(weather_data['main']['temp_max']):.0f}°C")
        with col3:
            st.metric('Sunrise', f"{dt.datetime.utcfromtimestamp(weather_data['sys']['sunrise'] + weather_data['timezone']).strftime('%H:%M')}")
            st.metric('Sunset', f"{dt.datetime.utcfromtimestamp(weather_data['sys']['sunset'] + weather_data['timezone']).strftime('%H:%M')}")

        st.write('The weather is ' + description)

    else:
        st.error('City not found')








