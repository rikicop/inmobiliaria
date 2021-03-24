from django.shortcuts import render, get_object_or_404
from .models import Inmueble,InmuebleImage
import pandas as pd
import json 

def inmueble_view(request):
    items = Inmueble.objects.all()
    inmuebles = Inmueble.objects.all()
    df= pd.DataFrame(list(Inmueble.objects.all().values()))
    json_records = df.reset_index().to_json(orient ='records')
    data = []

    data = json.loads(json_records) 
    context = {'d': data} 
    print(context)

    if request.method =="POST":
        
        tipo_form = request.POST['tipof']
        ubicacion_form = request.POST['ubicacionf']
        edo_form = request.POST['edof']

        items = Inmueble.objects.all()
        df= pd.DataFrame(list(Inmueble.objects.all().values()))
        print(df)
        #inmuebles = Inmueble.objects.all()
        if (tipo_form != '') and (ubicacion_form != '') and (edo_form != ''): 
            newdf = df.loc[((df.tipo == tipo_form) & (df.ubicacion == ubicacion_form) & (df.edo == edo_form))]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 
            

        elif (tipo_form != '') and (ubicacion_form != '') and (edo_form == ''): 
            newdf = df.loc[((df.tipo == tipo_form) & (df.ubicacion == ubicacion_form))]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 

        elif (tipo_form != '') and (ubicacion_form == '') and (edo_form == ''): 
            newdf = df.loc[df.tipo == tipo_form]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 

        elif (tipo_form == '') and (ubicacion_form != '') and (edo_form == ''): 
            newdf = df.loc[df.ubicacion == ubicacion_form]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 

        elif (tipo_form == '') and (ubicacion_form != '') and (edo_form != ''):
            newdf = df.loc[((df.ubicacion == ubicacion_form) & (df.edo == edo_form))]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 

        elif (tipo_form != '') and (ubicacion_form == '') and (edo_form != ''): 
            newdf = df.loc[((df.tipo == tipo_form) & (df.edo == edo_form))]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 

        elif (tipo_form == '') and (ubicacion_form == '') and (edo_form != ''): 
            newdf = df.loc[df.edo == edo_form]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 
        #return render(request, 'inmueble.html', {'inmuebles':inmuebles})
        return render(request, 'inmueble.html', context)
    
    else:

        return render(request, 'inmueble.html', context)
    
    return render(request, 'inmueble.html', context)

def detalle_view(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    #Va a filtrar un inmueble en particular
    fotos = InmuebleImage.objects.filter(inmueble=inmueble)
    return render(request, 'detalle.html', {
        'inmueble':inmueble,
        'fotos':fotos
    })