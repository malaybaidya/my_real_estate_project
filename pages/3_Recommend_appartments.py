import streamlit as st
import pickle
import pandas as pd
import numpy as np
st.set_page_config(page_title="Recommended Apartments")

location_df = pickle.load((open('datasets/location_distance.pkl','rb')))
cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl','rb'))
cosine_sim2 = pickle.load(open('datasets/cosine_sim1.pkl','rb'))
cosine_sim3 = pickle.load(open('datasets/cosine_sim1.pkl','rb'))


def recommend_properties_with_scores(property_name, top_n=247):
    cosine_sim_matrix = .5 * cosine_sim1 + .8 * cosine_sim2 + cosine_sim3
    # cosine_sim_matrix = cosine_sim3

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()

    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df



st.dataframe(location_df)
st.title("select the location and radius")

selected_location = st.selectbox("Location", sorted(location_df.columns.to_list()))
radius = st.number_input("Radius in km's")

if st.button("search"):
    result_ser = location_df[location_df[selected_location] < radius*1000][selected_location].sort_values()
    apartment = []
    distance = []
    for key, values in result_ser.items():

        st.text(str(key) +" "+str(values/1000) + "kms")

# ----------------------------------------------------------------------------------------------------
st.title("Recommend Apartments")
selected_apartment = st.selectbox("select an Apartment" , sorted(location_df.index.to_list()))
if st.button("recommended"):
    recommendation_df = recommend_properties_with_scores(selected_apartment)
    st.dataframe(recommendation_df)





