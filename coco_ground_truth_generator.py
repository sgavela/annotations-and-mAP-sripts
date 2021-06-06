#labels bdd
'''
LABEL_MAP = {
    0: "pedestrian",
    1: "rider",
    2: "car",
    3: "truck",
    4: "bus",
    5: "train",
    6: "motorcycle",
    7: "bicycle",
    8: "traffic-light",
    9: "traffic-sign",
}
'''
#labels coco
LABEL_MAP = {
    0: "pedestrian",
    1: "bicycle",
    2: "car",
    3: "motorcycle",
    5: "bus",
    7: "truck",
    9: "traffic-light",  
}

path_in = "C:/Users/Sergio Gil/Desktop/yolov4_tensorflow/data/dataset/val2017.txt"

contenido= list()

path_out = "C:/Users/Sergio Gil/Desktop/proces/ground-truth-coco"
i = 0
with open(path_in, 'r') as archivo:
   for linea in archivo:
       text_out = ""
       columnas = linea.split(" ")
       for columna in columnas[1:]:
           objeto = columna.split(",")
           if int(objeto[4]) in LABEL_MAP:
               text_out += LABEL_MAP[int(objeto[4])] + " "
               text_out += objeto[0] + " "
               text_out += objeto[1] + " "
               text_out += objeto[2] + " "
               text_out += objeto[3] + " "
               text_out += '\n'
       
           
       with open(path_out + "/" + str(i) + ".txt", 'w') as f:
           f.write(text_out)
       i += 1
       print(i)


