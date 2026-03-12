print('==Version Imperativa ==')
#Estudiante y sus notas
nombre_estudiante= 'Juan'
nota1=4.5
nota2=3.8
nota3=4.2
#Calcular promedio
suma=nota1+nota2+nota3
promedio=suma/3
#Determinar si aprobo
if promedio>=3.0:
    estado='APROBO'
else:
    eatdo='REPROBO'
print(f'{nombre_estudiante}:{promedio:.2f} - {estado}')

