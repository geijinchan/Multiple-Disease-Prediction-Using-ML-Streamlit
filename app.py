import pickle
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('Diabetics.sav','rb'))
heart_disease_model = pickle.load(open('Heart_disease.sav','rb'))
breast_cancer_model = pickle.load(open('breast_cancer.sav','rb'))


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Breast Cancer Prediction'],

                            icons=['activity','heart','person'],

                            default_index=0)
    
if(selected == 'Diabetes Prediction'):
    # Page Title
    st.title('Diabetes Prediction using ML')
    st.subheader('Enter Patient Information')
    # Create a 2x4 grid for input fields
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=None, step=1, value=0)

        Glucose = st.number_input('Glucose Level', min_value=0, max_value=None, step=1, value=0)

        BloodPressure = st.number_input('Blood Pressure', min_value=0, max_value=None, step=1, value=0)

        SkinThickness = st.number_input('Skin Thickness', min_value=0, max_value=None, step=1, value=0)

    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0, max_value=None, step=1, value=0)

        BMI = st.number_input('BMI', min_value=0.0, max_value=None, step=0.1, value=0.0)

        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=None, step=0.01, value=0.0)

        Age = st.number_input('Age of the Person', min_value=0, max_value=None, step=1, value=0)

    st.markdown('---')  # Add a horizontal line for separation

    # Code for Prediction
    diab_diagnosis = ''

    # Add a button to trigger the prediction
    if st.button('Predict Diabetes'):
        diab_pred = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if (diab_pred[0]==1):
            diab_diagnosis='The Person is Diabetic'
        else:
            diab_diagnosis='The Person is not Diabetic'
    st.success(diab_diagnosis)

if(selected == 'Heart Disease Prediction'):
    # Page Title
    st.title('Heart Disease Prediction using ML')
    st.subheader('Enter Patient Information')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age of Person', min_value=0, max_value=None, step=1, value=0)
        sex = st.selectbox('Select Gender',[0,1])
        cp = st.selectbox('Chest Pain Type',[0,1,2,3])
        trestbps = st.number_input('Resting Blood Presure',min_value=0, max_value=None, step=1, value=0)
        thalach = st.number_input('Maximum Heart Rate Achieved',min_value=0, max_value=None, step=1, value=0)

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl',min_value=0, max_value=None, step=1, value=0)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl',[0,1])
        restecg = st.selectbox('Resting Electrocardiographic Results (Values 0,1,2)',[0,1,2])
        exang = st.selectbox('Exercise Induced Angina',[0,1])

    with col3:
        oldpeak = st.number_input('Oldpeak = ST depression induced by exercise relative to rest', min_value=0.0, max_value=None, step=0.1, value=0.0)
        slope = st.selectbox('The Slope Of The Peak Exercise ST Segment',[0,1,2])
        ca = st.selectbox('number of major vessels (0-3) colored by flourosopy',[0,1,2,3])
        thal = st.selectbox('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',[0,1,2])
    st.markdown('---')
    heart_diag = ''
    # Add a button to trigger the prediction
    if st.button('Predict Heart Disease'):
        heart_predict = heart_disease_model.predict([[age,sex,cp,trestbps,thalach,chol,fbs,restecg,exang,oldpeak,slope,ca,thal]])
        if (heart_predict[0]==1):
            heart_diag='The Person is having heart disease'
        else:
            heart_diag='The Person is not having heart disease'
    st.success(heart_diag)


if(selected == 'Breast Cancer Prediction'):
    
    # Page Title
    st.title('Breast Cancer Prediction')
    st.subheader('Enter Cell Nuclei Measurements')
    col1, col2, col3 = st.columns(3)
    with col1:
        radius_mean = st.slider('Radius (mean)', float(0), float(30), float(15))
        texture_mean = st.slider('Texture (mean)', float(0), float(30), float(15))
        perimeter_mean = st.slider('Perimeter (mean)', float(0), float(200), float(100))
        area_mean = st.slider('Area (mean)', float(0), float(2000), float(1000))
        smoothness_mean = st.slider('Smoothness (mean)', float(0), float(1), float(0.5))
        compactness_mean = st.slider('Compactness (mean)', float(0), float(1), float(0.5))
        concavity_mean = st.slider('Concavity (mean)', float(0), float(1), float(0.5))
        concave_points_mean = st.slider('Concave points (mean)', float(0), float(1), float(0.5))
        symmetry_mean = st.slider('Symmetry (mean)', float(0), float(1), float(0.5))
        fractal_dimension_mean = st.slider('Fractal dimension (mean)', float(0), float(1), float(0.5))

    with col2:
        radius_se = st.slider('Radius (se)', float(0), float(5), float(2.5))
        texture_se = st.slider('Texture (se)', float(0), float(1), float(0.5))
        perimeter_se = st.slider('Perimeter (se)', float(0), float(1), float(0.5))
        area_se = st.slider('Area (se)', float(0), float(1), float(0.5))
        smoothness_se = st.slider('Smoothness (se)', float(0), float(1), float(0.5))
        compactness_se = st.slider('Compactness (se)', float(0), float(1), float(0.5))
        concavity_se = st.slider('Concavity (se)', float(0), float(1), float(0.5))
        concave_points_se = st.slider('Concave points (se)', float(0), float(1), float(0.5))
        symmetry_se = st.slider('Symmetry (se)', float(0), float(1), float(0.5))
        fractal_dimension_se = st.slider('Fractal Dimensions (se)', float(0), float(1), float(0.5))

    with col3:
        radius_worst = st.slider('Radius (worst)', float(0), float(30), float(15))
        texture_worst = st.slider('Texture (worst)', float(0), float(30), float(15))
        perimeter_worst = st.slider('Perimeter (worst)', float(0), float(200), float(100))
        area_worst = st.slider('Area (worst)', float(0), float(2000), float(1000))
        smoothness_worst = st.slider('Smoothness (worst)', float(0), float(1), float(0.5))
        compactness_worst = st.slider('Compactness (worst)', float(0), float(1), float(0.5))
        concavity_worst = st.slider('Concavity (worst)', float(0), float(1), float(0.5))
        concave_points_worst = st.slider('Concave points (worst)', float(0), float(1), float(0.5))
        symmetry_worst = st.slider('Symmetry (worst)', float(0), float(1), float(0.5))
        fractal_dimension_worst = st.slider('Fractal dimension (worst)', float(0), float(1), float(0.5))
    st.markdown('---')
    breast_cancer_scaler = pickle.load(open('scaler.pkl', 'rb'))
    input_data = {
        'radius_mean': radius_mean,
        'texture_mean': texture_mean,
        'perimeter_mean': perimeter_mean,
        'area_mean': area_mean,
        'smoothness_mean': smoothness_mean,
        'compactness_mean': compactness_mean,
        'concavity_mean': concavity_mean,
        'concave_points_mean': concave_points_mean,
        'symmetry_mean': symmetry_mean,
        'fractal_dimension_mean': fractal_dimension_mean,
        'radius_se': radius_se,
        'texture_se': texture_se,
        'perimeter_se': perimeter_se,
        'area_se': area_se,
        'smoothness_se': smoothness_se,
        'compactness_se': compactness_se,
        'concavity_se': concavity_se,
        'concave_points_se': concave_points_se,
        'symmetry_se': symmetry_se,
        'fractal_dimension_se': fractal_dimension_se,
        'radius_worst': radius_worst,
        'texture_worst': texture_worst,
        'perimeter_worst': perimeter_worst,
        'area_worst': area_worst,
        'smoothness_worst': smoothness_worst,
        'compactness_worst': compactness_worst,
        'concavity_worst': concavity_worst,
        'concave_points_worst': concave_points_worst,
        'symmetry_worst': symmetry_worst,
        'fractal_dimension_worst': fractal_dimension_worst
    }
    df = pd.DataFrame([input_data])

    # Scale the input features
    scaled_data = breast_cancer_scaler.transform(df)

    # Make the prediction
    breast_cancer_prediction = breast_cancer_model.predict(scaled_data)

    st.write(breast_cancer_prediction)
    if breast_cancer_prediction[0] == 1:
        st.success('The Cell is Malignant (Cancerous)')
    else:
        st.success('The Cell is Benign (Not Cancerous)')