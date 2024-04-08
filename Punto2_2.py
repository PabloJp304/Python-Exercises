from abc import ABC, abstractmethod
import datetime

class Persona(ABC):
    def __init__(self, identificacion, nombres, apellidos, fecha_nacimiento, telefono, correo, contacto_nombre, contacto_telefono):
        self.identificacion = identificacion
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.correo = correo
        self.contacto_nombre = contacto_nombre
        self.contacto_telefono = contacto_telefono

class Paciente(Persona):
    def __init__(self, identificacion, nombres, apellidos, fecha_nacimiento, telefono, correo, contacto_nombre, contacto_telefono):
        super().__init__(identificacion, nombres, apellidos, fecha_nacimiento, telefono, correo, contacto_nombre, contacto_telefono)
        self.ordenes = []

    @abstractmethod
    def registrar_examen(self, tipo_examen, fecha_realizacion, observaciones):
        pass

class PacienteParticular(Paciente):
    def __init__(self, identificacion, nombres, apellidos, fecha_nacimiento, telefono, correo, contacto_nombre, contacto_telefono, direccion):
        super().__init__(identificacion, nombres, apellidos, fecha_nacimiento, telefono, correo, contacto_nombre, contacto_telefono)
        self.direccion = direccion
        self.facturas = []

    def registrar_examen(self, tipo_examen, fecha_realizacion, observaciones):
        examen = Examen(tipo_examen, fecha_realizacion, observaciones)
        self.ordenes[-1].registrar_examen(examen)
        # Generar factura por cada examen para pacientes particulares
        valor_examen = self.calcular_valor_examen(tipo_examen)
        numero_factura = len(self.facturas) + 1
        fecha_creacion = datetime.datetime.now().strftime("%d/%m/%Y")
        factura = FacturaParticular(numero_factura, valor_examen, self, fecha_creacion)
        self.facturas.append(factura)

    def calcular_valor_examen(self, tipo_examen):
        # Esta función debería calcular el valor del examen según el tipo de examen
        # Por simplicidad, asignaremos valores fijos a los exámenes
        if tipo_examen == "Triglicéridos":
            return 15000
        elif tipo_examen == "Hemograma":
            return 10000
        else:
            return 0

class PacienteEntidadSalud(Paciente):
    def __init__(self, identificacion, nombres, apellidos, fecha_nacimiento, telefono, correo, contacto_nombre, contacto_telefono, entidad_salud):
        super().__init__(identificacion, nombres, apellidos, fecha_nacimiento, telefono, correo, contacto_nombre, contacto_telefono)
        self.entidad_salud = entidad_salud

    def registrar_examen(self, tipo_examen, fecha_realizacion, observaciones):
        examen = Examen(tipo_examen, fecha_realizacion, observaciones)
        self.ordenes[-1].registrar_examen(examen)

class Orden:
    def __init__(self, consecutivo, fecha_solicitud, fecha_ingreso, medico_tratante, numero_orden):
        self.consecutivo = consecutivo
        self.fecha_solicitud = fecha_solicitud
        self.fecha_ingreso = fecha_ingreso
        self.medico_tratante = medico_tratante
        self.numero_orden = numero_orden
        self.examenes = []

    def registrar_examen(self, examen):
        self.examenes.append(examen)

class Examen:
    def __init__(self, tipo_examen, fecha_realizacion, observaciones):
        self.tipo_examen = tipo_examen
        self.fecha_realizacion = fecha_realizacion
        self.observaciones = observaciones

class Medico(Persona):
    def __init__(self, identificacion, nombres, apellidos, telefono, direccion, tarjeta_profesional):
        super().__init__(identificacion, nombres, apellidos, None, telefono, None, None, None)
        self.direccion = direccion
        self.tarjeta_profesional = tarjeta_profesional
        self.pacientes_referidos = 0

class Factura(ABC):
    def __init__(self, numero_factura, valor_pagar, paciente, fecha_creacion):
        self.numero_factura = numero_factura
        self.valor_pagar = valor_pagar
        self.paciente = paciente
        self.fecha_creacion = fecha_creacion

    @abstractmethod
    def generar_factura(self):
        pass

class FacturaParticular(Factura):
    def __init__(self, numero_factura, valor_pagar, paciente, fecha_creacion):
        super().__init__(numero_factura, valor_pagar, paciente, fecha_creacion)

    def generar_factura(self):
        # Lógica para generar la factura para un paciente particular
        pass

class FacturaEntidadSalud(Factura):
    def __init__(self, numero_factura, valor_pagar, paciente, fecha_creacion):
        super().__init__(numero_factura, valor_pagar, paciente, fecha_creacion)

    def generar_factura(self):
        # Lógica para generar la factura para una entidad de salud
        pass

class Laboratorio:
    def __init__(self):
        self.pacientes_registrados = []
        self.medicos_registrados = []

    def registrar_paciente(self, paciente):
        self.pacientes_registrados.append(paciente)

    def registrar_medico(self, medico):
        self.medicos_registrados.append(medico)

    def realizar_examen(self, paciente, tipo_examen, fecha_realizacion, observaciones):
        # Crear una orden si no existe
        if not paciente.ordenes:
            medico = self.medicos_registrados[0]  # Asignar al primer médico por simplicidad
            numero_orden = len(paciente.ordenes) + 1
            nueva_orden = Orden("001", datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%d/%m/%Y"), medico, numero_orden)
            paciente.ordenes.append(nueva_orden)
        paciente.registrar_examen(tipo_examen, fecha_realizacion, observaciones)

    def consultar_factura_por_numero(self, numero_factura):
        for paciente in self.pacientes_registrados:
            if isinstance(paciente, PacienteParticular):
                for factura in paciente.facturas:
                    if factura.numero_factura == numero_factura:
                        return factura
        return None

    def medico_con_mas_pacientes(self):
        medico_mas_pacientes = None
        max_pacientes_referidos = 0
        for medico in self.medicos_registrados:
            if medico.pacientes_referidos > max_pacientes_referidos:
                medico_mas_pacientes = medico
                max_pacientes_referidos = medico.pacientes_referidos
        return medico_mas_pacientes

    def consolidado_ingresos_por_tipo_paciente(self):
        ingresos_por_tipo_paciente = {"Particular": 0, "Entidad de Salud": 0}
        for paciente in self.pacientes_registrados:
            if isinstance(paciente, PacienteParticular):
                for factura in paciente.facturas:
                    ingresos_por_tipo_paciente["Particular"] += factura.valor_pagar
            elif isinstance(paciente, PacienteEntidadSalud):
                for orden in paciente.ordenes:
                    for examen in orden.examenes:
                        # Suponiendo que el costo de los exámenes para las entidades de salud es el mismo
                        ingresos_por_tipo_paciente["Entidad de Salud"] += 10000  # Costo arbitrario
        ingresos_por_tipo_paciente = dict(sorted(ingresos_por_tipo_paciente.items(), key=lambda x: x[1], reverse=True))
        return ingresos_por_tipo_paciente

    def consultar_examenes_por_paciente(self, numero_cedula):
        for paciente in self.pacientes_registrados:
            if paciente.identificacion == numero_cedula:
                examenes_realizados = []
                for orden in paciente.ordenes:
                    for examen in orden.examenes:
                        examenes_realizados.append((examen.tipo_examen, examen.fecha_realizacion))
                return examenes_realizados
        return None

# Ejemplo de uso
lab = Laboratorio()

# Registrar médico
medico = Medico("1234567890", "Dr. José", "Gonzalez", "0987654321", "Calle Principal", "MP12345")
lab.registrar_medico(medico)

# Registrar paciente particular
paciente_particular = PacienteParticular("123456789", "Juan", "Perez", "01/01/1980", "1234567890", "juan@example.com", "Maria", "0987654321", "Calle 123")
lab.registrar_paciente(paciente_particular)

# Realizar exámenes
lab.realizar_examen(paciente_particular, "Triglicéridos", "04/04/2024", "Ninguna")
lab.realizar_examen(paciente_particular, "Hemograma", "05/04/2024", "Leve anemia")

# Imprimir información relevante
print("Paciente registrado:", paciente_particular.nombres, paciente_particular.apellidos)
for orden in paciente_particular.ordenes:
    for examen in orden.examenes:
        print("Examen:", examen.tipo_examen, "- Fecha:", examen.fecha_realizacion, "- Observaciones:", examen.observaciones)

# Consultar factura por número
factura = lab.consultar_factura_por_numero("1")
if factura:
    print("Factura encontrada - Valor a Pagar:", factura.valor_pagar)
else:
    print("No se encontró la factura con el número especificado.")

# Consultar médico con más pacientes
medico_mas_pacientes = lab.medico_con_mas_pacientes()
if medico_mas_pacientes:
    print("Médico con más pacientes:", medico_mas_pacientes.nombres, medico_mas_pacientes.apellidos)
else:
    print("No se encontró ningún médico con pacientes registrados.")

# Consultar ingresos por tipo de paciente
ingresos_por_tipo_paciente = lab.consolidado_ingresos_por_tipo_paciente()
print("Ingresos por tipo de paciente:", ingresos_por_tipo_paciente)

# Consultar exámenes realizados por un paciente específico
examenes_realizados = lab.consultar_examenes_por_paciente("123456789")
if examenes_realizados:
    print("Exámenes realizados por el paciente:")
    for examen in examenes_realizados:
        print("- Tipo de examen:", examen[0], "- Fecha de realización:", examen[1])
else:
    print("No se encontraron exámenes realizados para el paciente especificado.")
