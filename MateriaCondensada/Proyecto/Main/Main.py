#-----------------------------------------------------------------------------------------#
#----------------------------------------   MAIN   ---------------------------------------#
#-----------------------------------------------------------------------------------------#
#   Author: Jorge Alejandro Rodriguez Aldana                                              #
#   Date: 09/2021                                                                         #
#   File: Main.py                                                                         #
#-----------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------#
#                                        Packages                                         #
#-----------------------------------------------------------------------------------------#

# import numpy as np
import csv as csv
import Classes as cls

#-----------------------------------------------------------------------------------------#
#                                    Global Variables                                     #
#-----------------------------------------------------------------------------------------#

RndFile = 'RndData.csv'

NeutronsList = []
TotalNeutrons = 0

# NeutronsList = [0]*TotalNeutrons

#-----------------------------------------------------------------------------------------#
#                                          Code                                           #
#-----------------------------------------------------------------------------------------#

# p1 = cls.Particle(1,2,[5,2],[5,8],[3,2],7,9)

# p1.PrintAll()



def AsignRnd():

    '''
    Asigna los valores aleatorios a las particulas.
    '''
    global TotalNeutrons

    with open(RndFile, 'r') as Opened_RndFile:
        Readed_RndFile = csv.reader(Opened_RndFile, delimiter=' ')          #Readed_RndFile es la lista generada por csv


        for row in Readed_RndFile:
            TotalNeutrons += 1
            NeutronsList.append(cls.Particle(int(row[0]),float(row[1]),[float(row[2]),float(row[3])],[float(row[4]),float(row[5])],[float(row[6]),float(row[7])],float(row[8]),float(row[9])))
            # NeutronsList[int(row[0])] = cls.Particle(int(row[0]),float(row[1]),[float(row[2]),float(row[3])],[float(row[4]),float(row[5])],[float(row[6]),float(row[7])],float(row[8]),float(row[9]))
            
            # for j in range(10): 
            #     print(row[j])
        # print(Readed_RndFile)

        # for row in Readed_RndFile:
        #     print(row)
        
        # print(TotalNeutrons)
        
    for i in range(TotalNeutrons):
        NeutronsList[i].PrintAll()

AsignRnd()