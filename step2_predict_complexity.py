"""
STEP 2: Predictive Model - Random Forest
=========================================

This script trains a Random Forest model to predict social complexity
from input variables like subsistence patterns, climate, and kinship.

This is your "Dream Machine" - adjust the dials, predict the outcome!
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pickle

print("=" * 70)
print("STEP 2: TRAINING PREDICTIVE MODEL")
print("=" * 70)
print()

# Load the complexity scores from Step 1
print("Loading complexity scores from Step 1...")
df = pd.read_csv('complexity_scores.csv', index_col=0)
print(f"✓ Loaded {len(df)} societies with complexity scores\n")

# Load the full dataset to get additional variables
print("Loading full dataset for input variables...")
df_full = pd.read_csv('MASTER_DATASET.csv', index_col=0)
print(f"✓ Loaded {len(df_full)} societies with {len(df_full.columns)} variables\n")

# Merge complexity scores with full dataset
df_merged = df_full.join(df['complexity_score'], how='inner')
print(f"✓ Merged datasets: {len(df_merged)} societies ready for modeling\n")

# Define INPUT variables (the "dials" you can adjust)
input_vars = [
    # Subsistence (what % of food comes from each source)
    'EA001',  # Gathering
    'EA002',  # Hunting
    'EA003',  # Fishing
    'EA004',  # Animal husbandry
    'EA005',  # Agriculture
    
    # Environment
    'AnnualMeanTemperature',
    'MonthlyMeanPrecipitation',
    'TemperatureConstancy',
    
    # Kinship & Social Structure
    'EA043',  # Descent type (patrilineal, matrilineal, etc.)
    'EA009',  # Marital residence (where couples live)
    'EA012',  # Cousin marriages
    
    # Technology & Economic
    'EA042',  # Dominant subsistence activity
    'EA070',  # Slavery
    'EA028',  # Agriculture intensity
    'EA030',  # Settlement pattern
    'EA033',  # Political hierarchy
]

print("=" * 70)
print("INPUT VARIABLES (Your 'Dials'):")
print("=" * 70)
for var in input_vars:
    print(f"  {var}")
print()

# Prepare the data
print("Preparing training data...")
X = df_merged[input_vars].copy()
y = df_merged['complexity_score'].copy()

# Remove rows with missing values
valid_idx = X.dropna().index
X = X.loc[valid_idx]
y = y.loc[valid_idx]

print(f"✓ Training data ready: {len(X)} societies")
print(f"  (Removed {len(df_merged) - len(X)} societies due to missing values)")
print()

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Split into training/testing:")
print(f"  Training: {len(X_train)} societies")
print(f"  Testing: {len(X_test)} societies")
print()

# Train the Random Forest model
print("=" * 70)
print("TRAINING RANDOM FOREST MODEL...")
print("=" * 70)
print("This may take a moment...")

model = RandomForestRegressor(
    n_estimators=100,      # Number of trees
    max_depth=10,          # Prevent overfitting
    min_samples_split=10,  # Minimum samples to split
    random_state=42,
    n_jobs=-1              # Use all CPU cores
)

model.fit(X_train, y_train)
print("✓ Model trained!\n")

# Evaluate the model
print("=" * 70)
print("MODEL PERFORMANCE:")
print("=" * 70)

# Predictions on test set
y_pred = model.predict(X_test)

# Calculate metrics
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"  R² Score: {r2:.3f}")
print(f"  RMSE: {rmse:.3f}")
print()

# Cross-validation score
cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
print(f"  Cross-validation R² (5-fold): {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
print()

# Feature importance - which variables matter most!
print("=" * 70)
print("FEATURE IMPORTANCE (Which dials matter most?):")
print("=" * 70)

importance_df = pd.DataFrame({
    'Variable': input_vars,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)

print(importance_df.to_string(index=False))
print()

# Show top 3 most important variables
top3 = importance_df.head(3)
print("TOP 3 MOST IMPORTANT VARIABLES:")
for idx, row in top3.iterrows():
    print(f"  {idx+1}. {row['Variable']}: {row['Importance']:.3f}")
print()

# Save the model
print("=" * 70)
print("SAVING MODEL...")
print("=" * 70)

with open('dream_machine_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("✓ Model saved to: dream_machine_model.pkl")
print()

# Save the input variable names (needed for predictions later)
with open('input_vars.pkl', 'wb') as f:
    pickle.dump(input_vars, f)
print("✓ Input variables saved to: input_vars.pkl")
print()

# TESTING THE MODEL - Example predictions
print("=" * 70)
print("TESTING THE MODEL - Example Societies:")
print("=" * 70)
print()

# Example 1: Hunter-gatherer society
print("EXAMPLE 1: Hunter-Gatherer Society")
print("-" * 50)
test1 = pd.DataFrame([{
    'EA001': 4,  # 40% gathering
    'EA002': 5,  # 50% hunting
    'EA003': 1,  # 10% fishing
    'EA004': 0,  # No herding
    'EA005': 0,  # No agriculture
    'AnnualMeanTemperature': 20,
    'MonthlyMeanPrecipitation': 50,
    'TemperatureConstancy': 5,
    'EA043': 3,  # Bilateral descent
    'EA009': 1,  # Patrilocal residence
    'EA012': 1,  # No cousin marriage
    'EA042': 1,  # Hunting is dominant
    'EA070': 1,  # No slavery
    'EA028': 0,  # No intensive agriculture
    'EA030': 1,  # Nomadic
    'EA033': 0,  # No political hierarchy
}])

pred1 = model.predict(test1)[0]
print(f"Predicted Complexity: {pred1:.3f}")
print(f"Interpretation: {'Low' if pred1 < -1 else 'Medium-Low' if pred1 < 0 else 'Medium' if pred1 < 1 else 'High'}")
print()

# Example 2: Agricultural society
print("EXAMPLE 2: Agricultural Society")
print("-" * 50)
test2 = pd.DataFrame([{
    'EA001': 1,  # 10% gathering
    'EA002': 1,  # 10% hunting
    'EA003': 0,  # No fishing
    'EA004': 0,  # No herding
    'EA005': 8,  # 80% agriculture
    'AnnualMeanTemperature': 25,
    'MonthlyMeanPrecipitation': 100,
    'TemperatureConstancy': 8,
    'EA043': 1,  # Patrilineal descent
    'EA009': 1,  # Patrilocal residence
    'EA012': 2,  # Cousin marriage present
    'EA042': 4,  # Agriculture is dominant
    'EA070': 2,  # Slavery present
    'EA028': 6,  # Intensive agriculture
    'EA030': 6,  # Compact settlements
    'EA033': 3,  # Multiple hierarchy levels
}])

pred2 = model.predict(test2)[0]
print(f"Predicted Complexity: {pred2:.3f}")
print(f"Interpretation: {'Low' if pred2 < -1 else 'Medium-Low' if pred2 < 0 else 'Medium' if pred2 < 1 else 'High'}")
print()

# Example 3: Pastoral society
print("EXAMPLE 3: Pastoral Herding Society")
print("-" * 50)
test3 = pd.DataFrame([{
    'EA001': 2,  # 20% gathering
    'EA002': 1,  # 10% hunting
    'EA003': 0,  # No fishing
    'EA004': 6,  # 60% herding
    'EA005': 1,  # 10% agriculture
    'AnnualMeanTemperature': 15,
    'MonthlyMeanPrecipitation': 30,
    'TemperatureConstancy': 4,
    'EA043': 1,  # Patrilineal descent
    'EA009': 1,  # Patrilocal residence
    'EA012': 1,  # No cousin marriage
    'EA042': 3,  # Herding is dominant
    'EA070': 1,  # No slavery
    'EA028': 2,  # Some agriculture
    'EA030': 2,  # Semi-nomadic
    'EA033': 1,  # Local leadership only
}])

pred3 = model.predict(test3)[0]
print(f"Predicted Complexity: {pred3:.3f}")
print(f"Interpretation: {'Low' if pred3 < -1 else 'Medium-Low' if pred3 < 0 else 'Medium' if pred3 < 1 else 'High'}")
print()

print("=" * 70)
print("MODEL READY!")
print("=" * 70)
print()
print("Your Dream Machine is trained and ready to use!")
print()
print("NEXT STEPS:")
print("  1. Modify the test examples above with your own values")
print("  2. Run the script again to see new predictions")
print("  3. Or create step3_test_dream_machine.py for interactive testing")
print()
print("Files created:")
print("  - dream_machine_model.pkl (trained model)")
print("  - input_vars.pkl (variable names)")
print()