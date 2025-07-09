import pandas as pd
import matplotlib.pyplot as py
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

df=pd.read_csv("banglore_data.csv")
df_cleaned = df.dropna() # drop rows with missing values
# df_cleaned.to_csv('cleaned_data.csv', index=False) #to save with new file

df_modified = df.drop(['area_type', 'availability'], axis=1) # drop columns
# df_modified.to_csv('banglore_data.csv', index=False)
# print(df.head())

# Encode the Location
le=LabelEncoder()
df['Locationindex']=le.fit_transform(df['location'])
df['societyindex']=le.fit_transform(df['society'])
df['sizeindex']=le.fit_transform(df['size'])
df['total_sqftindex']=le.fit_transform(df['total_sqft'])
# print(df.head())

# Split the data into features and target
X=df[['sizeindex','societyindex','Locationindex','balcony','total_sqftindex','bath']]
y=df['price']

# Split the data into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#train the linear model
model=LinearRegression()
model.fit(X_train,y_train)
print("model trained")

# make predictions
predictions=model.predict(X_test)
# print(predictions)

#compare
c = pd.DataFrame({'Actual': y_test, 'Prediction': predictions.astype(int)})
print(c)
print(r2_score(y_test,predictions))