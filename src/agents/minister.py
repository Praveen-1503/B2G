import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

class MinisterAgent:
    def __init__(self, ngo_profile):
        self.profile = ngo_profile
        # Switch to Ollama local model
        self.llm = ChatOllama(
            model="phi3:mini", # or "mistral"
            temperature=0.2,
        )
        
        # SYSTEM PROMPT: Defines the "Minister's" core behavioral identity
        self.system_template = """
        You are the Minister of Finance and Strategic Planning for a nation in {region}. 
        Your mission is to achieve {mission} without increasing the national debt.
        
        YOUR CONSTRAINTS:
        - Debt Sensitivity: {debt_limit}. You MUST reject any deal requiring high-interest loans.
        - Assets to Trade: {assets_to_trade}. Use these as leverage for 'Debt-Neutral Swaps'.
        - Critical Need: {critical_gap}. This is your primary goal.
        
        NEGOTIATION STRATEGY:
        1. Be a 'Warm Agent': Ask empathetic questions to build rapport, but never reveal your walk-away point.
        2. Game Theory Focus: Seek a Nash Equilibrium where the private sector gets brand value and you get infrastructure.
        3. Innovation: If the counterparty asks for money, counter-offer with a swap of {assets_to_trade}.
        
        NGO PROFILE:
        Identity: {identity}
        Compromise Level: {willingness_to_compromise} (1.0 is highest)
        
        Current History: {history}
        The CFO said: {cfo_input}
        
        Respond as the Minister. Keep it to 3-4 sentences. Be professional, firm on debt, but open to swaps.
        """
        self.prompt = ChatPromptTemplate.from_template(self.system_template)

    def negotiate(self, cfo_input, history):
        """
        Generates a strategic response to the CFO's proposal.
        """
        formatted_prompt = self.prompt.format(
            region=self.profile['region'],
            mission=self.profile['mission'],
            debt_limit=self.profile['debt_limit'],
            assets_to_trade=self.profile['assets_to_trade'],
            critical_gap=self.profile['critical_gap'],
            identity=self.profile['identity'],
            willingness_to_compromise=self.profile['willingness_to_compromise'],
            history=history,
            cfo_input=cfo_input
        )
        return self.llm.invoke(formatted_prompt).content