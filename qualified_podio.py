

def podio_olimpico(tempo_chegada1,tempo_chegada2,tempo_chegada3):
    if(tempo_chegada1<tempo_chegada2 and tempo_chegada1<tempo_chegada3 and tempo_chegada2<tempo_chegada3):
        podio=(f"1 - {tempo_chegada1} minutos\n2 - {tempo_chegada2} minutos\n3 - {tempo_chegada3} minutos\n") 
    elif(tempo_chegada1<tempo_chegada2 and tempo_chegada1<tempo_chegada3 and tempo_chegada2>tempo_chegada3):
        podio=("1 - {} minutos\n2 - {} minutos\n3 - {} minutos\n".format(tempo_chegada1,tempo_chegada3,tempo_chegada2))
    elif(tempo_chegada1>tempo_chegada2 and tempo_chegada1<tempo_chegada3 and tempo_chegada2<tempo_chegada3):
        podio=("1 - {} minutos\n2 - {} minutos\n3 - {} minutos\n".format(tempo_chegada2,tempo_chegada1,tempo_chegada3))
    elif(tempo_chegada1>tempo_chegada2 and tempo_chegada1>tempo_chegada3 and tempo_chegada2<tempo_chegada3):
        podio=("1 - {} minutos\n2 - {} minutos\n3 - {} minutos\n".format(tempo_chegada2,tempo_chegada3,tempo_chegada1))
    elif(tempo_chegada1<tempo_chegada2 and tempo_chegada1>tempo_chegada3 and tempo_chegada2>tempo_chegada3):
        podio=("1 - {} minutos\n2 - {} minutos\n3 - {} minutos\n".format(tempo_chegada3,tempo_chegada1,tempo_chegada2))
    elif(tempo_chegada1>tempo_chegada2 and tempo_chegada1>tempo_chegada3 and tempo_chegada2>tempo_chegada3):
        podio=("1 - {} minutos\n2 - {} minutos\n3 - {} minutos\n".format(tempo_chegada3,tempo_chegada2,tempo_chegada1))
    return podio


tempo_chegada1 = 120
tempo_chegada2 = 90
tempo_chegada3 = 110


print(podio_olimpico(3,2,1))

