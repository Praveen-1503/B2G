import streamlit as st
from src.agents.mediator import MediatorAgent

class NegotiationEngine:
    def __init__(self, minister, cfo, max_rounds=5):
        """
        Orchestrates the bargaining loop between local AI agents.
        """
        self.minister = minister
        self.cfo = cfo
        self.mediator = MediatorAgent() # The conflict resolver
        self.max_rounds = max_rounds
        self.history = []

    def run_simulation(self):
        """
        Executes the Strategic Friction Engine loop.
        """
        # Step 1: CFO opens with an 'Anchored' corporate offer
        current_offer = "I propose a standard technology licensing agreement for $500,000 per year."
        self.history.append(f"CFO: {current_offer}")
        st.chat_message("user", avatar="💼").write(f"**CFO Initial Offer:** {current_offer}")

        for round_num in range(self.max_rounds):
            st.write(f"---")
            st.write(f"### 🔄 Negotiation Round {round_num + 1}")

            # Step 2: Minister counters based on Debt-Neutrality
            minister_response = self.minister.negotiate(current_offer, self.history)
            self.history.append(f"Minister: {minister_response}")
            st.chat_message("assistant", avatar="🏛️").write(minister_response)

            # Check for Agreement Convergence (must be explicit acceptance)
            acceptance_phrases = ["i accept", "we accept", "i agree to", "we agree to", "deal is done", "[ACCEPT]"]
            if any(phrase in minister_response.lower() for phrase in acceptance_phrases):
                st.success("🤝 A Debt-Neutral Agreement has been reached!")
                return self.history

            # Step 3: Mediator Intervention (The Novelty Piece)
            if round_num == 2: # Intervene at Round 3 to break the deadlock
                st.warning("⚖️ Mediator is intervening to resolve the deadlock...")
                mediator_suggestion = self.mediator.intervene(
                    self.history, 
                    self.minister.profile['assets_to_trade'],
                    self.minister.profile['critical_gap']
                )
                self.history.append(f"Mediator: {mediator_suggestion}")
                st.chat_message("mediator", avatar="⚖️").write(mediator_suggestion)
                current_offer = mediator_suggestion # Force the CFO to respond to the swap

            # Step 4: CFO counter-offers based on Business Utility
            cfo_response = self.cfo.negotiate(
                current_offer if round_num == 2 else minister_response, 
                self.history, 
                self.minister.profile['region'],
                self.minister.profile['critical_gap'],
                self.minister.profile['assets_to_trade']
            )
            self.history.append(f"CFO: {cfo_response}")
            st.chat_message("user", avatar="💼").write(cfo_response)

            # Update for next turn
            current_offer = cfo_response

            # Check for explicit acceptance from CFO
            acceptance_phrases = ["i accept", "we accept", "i agree to", "we agree to", "deal is done", "[ACCEPT]"]
            if any(phrase in cfo_response.lower() for phrase in acceptance_phrases):
                st.success("🤝 Corporate HQ has approved the resource swap!")
                return self.history

        st.error("⚠️ Deadlock: No debt-neutral agreement found within 5 rounds.")
        return self.history