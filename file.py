data_file_txt = open("dataSet03.txt", "r") 

list_points_Knowledge = []
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
    print (f"# Vector added to knowledge list: [{naturalvector}] #")
    list_points_Knowledge.append(naturalvector)
print("##############################################\n")

#close the .txt file
data_file_txt.close()