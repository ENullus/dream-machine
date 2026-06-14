"""
STEP 1: Create Social Complexity Score using PCA
================================================

This script takes 5 variables related to social complexity and combines them
into a single "complexity score" using Principal Component Analysis (PCA).
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the data
print("Loading dataset...")
df = pd.read_csv('MASTER_DATASET.csv', index_col=0)
print(f"Dataset loaded: {len(df)} societies, {len(df.columns)} variables\n")

# Define the complexity variables
complexity_vars = [
    'EA033',  # Jurisdictional hierarchy (0-4)
    'EA066',  # Class differentiation (0-5)
    'EA030',  # Settlement patterns (1-8, nomadic to urban)
    'EA028',  # Agriculture intensity (0-9)
    'EA039'   # Plow cultivation (0-2)
]

print("=" * 60)
print("COMPLEXITY VARIABLES SELECTED:")
print("=" * 60)
for var in complexity_vars:
    print(f"  {var}")
print()

# Extract these variables and remove rows with missing data
print("Extracting variables and removing missing data...")
complexity_data = df[complexity_vars].copy()
print(f"  Before: {len(complexity_data)} societies")

# Drop rows with any missing values
complexity_data_clean = complexity_data.dropna()
print(f"  After removing missing data: {len(complexity_data_clean)} societies")
print(f"  Data completeness: {len(complexity_data_clean)/len(complexity_data)*100:.1f}%\n")

# Show what the raw data looks like
print("=" * 60)
print("SAMPLE OF RAW DATA (first 10 societies):")
print("=" * 60)
print(complexity_data_clean.head(10))
print()

# Standardize the data (important for PCA!)
# This makes all variables have mean=0 and std=1
print("Standardizing variables (scaling to mean=0, std=1)...")
scaler = StandardScaler()
complexity_scaled = scaler.fit_transform(complexity_data_clean)
print("  ✓ Standardization complete\n")

# Apply PCA
print("=" * 60)
print("APPLYING PCA:")
print("=" * 60)
pca = PCA()
complexity_pca = pca.fit_transform(complexity_scaled)

# Show how much variance each component explains
print("\nVariance explained by each component:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"  PC{i+1}: {var*100:.2f}%")
print(f"\nTotal variance explained by PC1: {pca.explained_variance_ratio_[0]*100:.2f}%")

# Extract PC1 as the complexity score
complexity_score = complexity_pca[:, 0]

# Add it back to the dataframe
df_with_complexity = complexity_data_clean.copy()
df_with_complexity['complexity_score'] = complexity_score

print("\n" + "=" * 60)
print("COMPLEXITY SCORES CREATED!")
print("=" * 60)
print("\nSample societies with their complexity scores:")
print(df_with_complexity[['EA033', 'EA066', 'EA030', 'EA028', 'EA039', 'complexity_score']].head(10))
print()

# Show statistics
print("=" * 60)
print("COMPLEXITY SCORE STATISTICS:")
print("=" * 60)
print(f"  Mean: {complexity_score.mean():.3f}")
print(f"  Std Dev: {complexity_score.std():.3f}")
print(f"  Min: {complexity_score.min():.3f}")
print(f"  Max: {complexity_score.max():.3f}")
print()

# Find most and least complex societies
most_complex_idx = complexity_score.argmax()
least_complex_idx = complexity_score.argmin()

most_complex_society = df_with_complexity.iloc[most_complex_idx]
least_complex_society = df_with_complexity.iloc[least_complex_idx]

print("=" * 60)
print("MOST COMPLEX SOCIETY:")
print("=" * 60)
print(f"  Index: {df_with_complexity.index[most_complex_idx]}")
print(f"  Complexity Score: {complexity_score[most_complex_idx]:.3f}")
print(f"  Hierarchy (EA033): {most_complex_society['EA033']}")
print(f"  Class (EA066): {most_complex_society['EA066']}")
print(f"  Settlement (EA030): {most_complex_society['EA030']}")
print(f"  Agriculture (EA028): {most_complex_society['EA028']}")
print(f"  Plow (EA039): {most_complex_society['EA039']}")
print()

print("=" * 60)
print("LEAST COMPLEX SOCIETY:")
print("=" * 60)
print(f"  Index: {df_with_complexity.index[least_complex_idx]}")
print(f"  Complexity Score: {complexity_score[least_complex_idx]:.3f}")
print(f"  Hierarchy (EA033): {least_complex_society['EA033']}")
print(f"  Class (EA066): {least_complex_society['EA066']}")
print(f"  Settlement (EA030): {least_complex_society['EA030']}")
print(f"  Agriculture (EA028): {least_complex_society['EA028']}")
print(f"  Plow (EA039): {least_complex_society['EA039']}")
print()

# Show PCA loadings (which variables matter most)
print("=" * 60)
print("PCA LOADINGS (Which variables contribute most to complexity?):")
print("=" * 60)
loadings = pd.DataFrame(
    pca.components_[0],
    index=complexity_vars,
    columns=['PC1_Loading']
).sort_values('PC1_Loading', ascending=False)
print(loadings)
print("\nPositive = higher values increase complexity")
print("Negative = higher values decrease complexity")
print()

# Save the results
output_file = 'complexity_scores.csv'
df_with_complexity.to_csv(output_file)
print("=" * 60)
print(f"✓ Results saved to: {output_file}")
print("=" * 60)
print(f"\nYou now have {len(df_with_complexity)} societies with complexity scores!")
print("\nNext step: Use these complexity scores to train a predictive model!")
