from calendar import c
from email import message
from itertools import count
import json
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from .models import Cliente
from .models import Credito
from .models import Lineas_De_Credito
from .models import Usuario

from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

class ClienteViews(View):
 @method_decorator(csrf_exempt)
 def dispatch(self,request,*args,**kwargs):
      return super().dispatch(request,*args,**kwargs)
 #@login_required
 
 def get(self,request,doc=0):
   
   if doc>0:
     cli=list(Cliente.objects.filter(documento=doc).values())
     print(cli)
     if len(cli)>0:
      clirespuesta=cli[0]
      template_name="consultarcli.html"
      datos={"listadoclientes":cli}
      print("ENCONTRADO")
      return render(request,template_name,datos)
     else:
      datos={"respuesta":"Dato no se encontro"}
      print("ENCONTRADO")
      return render(request,template_name,datos)
   
   else:
    template_name="consultarcli.html"
    cli=Cliente.objects.all()
    datos={'listadoclientes':cli}
   #return JsonResponse (datos)
   return render(request,template_name,datos)

 #@login_required
 def post(self,request,documento=0):
   if documento>0:
      print("RRRRRRRRRRRRRRRRR")
      cli=list(Cliente.objects.filter(documento=documento).values())
      if len(cli)>0:
         print("EEEEEEEEEEEE")
         template_name="modificar.html"
         documento=request.POST["documento"],
         nombre =request.POST["nombre"],
         apellido=request.POST["apellido"],
         correo=request.POST["correo"],
         celular=request.POST["celular"]
         #clie=Cliente.objects.get(documento=doc)  
        
         cli.nombre=['nombre']
         cli.apellido=['apellido']
         cli.correo=['correo']
         cli.celular=['celular']
         cli.save()

         mensaje={"Respuesta":"Datos actualizado"}
      else:
         mensaje={"Respuesta":"Datos no encontrado"}
      #return JsonResponse(mensaje)
      #return render(request,'modificar.html')
      return redirect('/cliente/')
  
      
   else:
    print("ZZZZZZZZZZZZZZZZZZZZZZZ")
    template_name="registrocliente.html"
    #datos=json.loads(request.body)
    Cliente.objects.create(
     documento=request.POST["documento"],
     nombre =request.POST["nombre"],
     apellido=request.POST["apellido"],
     correo=request.POST["correo"],
     celular=request.POST["celular"])
    return redirect('/cliente/')

 def put(self,request,doc):
   cli=list(Cliente.objects.filter(documento=doc).values())
   if len(cli)>0:
     documento=request.POST["documento"],
     nombre =request.POST["nombre"],
     apellido=request.POST["apellido"],
     correo=request.POST["correo"],
     celular=request.POST["celular"]
     clie=Cliente.objects.get(documento=doc)  
     documento=cli
     cli.nombre=['nombre']
     cli.apellido=['apellido']
     cli.correo=['correo']
     cli.celular=['celular']
     cli.save()
     return redirect('/login/cliente')
    # mensaje={"Respuesta":"Datos actualizado"}
  # else:
    #   mensaje={"Respuesta":"Datos no encontrado"}
   #return JsonResponse(mensaje)
   #return render(request,'modificar.html')
   


 def delete(self,request,doc):
      cli=list(Cliente.objects.filter(documento=doc).values())
      if len(cli)>0:
         Cliente.objects.filter(documento=doc).delete()
         mensaje={"Respuesta":"El registro se elimino"}
      else:
          mensaje={"Respuesta":"El registro no se encontro"}
      return JsonResponse (mensaje)

   
class Creditosview(View):
   @method_decorator(csrf_exempt)
   def  dispatch(self,request,*args,**kwargs):
      return super().dispatch(request,*args,**kwargs)

   def get(self,request):
      cre=list(Credito.objects.values())
      if  len(cre)>0:
         datos={"Datos":cre}
        # return JsonResponse(datos)
         return render(request, "gestionc.html",{"clientes":datos})
      else:
         datos={"Mensaje":"Dtaos no encontrador"}
      return JsonResponse(datos)
   
   def post(self,request):
      datos=json.loads(request.body)
      try:
         linea=Lineas_De_Credito.objects.get(codigo=datos["codigo"])
         cli=Cliente.objects.get(documento=datos["documento"])
         cre=Credito.objects.create(codigo_credito=datos["codigo_credito"],fecha=datos["fecha"],montoprestado =datos["montoprestado"],documento=cli,codigo=linea)
         cre.save()
         mensaje={"mensaje":"Guardado"}
       # Credito.objects.create( codigo_credito=datos["codigo_credito"],fecha=datos["fecha"],montoprestado =datos["montoprestado"], documento=datos["documento"],codigol=datos["codigo"])
         return JsonResponse(datos)
      except Cliente.DoesNotExist:
         mensaje={"mensaje":"La linea no existe"}
      except Lineas_De_Credito.DoesNotExist:
         mensaje={"mensaje":"clddddd"}
      return JsonResponse(mensaje)

class UsuarioViews(View):
 @method_decorator(csrf_exempt)
 def dispatch(self,request,*args,**kwargs):
      return super().dispatch(request,*args,**kwargs)

 def get(self,request,doc=0):
   if doc>0:
     cli=list(Usuario.objects.filter(documento=doc).values())
     if len(cli)>0:
      clirespuesta=cli[0]
      datos={"cliente":clirespuesta}
     else:
      datos={"respuesta":"Dato no se encontro"}
   else:
    cli=list(Usuario.objects.values())
    datos={'listadoclientes':cli}
   return JsonResponse (datos)


 def post(self,request):
    datos=json.loads(request.body)
    cli=Cliente.objects.get(documento=datos["documento"])
    Usuario.objects.create(Documento=datos["documento"],nomusuario=datos["nomusuario"],clave=datos["clave"],rol=datos["rol"],documento=cli)
                      
    return JsonResponse(datos)


def loginusuario(request):
      if request.method=='POST':
         try:
            detalleusuario=Usuario.objects.get(nomusuario=request.POST['nomusuario'], clave=request.POST['clave'])
            #detalleusuario=Cliente.objects.get(documento=['documento'], correo=['correo'])
         #   cli=list(Cliente.objects.get(documento=detalleusuario.documento))
            cli=list(Cliente.objects.filter(documento=200).values())
            print(detalleusuario.documento)
           
            datos={"listadoclientes":cli}
            print(datos)
            aaaa=request.POST['nomusuario']
            print("datosssssssssssss", aaaa)
            if detalleusuario.rol=="admin":
               print("wwww", request.session['nomusuario'])
               request.session['nomusuario']=detalleusuario.nomusuario
               request.session['documento']=detalleusuario.documento
               return render(request, 'gestionc.html')
            elif detalleusuario.rol=="empleado":
               request.session['nomusuario']=detalleusuario.nomusuario
               return render(request, 'empleados.html')
            elif detalleusuario.rol=="cliente":
               request.session['nomusuario']=detalleusuario.nomusuario
               return render(request, 'clientes.html')   
         except Usuario.DoesNotExist as e:
            message.success(request,"No existe")
      return render(request,"login.html")


def gestioncliente(request):
   return render(request,"gestionc.html")

def frminsertar(request):
   return render(request,"registrocliente.html")

def frmmodificar(request,documento):
   cl=Cliente.objects.get(documento=documento)
   

   datos={
      'cl':cl
      }
   print(cl)
   print(cl.documento)
   return render(request,"modificarc.html",datos)

def editar(request):
   if request.method=='POST':
      doc=request.POST['documento']
      nom =request.POST['nombre']
      ape=request.POST['apellido']
      cor=request.POST['correo']
      cel=request.POST['celular']
      print("dosss",nom)
      cl=Cliente.objects.get(documento=doc)  
   
      documento=cl

      cl.nombre=nom
      cl.apellido=ape
      cl.correo=cor
      cl.celular=cel
      cl.save()
      return redirect('/cliente/')
    


def eliminarcli(request,documento):
    cli=list(Cliente.objects.filter(documento=documento).values())
    Cliente.objects.filter(documento=documento).delete()
    return redirect('/cliente/')
    
 
def consultainner(request,documento):
    #datoconsulta=Cliente.objects.get(documento=request.POST['datobus'])
    #print(datoconsulta)
    #usuario = Usuario.objects.get(documento__documento = correo).select_related('documento')
   # usuario = Usuario.objects.get(documento__documento = documento)
    #print(usuario)
    #cli=Credito.objects.filter(documento__nombre='Pepino')
   # cli=list(Credito.objects.filter(documento__documento=200).values())
   # cli=list(Credito.objects.filter(documento__nombre="Ramon").filter(codigo__codigo_id=101010))
   # da=list(Credito.objects.filter(documento__documento=200).values())
    #credito=list(Credito.objects.filter(documento__documento=documento).values('documento__documento', 'documento__nombre',
     #       'documento__apellido', 'documento__correo', 'documento__celular'))
    #print("khjdhc")
    #Credito.objects.select_related('creditos', 'cliente').values('name','provider__name')
    #cre=Credito.objects.all().select_related('documento', 'codigo')

    #credito=Credito.objects.filter().select_related('documento').values('documento__documento', 'documento__nombre',
     #              'documento__apellido', 'documento__correo', 'documento__celular')
    #if request.method=='POST':
      #documento=request.POST["documento"]
      #print("AAAAAA",doc)
      credit = Credito.objects.select_related('documento').filter(documento=documento)
      print("HOLA",credit)
      #cre = Credito.objects.select_related("documento", "codigo").values("codigo_credito" ,"montoprestado","fecha" , "documento", "codigo")



      template_name="consultarmultiples.html"
      datos={"listado":credit}
      print(datos)
      #dat={"list":da}
      print("ENCONTRADO")
      return render(request,template_name,datos)
      #cli=list(Cliente.objects.filter(documento__nombre="Pepino").values())
      #return render(request, 'satrent/population_list.html', {'populations' : populations})
      # print("dksjkjdsjksjfkjd",cli)
      #datos=Credito.objects.all().select_related("documento")
   
def principal(request):
    return render(request, 'index.html')
