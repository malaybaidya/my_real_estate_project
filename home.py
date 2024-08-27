import streamlit as st
import streamlit.components.v1 as stc

st.set_page_config(
    page_title="hello",
)
st.sidebar.success("select a demo above")

html_temp = """
			<div style="background-color:#8A9A5B;padding:10px;border-radius:10px">
			<h1 style="color:white;text-align:center;"> Real Estate Price Prediction</h1>
			<h3 style="color:white;text-align:center;"> Presented by : Malay Baidya </h3>
			</div>
			"""
stc.html(html_temp)
st.write("""
				### Thinking Ahead
				Real estate prices are deeply cyclical and much of it is dependent on factors you can't control.
				Whether you plan on buying a new property or want to use the equity in your home for other expenses,
				it is important to analyze both broader market conditions and your specific property
				to determine how the home's value may fare over the course of time.

				### Real Estate Price Prediction ML App
				##### 1. This App predict the price of property.
				##### 2. Estimate your budget as per your requirements.
				""")
