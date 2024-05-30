class Trabajador(object):
    def _init_(self, nombre:str, salario:float, departamento:str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")
        print(f"Departamento: {self.departamento}")      
    
    def aumentar_salario(self, porcentaje:float):
        self.salario += self.salario * porcentaje
        
