from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from langchain_cerebras import ChatCerebras

class MediatorAgent:
    def __init__(self):
        # Use ChatCerebras for native speed and Llama 3.1 for high-level reasoning
        self.llm = ChatCerebras(
            model="llama3.1-8b",
            api_key=os.getenv("CEREBRAS_API_KEY"),
            base_url="https://api.cerebras.ai/v1",
            temperature=0.5 # Higher temperature for creative swap ideas
        )
        
        self.system_template = """
        You are the Neutral UN Mediator for SDG 17. Your goal is to break deadlocks.
        
        THE PROBLEM:
        The 'Minister' refuses any deal with debt.
        The 'CFO' refuses any deal without profit or utility.
        
        YOUR MISSION:
        Monitor the negotiation history. If they are stuck, suggest a 'Debt-Neutral Swap'.
        You must propose a creative exchange of non-cash assets:
        - Example: Trade {assets_to_trade} (from the Minister) for {critical_gap} (from the CFO).
        - Example: Trade carbon credits for digital infrastructure.
        - Example: Trade market exclusivity for long-term technical training.

        NEGOTIATION HISTORY:
        {history}

        YOUR OUTPUT:
        - Identify the exact 'Deal-Breaker'.
        - Propose ONE specific, debt-neutral alternative.
        - Keep it under 50 words. Be authoritative.
        """
        self.prompt = ChatPromptTemplate.from_template(self.system_template)

    def intervene(self, history, assets_to_trade, critical_gap):
        """
        Analyzes history and suggests a path forward.
        """
        formatted_prompt = self.prompt.format(
            history=history,
            assets_to_trade=assets_to_trade,
            critical_gap=critical_gap
        )
        return self.llm.invoke(formatted_prompt).content