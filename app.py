import pandas as pd
import streamlit as st
import joblib

model = joblib.load('xgb_model.jb')

st.title("House Price Prediction")
st.write("Enter the Details Below to predict the House Price")

# Remove SalePrice from inputs as it's the target variable
inputs = ['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea',
          'TotalBsmtSF', '1stFlrSF', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt',
          'YearRemodAdd', 'GarageYrBlt', 'MasVnrArea', 'Fireplaces', 'BsmtFinSF1',
          'Foundation', 'LotFrontage', 'WoodDeckSF', '2ndFlrSF', 'OpenPorchSF',
          'HalfBath', 'LotArea', 'CentralAir']

# Create two columns for better layout
col1, col2 = st.columns(2)

input_data = {}
for i, feature in enumerate(inputs):
    # Alternate between columns
    with col1 if i % 2 == 0 else col2:
        if feature == 'CentralAir':
            input_data[feature] = st.selectbox(
                f"{feature}",
                options=['Yes', 'No'],
                index=0
            )
        elif feature in ['OverallQual', 'FullBath', 'HalfBath', 'Fireplaces']:
            input_data[feature] = st.number_input(
                f"{feature}",
                min_value=0,
                max_value=20,
                value=0,
                step=1
            )
        elif feature in ['YearBuilt', 'YearRemodAdd', 'GarageYrBlt']:
            input_data[feature] = st.number_input(
                f"{feature}",
                min_value=1800,
                max_value=2025,
                value=2000,
                step=1
            )
        else:
            input_data[feature] = st.number_input(
                f"{feature}",
                min_value=0.0,
                value=0.0,
                step=0.1
            )

if st.button("Predict Price", type="primary"):
    try:
        # Convert CentralAir to numeric
        input_data['CentralAir'] = 1 if input_data['CentralAir'] == "Yes" else 0
        
        # Create DataFrame with features in correct order
        input_df = pd.DataFrame([input_data], columns=inputs)
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        
        # Display result with formatting
        st.success(f"Predicted House Price: ${prediction:,.2f}")
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.write("Please check your input values and try again.")