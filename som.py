# encoding: utf-8

import functions
import plot_functions
import math
from clusters import Cluster

class SOM:
    list_points_Knowledge = []
    InitialClustersList = []
    number_of_clusters = 5
    LearnRestrictor = 1
    clustersList = []
    MaxStep = 1
    listObjetcCluster = []
    t = 1

    def __init__(self,number_of_clus,LearnRe,data_fi,MaxSt):
        #data_file_txt = open("data_r2.txt", "r")
        data_file_txt = open(data_fi, "r")
        self.list_points_Knowledge = functions.load_from_txt(data_file_txt)
        self.number_of_clusters = number_of_clus
        self.LearnRestrictor = LearnRe
        self.MaxStep = MaxSt

    def start(self):
        self.clustersList = functions.generate_random_list(self.number_of_clusters)
        self.InitialClustersList = self.clustersList.copy()
        c=0
        while(c < len(self.clustersList)):
            self.listObjetcCluster.append(Cluster(c))
            c=c+1
        
        while( self.t <= self.MaxStep):
            #print(f"========================[ITERACION: {self.t}]========================")
            self.LearnRestrictor=1/self.t
            #for each known point in the data list
            for point in self.list_points_Knowledge:
                #get the winning centroid
                winning_centroid = functions.closest_weight(point,self.clustersList)
                i=0
                while(i < len(self.clustersList)):
                    #find the value of the neighborhood
                    vecinity_value = functions.vicinityImpactFunction(winning_centroid,self.clustersList[i])
                    #if not the winning centroid
                    if (self.clustersList[i] != winning_centroid):
                     #I update the cluster with respect to the winning cluster
                        self.clustersList[i] = functions.update_weight(self.clustersList[i] ,winning_centroid, vecinity_value, self.LearnRestrictor)
                        #print(f"\t=>[✗ FUNC VECINDAD PARA PERDEDORA: {round(vecinity_value,2)}]")
                    else:
                        #else I update the cluster with respect to the point
                        self.clustersList[i] = functions.update_weight(self.clustersList[i] ,point, vecinity_value , self.LearnRestrictor)
                        nombreCluster=i
                        self.listObjetcCluster=functions.checkListPoint(self.listObjetcCluster,nombreCluster, point)
                        #print(f"\t=>[★ FUNC VECINDAD PARA GANADORA:  {vecinity_value} ]")
                    #increment the while
                    i=i+1
            #show iteration
            #print("iteracion ", self.t)
            plot_functions.plot_r2(self.listObjetcCluster,self.clustersList,self.t)
            #increment the while of the iteration
            self.t+=1
        #end algorithm


    
    