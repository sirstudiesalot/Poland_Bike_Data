import pandas as pd


df = pd.read_csv("C:/Users/Tarang/Desktop/Python/Python 2025/Poland_Bike_Data/Poland_Bike_trips.csv")

#print (df.info())



#Converting String to Datetime

df['start_date'] = pd.to_datetime(df['start_date'], format='%m/%d/%Y %H:%M:%S')

#Updating dataset to be contemporary, adding +10 years to dataset

df['start_date'] = df['start_date'] + pd.DateOffset(years=10)

#print (df['start_date'])

#Creating Useful Features
df['month'] = df['start_date'].dt.month
df['weekday'] = df['start_date'].dt.day_name()
df['hour'] = df['start_date'].dt.hour  # if time info exists

#print (df['month'])


# Starting with Predicting Trip length with our features

#Convert duration from seconds to minutes
df['duration_min'] = df['duration'] / 60

# Keep trips between 1 minute and 240 minutes or 4 hours
df = df[(df['duration_min'] >= 1) & (df['duration_min'] <= 240)]

#For safe measures, dropping everything below 0
df = df[df['duration'] >= 0]

from sklearn.model_selection import train_test_split

X = df.drop(['duration', 'seq_id', 'hubway_id', 'start_date', 'end_date', 'birth_date'], axis=1)
y = df['duration']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Now we can train and test the model

