import math
import random
from clusters import Cluster
from math import e

#encoding: utf-8

#return a list of vectors from the .txt
def load_from_txt(data_file_txt):
    #create a list
    list_points_Knowledge = []
    print("\n##############################################")
    print("# Loading data from txt:\t\t     #")
    
    for data in data_file_txt.readlines():
        vectorString = ""
        for caracter in enumerate(data[0:],1):
            if(caracter[1] == ","):
                vectorString+=" " 
            else:
                vectorString+=caracter[1]
        vector = vectorString.split()
        naturalvector=[]
        naturalvector.append(float(vector[0]))
        naturalvector.append(float(vector[1]))
        print (f" Vector added to knowledge list: [{naturalvector}]")
        list_points_Knowledge.append(naturalvector)
    data_file_txt.close()
    return list_points_Knowledge 

def give_random_values():
    return random.random()

#return a list of generated random numbers based on number_of_clusters
def generate_random_list(number_of_clusters):
    clustersList = []
    for i in range(number_of_clusters):
      clustersList.append([give_random_values(),give_random_values()])
    show_random_generated(clustersList)
    return clustersList

#show the random values generated from generate_random_list()
def show_random_generated(clustersList):
    print("\n#########################################################")
    print("# Showing the random values added:")
    for r in clustersList:
        print("# Cluster vector added to clusters_List: ",r)
    print("#########################################################\n")
    
#check if the point is already in a list of another centroid
def checkListPoint(listObjetcCluster,clusterAppend,point):
    for cluster in listObjetcCluster:
        listita= cluster.getListaPoint()
        if (point in listita):
            cluster.removPoint(point)
    for cluster in listObjetcCluster:
        if(cluster.getNombre()==clusterAppend):
            cluster.setPoint(point)
    return listObjetcCluster

#return a euclidian distance from two points
def euc_distance(point, weightToCalcule): 
    result = (math.sqrt((point[0]-weightToCalcule[0])**2+(point[1]-weightToCalcule[1])**2))
    return result

#return the closest centroide according to a point
def closest_weight(point, centroides):
    #define a empty list witch save the results of euclidean results evaluating the point and the centroides(list)
    allResultsEuclidean = []
    #for any centroide calculate the euclidean distance
    for w in centroides:
        #print("calculating eucliden distance of", w , " = ", euc_distance(point,w)," and added to list of results")
        allResultsEuclidean.append(euc_distance(point,w))
    #catching the index of the min result in allResultsEuclidean list (this tells us which element of the list of centroids is the minimum)
    indexOfClosest = allResultsEuclidean.index(min(allResultsEuclidean))
    #returning the centroide in the index of min result in allResultsEuclidean
    return (centroides[indexOfClosest])

#return the value from evaluate the function
def vicinityImpactFunction(centroideWeightWinner,centroideToUpdate):
    #function of the mexican hat
    result = (math.exp((-0.5)*(math.sqrt(euc_distance(centroideToUpdate,centroideWeightWinner))/0.5)**2))
    return result

#return the centroide updated with the new values
def update_weight(centroide, pointKnow, vecinityFuncValue,LearnRestrictor):
    #apply the formula for update weights
    weight_x = (centroide[0])+float(vecinityFuncValue)*float(LearnRestrictor)*float(pointKnow[0]-centroide[0])
    weight_y = (centroide[1])+float(vecinityFuncValue)*float(LearnRestrictor)*float(pointKnow[1]-centroide[1])
    centroide_weight_Updated = (weight_x,weight_y)
    return centroide_weight_Updated
