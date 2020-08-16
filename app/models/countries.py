#Importacion de clases desde mongoengine
from mongoengine import Document, StringField, BooleanField, ListField, ReferenceField

#Importacion de la clase State desde el archivo states.py 
from .states import States

#Declaracion de clase Countries, Heredando las propiedades de la clase Document que inicializa como modelo de base de datos
class Countries(Document):
    #Declaracion de datos del modelo Countries
    name = StringField(max_length=100, required=True)
    phone_prefix = StringField(max_length=10)
    active = BooleanField(required=True, default=0)
    states = ListField(ReferenceField(States, dbref=False))