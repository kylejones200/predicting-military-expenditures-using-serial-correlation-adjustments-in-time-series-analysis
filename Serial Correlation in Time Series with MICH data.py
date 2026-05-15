"""Generated from Jupyter notebook: Serial Correlation in Time Series with MICH data

Magics and shell lines are commented out. Run with a normal Python interpreter."""


# --- code cell ---

https://fred.stlouisfed.org/series/MICH


# --- code cell ---

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.graphics.tsaplots as tsaplots
from statsmodels.stats.diagnostic import acorr_breusch_godfrey
from statsmodels.regression.linear_model import GLS, GLSAR
from datetime import datetime
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from visualization import plot_time_series, plot_decomposition

# Function to fetch data from FRED
def get_fred_data(series_id, start_date="2000-01-01", end_date=None):
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
    df = web.DataReader(series_id, 'fred', start_date, end_date)
    return df.dropna()

# Fetch University of Michigan Consumer Sentiment Index (MICH)
series_id = "MICH"
mich_data = get_fred_data(series_id)
mich_data = mich_data.pct_change().dropna()  # Convert to percentage change

# Prepare DataFrame
mich_data = mich_data.rename(columns={series_id: "MICH"})
mich_data["Date"] = mich_data.index  # Ensure a date column for plotting

# Create lagged MICH values
for lag in range(1, 3):  # Include 2 lags
    mich_data[f"MICH_lag{lag}"] = mich_data["MICH"].shift(lag)

# Drop missing values due to lagging
mich_data.dropna(inplace=True)

# Define independent and dependent variables
X_lags = ["MICH", "MICH_lag1", "MICH_lag2"]
X_matrix = sm.add_constant(mich_data[X_lags])  # Add intercept
y_vector = mich_data["MICH"]  # Target is MICH itself (can be changed)

# Fit a distributed lag model
model = sm.OLS(y_vector, X_matrix).fit()

# Perform the Breusch-Godfrey test for serial correlation
bg_test = acorr_breusch_godfrey(model, nlags=2)
print(f"Breusch-Godfrey Test p-value: {bg_test[1]:.4f}")

# Generalized Least Squares (GLS)
gls_model = GLS(y_vector, X_matrix).fit()
print(gls_model.summary())

# Cochrane-Orcutt Method
cochrane_orcutt = GLSAR(y_vector, X_matrix, rho=1).iterative_fit()
print(cochrane_orcutt.summary())

# Newey-West Standard Errors
model_robust = model.get_robustcov_results(cov_type="HAC", maxlags=2)
print(model_robust.summary())

# Visualizing Serial Correlation
residuals = model.resid
plt.figure(figsize=(10, 5))
tsaplots.plot_acf(residuals, lags=20, alpha=0.05)
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.title("Autocorrelation of Residuals")
plt.savefig("residual_acf.png")
plt.show()

# Visualizing MICH Data
time_column = "Date"
value_columns = ["MICH", "MICH_lag1", "MICH_lag2"]
plot_time_series(mich_data, time_column, value_columns, title="MICH Time Series")

# Perform and plot decomposition
plot_decomposition(mich_data["MICH"], model="additive", title="MICH Decomposition")


# --- code cell ---

print(model.summary())


# --- code cell ---

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.dates as mdates
from pandas_datareader import data as web
from datetime import datetime

# Function to fetch data from FRED
def get_fred_data(series_id, start_date="2000-01-01", end_date=None):
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
    df = web.DataReader(series_id, 'fred', start_date, end_date)
    return df.dropna()

# Fetch University of Michigan Consumer Sentiment Index (MICH)
series_id = "MICH"
mich_data = get_fred_data(series_id)
mich_data = mich_data.pct_change().dropna()  # Convert to percentage change

# Prepare DataFrame
mich_data = mich_data.rename(columns={series_id: "MICH"})
mich_data["Date"] = mich_data.index  # Ensure a date column for plotting

# Perform decomposition on the data
decomposition = seasonal_decompose(mich_data["MICH"], model="additive", period=10)

# Create an animation of the decomposition
fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

def update_plot(i):
    # Clear the axes
    for ax in axes:
        ax.clear()

    # Plot the data incrementally
    axes[0].plot(mich_data["Date"][:i], mich_data["MICH"][:i], label="Original", color='black')
    axes[0].set_title("Original Series")

    axes[1].plot(mich_data["Date"][:i], decomposition.trend[:i], label="Trend", color='black')
    axes[1].set_title("Trend")

    axes[2].plot(mich_data["Date"][:i], decomposition.resid[:i], label="Residual", color='black')
    axes[2].set_title("Residual")

    # Set axis limits and labels
    for ax in axes:
        ax.set_xlim(mich_data["Date"].min(), mich_data["Date"].max())
        ax.xaxis.set_major_locator(mdates.YearLocator(10))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_position(('outward', 5))
        ax.spines['bottom'].set_position(('outward', 5))
        

    plt.tight_layout()

# Create an animation
ani = animation.FuncAnimation(fig, update_plot, frames=len(mich_data), interval=100, repeat=False)

# Save the animation as a GIF
gif_path = "mich_decomposition_animation.gif"
ani.save(gif_path, writer="pillow", fps=10)

print(f"GIF saved at {gif_path}")


# --- code cell ---

"""
initial version
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.diagnostic import acorr_breusch_godfrey
# Set seed for reproducibility
np.random.seed(42)
# Generate independent variable (advertising spend)
n = 100
X = np.random.rand(n) * 100  # Advertising spend in $1000s
# Generate serially correlated errors using an AR(1) process
rho = 0.6  # Level of serial correlation
errors = np.zeros(n)
errors[0] = np.random.randn()
for t in range(1, n):
    errors[t] = rho * errors[t - 1] + np.random.randn()
# Generate dependent variable (sales) with lag effects and correlated errors
beta = [0.5, 0.3, 0.1]
Y = np.zeros(n)
for t in range(2, n):
    Y[t] = beta[0] * X[t] + beta[1] * X[t-1] + beta[2] * X[t-2] + errors[t]
# Convert to DataFrame
data = pd.DataFrame({"Y": Y, "X": X})
for lag in range(1, 3):
    data[f"X_lag{lag}"] = data["X"].shift(lag)
# Drop missing values due to lagging
data.dropna(inplace=True)
# Fit a distributed lag model
X_lags = ["X", "X_lag1", "X_lag2"]
X_matrix = sm.add_constant(data[X_lags])
y_vector = data["Y"]
model = sm.OLS(y_vector, X_matrix).fit()
# Perform the Breusch-Godfrey test for serial correlation
bg_test = acorr_breusch_godfrey(model, nlags=2)
print(f"Breusch-Godfrey Test p-value: {bg_test[1]:.4f}")
# If p-value < 0.05, serial correlation is present.
If the p-value < 0.05, we reject the null hypothesis of no serial correlation, indicating that our model suffers from autocorrelation.
4. Addressing Serial Correlation
If serial correlation is detected, there are several ways to correct it:
1. Generalized Least Squares (GLS)
GLS modifies OLS by accounting for the structure of the serial correlation:
from statsmodels.regression.linear_model import GLS
gls_model = GLS(y_vector, X_matrix).fit()
print(gls_model.summary())
2. Cochrane-Orcutt Method
This iterative procedure transforms the regression model to eliminate serial correlation.
from statsmodels.regression.linear_model import GLSAR
cochrane_orcutt = GLSAR(y_vector, X_matrix, rho=1).iterative_fit()
print(cochrane_orcutt.summary())
3. Newey-West Standard Errors
If correcting the model structure is not feasible, robust standard errors (Newey-West) provide valid inference.
model_robust = model.get_robustcov_results(cov_type="HAC", maxlags=2)
print(model_robust.summary())
5. Visualizing Serial Correlation
To diagnose serial correlation, we can plot the Autocorrelation Function (ACF) of the residuals.
import statsmodels.graphics.tsaplots as tsaplots
# Extract residuals
residuals = model.resid
# Plot ACF
plt.figure(figsize=(10, 5))
tsaplots.plot_acf(residuals, lags=20, alpha=0.05)
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.title("Autocorrelation of Residuals")
plt.savefig("/mnt/data/residual_acf.png")
plt.show()
