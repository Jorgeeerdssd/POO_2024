b=.987
I=1.203

kWh=int(input("kWh consumidos por el cliente:"))

exedente= int(kWh-150)
if kWh <= 150:
    kWh=kWh*b
    print("Total de kWh:", kWh)
    
elif kWh > 150:
    exedente=kWh-150
    exedente_pagar=exedente*I
    print("exedente", exedente)
    print("total exedente: ", exedente_pagar)

Sub_total=exedente_pagar+kWh
print("Sub total:", Sub_total)

iva=Sub_total*.16
print("Iva",iva)
total_a_pagar=Sub_total+iva+12
print("Total a pagar: ", total_a_pagar)
    
4