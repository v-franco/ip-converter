class getValue():
    def __init__(self, message, li=0, ls=0, cycle="no", type="float"):
        self.message=message
        self.li=li
        self.ls=ls
        self.cycle=cycle.upper()
        self.type=type

    def __del__(self):
        pass

    def error(self):
        input(self.message)

    def getString(self):
        while True:
            cad=input(self.message)
            if (self.cycle=="NO"): return cad
            else:
                if (self.li==0) and (self.ls==0): return cad
                else:
                    if len(cad)<self.li or len(cad)>self.ls:
                        er="Error, la cadena debe estar entre "+str(self.li)+" y "+str(self.ls)+" caracteres ..."
                        oe=getValue(er)
                        oe.error()
                        del oe
                    else: return cad

    def getNumber(self):
        while True:
            cad=input(self.message)
            if not cad.isnumeric():
                oe=getValue("Error, ingrese una opción entre 1 y 8, ENTER para continuar. ")
                oe.error()
                del oe
            else:
                if self.type=="int" : number=int(cad)
                else: number=float(cad)
                if self.cycle=="NO": return number
                else:
                    if (self.li==0) and (self.ls==0): return number
                    else:
                        if number<self.li or number>self.ls:
                            er="Error, valor fuera de rango entre "+str(self.li)+" y "+str(self.ls)+" ..."
                            oe=getValue(er)
                            oe.error()
                            del oe
                        else : return number

