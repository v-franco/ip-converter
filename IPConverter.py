#A01366475 Victor Hugo Franco Juárez
#Python program that converts IPv4 adresses between decimal, hexadecimal, and binary

from GetValue import getValue

class IP:

    def __init__(self):
        self.ip = ""

    def readIP(self):
        self.ip=input("Ingrese la IP: ")
        print("------------------------")
        return self.ip
        
    def intToBin(self):
        if self.ip != "":
            divs = self.ip.split(".")
            length = len(divs)
            self.ip = ""
            for i in range(0,length):
                octet = int(divs[i])
                octet = bin(octet)
                octet = octet[1:]
                octet = octet.replace('b','')
                for j in range(0,6):
                    if (len(octet) < 8):
                        octet = "0" + octet
                self.ip = self.ip + octet + "."
            self.ip = self.ip[:-1]
            return(self.ip) 
        else:
            print("Ingrese una IP para convertir con la opción 1)")

    def binToInt(self):
        if self.ip != "":
            divs = self.ip.split(".")
            length = len(divs)
            self.ip = ""
            for i in range(0,length):
                octet = divs[i]
                octet = "0b"+octet
                octet = int(octet,2)
                self.ip = self.ip + str(octet) + "."    
            self.ip = self.ip[:-1]
            return(self.ip) 
        else:
            print("Ingrese una IP para convertir con la opción 1)")

    def intToHex(self):
        if self.ip != "":
            divs = self.ip.split(".")
            length = len(divs)
            self.ip = ""
            for i in range(0,length):
                octet = int(divs[i])
                octet = hex(octet)[2:]
                self.ip = self.ip + octet + "."
            self.ip = self.ip[:-1]
            return(self.ip) 
        else:
            print("Ingrese una IP para convertir con la opción 1)")

    def binToHex(self):
        self.binToInt()
        self.intToHex()
        return(self.ip)

    def hexToInt(self):
        if self.ip != "":
            divs = self.ip.split(".")
            length = len(divs)
            self.ip = ""
            for i in range(0,length):
                octet = divs[i]
                octet = int(octet, 16)
                self.ip = self.ip + str(octet) + "."
            self.ip = self.ip[:-1]    
            return(self.ip)
        else:
            print("Ingrese una IP para convertir con la opción 1)")
    
    def hexToBin(self):
        self.hexToInt()
        self.intToBin()
        return(self.ip)

def menu():
    converter=IP()
    option=0
    while option!=10:

        print("------------------------------")
        print("------------MENU--------------")
        print("------------------------------")
        print("1) Leer IP en Dec, Hex, o Bin     ")
        print("2) Convertir decimal a binario    ")
        print("3) Convertir binario a decimal    ")
        print("4) Convertir decimal a hexadecimal")
        print("5) Convertir binario a hexadecimal")
        print("6) Convertir hexadecimal a decimal")
        print("7) Convertir hexadecimal a binario")
        print("8) Salir                          ")
        
        
        op=getValue("Indica opción deseada : ",li=1,ls=8,cycle="yes")
        option=op.getNumber()
        if option==1:
            converter.readIP()

        if option==2:
            print(converter.intToBin())

        if option==3:
            print(converter.binToInt())

        if option==4:
            print(converter.intToHex())

        if option==5:
            print(converter.binToHex())

        if option==6:
            print(converter.hexToInt())

        if option==7:
            print(converter.hexToBin())

        if option==8:
            exit()  
         
menu()

