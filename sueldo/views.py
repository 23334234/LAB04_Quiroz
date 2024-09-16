from django.shortcuts import render, redirect
from .forms import LoginForm, CalculoPagoForm
from decimal import Decimal, ROUND_HALF_UP

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            apellido = form.cleaned_data['apellido']
            password = form.cleaned_data['password']
            if apellido == "Quiroz" and password == "123":
                return redirect('calculo_pago')  
    else:
        form = LoginForm()
    return render(request, 'sueldo/login.html', {'form': form})

def calculo_pago_view(request):
    if request.method == 'POST':
        form = CalculoPagoForm(request.POST)
        if form.is_valid():
            horas_trabajadas = form.cleaned_data['horas_trabajadas']
            pago_por_hora = form.cleaned_data['pago_por_hora']  
            numero_hijos = form.cleaned_data['numero_hijos']

            horas_trabajadas = Decimal(horas_trabajadas)

            if horas_trabajadas <= 48:
                pago_semanal = horas_trabajadas * pago_por_hora
            else:
                pago_semanal = (48 * pago_por_hora) + ((horas_trabajadas - 48) * pago_por_hora * Decimal(2))

            bonificacion = numero_hijos * Decimal(50)
            descuento = pago_semanal * Decimal(0.08)
            pago_final = pago_semanal - descuento + bonificacion

            pago_semanal = pago_semanal.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            bonificacion = bonificacion.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            descuento = descuento.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            pago_final = pago_final.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            return render(request, 'sueldo/resultado.html', {
                'pago_semanal': pago_semanal,
                'bonificacion': bonificacion,
                'descuento': descuento,
                'pago_final': pago_final,
            })
    else:
        form = CalculoPagoForm()
    return render(request, 'sueldo/calculo_pago.html', {'form': form})
