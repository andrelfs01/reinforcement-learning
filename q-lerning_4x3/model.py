from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import Grid
from mesa.datacollection import DataCollector
from model import IntelligentAgent

class NMModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height, positions):
        self.running = True
        self.num_agents = N
        self.grid = Grid(width, height, False)
        self.schedule = RandomActivation(self)

        # Create Agent
        for i in range(self.num_agents):
            a = IntelligentAgent("t_"+str(i), self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            self.grid.place_agent(a, positions[i])

        self.datacollector = DataCollector(
            agent_reporters={"TotalReward": "reward"})  # An agent attribute

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)