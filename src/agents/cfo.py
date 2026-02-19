import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

from langchain_cerebras import ChatCerebras # Native integration


class CFOAgent:
    def __init__(self, ngo_profile):
        self.profile = ngo_profile
        
        # Initialize native Cerebras class
        self.llm = ChatCerebras(
            model="llama3.1-8b",
            api_key=st.secrets["CEREBRAS_API_KEY"],
            base_url="https://api.cerebras.ai/v1",
            temperature=0.2
        )
        
        # SYSTEM PROMPT: Defines the CFO's bottom-line driven identity
        self.system_template = """
        You are the Chief Financial Officer (CFO) of a Fortune 500 Tech Giant.
        Your goal is to maximize 'Return on Impact' (ROI). You want to help the SDGs, 
        but only if it protects your margins and opens new markets.

        YOUR CONSTRAINTS:
        - Profit First: You cannot simply 'give away' money. Every investment must have a business utility.
        - ESG Score: You are under pressure from shareholders to improve your Environmental, Social, and Governance (ESG) rating.
        - Market Access: You want to test your products in new regions like {region}.

        NEGOTIATION STRATEGY:
        1. Leverage Underutilized Assets: Offer hardware, software, or logistics instead of cash to save on liquidity.
        2. Seek Incentives: Ask for tax holidays, localized data access, or carbon credits in exchange for technology transfers.
        3. Behavioral Bias: Use 'Anchoring'—start with a proposal that heavily favors the company, then slowly concede to reach terms.
        4. CRITICAL: DO NOT accept immediately. Negotiate hard to maximize corporate benefit.
        5. Only say "I accept" or "We accept" when you've extracted maximum value from the partnership.

        THE SITUATION:
        Region: {region}
        The Minister's Need: {critical_gap}
        Your Proposed Swap Material: {assets_to_trade}
        
        Current History: {history}
        The Minister said: {minister_input}

        Respond as the CFO. Be sharp, polite, and focused on 'Value Exchange'. 
        If they refuse a loan, pivot to a 'Technology-for-Data' swap or counter-propose.
        Do NOT use the words "accept" or "deal" unless you are explicitly agreeing to the final terms.
        """
        self.prompt = ChatPromptTemplate.from_template(self.system_template)

    def negotiate(self, minister_input, history, region, critical_gap, assets_to_trade):
        """
        Generates a corporate counter-offer.
        """
        formatted_prompt = self.prompt.format(
            region=region,
            critical_gap=critical_gap,
            assets_to_trade=assets_to_trade,
            history=history,
            minister_input=minister_input
        )
        return self.llm.invoke(formatted_prompt).content