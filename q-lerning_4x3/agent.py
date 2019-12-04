# model.py
from mesa import Agent, Model
import random
import pandas as pd
import numpy as np

class   IntelligentAgent(Agent):
    conjunto_s = range(0,11,1)
    conjunto_a = ['cima', 'baixo', 'direita', 'esquerda']

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.n_sa = pd.DataFrame(np.zeros((self.conjunto_s, self.conjunto_a)))
        self.q_sa = pd.DataFrame(np.zeros((self.conjunto_s, self.conjunto_a)))
        self.estado = None
        self.recompensa = None
        self.acao = None
        
    def step(self):
        self.move()
    
    def move(self):
        if (self.estado == 7): #-1
            self.q_sa.iloc[self.estado, acao] = -1 
            return
        elif(self.estado == 11): #-1
            self.q_sa.iloc[self.estado, acao] = 1
            return

        acao_escolhida = self.aprendizagemQ()

        

    def aprendizagemQ(self):
        #incrementar N sa [s, a]
        self.n_sa.iloc[self.estado, self.acao] =  self.n_sa.iloc[self.estado, self.acao] + 1
        #Q[s, a] ← Q[s, a] + α(N sa [s, a])(r + γ max a′ Q[s′, a′]
        self.q_sa.iloc[self.estado, self.acao] =  self.q_sa.iloc[self.estado, self.acao] + 
                                                  ((self.model.alpha * self.n_sa.iloc[self.estado, self.acao]) * (self.recompensa + self.model.gama))
        #s, a, r ← s′, argmax a′ , f(Q [s′, a′], N sa [s′, a′]), r′
        self.estado = 
        return self.acao