import requests
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 1: JSON Data Collection
def fetch_stock_data(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full"
    response = requests.get(url)
    data = response.json()
    return data

# Step 2: Data Preprocessing
def preprocess_data(data):
    time_series = data['Time Series (Daily)']
    closing_prices = [float(entry['4. close']) for entry in time_series.values()]
    sma_values = [sum(closing_prices[i-5:i]) / 5 for i in range(5, len(closing_prices))]
    return sma_values

# Step 3: Model Selection
def select_model():
    return LinearRegression()

# Step 4: Training and Validation
def train_model(model, X, y):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    return model, X_val, y_val

# Step 5: Model Evaluation and Refinement
def evaluate_model(model, X_val, y_val):
    score = model.score(X_val, y_val)
    return score

# Step 6: Pattern Identification and Prediction
def predict_sma(model, latest_prices):
    next_sma = model.predict([latest_prices])[0]
    return next_sma

# Example Usage:
api_key = 'NGQKTSLQAF79PJFV'
symbol = 'IMB'

# Step 1: JSON Data Collection
data = fetch_stock_data(symbol, api_key)

# Step 2: Data Preprocessing
sma_values = preprocess_data(data)

# Step 3: Model Selection
model = select_model()

# Step 4: Training and Validation
X = [[sma_values[i]] for i in range(len(sma_values) - 1)]  # Use current SMA as feature
y = sma_values[1:]  # Predict next SMA
model, X_val, y_val = train_model(model, X, y)

# Step 5: Model Evaluation and Refinement
score = evaluate_model(model, X_val, y_val)
print("Model Score:", score)

# Step 6: Pattern Identification and Prediction
latest_prices = [sma_values[-5:]]  # Use last 5 SMA values as input
next_sma = predict_sma(model, latest_prices)
print("Predicted Next SMA:", next_sma)
