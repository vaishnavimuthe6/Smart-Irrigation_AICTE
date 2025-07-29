import streamlit as st
import numpy as np
import joblib  
model = joblib.load("Farm_Irrigation_System.pkl")  

st.title("Smart/Automate irrigation System")
st.subheader("Enter scaled sensor values between (0 to 1) to predict status")

sensor_values = []
for i in range(20):
    val = st.slider(f"Sensor {i}", min_value=0.0,max_value=1.0,value=0.5,step=0.01)
    sensor_values.append(val)
    
if st.button("Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("### Prediction:")
    for i, status in enumerate(prediction):
        st.write(f"Sprinkler {i} (parcel_{i}): {'ON' if status == 1 else 'OFF'}")