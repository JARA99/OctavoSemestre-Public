#-----------------------------------------------------------------------------------------#
#---------------------------------------   CLASES   --------------------------------------#
#-----------------------------------------------------------------------------------------#
#   Author: Jorge Alejandro Rodriguez Aldana                                              #
#   Date: 09/2021                                                                         #
#   File: Classes.py                                                                      #
#-----------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------#
#                                        Packages                                         #
#-----------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------#
#                                          Code                                           #
#-----------------------------------------------------------------------------------------#
class Particle:
    def __init__(self,ID,radius,r,v,a,m,q):
        self.ID = ID
        self.radius = radius
        self.position = r
        self.velocity = v
        self.aceleration = a
        self.mass = m
        self.charge = q

    def PrintData(self, data):
        switch = {
            'ID': print(self.ID),
            'radious': print(self.radius),
            'position': print(self.position),
            'velocity': print(self.velocity),
            'aceleration': print(self.aceleration),
            'mass': print(self.mass),
            'charge': print(self.charge)
        }

        return switch.get(data, 'Valid inputs are: ID, radious, position, velocity, aceleration, mass, charge')