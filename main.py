import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df_2017 = pd.read_excel("2017_disposal_rates_muni.xlsx")
#COLUMN NAMES: 'COUNTY', 'MUNICIPALITY', 'POPULATION', 'GENERATION', 'DISPOSAL Total', 'RECYCLING', 'Recycled %'
#weighing the data
df_2017["Weighted Recycling Rate"] = (df_2017["Recycled %"] * 100 * df_2017["POPULATION"]) / df_2017["POPULATION"].sum()
X = df_2017[["POPULATION"]]
y = df_2017["Weighted Recycling Rate"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize and fit the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Model evaluation
print(f"Intercept: {model.intercept_}")
print(f"Coefficient: {model.coef_[0]}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
print(f"R² Score: {r2_score(y_test, y_pred)}")

plt.scatter(X, y, label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.xlabel("POPULATION")
plt.ylabel("Weighted Recycling Rate")
plt.legend()
plt.title("2017 Regression Analysis")
plt.show()

