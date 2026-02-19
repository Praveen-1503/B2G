import pandas as pd
import random
import os

# Ensure the data directory exists
if not os.path.exists('data'):
    os.makedirs('data')

def generate_indian_ngo_data(num_rows=1000):
    # Specialized Indian State List
    indian_states = [
        "Tamil Nadu", "Maharashtra", "Karnataka", "Uttar Pradesh", 
        "West Bengal", "Gujarat", "Rajasthan", "Kerala", "Bihar", "Odisha"
    ]
    
    sdgs = ["SDG 4: Quality Education", "SDG 9: Industry & Innovation", "SDG 13: Climate Action", "SDG 17: Partnerships"]
    
    # Localized assets for Debt-Neutral Swaps
    assets = [
        "Vernacular Language Datasets", "Rural Land Records", 
        "Self-Help Group (SHG) Networks", "Localized Crop Yield Data", 
        "Traditional Craft Knowledge"
    ]
    
    # Localized infrastructure gaps
    gaps = [
        "Tier-3 City Cloud Infrastructure", "Last-mile Fiber (BharatNet)", 
        "Vernacular AI Models", "Agri-Tech Sensors", "Smart Village Grids"
    ]

    data = {
        "NGO_Name": [f"Bharat_Impact_NGO_{i:04d}" for i in range(1, num_rows + 1)],
        "Region_Focus": [random.choice(indian_states) for _ in range(num_rows)],
        "Primary_SDG": [random.choice(sdgs) for _ in range(num_rows)],
        "Annual_Budget": [random.randint(50000, 5000000) for _ in range(num_rows)],
        "Data_Assets": [random.choice(assets) for _ in range(num_rows)],
        "Infrastructure_Gap": [random.choice(gaps) for _ in range(num_rows)],
        "Debt_Sensitivity": [random.choice(["High", "Medium", "Low"]) for _ in range(num_rows)],
        "ZOPA_Flexibility": [round(random.uniform(0.1, 0.9), 2) for _ in range(num_rows)]
    }

    df = pd.DataFrame(data)
    df.to_csv("data/ngo_details.csv", index=False)
    print(f"✅ Successfully generated {num_rows} rows of Indian-context data at data/ngo_details.csv")

if __name__ == "__main__":
    generate_indian_ngo_data()