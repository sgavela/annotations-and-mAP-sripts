import json
import os

'''
LABEL_MAP = {
    0: "car",
    1: "bus",
    2: "pedestrian",
    3: "bicycle",
    4: "truck",
    5: "motorcycle",
    6: "train",
    7: "rider",
    8: "traffic-sign",
    9: "traffic-light",
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

IMG_WIDTH = 1280
IMG_HEIGHT = 720


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

label_path = "C:/Users/Sergio Gil/Desktop/proces/archivos json inferidos por darknet/result_yolov3_bdd.json"
output_path = "C:/Users/Sergio Gil/Desktop/proces/predicted_yolov3_bdd"
frames = json.load(open(label_path, "r"))
i = 0

for frame in frames:
    out_text = ""
    for objeto in frame['objects']:
        if int(objeto['class_id']) in LABEL_MAP:
            out_text += LABEL_MAP[objeto['class_id']] + " "
            out_text += str(objeto['confidence']) + " "
            
            coord = objeto['relative_coordinates']      
            box2d = yolo_to_box2d(coord['center_x'], coord['center_y'], 
                                  coord['width'], coord['height'])
            out_text += str(round(box2d['x1'],2)) + " "
            out_text += str(round(box2d['y1'],2)) + " "
            out_text += str(round(box2d['x2'],2)) + " "
            out_text += str(round(box2d['y2'],2)) + " "
            out_text += '\n'

    with open(output_path + "/" + str(i) + ".txt","w") as f:
        f.write(out_text)
    i = i + 1
    





