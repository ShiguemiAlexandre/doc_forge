from enum import Enum

class TypeContract(Enum):
    FIADOR = "fiador"
    SEGURO = "seguro"
    CAUCAO = "caucao"

class PersonRole(Enum):
    LOCADOR = "locador"
    LOCATARIO = "locatario"

class Locador(Enum):
    EMOJI = ":material/real_estate_agent:"

class Locatario(Enum):
    EMOJI = ":material/person_pin:"

class DateContract(Enum):
    EMOJI = ":material/date_range:"

class Gender(Enum):
    MASCULINO = "masculino"
    FEMININO = "feminino"