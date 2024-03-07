
from .service import pbn

def create_pbn(request):
    canvas = pbn.get_pbn(request)
    return canvas

def handler(event, context):
    image = event.get('image','')
    if image == '':
        return {
            'status':401,
            'message':"invalid image"
                }
    image = create_pbn(image)
    return {
            'status':200,
            'message':image
                }
