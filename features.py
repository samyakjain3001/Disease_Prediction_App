def cancer_features():
    features = [
        'Radius_mean',
        'Texture_mean',
        'Perimeter_mean',
        'Area_mean',
        'Smoothness_mean',
        'Compactness_mean',
        'Concavity_mean',
        'concave points_mean',
        'symmetry_mean',
        'Compactness_mean',
        'radius_se',
        'texture_se',
        'perimeter_se',
        'area_se',
        'smoothness_se',
        'compactness_se',
        'concavity_se',
        'concave points_se',
        'symmetry_se',
        'fractal_dimension_se',
        'radius_worst',
        'texture_worst',
        'perimeter_worst',
        'area_worst',
        'smoothness_worst',
        'compactness_worst',
        'concavity_worst',
        'concave points_worst',
        'symmetry_worst',
        'fractal_dimension_worst'
    ]

    return features


def heart_features():
     

    features = [
        'age',
        'sex',
        'chest pain type', 
        'trestbps',
        'serum cholestoral in mg/dl', 
        'restecg',
        'thalach',
        'exang',
        'oldpeak', 
        'slope',
        'thal'
    ]

    return features

def diabetes_features():
    features = [
        'Pregnancies',
        'Glucose',
        'BloodPressure',
        'SkinThickness',
        'Insulin',
        'BMI',
        'DiabetesPedigreeFunction',
        'Age'
    ]

    return features


def liver_features():
    features = [
        'Age',
        'Gender',
        'Total_Bilirubin',
        'Direct_Bilirubin',
        'Alkaline_Phosphotase',
        'Alamine_Aminotransferase',
        'Aspartate_Aminotransferase',
        'Total_Protiens',
        'Albumin',
        'Albumin_and_Globulin_Ratio'
    ]
    return features

def kidney_features():
    features = [
        'age',
        'bp',
        'al',
        'pcc',
        'bgr',
        'bu',
        'sc',
        'hemo',
        'pcv',
        'htn',
        'dm',
        'appet'       
    ]
    return features