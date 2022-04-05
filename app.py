import pickle
import joblib,os
import streamlit as st


def model(model_file):
	return joblib.load(open(os.path.join(model_file),"rb"))

def main():
    st.title("used car price prediction")
    st.write("---")
    st.header('Enter values')
    col1 ,col2 = st.columns(2)
    with col1:
        year=st.number_input("Year",min_value=1000,max_value=2022,help="Enter the manufractured year of car")
    with col2:
        km_driven=st.number_input("Kilo Meters",min_value=1,max_value=200000,help="Enter kilometers travelled by the car")
    col3,col4 = st.columns(2)
    with col3:
        fuel= st.number_input("Fuel Type",min_value=1,max_value=4, help="Enter 1 for diesel 2 for petrol 3 for LPG 4 for CNG") 
    with col4:
        sellertype = st.number_input("Seller",min_value=1,max_value=3,help="1 for individual  2 for Dealer  3 for Trustmark Dealer")
    col5,col6 = st.columns(2)
    with col5:
        transmission= st.number_input("Transmission Type", min_value=0,max_value=1,help="1 for manual 0 for automatic")
    with col6:
       owner= st.number_input("owner", min_value=1,max_value=5,help="Enter 1 for 1st owner 2 for 2nd owner 3 for 3rd owner 4 for 4th owner 5 for test drive")
    col7,col8 = st.columns(2)
    with col7:
        mileage= st.number_input("Mileage",help="Enter Mileage")
    with col8:
        engine = st.number_input("Engine",min_value=20,max_value=2022, help="Enter Engine cc")
    col9,col10 = st.columns(2)
    with col9:
        max_power = st.number_input("max_power",min_value=10,max_value=2022, help="Enter maximum power")
    with col10:
       seats = st.number_input("Seats",min_value=1,max_value=10, help="Enter Seating Capacity")
    predict= st.button("Predict")
    if predict:
        model = pickle.load(open('model.pkl', 'rb'))
        prediction= model.predict([[year,km_driven,fuel,sellertype,transmission,owner,mileage,engine,max_power,seats]])
        st.header('The Car Price will be {}'.format(prediction*(-10)))
if __name__=='__main__':
    main()