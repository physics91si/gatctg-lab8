from particle import Particle
import numpy as np
class Molecule:
    def __init__(self, pos1, pos2, mass1, mass2, k, L0):
        self.k = k
        self.L0 = L0
        self.p1 = Particle(pos1, mass1)
        self.p2 = Particle(pos2, mass2)

    def get_displ1(self):
        return np.array([self.p1.pos[0] - self.p2.pos[0],self.p1.pos[1] - self.p2.pos[1]])
    def get_force(self):
        mag = np.linalg.norm(self.get_displ1())
        unit = self.get_displ1()/mag
        return (unit*self.k*(mag-self.L0)**2)
