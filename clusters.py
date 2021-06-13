import functions

class Cluster:
    def __init__(self,elnombre,pos):
        self.nombre=elnombre
        self.pos = pos
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
        
    def getSumAllEuc(self):
        sum_euc = 0
        for point in self.list_group_points:
            sum_euc = sum_euc + functions.euc_distance(point,self.pos)
        #print(f"W({self.nombre}) sumeuc => {sum_euc}")
        return sum_euc
