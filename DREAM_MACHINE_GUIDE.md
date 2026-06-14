# 🎛️ SOCIETY DREAM MACHINE - Complete Guide

## 🎉 YOUR DATASET IS READY!

You now have **1,291 societies** with **66 carefully selected variables** - a perfect foundation for your society simulator!

---

## 📊 What You Have

### Master Dataset: `MASTER_DATASET.csv`
- **1,291 societies** from the Ethnographic Atlas
- **66 total variables:**
  - **60 cultural/social variables** (subsistence, politics, kinship, etc.)
  - **6 environmental variables** (climate data)
- **89.3% average completeness** - very clean data!

### Supporting Files:
- `EA_variable_summary.csv` - Full codebook (what each variable means)
- `EA_variable_completeness.csv` - Completeness statistics
- `codes.csv` - What each numeric code means (e.g., 0 = "0-5%", 1 = "6-15%")

---

## 🎛️ Your "Dials" (Input Variables)

### **SUBSISTENCE (8 variables)** - 99.9% complete
- **EA001**: Gathering dependence (0-9 scale: 0-5% to 86-100%)
- **EA002**: Hunting dependence (0-9 scale)
- **EA003**: Fishing dependence (0-9 scale)
- **EA004**: Animal husbandry dependence (0-9 scale)
- **EA005**: Agriculture dependence (0-9 scale)
- **EA028**: Agriculture intensity (0=None, 1=Casual, 2=Extensive, 3=Intensive, 4=Irrigated)
- **EA029**: Major crop type (0=None, 1=Root/tuber, 2=Cereal, 3=Tree fruits)
- **EA042**: Dominant activity (0=Gathering, 1=Hunting, 2=Fishing, 3=Pastoral, 4-7=Agriculture types)

### **POLITICAL (4 variables)** - 70-90% complete
- **EA033**: Jurisdictional hierarchy (0=None to 4=State with 4+ levels)
- **EA070**: Slavery type (0=Absent, 1=Incipient, 2=Reported, 3=Societal)
- **EA071**: Slavery timing (0=Absent, 1=Early contact only, 2=Aboriginal, 3=Post-contact)
- **EA076**: Inheritance rules for movable property

### **SOCIAL STRATIFICATION (5 variables)** - 76-86% complete
- **EA065**: Agricultural specialization by age/occupation
- **EA066**: Class differentiation primary type
- **EA067**: Class differentiation secondary features
- **EA068**: Caste differentiation primary
- **EA069**: Caste differentiation secondary

### **KINSHIP (10 variables)** - 97-99% complete ⭐ Best quality!
- **EA008**: Domestic organization (family structure)
- **EA009**: Marital composition (monogamy vs polygamy)
- **EA010-EA012**: Marital residence patterns
- **EA017**: Largest patrilineal kin group
- **EA018**: Largest patrilineal exogamous group
- **EA019**: Largest matrilineal kin group
- **EA020**: Largest matrilineal exogamous group
- **EA043**: Descent type (patrilineal, matrilineal, bilateral, etc.)

### **SETTLEMENT (3 variables)** - 91-93% complete
- **EA030**: Settlement patterns (nomadic to urban)
- **EA079**: House ground plan
- **EA080**: House floor level

### **TECHNOLOGY (2 variables)** - 72-92% complete
- **EA039**: Plow cultivation (0=None, 1=Aboriginal, 2=Post-contact)
- **EA073**: Hereditary succession

### **ENVIRONMENTAL (6 variables)** - 100% complete ⭐
- **AnnualMeanTemperature**: Mean annual temp (Celsius)
- **MonthlyMeanPrecipitation**: Precipitation (ml/m²/month)
- **PrecipitationPredictability**: How predictable (0-1 scale)
- **TemperaturePredictability**: How predictable (0-1 scale)
- **PrecipitationConstancy**: How constant (0-1 scale)
- **TemperatureConstancy**: How constant (0-1 scale)

---

## 🎯 How to Use This Data

### Phase 1: Predictive Modeling (Start Here!)

**Goal:** Predict "social complexity" from other variables

#### Step 1: Create a Complexity Score
Use **Principal Component Analysis (PCA)** on:
- EA033 (Jurisdictional hierarchy)
- EA066 (Class differentiation)
- EA030 (Settlement patterns)
- EA028 (Agriculture intensity)
- EA039 (Plow cultivation)

This gives you a single "complexity score" (PC1).

#### Step 2: Train a Random Forest
**Inputs (your "dials"):**
- Subsistence variables (EA001-EA005, EA042)
- Environmental variables (all 6)
- Kinship variables (EA043, EA008-EA012)

**Output:**
- Social complexity score (from PCA)

**Result:** You'll get "feature importance" - which dials matter most!

#### Step 3: Build a Neural Network
Same inputs/outputs, but use a feed-forward NN for better predictions.

---

### Phase 2: Generative Modeling (Advanced)

**Goal:** Generate new plausible societies

Use a **Variational Autoencoder (VAE)**:
- **Input:** All 66 variables for all societies
- **VAE learns:** A "latent space" of possible societies
- **Output:** Adjust latent space "dials" → generate new society configurations

This lets you say: "What would a society look like with high agriculture, low hierarchy, and matrilineal descent?"

---

## 📖 Reading the Codes

**Example:** A society has `EA005 = 7.0`

Look up in `codes.csv`:
- var_id: EA005
- code: 7.0
- description: "66 to 75 percent dependence"
- name: "66-75%"

This means: **Agriculture accounts for 66-75% of subsistence**

---

## 🚀 Quick Start Code (Python)

```python
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv('MASTER_DATASET.csv', index_col=0)
codes = pd.read_csv('codes.csv')

# Step 1: Create complexity score via PCA
complexity_vars = ['EA033', 'EA066', 'EA030', 'EA028', 'EA039']
X_complexity = df[complexity_vars].dropna()

pca = PCA(n_components=1)
df.loc[X_complexity.index, 'complexity_score'] = pca.fit_transform(X_complexity)

# Step 2: Define input "dials"
input_vars = [
    'EA001', 'EA002', 'EA003', 'EA004', 'EA005', 'EA042',  # Subsistence
    'EA043', 'EA008', 'EA009',  # Kinship
    'AnnualMeanTemperature', 'MonthlyMeanPrecipitation',  # Environment
    'PrecipitationPredictability', 'TemperaturePredictability'
]

# Step 3: Prepare data
data_complete = df[input_vars + ['complexity_score']].dropna()
X = data_complete[input_vars]
y = data_complete['complexity_score']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Step 5: Get feature importance (which dials matter!)
importance = pd.DataFrame({
    'variable': input_vars,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

print("🎛️ Most Important Dials:")
print(importance)

# Step 6: Make predictions
predictions = rf.predict(X_test)
print(f"\nR² Score: {rf.score(X_test, y_test):.3f}")
```

---

## 🎨 Next Steps

1. **Start with Random Forest** (code above) - easy to interpret
2. **Build a Neural Network** - better predictions
3. **Try a VAE** - generate new societies
4. **Add more variables** - we have 60, experiment!
5. **Create visualizations** - plot complexity vs subsistence types
6. **Build an interactive web app** - let users adjust dials in real-time

---

## 📚 Key Papers to Read

1. **Seshat/D-PLACE papers:** Search "Seshat social complexity" on Google Scholar
2. **Turchin et al.** - Uses this exact approach (PCA + prediction)
3. **"Cultural evolution with neural networks"** - VAE for ethnographic data

---

## 🎉 You're Ready!

Your dream machine dataset is clean, well-structured, and ready for modeling. You have:
- ✅ 1,291 societies
- ✅ 66 high-quality variables  
- ✅ Clear "dials" (inputs) identified
- ✅ Codebooks to interpret results
- ✅ A concrete path forward (RF → NN → VAE)

**Start with the Quick Start code above and build from there!**

This is genuinely an exciting project - you're using real ethnographic data to model human social organization. Have fun! 🚀
