# Aqui voy a hacer un codigo de tal forma que se puedan 
# fucionar las imagenes en un determinado recuadro, con el objetivo
# de tener las imagenes de istmina

#import of function
from gimpfu import *
import os

#function for open the images
def fusion_de_imagenes(directory):
    # The directory variable is where the files are safe
    os.chdir(directory)      #Here we move to the file ubication

    #The objety this code is open 5 to 5 images and save them names in lists
    imagenes=os.listdir()
    for img in imagenes:
        second_capa= pdb.gimp_file_load_layer(image,secon_capa)
        pbd,gimp_image_insert_layer(image,second_capa,None,0)

    pass

register(
    "image_fusion",
    "Aqui voy a haccer un codigo de tal forma que se e pueda fucionar las imagenes en un determinado recuadro con el objetivo de tener las imagenes de istmina",
    "en esta funcion se colocara la direccion de las imagenes de istimna ",
    "Isaac P",
    "Copyright AULA STEM",
    "28/11/2023",
    "<Image>/Filtros/fusion de imagenes",

    [
        (PF_STRING, "directory", "Es la ubicacion donde se encuentran las imagenes en el pc")
    ],
    fusion_de_imagenes)

main()