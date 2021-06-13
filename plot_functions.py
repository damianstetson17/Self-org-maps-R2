# encoding: utf-8
# importar todas las funciones de pylab
from time import *
from pylab import *
from clusters import Cluster
import matplotlib.pyplot as plt

def plot_r2(listObjetcCluster, clustersList,t):
    plt.subplot(1, 2, 1)
    plt.ion()
    #clean the axes
    plt.cla()
    #plot atributes
    title("SOM (Iteración: " + str(t) + ")")
    xlabel('Eje X')
    ylabel('Eje Y')
 
    for i in listObjetcCluster:
        ArrayPoints= i.getListaPoint()
        xArrayPoints = [point[0] for point in ArrayPoints]
        yArrayPoints=[point[1] for point in ArrayPoints]
        scatter(xArrayPoints,yArrayPoints, s=50)

    xArrayCentroide = [point[0] for point in clustersList]
    yArrayCentroide=[point[1] for point in clustersList]
    #scatter(xArrayCentroide,yArrayCentroide, s=50,label='Centroides', marker="d") 
    for x,y in zip (xArrayCentroide,yArrayCentroide):
        label = f"({round(x,2)},{round(y,2)})"
        plt.plot(x,y,'kD',ms=8, mec='w',mew=2)
        plt.annotate(label,(x,y))
    plt.draw()
    #wait before "update" the plot
    plt.pause(0.001)