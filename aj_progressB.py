from sys import stdout

class Bar():

    def __init__(self,texto='',max_val=2,max_val1=int,ancho=40):
        self.texto=texto
        self.ancho=ancho
        self.max_val=max_val
        self.max_val1=max_val1
        self.text_porc = ' {0} %   '
        self.old_porciento=self.text_porc.format('0.0')
        self.i=0
        self.i1=0
        stdout.write('{0}|{1}|{2}'.format(self.texto,' ' * self.ancho,self.old_porciento))
        stdout.flush()

    def __porciento(self):
        return round((self.i1 * 100) / self.max_val1,1)

    def update(self,i=1):
        self.i=self.i+i
        porciento=self.__porciento()
        parte_s=self.i/self.max_val
        barra_s=int(parte_s*self.ancho)
        valor_p=self.text_porc.format(porciento)
        borrar_c='\b'*(self.ancho+len(self.old_porciento)+1)
        self.old_porciento=valor_p
        stdout.write('{0}{1}{2}|{3}'.format(borrar_c, '█' * (barra_s), ' ' * (self.ancho - barra_s),valor_p))
        stdout.flush()

    def update1(self,i1=1):
        self.i1=self.i1+i1
        porciento=self.__porciento()
        valor_p=self.text_porc.format(porciento)
        borrar_c='\b'*(len(self.old_porciento))
        self.old_porciento=valor_p
        stdout.write('{0}{1}'.format(borrar_c, valor_p))
        stdout.flush()

    def set_max_val(self,max_val):
        self.i=0
        self.max_val=max_val
