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

        '''
        Prints the requested data on a terminal. 
        Possible inputs are: \'ID\', \'radious\', \'position\', \'velocity\', \'aceleration\', \'mass\', \'charge\'.
        '''

        if      data == 'ID':           print(self.ID)
        elif    data == 'radious':      print(self.radius)
        elif    data == 'position':     print(self.position)
        elif    data == 'velocity':     print(self.velocity)
        elif    data == 'aceleration':  print(self.aceleration)
        elif    data == 'mass':         print(self.mass)
        elif    data == 'charge':       print(self.charge)
        else:                           print('Valid inputs are: ID, radious, position, velocity, aceleration, mass, charge.')