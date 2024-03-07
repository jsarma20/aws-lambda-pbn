import base64
from subprocess import run
from pathlib import Path
from .imageEncoding import encodeFileToPost, decodePostToImageFile
import os

CURRENT_DIR = os.path.dirname(__file__)


def generate_canvas(inputImage:str, nColors:int = 5, outputDir:str='bin/') -> dict:
    executable =  os.path.join(CURRENT_DIR,'bin','PBN')
    outputDir = os.path.join(CURRENT_DIR,outputDir)
    output = run([executable, inputImage,str(nColors), outputDir])
    success = output.returncode == 0
    if not success:
        return {'status':1,
                'error':'Failed to generate canvas'
                }
    canvas = encodeFileToPost(os.path.join(CURRENT_DIR,outputDir,'canvas.jpeg'))
    painting = encodeFileToPost(os.path.join(CURRENT_DIR,outputDir,'painting.jpeg'))
    colorPallet = encodeFileToPost(os.path.join(CURRENT_DIR,outputDir,'colorPallet.jpeg'))

    return {
        'status':0,
        'canvas':canvas,
        'painting':painting,
        'colorPallet':colorPallet,
        'format':'jpeg'
    }



def get_pbn(request:dict):
    n = request.get('nColors')
    encodedImg = request.get('image')
    
    extension = request.get('format')

    inputFile = "temp.{0}".format(extension)
    inputFile = os.path.join(os.path.dirname(__file__),'bin',inputFile)
    
    decodePostToImageFile(encodedImg,inputFile)
    
    canvas_resp = generate_canvas(inputFile,n)
    return canvas_resp

    

    