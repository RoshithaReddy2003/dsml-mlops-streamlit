import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.title('Cars 24 App')

col1, col2 = st.columns(2)
with col1:
    fuel_type = st.radio("Select Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])

with col2:
    transmission_type = st.selectbox("Select Transmission Type", ["Manual", "Automatic"])

col3, col4 = st.columns(2)
with col3:
    engine_power = st.slider("Engine Power", 500, 5000, step=100)

with col4:
    seats = st.selectbox("Seats", [2, 4, 5, 6, 7, 8, 9, 10])

# ------------------- Load Dataset -------------------
df = pd.read_csv("train-cars24-car-price.csv")

# Remove text column
df.drop("full_name", axis=1, inplace=True)

# Encode categorical columns
df["seller_type"] = df["seller_type"].map({
    "Individual": 1,
    "Dealer": 2,
    "Trustmark Dealer": 3
})

df["fuel_type"] = df["fuel_type"].map({
    "Diesel": 1,
    "Petrol": 2,
    "CNG": 3,
    "LPG": 4,
    "Electric": 5
})

df["transmission_type"] = df["transmission_type"].map({
    "Manual": 1,
    "Automatic": 2
})

# ------------------- Train Model -------------------
X = df.drop("selling_price", axis=1)
y = df["selling_price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

pickle.dump(model, open("car_pred.pkl", "wb"))

model = pickle.load(open("car_pred.pkl", "rb"))

# ------------------- Prediction -------------------
encode_dict = {
    "fuel_type": {
        "Diesel": 1,
        "Petrol": 2,
        "CNG": 3,
        "LPG": 4,
        "Electric": 5
    },
    "transmission_type": {
        "Manual": 1,
        "Automatic": 2
    }
}

def model_pred(fuel_type, transmission_type, engine_power, seats):

    fuel_type = encode_dict["fuel_type"][fuel_type]
    transmission_type = encode_dict["transmission_type"][transmission_type]

    data = [[
        2018,          # year
        1,             # seller_type
        40000,         # km_driven
        fuel_type,
        transmission_type,
        18.0,          # mileage
        engine_power,  # engine
        85.0,          # max_power
        seats
    ]]

    return round(model.predict(data)[0],2)

if st.button("Predict Price"):
    st.success(model_pred(fuel_type, transmission_type, engine_power, seats))
else:
    st.write("Click on Predict once you have selected the values.")