import pandas as pd
import streamlit as st

def load_ngo_data(file_path="data/ngo_details.csv"):
    """
    Loads the NGO dataset and prepares it for the negotiation agents.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error("NGO dataset not found. Please ensure the CSV is in the /data folder.")
        return None

def get_negotiation_profile(df, ngo_name):
    """
    Extracts a specific NGO's data and formats it as a 
    'Strategic Brief' for the AI Agents.
    """
    ngo_data = df[df['NGO_Name'] == ngo_name].iloc[0]
    
    # This dictionary feeds directly into your Agent System Prompts
    profile = {
        "identity": ngo_data['NGO_Name'],
        "region": ngo_data['Region_Focus'],
        "mission": ngo_data['Primary_SDG'],
        "assets_to_trade": ngo_data['Data_Assets'], # The "Swap" material
        "critical_gap": ngo_data['Infrastructure_Gap'], # The "Ask"
        "debt_limit": ngo_data['Debt_Sensitivity'], # The "Red Line"
        "willingness_to_compromise": ngo_data['ZOPA_Flexibility'] # The "Behavior"
    }
    return profile

def filter_ngos(df, region=None, sdg=None):
    """
    Filters the 1000-row dataset to find the best match for a specific simulation.
    """
    filtered_df = df
    if region:
        filtered_df = filtered_df[filtered_df['Region_Focus'] == region]
    if sdg:
        filtered_df = filtered_df[filtered_df['Primary_SDG'] == sdg]
    return filtered_df