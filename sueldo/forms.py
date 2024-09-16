from django import forms

class LoginForm(forms.Form):
    apellido = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class CalculoPagoForm(forms.Form):
    horas_trabajadas = forms.IntegerField(label='Horas trabajadas', min_value=0)
    pago_por_hora = forms.DecimalField(label='Pago por hora', max_digits=6, decimal_places=2, min_value=0.0)
    numero_hijos = forms.IntegerField(label='Número de hijos', min_value=0)
