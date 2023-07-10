xven = int(input("Ingrese la cantidad de vendedores: "))
docu = int(input("Ingrese el numero del documnento: "))
nombre = input("Ingrese el nombre: ")

valor_total = 0

def operacion():
    global valor_total
    global docu
    global nombre
    
    while v < xven:
        print("Tipo de vendedor")
        print("1-Vendedor puerta a puerta")
        print("2-Telemercadeo")
        print("3-Ejecutivo de ventas")
        tipo_vende = int(input("Ingrese el tipo de vendedor"))
        print("Tipo de venta")
        print("1-Contado")
        print("2-Credito")
        tipo_venta = int(input("Ingrese el tipo de venta: "))
        valor_venta = int(input("Ingrese el valor de la venta: "))
        if tipo_vende == 1 and tipo_venta == 1:
            valor_total = (valor_venta*25)/100
        if tipo_vende == 1 and tipo_venta == 2:
            valor_total = (valor_venta*20)/100
        if tipo_vende == 2 and tipo_venta == 1:
            valor_total = (valor_venta*15)/100
        if tipo_vende == 2 and tipo_venta == 2:
            valor_total = (valor_venta*10)/100
        if tipo_vende == 3 and tipo_venta == 1:
            valor_total = (valor_venta*20)/100
        if tipo_vende == 3 and tipo_venta == 2:
            valor_total = (valor_venta*15)/100
            
        v += 1
        print("La comision de el vendedor es: " , valor_total)
        print("El valor de las ventas del vendedor es: " , valor_venta)
        total += valor_total
        
operacion()        
print("Valor total a pagar de comision a todos los empleados: " , total)
