import mesa
import time

class LLMAgent(mesa.Agent):
    """A base agent simulating an LLM API call delay."""
    def __init__(self, unique_id, model, role):
        super().__init__(unique_id, model)
        self.role = role

    def step(self):
        print(f"[{self.role} {self.unique_id}] is thinking...")
        start_time = time.time()
        
        # This sleep simulates the synchronous block of waiting for OpenAI/Gemini
        # In your actual proposal, this is where the LangChain API call goes
        time.sleep(2.5) 
        
        end_time = time.time()
        latency = end_time - start_time
        print(f"[{self.role} {self.unique_id}] responded in {latency:.2f} seconds.")

class NegotiationModel(mesa.Model):
    def __init__(self):
        super().__init__()
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.MultiGrid(10, 10, True)

        # Create Buyer
        buyer = LLMAgent(1, self, "Buyer")
        self.schedule.add(buyer)
        self.grid.place_agent(buyer, (2, 5))

        # Create Seller
        seller = LLMAgent(2, self, "Seller")
        self.schedule.add(seller)
        self.grid.place_agent(seller, (7, 5))

    def step(self):
        print("\n--- New Negotiation Turn ---")
        self.schedule.step()