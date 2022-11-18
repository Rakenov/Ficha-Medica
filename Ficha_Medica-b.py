class Patient:

    ## Metodos##
    def __init__(self):
        self.date_of_birth = ""
        self.gender = ""
        self.weight = 0
        self.height = 0
        self.run = ""
        self.email = ""
        self.phone = ""
        self.adress = ""
        self.previous_operation = ""
        self.previous_trauma = ""
        self.diagnosed_diseases = ""
        self.allergies = ""
        self.family_history = ""
        self.observation = ""

def data(self):
    print("Registro de paciente: \n")
    self.name = input("Ingrese nombre: \n")
    self.date_of_birth = input("Ingrese lfecha de nacimiento: \n")
    self.gender = input("Ingrese sexo: \n")
    self.weight = input("Ingrese peso: \n")
    self.height = input("Ingrese altura: \n")
    self.run = input("Ingrese run: \n")
    self.email = input("Ingrese email: \n")
    self.phone = input("Ingrese numero de telefono: \n")
    self.adress = input("Ingrese dirección: \n")
    self.previous_operation = input("Ingrese operaciones previas: \n")
    self.previous_trauma = input("Ingrese traumas previos: \n")
    self.diagnosed_diseases = input("Ingrese enfermedades diagnosticadas: \n")
    self.allergies = input("Ingrese alergias: \n")
    self.family_history = input("Ingrese el historial medico familiar: \n")
    self.observation = input("Ingrese las observaciones del paciente: \n")
    
    print("Elije una de las siguientes opciones:")

    print("1)Registrar datos de paciente")
    print("2)Mostrar datos paciente")
    print("3)Salir\n")

    menu=int(input(""))
    if (menu==1):
        data(a)
    if (menu==2):
        show(a)   
    if (menu==3):
        print("saliendo")

def show(self):
    print("Ficha medica:")
    print("El nombre del paciente es:",self.name)
    print("La fecha de nacimiento del Paciente es:",self.date_of_birth)
    print("El sexo del paciente es:",self.gender)
    print("El peso del paciente es:",self.weight)
    print("La altura del paciente es",self.height)
    print("El run del paciente es:",self.run)
    print("El correo del paciente es:",self.email)
    print("El número de telefono del paciente es:",self.phone)
    print("La direccion del paciente es:",self.adress)
    print("Operaciones anteriores:",self.previous_operation)
    print("Traumas anteriores:",self.previous_trauma)
    print("Enfermedades diagnosticadas:",self.diagnosed_diseases)
    print("Alergias:",self.allergies)
    print("Historial familiar:",self.family_history)
    print("Observación:\n",self.observation)


    
a=Patient()

print("Elije una de las siguientes opciones:")
print("1)Registrar datos de paciente")
print("2)Mostrar datos paciente")
print("3)Salir\n")

menu=int(input(""))
if (menu==1):
    data(a)
if (menu==2):
    show(a)   
if (menu==3):
    print("saliendo")
        
   