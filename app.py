import streamlit as st
import joblib
import numpy as np


model = joblib.load(
    "churn_model.pkl"
)



st.title(
    "📊 Customer Churn Predictor"
)



st.write(
    "Predict whether a customer will leave the service"
)



age = st.number_input(
    "Age"
)


tenure = st.number_input(
    "Tenure (Years)"
)


monthly = st.number_input(
    "Monthly Charges"
)


total = st.number_input(
    "Total Charges"
)


internet = st.selectbox(
    "Internet Service",
    [0,1]
)


contract = st.selectbox(
    "Contract Type",
    [0,1]
)



if st.button("Predict"):


    input_data = np.array(
        [
            age,
            tenure,
            monthly,
            total,
            internet,
            contract
        ]
    ).reshape(1,-1)



    result = model.predict(
        input_data
    )


    if result[0]==1:

        st.error(
            "Customer is likely to churn"
        )

    else:

        st.success(
            "Customer will stay"
        )
        