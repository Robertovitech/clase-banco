class Banco:
    def __init__(self):
        self.__name = input('Ingrese su nombe: ')
        self.__clave = input('Introduzca su contraseña: ')
        self.__listUser = [
                    { 'name': 'Karla Perez', 'password': 'karla007', 'monto': 2500},
                    { 'name': 'Juan Castro', 'password': 'juancat', 'monto': 2000},
                    { 'name': 'Jorge Aguilar', 'password': 'aguila58', 'monto': 3700},
                    { 'name': 'Martha Lopez', 'password': 'lopez111', 'monto': 2800},
                          ]
        self.__addData = ''
        self.value_name()
    
    def value_name(self):
        valor = False

        for elemento in self.__listUser:
            if(self.__name.strip() == elemento['name'] and self.__clave.strip() == elemento['password']):
                valor = True
                self.__addData = elemento
                
        if(valor):
            self.muestra_menu()
        else:
            print("""
    +------------------------------------------------+             
    |  Ingresa correctamente tu nombre y contraseña. |
    +------------------------------------------------+              
                  """)
            self.__init__()
            
    def muestra_menu(self):
        print("""
    ╔═══════════════════════════════╗
    ║  ¡BIENVENIDO A CAJITA FELIZ!  ║   
    ╚═══════════════════════════════╝ 
              """)
        print('ELIJA LAS SIGUIENTES OPCIONES:\n1) Mostrar mi monto.\n2) Depositar a mi cuenta.\n3) Depositar a otra cuenta\n4) Retirar Monto\n5) Salir')
        option = input('¿Qué opción deseas elegir?: ')
        
        if(option.strip().isdigit() and int(option.strip()) == 1):
            self.mi_monto()
            
        elif(option.strip().isdigit() and int(option.strip()) == 2):
            self.deposita_mi_cuenta()
            
        elif(option.strip().isdigit() and int(option.strip()) == 3):
            self.valida_otra_cuenta()
            
        elif(option.strip().isdigit() and int(option.strip()) == 4):
            self.retirar_monto()
            
        elif(option.strip().isdigit() and int(option.strip()) == 5):
            return
        else:
            print("""
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx              
    || Se debe ingresar una de las opciones del menú ||
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                  """)
            self.muestra_menu()
            
    def mi_monto(self):
        print('»» Su monto es de: {} $'.format(self.__addData['monto']))
        self.muestra_menu()
        
    def deposita_mi_cuenta(self):
        deposita_dinero = input('Ingrese la cantidad de dinero ha depositar: ')
        
        if(deposita_dinero.strip().isdigit()):
            deposita_dinero = int(deposita_dinero)
            self.__addData['monto'] = self.__addData['monto'] + deposita_dinero
            print("""
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++              
    | ¡Transferencia éxitosa!, elija la opción 1 para que vea su monto actual. |
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++              
                  """)
            self.muestra_menu()
        else:
            print("""
    +------------------------------------------+              
    | Introduzca de forma correcta los dígitos |
    +------------------------------------------+              
                  """)
            self.muestra_menu()
            
    def valida_otra_cuenta(self):
        another_account = input('Ingrese el nombre del usuario al que desea depositar: ')
        valor = False
        datos = ''
        
        for otroUsuario in self.__listUser:
            if(another_account.strip() == otroUsuario['name']):
                valor = True
                datos = otroUsuario
                
        if(valor):
            self.deposita_otra_cuenta(datos)
            
        else:
            print("""
    +---------------------------------------------+              
    | Ingresa correctamente el nombre del usuario |
    +---------------------------------------------+              
                  """)
            self.muestra_menu()
            
    def deposita_otra_cuenta(self, datos):
        self.datos = datos
        deposita_dinero = input('Ingrese la cantidad de dinero ha depositar: ')
        
        if(deposita_dinero.strip().isdigit() and self.__addData['monto'] > int(deposita_dinero)):
            deposita_dinero = int(deposita_dinero)
            self.__addData['monto'] = self.__addData['monto'] - deposita_dinero
            self.datos['monto'] = self.datos['monto'] + deposita_dinero
            #print(self.datos)
            print("""
    +++++++++++++++++++++++++++++++++++++++              
    | ¡La transferencia ha sido éxitosa!. |
    +++++++++++++++++++++++++++++++++++++++              
                  """)
            self.muestra_menu()
        else:
            print("""
    +--------------------------------------------+              
    |*Introduzca de forma correcta los dígitos y |
    | la cantidad a transferir debe ser menor al |
    | monto actual de tu cuenta.*                |
    +--------------------------------------------+              
                  """)
            self.muestra_menu()
            
    def retirar_monto(self):
        retira_dinero = input('Ingrese la cantidad de dinero que quiere retirar: ')
        if(retira_dinero.strip().isdigit() and self.__addData['monto'] > int(retira_dinero)):
            retira_dinero = int(retira_dinero)
            self.__addData['monto'] = self.__addData['monto'] - retira_dinero
            print(f'»» Usted ha retirado la cantidad de {retira_dinero} $')
            self.muestra_menu()
        else:
            print("""
    +--------------------------------------------+              
    |*Introduzca de forma correcta los dígitos y |
    | la cantidad a retirar debe ser menor que   |
    |  su monto actual.*                         |
    +--------------------------------------------+              
                  """)
            self.muestra_menu()
            
usuario = Banco()