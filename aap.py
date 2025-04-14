# -*- coding: utf-8 -*-
"""

@author: Khushnaz 
"""

import numpy as np
import joblib
import streamlit as st

# loading the saved model
loaded_model = joblib.load('property_price_model.pkl')

# creating a function for Prediction
def property_price_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    return prediction[0]

def main():
    # giving a title
    st.title('Property Price Prediction Web App')

    # getting the input data from the user
    PropertyClass = st.text_input('Property Class')
    PropertyZone = st.text_input('Property Zone')
    PropertyFrontage = st.text_input('Property Frontage')
    PropertySize = st.text_input('Property Size')
    Street = st.text_input('Street')
    Alley = st.text_input('Alley')
    PropertyShape = st.text_input('Property Shape')
    Elevation = st.text_input('Elevation')
    Amenities = st.text_input('Amenities')
    LotOrientation = st.text_input('Lot Orientation')
    Grade = st.text_input('Grade')
    Neighborhood = st.text_input('Neighborhood')
    Condition1 = st.text_input('Condition 1')
    Condition2 = st.text_input('Condition 2')
    BldgType = st.text_input('Building Type')
    PropertyStyle = st.text_input('Property Style')
    OverallQual = st.text_input('Overall Quality')
    OverallCond = st.text_input('Overall Condition')
    YearBuilt = st.text_input('Year Built')
    YearRemodAdd = st.text_input('Year Remodeled/Add')
    RoofStyle = st.text_input('Roof Style')
    RoofMatl = st.text_input('Roof Material')
    Roof1Material = st.text_input('Roof 1 Material')
    Roof2Material = st.text_input('Roof 2 Material')
    ExteriorCladdingType = st.text_input('Exterior Cladding Type')
    ExteriorCladdingArea = st.text_input('Exterior Cladding Area')
    ExterQual = st.text_input('Exterior Quality')
    ExterCond = st.text_input('Exterior Condition')
    PropertyFooting = st.text_input('Property Footing')
    BsmntFinish = st.text_input('Basement Finish')
    BsmntMaintenance = st.text_input('Basement Maintenance')
    BsmntVisibility = st.text_input('Basement Visibility')
    BsmntFinRat1 = st.text_input('Basement Finish Ratio 1')
    BsmntFinSty1 = st.text_input('Basement Finish Style 1')
    BsmntFinQual1 = st.text_input('Basement Finish Quality 1')
    BsmtFinSF2 = st.text_input('Basement Finish SF 2')
    BsmtUnfSF = st.text_input('Basement Unfinished SF')
    BsmntSqFtage = st.text_input('Basement Square Footage')
    Heating = st.text_input('Heating Type')
    HeatingEfficiency = st.text_input('Heating Efficiency')
    CentralAir = st.text_input('Central Air Conditioning (Y/N)')
    Electrical = st.text_input('Electrical System')
    FirstFlrSF = st.text_input('First Floor SF')
    SecondFlrSF = st.text_input('Second Floor SF')
    LowQualFinSF = st.text_input('Low Quality Finished SF (all floors)')
    GrLivArea = st.text_input('Above Grade (ground) Living Area SF')
    BsmtBath1 = st.text_input('Basement Full Bathrooms')
    BsmtBath2 = st.text_input('Basement Half Bathrooms')
    Bath1 = st.text_input('Full Bathrooms Above Grade')
    Bath2 = st.text_input('Half Baths Above Grade')
    BedroomUpLev = st.text_input('Number of Bedrooms Above Basement Level')
    KitchenUpLev = st.text_input('Number of Kitchens Above Basement Level')
    KitchenQual = st.text_input('Kitchen Quality')
    CntRmsUpLev = st.text_input('Total Rooms Above Grade (does not include bathrooms)')
    Functional = st.text_input('Home Functionality Rating')
    CntFireplaces = st.text_input('Number of Fireplaces')
    QualFireplace = st.text_input('Fireplace Quality')
    BasementType = st.text_input('Garage Location')
    BasementYrBlt = st.text_input('Year Garage was Built')
    BasementFinish = st.text_input('Interior Finish of the Garage')
    BasementCars = st.text_input('Size of Garage in Car Capacity')
    SquareFootage = st.text_input('Size of Garage in Square Feet')
    BasementQual = st.text_input('Garage Quality')
    BasementSqFootage = st.text_input('Garage Condition')
    PavedDrive = st.text_input('Paved Driveway')
    WoodDeckSF = st.text_input('Wood Deck Area in Square Feet')
    OpenPorchSF = st.text_input('Open Porch Area in Square Feet')
    EnclosedPorch = st.text_input('Enclosed Porch Area in Square Feet')
    ThreeSsnPorch = st.text_input('Three Season Porch Area in Square Feet')
    ScreenPorch = st.text_input('Screen Porch Area in Square Feet')
    PoolArea = st.text_input('Pool Area in Square Feet')
    PoolQC = st.text_input('Pool Quality')
    BoundaryFeatures = st.text_input('Boundary Features Quality')
    AddFeatures = st.text_input('Miscellaneous Feature Not Covered in Other Categories')
    AddVal = st.text_input('Value of Miscellaneous Feature')
    SaleMon = st.text_input('Month Sold')
    YrSold = st.text_input('Year Sold')
    SaleType = st.text_input('Type of Sale')
    SaleCondn = st.text_input('Condition of Sale')

    # code for Prediction
    prediction = ''

    # creating a button for Prediction
    if st.button('Predict Property Price'):
        prediction = property_price_prediction([PropertyClass, PropertyZone, PropertyFrontage, PropertySize, Street, Alley, PropertyShape, Elevation, Amenities, LotOrientation, Grade, Neighborhood, Condition1, Condition2, BldgType, PropertyStyle, OverallQual, OverallCond, YearBuilt, YearRemodAdd, RoofStyle, RoofMatl, Roof1Material, Roof2Material, ExteriorCladdingType, ExteriorCladdingArea, ExterQual, ExterCond, PropertyFooting, BsmntFinish, BsmntMaintenance, BsmntVisibility, BsmntFinRat1, BsmntFinSty1, BsmntFinQual1, BsmtFinSF2, BsmtUnfSF, BsmntSqFtage, Heating, HeatingEfficiency, CentralAir, Electrical, FirstFlrSF, SecondFlrSF, LowQualFinSF, GrLivArea, BsmtBath1, BsmtBath2, Bath1, Bath2, BedroomUpLev, KitchenUpLev, KitchenQual, CntRmsUpLev, Functional, CntFireplaces, QualFireplace, BasementType, BasementYrBlt, BasementFinish, BasementCars, SquareFootage, BasementQual, BasementSqFootage, PavedDrive, WoodDeckSF, OpenPorchSF, EnclosedPorch, ThreeSsnPorch, ScreenPorch, PoolArea, PoolQC, BoundaryFeatures, AddFeatures, AddVal, SaleMon, YrSold, SaleType, SaleCondn])
        
    st.success(f'The predicted property price is: ${prediction}')

if __name__ == '__main__':
    main()
