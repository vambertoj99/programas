crimes = ("ROUBO","TRAFICO","HOMICIDIO",)    
crimes_valores = ("ROUBO","TRAFICO",)

crime_delator = input().upper()

#verificação dos crimes#
if crime_delator in crimes:
    if crime_delator in crimes_valores:
        valor_delator = float(input())
        crime_delatado = input().upper()
        
        if crime_delatado in crimes:
            if crime_delatado in crimes_valores:
                valor_delatado = float(input())
            
            if crime_delator == "ROUBO" or crime_delator == "TRAFICO" and crime_delatado == "HOMICIDIO":
                print("Delação concedida.")

            elif crime_delator == "ROUBO" and crime_delatado == "ROUBO" and (valor_delatado > 6*valor_delator):
                print("Delação concedida.")
    
            elif crime_delator == "ROUBO" and crime_delatado == "TRAFICO" and (valor_delatado > 4*valor_delator):
                print("Delação concedida.")
    
            elif crime_delator == "TRAFICO" and crime_delatado == "TRAFICO" and (valor_delatado > 6*valor_delator):
                print("Delação concedida.")

            elif crime_delator == "HOMICIDIO" and crime_delatado == "HOMICIDIO":
                print("Delação concedida.")
    
            else:
                print("Delação rejeitada.")
            
            
        else:
            print("Crime inválido.")
                
else:
    print("Crime inválido.")



