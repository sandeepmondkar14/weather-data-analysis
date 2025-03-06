# weather-data-analysis

## Project Overview
This project applies **K-Means Clustering** and **Regression Analysis** on weather data collected from OpenWeatherMap for **17 Canadian cities**. The goal is to identify distinct weather patterns through clustering and predict temperature using regression.

- **K-Means Clustering** is applied on **real-time weather data** to segment cities based on temperature, humidity, pressure, and wind speed.
- **Regression Analysis** is performed using a **combined dataset (real-time, historical, and forecasted data)** to predict temperature based on other weather factors.
This project applies **K-Means Clustering** on real-time weather data collected from OpenWeatherMap for **17 Canadian cities**. The goal is to identify distinct weather patterns based on key meteorological features such as **temperature, humidity, pressure, and wind speed**.

## Dataset
The dataset consists of real-time weather data for 17 Canadian cities, including:
- **Temperature (°C)**
- **Feels-like Temperature (°C)**
- **Humidity (%)**
- **Pressure (hPa)**
- **Wind Speed (m/s)**

### Data Availability
- **Pre-fetched CSV files**: The dataset provided was generated on **March 6, 2025, at 12:56 PM**.
- **Live Data Fetching**: Users who want **real-time weather data** can use the included **Python scripts** to fetch data from OpenWeatherMap API.
- **File Paths**: Ensure that the paths in the Jupyter Notebook (`.ipynb`) and the destination paths in the Python scripts are correctly set.

## Methodology

### Clustering (K-Means)
1. **Data Preprocessing**
   - Missing values are handled.
   - Categorical city names are encoded.
   - Numerical features are standardized using **StandardScaler**.

2. **Finding Optimal Clusters**
   - **Elbow Method**: Determines the best `K` value by analyzing SSE (Sum of Squared Errors).
   - **Silhouette Score**: Evaluates cluster cohesion and separation.

3. **Applying K-Means Clustering**
   - The optimal number of clusters (`K=4`) is used to segment cities into distinct weather groups.

4. **Visualization & Analysis**
   - Scatter plots of **Temperature vs Humidity** illustrate the cluster distribution.
   - The cluster summary provides insights into weather conditions for each group.

### Regression Analysis
1. **Data Combination**
   - Unlike clustering, the regression analysis uses a **combined dataset** from all four CSV files (real-time, historical, 24-hour forecast, and 14-day forecast).

2. **Feature Selection**
   - Target Variable: **Temperature (°C)**
   - Predictor Variables: **Humidity, Pressure, Wind Speed, and Feels-like Temperature**

3. **Model Selection & Training**
   - A **linear regression model** is used to predict temperature based on the other weather factors.
   - The dataset is split into **training and testing sets** to evaluate model performance.

4. **Evaluation Metrics**
   - **Mean Absolute Error (MAE)**
   - **Root Mean Squared Error (RMSE)**
   - **R² Score** to measure model accuracy.

5. **Insights**
   - The model helps understand how different weather conditions impact temperature.
   - Feature importance analysis provides insights into which variables have the strongest influence on temperature predictions.
1. **Data Preprocessing**
   - Missing values are handled.
   - Categorical city names are encoded.
   - Numerical features are standardized using **StandardScaler**.

2. **Finding Optimal Clusters**
   - **Elbow Method**: Determines the best `K` value by analyzing SSE (Sum of Squared Errors).
   - **Silhouette Score**: Evaluates cluster cohesion and separation.

3. **Applying K-Means Clustering**
   - The optimal number of clusters (`K=4`) is used to segment cities into distinct weather groups.

4. **Visualization & Analysis**
   - Scatter plots of **Temperature vs Humidity** illustrate the cluster distribution.
   - The cluster summary provides insights into weather conditions for each group.

## Results
### Clustering Results
The clustering process identified four distinct weather patterns among Canadian cities:

- **Cluster 0**: Cities with moderate temperatures (~2.6°C), mild wind speeds (~4.1 m/s), and stable atmospheric pressure.
- **Cluster 1**: Cities with warmer temperatures (~6.4°C), high wind speeds (~7.7 m/s), and lower pressure, indicating possible stormy conditions.
- **Cluster 2**: Cold regions (~-8.5°C), very low wind chills (~-15.1°C), and high pressure, characteristic of stable cold climates.
- **Cluster 3**: A unique cluster (Toronto), characterized by cold temperatures (~-3.1°C) but significantly higher wind speeds (~12.5 m/s), likely influenced by local urban effects.

### Regression Analysis Results
The regression analysis, using a combined dataset from real-time, historical, and forecasted data, provided the following insights:

- **Model Performance:**
  - Mean Absolute Error (MAE): Measures the average absolute error between predicted and actual temperatures.
  - Root Mean Squared Error (RMSE): Indicates the standard deviation of prediction errors.
  - R² Score: Determines how well the independent variables explain temperature variations.

- **Key Findings:**
  - **Humidity and pressure** had the strongest correlation with temperature changes.
  - **Wind speed** had a moderate impact but varied across different cities.
  - The model performed well in predicting short-term temperature trends but showed reduced accuracy for long-range forecasts due to external weather influences.

These results suggest that temperature predictions can be improved by incorporating additional features such as wind direction and cloud cover.
The clustering process identified four distinct weather patterns among Canadian cities:

- **Cluster 0**: Cities with moderate temperatures (~2.6°C), mild wind speeds (~4.1 m/s), and stable atmospheric pressure.
- **Cluster 1**: Cities with warmer temperatures (~6.4°C), high wind speeds (~7.7 m/s), and lower pressure, indicating possible stormy conditions.
- **Cluster 2**: Cold regions (~-8.5°C), very low wind chills (~-15.1°C), and high pressure, characteristic of stable cold climates.
- **Cluster 3**: A unique cluster (Toronto), characterized by cold temperatures (~-3.1°C) but significantly higher wind speeds (~12.5 m/s), likely influenced by local urban effects.

## Installation & Usage
### Option 1: Use Provided CSV Files
Users can directly use the **pre-fetched CSV files** for analysis.

### Option 2: Fetch Live Data from API
Users who want **real-time weather data** can run the provided **Python scripts** to fetch and generate new CSV files. Simply copy and run the scripts in any Python environment, ensuring the correct file paths are set.

### Running the Analysis
### Running Clustering
To run the clustering analysis, install the required dependencies and execute the script:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python weather_clustering.py
```

### Running Regression Analysis
To run the regression analysis using the combined dataset, execute:
```bash
python weather_regression.py
```
Ensure that all CSV files are available and correctly referenced in the script.
To run the clustering analysis, install the required dependencies and execute the script:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python weather_clustering.py
```

## Future Improvements
- Incorporate additional weather parameters such as **wind direction and precipitation**.
- Use **Geospatial Data** (latitude/longitude) to analyze regional influences.
- Compare K-Means results with other clustering algorithms like **DBSCAN or Hierarchical Clustering**.

## Author
[Sandeep Mondkar](https://github.com/sandeepmondkar14)

