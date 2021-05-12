
class Cluster:
    def __init__(self,elnombre):
        self.nombre=elnombre
        self.list_group_points = []
        #print("soy el cluster  ", self.nombre)

    def setPoint(self,point):
            self.list_group_points.append(point)       
            #print("soy el cluster ",self.nombre, "agregue el punto ",point," a mi lista ", self.list_group_points )

    def getNombre(self):
        nombre =self.nombre
        return nombre

    def getListaPoint(self):
        listaPoint= self.list_group_points
        #print("soy el cluster mis puntos son  ", self.nombre, self.list_group_points )
        return listaPoint
    
    def setListaPoint(self):
        self.list_group_points= []
        
    def removPoint(self, point):
        #print(" soy el cluster", self.nombre,"tengo el punto ",point ," mi lista   antes ", self.list_group_points)
        self.list_group_points.remove(point)
        #print(" soy el cluster", self.nombre," mi lista   despues ", self.list_group_points)
    
    
