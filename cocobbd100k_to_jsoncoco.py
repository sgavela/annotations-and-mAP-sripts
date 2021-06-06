import json
import sys


def leer_annotations(path_to_json):
    with open(path_to_json) as file:
        data_in=json.load(file)
    
    ann_out=[]    
    for ann in  data_in['annotations']:
        aux_dict = {
            'category_id': ann['category_id'], 
            'id': ann['id'], 
            'image_id': ann['image_id'],
            'area': ann['area'],
            'segmentation': [],
            'bbox': ann['bbox'],
            'iscrowd': ann['iscrowd']
        }
        ann_out.append(aux_dict)
    
    img_out=[] 
    for img in data_in['images']:
        aux_dict = {
            'id': img['id'],
            'license': 1,
            'file_name': img['file_name'], 
            'height': img['height'],
            'width': img['width'],
            'date_captured': "26/04/2021"
        }
        img_out.append(aux_dict)
    
    licenses_list = [{
            "id": 1,
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
            "name": "Public Domain"
        }]
    
    data_out={
        'info': {
            "year": "2020",
            "version": "1",
            "description": "Exported from bdd",
            "contributor": "Sergi",
            "url": "",
            "date_created": "2000-01-01T00:00:00+00:00"
        },
        'licenses': licenses_list,
        'categories': data_in['categories'],
        'images': img_out, 
        'annotations':ann_out
    }
                        
    return data_out

if(len(sys.argv) == 2):
    data_out = leer_annotations(sys.argv[1])
    with open(sys.argv[1].replace(".json", "_parsed.json"), 'w') as file:
        json.dump(data_out, file, indent=4)
else:
    print("Introducir la ruta del archivo .json como argumento")


