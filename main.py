# need >pip install matplotlib
# encoding: utf-8
import functions
import plot_functions
import math

def main():
  #read the knowledge and save it in to a list of vectors:
  data_file_txt = open("data_r2.txt", "r")
  list_points_Knowledge=functions.load_from_txt(data_file_txt)
  
  #gui parameters
  clustersList = []
  MaxStep=20
  t=1
  LearnRestrictor=0.5
  number_of_clusters= 3

  #generate the clusters
  clustersList = functions.generate_random_list(number_of_clusters)
  listaClusterInicial = clustersList.copy()

  #start algorithm
  while( t <= MaxStep):
    print(f"####################### NUMERO DE ITERACION {t} #######################")
    LearnRestrictor=1/t
    #for each known point in the data list
    #print("la lista de centroides antes de empezar a recorrerla es:", clustersList)
    for point in list_points_Knowledge:
      #get the winning centroid
      #print("la lista de centroides antes de buscar el ganador a recorrerla es:", clustersList)
      winning_centroid = functions.closest_weight(point,clustersList)
      print(f"El centroide mas cercano para el punto {point} es: {winning_centroid}")
      
      print(f"PARA EL CENTROIDE GANADOR {winning_centroid} :")
      i=0

      while(i < len(clustersList)):
        print(f"\t# los valores de los clusters son {clustersList}")
        vecinity_value = functions.vicinityImpactFunction(winning_centroid,clustersList[i])
        if (clustersList[i] != winning_centroid):
          print(f"\t->{clustersList[i]} NO es igual que {winning_centroid}")
          # vecinity_value = functions.vicinityImpactFunction(winning_centroid,clustersList[i])
          #clustersList[i] = functions.update_weight(clustersList[i] ,point, vecinity_value , LearnRestrictor)
          clustersList[i] = functions.update_weight(clustersList[i] ,winning_centroid, vecinity_value , LearnRestrictor)
          plot_functions.plot_r2(list_points_Knowledge,clustersList)
          print(f"\t\t↳el nuevo valor para el centroide es {clustersList[i]}")
        else:
          print(f"\t->{clustersList[i]} es igual que {winning_centroid}")
          clustersList[i] = functions.update_weight(clustersList[i] ,point, vecinity_value , LearnRestrictor)
          print(f"\t\t↳el nuevo valor para el centroide es {clustersList[i]}")
        i=i+1
    t+=1
  #end algorithm
  print("\n\n")
  print(f"####################### FINAL ALGORITMO #######################")
  print(f"\tlos valores iniciales de los clusters son {listaClusterInicial}\n\n")
  print(f"\tlos valores del data set son {list_points_Knowledge}\n\n")
  print(f"\tlos valores finales de los clusters son {clustersList}")
  
if __name__=="__main__":
  main()
  