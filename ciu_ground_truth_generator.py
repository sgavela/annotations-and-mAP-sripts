import os

#labels ciu
LABEL_MAP = {
    0: "bicycle",
    1: "bus",
    2: "car",
    3: "motorcycle",
    4: "pedestrian",
    5: "traffic-light",
    6: "truck"
}

IMG_WIDTH = 416
IMG_HEIGHT = 416

def yolo_to_box2d(cx, cy, w, h):
    cx = cx * IMG_WIDTH
    cy = cy * IMG_HEIGHT    
    w = w * IMG_WIDTH
    h = h * IMG_HEIGHT
    
    x1 = cx - w/2
    x2 = cx + w/2
    y1 = cy - h/2
    y2 = cy + h/2

    return {'x1': x1, "y1": y1, "x2": x2, "y2": y2}

path_in = "C:/Users/Sergio Gil/Desktop/valid"
path_out = "C:/Users/Sergio Gil/Desktop/proces/ground-truth-ciu"
contenido = os.listdir(path_in)

i = 0
for fichero in contenido:
    if(fichero[-4:] == ".txt"):
        out_text = ""
        with open(path_in + "/" + fichero,'r') as f:
            if(os.stat(path_in + "/" + fichero).st_size != 0):
                for linea in f:
                    columnas = linea.split(" ")
                    out_text += LABEL_MAP[int(columnas[0])] + " "
                    box2d = yolo_to_box2d(float(columnas[1]), float(columnas[2]), 
                                          float(columnas[3]), float(columnas[4]))
                    out_text += str(box2d['x1']) + " "
                    out_text += str(box2d['y1']) + " "
                    out_text += str(box2d['x2']) + " "
                    out_text += str(box2d['y2']) + '\n'
                with open(path_out + "/" + str(i) + ".txt", 'w') as f:
                    f.write(out_text)
                i += 1
                print(i)
