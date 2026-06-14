"""
STEP 3: Variational Autoencoder (VAE) for Society Generation
=============================================================

This script trains a VAE to generate entirely new, plausible societies.

Unlike the Random Forest (which predicts), the VAE can:
- Generate random societies from scratch
- Interpolate between two real societies
- Explore the latent space of all possible societies
"""

import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import pickle
import matplotlib.pyplot as plt
from vae_postprocessor import fix_vae_output

print("=" * 70)
print("STEP 3: TRAINING VAE FOR SOCIETY GENERATION")
print("=" * 70)
print()

# Set random seeds for reproducibility
torch.manual_seed(42)
np.random.seed(42)

# Check if GPU available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")
print()

# Load the dataset
print("Loading dataset...")
df = pd.read_csv('MASTER_DATASET.csv', index_col=0)
print(f"✓ Loaded {len(df)} societies with {len(df.columns)} variables")
print()

# Remove rows with too many missing values (keep if >50% complete)
threshold = len(df.columns) * 0.5
df_clean = df.dropna(thresh=threshold)
print(f"After removing sparse rows: {len(df_clean)} societies")
print()

# Fill remaining NaNs with column means (for continuous) or mode (for categorical)
print("Handling missing values...")
for col in df_clean.columns:
    if df_clean[col].isna().sum() > 0:
        # Use median for numerical columns
        if df_clean[col].dtype in ['float64', 'int64']:
            df_clean[col].fillna(df_clean[col].median(), inplace=True)
        else:
            df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)

print(f"✓ Dataset is now complete with {len(df_clean)} societies")
print()

# Preserve column order for post-processing and saving
column_names = df_clean.columns.tolist()

# Standardize the data
print("Standardizing features...")
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df_clean)
print("✓ Data standardized")
print()

# Convert to torch tensors
data_tensor = torch.FloatTensor(data_scaled)

# Split into train/test
train_data, test_data = train_test_split(data_tensor, test_size=0.2, random_state=42)
print(f"Split: {len(train_data)} training, {len(test_data)} test")
print()

# Create DataLoaders
batch_size = 32
train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)

# VAE Architecture
class VAE(nn.Module):
    def __init__(self, input_dim, latent_dim=20):
        super(VAE, self).__init__()
        
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
        )
        
        # Latent space
        self.fc_mu = nn.Linear(64, latent_dim)
        self.fc_logvar = nn.Linear(64, latent_dim)
        
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, input_dim)
        )
        
    def encode(self, x):
        h = self.encoder(x)
        mu = self.fc_mu(h)
        logvar = self.fc_logvar(h)
        return mu, logvar
    
    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std
    
    def decode(self, z):
        return self.decoder(z)
    
    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        recon = self.decode(z)
        return recon, mu, logvar

# Loss function
def vae_loss(recon_x, x, mu, logvar, beta=1.0):
    # Reconstruction loss (MSE)
    recon_loss = nn.MSELoss(reduction='sum')(recon_x, x)
    
    # KL divergence loss
    kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    
    return recon_loss + beta * kl_loss

# Initialize model
input_dim = data_scaled.shape[1]
latent_dim = 20  # The number of "essence dials"

print("=" * 70)
print("VAE ARCHITECTURE:")
print("=" * 70)
print(f"  Input dimension: {input_dim} (all society variables)")
print(f"  Latent dimension: {latent_dim} (compressed 'essence' dials)")
print(f"  Hidden layers: 128 → 64 → {latent_dim} → 64 → 128 → {input_dim}")
print()

model = VAE(input_dim, latent_dim).to(device)
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training
print("=" * 70)
print("TRAINING VAE...")
print("=" * 70)
print("This will take a few minutes...")
print()

num_epochs = 100
train_losses = []
test_losses = []

for epoch in range(num_epochs):
    # Training
    model.train()
    train_loss = 0
    for batch in train_loader:
        batch = batch.to(device)
        optimizer.zero_grad()
        
        recon, mu, logvar = model(batch)
        loss = vae_loss(recon, batch, mu, logvar)
        
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
    
    train_loss /= len(train_loader.dataset)
    train_losses.append(train_loss)
    
    # Testing
    model.eval()
    test_loss = 0
    with torch.no_grad():
        for batch in test_loader:
            batch = batch.to(device)
            recon, mu, logvar = model(batch)
            loss = vae_loss(recon, batch, mu, logvar)
            test_loss += loss.item()
    
    test_loss /= len(test_loader.dataset)
    test_losses.append(test_loss)
    
    # Print progress every 10 epochs
    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1}/{num_epochs} - Train Loss: {train_loss:.4f}, Test Loss: {test_loss:.4f}")

print()
print("✓ Training complete!")
print()

# Save the model
print("=" * 70)
print("SAVING MODEL...")
print("=" * 70)

torch.save(model.state_dict(), 'dream_machine_vae.pth')
print("✓ VAE model saved to: dream_machine_vae.pth")

with open('vae_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
print("✓ Scaler saved to: vae_scaler.pkl")

with open('vae_columns.pkl', 'wb') as f:
    pickle.dump(column_names, f)
print("✓ Column names saved to: vae_columns.pkl")

print()

# Generate example societies
print("=" * 70)
print("GENERATING EXAMPLE SOCIETIES:")
print("=" * 70)
print()

model.eval()
with torch.no_grad():
    # Generate 3 random societies
    for i in range(3):
        print(f"GENERATED SOCIETY #{i+1}")
        print("-" * 50)
        
        # Sample from latent space
        z = torch.randn(1, latent_dim).to(device)
        
        # Decode to get society
        generated = model.decode(z).cpu().numpy()
        
        # Inverse transform to original scale
        generated_society = scaler.inverse_transform(generated)[0]
        
        # Post-process to ensure valid values
        fixed_society = fix_vae_output(generated_society, column_names=column_names)
        
        # Show first 10 variables
        for j, col in enumerate(column_names[:10]):
            print(f"  {col}: {fixed_society[j]:.2f}")
        print("  ...")
        print()

print("=" * 70)
print("VAE READY!")
print("=" * 70)
print()
print("Your generative Dream Machine is trained!")
print()
print("WHAT YOU CAN DO NOW:")
print("  1. Generate random societies from noise")
print("  2. Interpolate between two real societies")
print("  3. Explore the latent space with sliders")
print("  4. Create step4_generate_societies.py for easy generation")
print()
print("Files created:")
print("  - dream_machine_vae.pth (trained VAE)")
print("  - vae_scaler.pkl (for scaling)")
print("  - vae_columns.pkl (variable names)")
print()
