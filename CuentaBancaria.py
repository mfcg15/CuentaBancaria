class CuentaBancaria:

    todas_las_cuentas = []

    def __init__(self,tasa_interes):
        self.tasa_interes = tasa_interes/100
        self.balance = 0
        CuentaBancaria.todas_las_cuentas.append(self)
    
    def deposito(self,amount):
        self.balance += amount
        return self
    
    def retiro(self,amount):
        auxBalnce = self.balance - amount
        if(auxBalnce>0):
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance = self.balance-5
        return self
    
    def mostrar_info_cuenta(self):
        print("Blance: $"+str(self.balance))
        return self
    
    def generar_initeres(self):
        if(self.balance>0):
            self.balance = self.balance * self.tasa_interes
        else:
            print("El balance actual es negativo")
        return self
    
    @classmethod
    def mostrar_informacion_banco(cls):
        for cuenta in cls.todas_las_cuentas:
            cuenta.mostrar_info_cuenta()

cuenta1 = CuentaBancaria(10)
cuenta2 = CuentaBancaria(10)

cuenta1.deposito(1000).deposito(2000).deposito(3000).retiro(1065).generar_initeres().mostrar_info_cuenta()
cuenta2.deposito(50000).deposito(15000).retiro(5050).retiro(1050).retiro(900).retiro(472).generar_initeres().mostrar_info_cuenta()
cuenta1.mostrar_informacion_banco()

