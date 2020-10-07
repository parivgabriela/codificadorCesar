import sys
def reemplazarUnElementoLista(elemento,reemplazo,lista):
  otroArray=[]
  for unElemento in lista:
    nuevoElemento=unElemento.replace(elemento,reemplazo)
    otroArray.append(nuevoElemento)
  return otroArray

def transformarArrayAcii(lista):
  arrayAscii=[]
  for letra in lista:
      letraAscii=ord(letra)
      arrayAscii.append(letraAscii)
  return arrayAscii


def sumarElementoArray(aSumar,listaAmodificar):
  listaModificada=[]
  nuevoValor=0
  limiteSuperior=90
  limiteInferior=65
  espacio=32
  for unNumero in listaAmodificar:
    nuevoValor=int(unNumero)+aSumar
    if nuevoValor>=limiteInferior and nuevoValor<limiteSuperior:
      listaModificada.append(nuevoValor)
    elif unNumero==espacio:
      listaModificada.append(espacio)
    elif unNumero<limiteInferior and unNumero!=espacio:
      listaModificada.append(unNumero)
    elif nuevoValor>limiteSuperior:
      resto=nuevoValor-limiteSuperior
      nuevaPosicion=limiteInferior+resto
      listaModificada.append(nuevaPosicion)
  return listaModificada

def transformarAChar(lista):
  arrayNuevo=[]
  for numero in lista:
    letra=chr(numero)
    arrayNuevo.append(letra)
  return arrayNuevo

def codificarMensaje(mensajeAcodificar,recorrido):
  mensajeCodificado=[]
  for renglon in mensajeAcodificar:
    arrayRenglon=list(renglon)
    arrayAscii=transformarArrayAcii(arrayRenglon)
    #desplazo
    nuevoArrayAscii=sumarElementoArray(recorrido,arrayAscii)
    #traduccion
    arrayMensajeCodificado=transformarAChar(nuevoArrayAscii)
    #junto el array de caracteres para tener un array palabras
    palabraCodificada=''.join(arrayMensajeCodificado)
    #agrego los saltos de linea \n
    mensajePalabraCodificada=palabraCodificada+'\n'
    #agrega la palabra codificada en un array que los almacena renglon por renglon
    mensajeCodificado.append(mensajePalabraCodificada)
  return mensajeCodificado
def miFirma(nombreArchivo):
    print("Nombre del Programa: Cifrador")
    print("Autora: Gabriela Pari Vaca | parivgabriela@gmail.com")
    print(f"Archivo a cifrar: {nombreArchivo}")
    archivoCifrado=nombreArchivo+".cifrado"
    print(f"Archivo cifrado: {archivoCifrado}")


nombreArchivo=sys.argv[1]
miFirma(nombreArchivo)
arrayMensajeCodificado=[]

with open(nombreArchivo,"r+") as f:
  #contenidoACodificar=f.read()
  contenidoPrevioACodificar=f.readlines()
  contenidoACodificar=reemplazarUnElementoLista('\n','',contenidoPrevioACodificar)
  numero_clave=int(contenidoACodificar.pop(0))
  #print(unArray)
  arrayMensajeCodificado=codificarMensaje(contenidoACodificar,numero_clave)
  f.close()
  
with open("codificado.txt.cifrado","w+") as f:
  f.writelines(arrayMensajeCodificado)
  f.close()