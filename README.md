# Project explanation
About the dataset:
The dataset is publicly available on the Kaggle website, and it is from an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. The classification goal is to predict whether the patient has a 10-year risk of future coronary heart disease (CHD). The dataset provides the patients' information. It includes over 4,240 records and 15 attributes.

Attributes:

sex: male(0) or female(1); (Nominal)
age: age of the patient; (Continuous - Although the recorded ages have been truncated to whole numbers, the concept of age is continuous)
currentSmoker: whether or not the patient is a current smoker (Nominal)
cigsPerDay: the number of cigarettes that the person smoked on average in one day (can be considered continuous as one can have any number of cigarettes, even half a cigarette.)
BPMeds: whether or not the patient was on blood pressure medication (Nominal)
prevalentStroke: whether or not the patient had previously had a stroke (Nominal)
prevalentHyp: whether or not the patient was hypertensive (Nominal)
diabetes: whether or not the patient had diabetes (Nominal)
totChol: total cholesterol level (Continuous)
sysBP: systolic blood pressure (Continuous)
diaBP: diastolic blood pressure (Continuous)
BMI: Body Mass Index (Continuous)
heartRate: heart rate (Continuous - In medical research, variables such as heart rate though in fact discrete, yet are considered continuous because of a large number of possible values.)
glucose: glucose level (Continuous)
10 year risk of coronary heart disease CHD (binary: "1", means "Yes"; "0" means "No") - Target Variable
Objective: To Build a classification model that predicts heart disease in a subject. (Note the target column to predict is 'TenYearCHD' where CHD = Coronary heart disease)

Performed the following steps:

Read the file and displayed columns.
Handled missing values, Outliers, and Duplicate Data.
Calculated basic statistics of the data (count, mean, std, etc.) and exploratory analysis and described my observations.
Selected columns that will be probably important to predict heart disease.
 removed some columns explain why I removed those.
Created training and testing sets (used 60% of the data for the training and the remainder for testing).
Built a machine learning model to predict TenYearCHD.
Evaluated the model (F1 score, Accuracy, Precision, Recall, and Confusion Matrix)
Concluded my findings (Model which is giving the best F1 score and why)

