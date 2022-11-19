
from django import forms

class FormularioEmpleados(forms.Form):

    TIPODOC = (
        (1,'CC'),
        (2,'PP'),
        (3,'PEP'),
        (4,'C.E'),
    )

     
    tipoDoc=forms.ChoiceField(
    widget=forms.Select(attrs={"class":"form-control mb-3"}),
    choices= TIPODOC
    )


    numeroDocumento=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        max_length=12,
        required=True,
        label="Numero Documento"
    )
    nombreEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=30,
        required=True,
        
    )
    telefonoEmpleado=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        max_length=12,
        required=True
    )
    correoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True
    )
    


    