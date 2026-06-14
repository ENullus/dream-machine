"""
Test VAE - Generate a Random Society
"""

import torch
import torch.nn as nn
import pickle
import pandas as pd
import numpy as np
from vae_postprocessor import fix_vae_output, validate_fixed_output
from descriptions_mega import generate_full_description

# VAE Architecture (same as training)
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

print("=" * 70)
print("TESTING VAE - GENERATING RANDOM SOCIETIES")
print("=" * 70)
print()

# Load the model
print("Loading VAE model...")
model = VAE(66, 20)
model.load_state_dict(torch.load('dream_machine_vae.pth'))
model.eval()
print("✓ VAE loaded")
print()

# Load scaler
print("Loading scaler...")
with open('vae_scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
print("✓ Scaler loaded")
print()

# Load column names
print("Loading column names...")
with open('vae_columns.pkl', 'rb') as f:
    columns = pickle.load(f)
print(f"✓ {len(columns)} variables loaded")
print()

# Generate 3 random societies
print("=" * 70)
print("GENERATING 3 RANDOM SOCIETIES:")
print("=" * 70)
print()

for i in range(3):
    print(f"GENERATED SOCIETY #{i+1}")
    print("-" * 70)
    
    # Sample random latent vector
    z = torch.randn(1, 20)
    
    # Decode to get society
    with torch.no_grad():
        generated = model.decode(z).numpy()
    
    # Inverse transform to original scale
    society = scaler.inverse_transform(generated)[0]
    
    # Post-process to fix invalid outputs
    raw_dict = dict(zip(columns, society))
    fixed_dict = fix_vae_output(raw_dict)
    
    # Create DataFrame for nice display (drop removed vars)
    display_columns = [col for col in columns if col in fixed_dict]
    society_df = pd.DataFrame({
        'Variable': display_columns,
        'Value': [fixed_dict[col] for col in display_columns]
    })
    
    # Show all 66 variables
    print(society_df.to_string(index=False))
    print()
    print()
    
    # Validate all fixed outputs
    is_valid, errors = validate_fixed_output(fixed_dict)
    print(f"Validation (All variables): {'✓ VALID' if is_valid else '✗ INVALID'}")
    if errors:
        for error in errors:
            print(f"  - {error}")
    print()
    
    # Generate a narrative description
    description = generate_full_description(fixed_dict)
    print("NARRATIVE DESCRIPTION:")
    print(description)
    print()

print("=" * 70)
print("VAE IS WORKING!")
print("=" * 70)
print()
print("You can now:")
print("  1. Generate random societies by adjusting latent vectors")
print("  2. Interpolate between two real societies")
print("  3. Build an interface to control the 20 latent dials")
print()
