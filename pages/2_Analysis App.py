import streamlit as st
import numpy as np
import pandas as pd
import pickle
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
st.set_page_config(page_title= "viz demo")

st.title("Analytics")
feature_text = pickle.load(open('datasets/feature_text.pkl','rb'))
new_df = pd.read_csv("datasets/data_viz1.csv")

#1_________________________________
group_df = new_df.groupby('sector',as_index=False)[['price','price_per_sqft','built_up_area','latitude','longitude']].mean()
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",text=group_df["sector"],width=1200,height=700)
st.plotly_chart(fig,use_container_width=True)


#2-----------------------------------------------------------
st.header("Word Cloud")
wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)
fig, ax = plt.subplots()
fig = plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)
st.pyplot(fig)

#3------------------------------------------------------------------------
property_type =st.selectbox("Select Property Type",['flat','house'])
if property_type == 'house':
   fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price",width=1200,height=500)
   st.plotly_chart(fig1)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",title="Area Vs Price", width=1200, height=500)
    st.plotly_chart(fig1,use_container_width=True)

#4----------------------------------------------------------------------------------
sector_options = new_df["sector"].unique().tolist()
sector_options.insert(0,'overall')
select_sector =st.selectbox("Select Sector",sector_options)
st.header("BHK Pie Chart")
if select_sector=='overall':
    fig2 = px.pie(new_df,names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.pie(new_df[new_df['sector'] == select_sector], names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)


#5 ---------------------------------------------------------------------------------
temp_df = new_df[new_df['bedRoom'] <= 4]
# Create side-by-side boxplots of the total bill amounts by day
fig3 = px.box(temp_df, x='bedRoom', y='price', title='BHK Price Range',height=800,width=1000)
st.plotly_chart(fig3, use_container_width=True)

#6---------------------------------------------------------------------------------------
st.header("Side by Side Distplot for Property Type")
fig4 = plt.figure(figsize = (10,4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'],label= 'flat')
st.pyplot(fig4)

