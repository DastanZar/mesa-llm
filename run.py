from model import NegotiationModel
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 0.8}
    if agent.role == "Buyer":
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    return portrayal

# Create a 10x10 grid, 500x500 pixels
grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

server = ModularServer(NegotiationModel,
                       [grid],
                       "LLM Agent Market",
                       {})

server.port = 8765

if __name__ == "__main__":
    server.launch()