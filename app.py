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
        year =float((year - 2005) / (2020 - 2005) )
    with col2:
        km_driven=st.number_input("Kilo Meters",min_value=1,max_value=200000,help="Enter kilometers travelled by the car")
        km_driven=float((km_driven - 1000) / (195000 - 1000))
    col3,col4=st.columns(2)
    with col3:
        mileage=st.number_input("Mileage",help="Enter Mileage")
        mileage=float((mileage - 12.0) / (28.4 - 12.0))
    with col4:
        engine=st.number_input("Engine",help="Enter Engine cc")
        engine=float((engine - 793) / (1896 - 793))
    col5,col6 = st.columns(2)
    with col5:
        max_power = st.number_input("max_power",min_value=10,max_value=2022, help="Enter maximum power")
        max_power=float((max_power-34.2) / (138.1 -34.2))
    with col6:
       seats = st.number_input("Seats",min_value=1,max_value=10, help="Enter Seating Capacity")
    col7,col8 = st.columns(2)
    with col7:
        transmission = st.selectbox('Select Transmission Type',('manual','automatic'))
        if(transmission=='manual'):
            manual=1
        elif(transmission=='automatic'):
            manual=0
    with col8:
        seller_type= st.selectbox('Select Seller Type',('individual','dealer','trustmark dealer'))
        if(seller_type=='individual'):
            individual=1
            trust_dealer=0
        elif(seller_type=='dealer'):
            individual=0
            trust_dealer=0
        elif(seller_type=='trustmark dealer'):
            individual=0
            trust_dealer=1
    col9,col10 = st.columns(2)
    with col9:
        fuel= st.selectbox('Select fuel Type',('diesel','lpg','petrol','cng'))
        if(fuel=='diesel'):
            diesel=1
            lpg=0
            petrol=0
        elif(fuel=='lpg'):
            diesel=0
            lpg=1
            petrol=0
        elif(fuel=='petrol'):
            diesel=0
            lpg=0
            petrol=1
        elif(fuel=='cng'):
            diesel=0
            lpg=0
            petrol=0
    with col10:
        owner= st.selectbox('Select previous owner',('first','second','third','fourth','test'))
        if(owner=='first'):
            second=0
            third=0
            fourth=0
            test=0
        elif(owner=='second'):
           second=1
           third=0
           fourth=0
           test=0
        elif(owner=='third'):
            second=0
            third=1
            fourth=0
            test=0
        elif(owner=='fourth'):
            second=0
            third=0
            fourth=1
            test=0
        elif(owner=='test'):
            second=0
            third=0
            fourth=0
            test=1
    predict= st.button("Predict")
    if predict:
        model = pickle.load(open('model.pkl', 'rb'))
        prediction=model.predict([[year,km_driven,mileage,engine,max_power,seats,manual,individual,trust_dealer,diesel,lpg,petrol,fourth,second,test,third]])
        prediction=(prediction*(1227000-45000)+45000)
        if(prediction<0):
            prediction=prediction*-1
        output=round(prediction[0],2)
        st.header("The car price will be : ")
        st.header(output)
if __name__=='__main__':
    main()