from os import listdir,system
from time import time
from aj_progressB import Bar

class Procesar_Similares():

    def __init__(self):
        self.similares=[]
        self.similares_proc=[]


    def add_similar(self,texto):

        if texto not in self.similares:
            self.similares.append(texto)

    def reprocesar(self):
        self.similares_proc=self.similares[:]
        if self.similares:
            bar1=Bar('\nReprocesando: ',max_val1=len(self.similares_proc))

            for cont in range(len(self.similares)):

                similar=self.similares[cont]
                bar1.set_max_val( len(self.similares[cont + 1:]))

                for similar1 in self.similares[cont+1:]:

                    match = comparar(similar,similar1)
                    if match[0]>80:
                        if similar in self.similares_proc:
                            self.similares_proc.remove(similar)
                        if similar1 in self.similares_proc:
                            self.similares_proc.remove(similar1)
                        self.similares_proc.append(match[1])
                    bar1.update()


                bar1.update1()

def comparar(nombre='',nombre2=''):
    'Compara dos textos y devuelve el porciento de similitud y el fragmento comun'
    caract_selec_min = 2

    similar = (0,'')
    len_nombre=len(nombre)
    len_nombre2=len(nombre2)

    for cant_caract in range(caract_selec_min, len_nombre + 1):

        for cont_ini in range(len_nombre-cant_caract+1):

            seleccion=nombre[cont_ini:cant_caract+cont_ini]
            if  seleccion in nombre2:
                if cant_caract>similar[0]:
                    similar=(cant_caract,seleccion)

    total= len_nombre if len_nombre>len_nombre2 else len_nombre2
    return (similar[0]*100)/total,similar[1]

def inicio():

    ini = time()
    print('\nOrganizando archivos:\n')
    archivos = listdir()
    archivos1 = []
    arch_v=[]
    if 'Organizados' in archivos:
        #Ya hay archivos similares de búsquedas pasadas
        arch_v=listdir('Organizados')
        archivos1.extend(map(lambda x:[x,True],arch_v))


    for arch in archivos:
        # quitar extension y carpetas
        # lista_negra={'Episodio':'','[1080p]':''}

        arch_mod = '.'.join(arch.split('.')[:-1])

        '''for pal in lista_negra:
            arch_mod=arch_mod.replace(pal,lista_negra[pal])'''

        if arch_mod: archivos1.append([arch_mod, True])

    proc=Procesar_Similares()

    cont=0
    bar=Bar('Buscando: ',max_val1=len(archivos1))

    while cont<len(archivos1):

        if archivos1[cont][1]:#si el archivo seleccionado no ha dado similar .

            archivo = archivos1[cont][0]

            l_archivos_comp=archivos1[cont+1:] #lista de archivos a comparar con el archivo seleccionado

            if l_archivos_comp:#si existen archivos para comparar con el archivo seleccionado

                bar.set_max_val(len(l_archivos_comp))

                similar_general=(101,'')

                for archivo_comp in l_archivos_comp:

                    if archivo_comp[1] :#si el archivo a comparar seleccionado no a dado similar

                        match=comparar(archivo,archivo_comp[0])

                        if match[0]>85:
                            #print(match)
                            archivo_comp[1]=False
                            if similar_general[0]>match[0]:
                                similar_general=match

                    bar.update()

                if similar_general[0]!=101 :proc.add_similar(similar_general[1])
        cont+=1
        bar.update1()



    proc.reprocesar()


    #for x in proc.similares:print(x)
    #print('*****************************************')
    #for x in proc.similares_proc:print(x)



    '''def get_Mm(text=''):
        l_t=[]
        for c in text:
            if re.match('[A-Za-z]',c):
                l_t.append('[{0} {1}]'.format(c.lower(),c.upper()))
            else:
                l_t.append(c)
    
        return ''.join(l_t)'''

    if proc.similares_proc:

        print('\n\nCaracteres similares: {0}'.format(len(proc.similares)))
        print('Reprocesando resultados: {0}'.format(len(proc.similares_proc)))

        #moviendo archivos
        if not 'Organizados' in archivos:
            system('mkdir Organizados')

        for similar in proc.similares_proc:

            while similar[-1]==' ' or similar[-1]=='.':
                #quitar el espacio y el punto despues de la palabra
                similar=similar[:-1]

            if not similar in arch_v:
                system('mkdir Organizados/"{0}"'.format(similar))
            system('mv *"{0}"* Organizados/"{0}"'.format(similar))


    print('\nTerminado en {0} segundos.'.format(round((time()-ini),2)))

if __name__ == '__main__':inicio()