# encoding: utf-8
from tkinter import *
from som import SOM
import tkinter.messagebox

class Main_window:
    root = Tk()
    root.title("Main Menú - SOM (Self-Organizing Map) - Stetson & Piotroski")

    #initial values for start the algorithm
    pathDataSetFile = "Not selected."
    clustersNumber = 5
    MaxStep = 50
    learn = 0.5

    def __init__(self):
        #inputs frame
        frame_inputs = LabelFrame(self.root, text="INITIAL VALUES", padx=50,pady=50)
        frame_inputs.grid(row=1, column=0)

        button_select_data_set = Button(frame_inputs, text = "Select DATA SET .txt file", width=25,
                                        command = lambda: self.setPathFile(label_data_set_path))
        button_select_data_set.pack()

        #clusters scale
        clusters_scale = Scale(frame_inputs, label="Select the number of clusters:", 
                            from_=1, to=10, orient=HORIZONTAL, length=200,
                            command = lambda a: self.setClusterNumber(a,label_clusters))
        clusters_scale.set(self.clustersNumber)
        clusters_scale.pack()

        #maxsteps label and input
        label_maxSteps = Label(frame_inputs, text="Select the number of STEPS: ")
        label_maxSteps.pack()
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.setSteps(sv,label_steps_final))
        entry_maxSteps = Entry(frame_inputs,textvariable=sv, width=25,justify='center')
        #entry_maxSteps.insert(END,self.MaxStep)
        entry_maxSteps.pack()

        #learn input
        label_learn = Label(frame_inputs, text="Select the number of learn restrictor: ")
        label_learn.pack()
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.setLearn(sv,label_learn_restrictor))
        entry_maxLearn = Entry(frame_inputs,textvariable=sv, width=25,justify='center')
        #entry_maxLearn.insert(END,self.learn)
        entry_maxLearn.pack()

        #values setted frame
        frame_values_selected = LabelFrame(self.root, text="SELECTED VALUES", padx=65,pady=71.5)
        frame_values_selected.grid(row=1, column=1)
        #data set path label
        label_data_set_path = Label(frame_values_selected, text="DATA SET path file: "+self.pathDataSetFile)
        label_data_set_path.pack()
        #number clusters label
        label_clusters = Label(frame_values_selected, text="Number of clusters selected: "+str(self.clustersNumber))
        label_clusters.pack()
        #number steps label
        label_steps_final = Label(frame_values_selected, text="Number of steps selected: "+str(self.MaxStep))
        label_steps_final.pack()
        #number learn restrictor
        label_learn_restrictor = Label(frame_values_selected, text="Number of Learn Restrictor: "+str(self.learn))
        label_learn_restrictor.pack()
        #start the SOM algorithm button
        button_start_som = Button(frame_values_selected,text="START SOM ALGORITHM", command=self.startSom)
        button_start_som.pack()

    #som start method
    def startSom(self):
        if self.pathDataSetFile != "Not selected.":
            somi = SOM(int(self.clustersNumber),int(self.learn),self.pathDataSetFile,int(self.MaxStep))
            somi.start()
        else:
            print("NO SE HA SELECCIONADO UN DATASET")
            tkinter.messagebox.showerror('ERROR AL INTENTAR EJECUTAR SOM', 'Primero debe seleccionar un DATASET antes de ejecutar')
            
    #setter methods
    def setPathFile(self,label_data_set_path):
            from tkinter import filedialog
            self.pathDataSetFile = filedialog.askopenfilename(title="Select a data set",
                                                    filetypes = (("text files","*.txt"),("all files","*.*")))
            label_data_set_path.config(text="DATA SET path file: "+self.pathDataSetFile)
            
    def setClusterNumber(self,val,label_clusters):
        self.clustersNumber=val
        print(self.clustersNumber)
        label_clusters.config(text="Number of clusters selected: "+str(self.clustersNumber))
    
    def setSteps(self, sv,label_steps_final):
        try:
            #if is a number and > 0
            if(int(sv.get()) > 0):
                self.MaxStep = int(sv.get())
                label_steps_final.config(
                    text="Number of steps selected: "+str(self.MaxStep))
            print(self.MaxStep)
        except:
            print("Not a number")
    
    def setLearn(self, sv,label_steps_final):
        try:
            #if is a number and > 0
            if(int(sv.get()) > 0):
                self.learn = int(sv.get())
                label_steps_final.config(
                    text="Number of Learn Restrictor selected: "+str(self.learn))
            print(self.learn)
        except:
            print("Not a number")

    #close or display methods
    def display(self):
        self.root.mainloop()
    
    def destroy(self):
        self.root.destroy()