from os import listdir,system
from time import time,sleep
from aj_progressB import Bar

class Procesar_Similares():

    def __init__(self,files):
        self.files=files


    def buscar(self,percent_match,reprocesar=False):
        if self.files:
            cont = 0
            files=list(map(lambda x:[x,True],self.files))

            if not reprocesar:
                self.files=[]
            texto='\nReprocesando al {0}%: ' if reprocesar else '\nBuscando al {0}%: '
            bar = Bar(texto.format(percent_match), max_val1=len(files))

            while cont < len(files):

                if files[cont][1]:  # si el archivo seleccionado no ha dado similar .

                    archivo = files[cont][0]

                    l_archivos_comp = files[cont + 1:]  # lista de archivos a comparar con el archivo seleccionado

                    if l_archivos_comp:  # si existen archivos para comparar con el archivo seleccionado

                        bar.set_max_val(len(l_archivos_comp))

                        similar_general = (101, '')

                        for archivo_comp in l_archivos_comp:

                            if archivo_comp[1]:  # si el archivo a comparar seleccionado no a dado similar

                                match = self._comparar(archivo, archivo_comp[0])
                                #print('{2}{3} {0} == {1}'.format(archivo,archivo_comp[0],reprocesar,match[0]))
                                if match[0] > percent_match:
                                    # print(match)
                                    archivo_comp[1] = False
                                    if similar_general[0] > match[0]:
                                        similar_general = match

                                    if reprocesar:self.files.remove(archivo_comp[0])



                            bar.update()

                        if similar_general[0] != 101:
                            self.files.append(similar_general[1])
                            if reprocesar:self.files.remove(archivo)

                cont += 1
                bar.update1()
            #print('\n\n[{0}]\n\n'.format(','.join(self.files)))
            print('\nSimilares: {0}'.format(len(self.files)))

    def _comparar(self,nombre='', nombre2=''):
        'Compara dos textos y devuelve el porciento de similitud y el fragmento comun'
        caract_selec_min = 2

        similar = (0, '')
        len_nombre = len(nombre)
        len_nombre2 = len(nombre2)

        for cant_caract in range(caract_selec_min, len_nombre + 1):

            for cont_ini in range(len_nombre - cant_caract + 1):

                seleccion = nombre[cont_ini:cant_caract + cont_ini]
                if seleccion in nombre2:
                    if cant_caract > similar[0]:
                        similar = (cant_caract, seleccion)

        total = len_nombre if len_nombre > len_nombre2 else len_nombre2
        return (similar[0] * 100) / total, similar[1]

def get_nombre_arch(archivos):
    def get_name(texto):
        a=texto.split('.')

        if len(a)==2:result=a[0]
        elif len(a)>2:result='.'.join(a[:-1])
        else:result=None

        return result

    if type(archivos) == str:
        return get_name(archivos)

    else:
        cont=0
        for arch in archivos:
            if get_name(arch):cont+=1

        return cont

def inicio():

    ini = time()
    print('\nOrganizando archivos:\n')
    archivos = listdir()
    archivos1 = []
    #arch_v=[]
    cant_arch_ini=get_nombre_arch(archivos)

    NUEVOS='Nuevos'
    ORGANIZADOS='Organizados'
    BORRAR='Borrar'
    ERRORES='Errores'

    def mover_existentes(nombre,archivos):
        if nombre in archivos:
            arch_v = listdir(nombre)

            if arch_v:
                #Ya hay archivos similares de búsquedas pasadas
                arch_v=listdir(nombre)

                if not ERRORES in archivos:
                    system(f'mkdir {ERRORES}')

                for arch_o in arch_v:

                    system(f'mv *"{arch_o}"* {nombre}/"{arch_o}" 2>>{ERRORES}/errores_{nombre}.txt')
                    #sleep(0.1)
                sleep(3)
                #archivos = listdir()
                #return arch_v,listdir()
                return listdir()

            else: return archivos
        #return [],archivos
        return archivos
    #'Organizados'

    #arch_v,archivos=mover_existentes(ORGANIZADOS,archivos)
    archivos = mover_existentes(ORGANIZADOS, archivos)
    cant_arch_org=get_nombre_arch(listdir())

    #archivos = mover_existentes(BORRAR, archivos)[1]
    archivos = mover_existentes(BORRAR, archivos)
    cant_arch_borrar=get_nombre_arch(listdir())



    for arch in archivos:
        # quitar extension y carpetas
        # lista_negra={'Episodio':'','[1080p]':''}

        #arch_mod = '.'.join(arch.split('.')[:-1])
        arch_mod= get_nombre_arch(arch)

        '''for pal in lista_negra:
            arch_mod=arch_mod.replace(pal,lista_negra[pal])'''

        if arch_mod: archivos1.append(arch_mod)

    proc=Procesar_Similares(archivos1)

    proc.buscar(85)
    proc.buscar(90,True)

    if proc.files:

        #print('\n\nCaracteres similares: {0}'.format(len(proc.files)))
        #print('Reprocesando resultados: {0}'.format(len(proc.similares_proc)))

        #moviendo archivos
        if not ORGANIZADOS in archivos:
            system(f'mkdir {ORGANIZADOS}')
        if not ERRORES in archivos:
            system(f'mkdir {ERRORES}')
        if not BORRAR in archivos:
            system(f'mkdir {BORRAR}')
        if not NUEVOS in archivos:
            system(f'mkdir {NUEVOS}')

        for similar in proc.files:

            while similar[-1]==' ' or similar[-1]=='.':
                #quitar el espacio y el punto despues de la palabra
                similar=similar[:-1]

            '''if not similar in arch_v:#si no esta la carpeta creada
                system(f'mkdir {NUEVOS}/"{similar}"')'''

            system(f'mkdir {NUEVOS}/"{similar}"')

            system(f'mv *"{similar}"* {NUEVOS}/"{similar}" 2>Errores/errores_similares.txt')

    cant_arch_finales=get_nombre_arch(listdir())

    print(f'\narch iniciales: {cant_arch_ini}\n'
          f'arch organizados: {cant_arch_ini-cant_arch_org}\n'
          f'arch borrar: {cant_arch_org-cant_arch_borrar}\n'
          f'arch nuevos: {cant_arch_borrar-cant_arch_finales}\n'
          f'arch sin procesar: {cant_arch_finales}')
    print('\nTerminado en {0} segundos.'.format(round((time()-ini),2)))

if __name__ == '__main__':inicio()