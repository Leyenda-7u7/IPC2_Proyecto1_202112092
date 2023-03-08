
import subprocess
import os


                    
    

def crear_archivo_dot():
    mi_grafo = ''
    contador_periodo = 1
    # Hacer un for doble para contar las celdas contagiadas y las celdas
    # sanas. Usar dos contadores. Luego usar esos contadores para la
    # etiqueta del grafo
    
    contadorI=0
    contadorS=0
    for i in range(500):
        for j in range(500):
            nodo = 1
            if nodo == 1:
                contadorI += 1
                nodo+=1
                break
            else:
                contadorS+=1 
                
                
                
    mi_grafo = 'graph grid{\n' \
    'label="'+"organismo"+ "Rejilla No." +str(contador_periodo)+'\\n\\n Celulas Infectadas: '+ str(contadorI) +'               Celulas Sanas:'+ str(contadorS)+ '"\n'
    mi_grafo+='fontname="Helvetica,Arial,sans-serif"\n' \
    'node [fontname="Helvetica,Arial,sans-serif"]\n' \
    'edge [fontname="Helvetica,Arial,sans-serif"]\n' \
    'rankdir="LR"\n'\
    'layout=dot\n' \
    'labelloc = "t"\n' \
    'node [shape=box label=""]\n' \
    'edge [weight=1000 style=dashed color=dimgrey]\n'\
    
    contador_nodos = 0
    conexiones = ''
    
    
    for i in range(500):
        print()  
        for j in range(500):
            nodo = 1
            if nodo == 1:
                celda_infectada = f'"{contador_nodos}"[style="filled"   fillcolor="black"]\n' 
                mi_grafo += celda_infectada
                nodo+=1
                if j == 500 - 1:
                    conexiones += f'{contador_nodos}\n'
                else:
                    conexiones += f'{contador_nodos} -- '   
                contador_nodos += 1
                break
            else:
                if j == 500-1:
                    conexiones += f'{contador_nodos}\n'
                else:
                    conexiones += f'{contador_nodos} -- '
                contador_nodos += 1
                
                
                    
        
    mi_grafo += conexiones
    conexiones_vertical = ''
    for i in range(500):   
        contador_nodos = 0
        conexiones_vertical += 'rank="same" {'
        for j in range(500):
            if j != 500- 1:
                conexiones_vertical += f'{i+500} -- '
                contador_nodos += 1
                break
            else:
                conexiones_vertical += str(i+500)+'}\n'
    mi_grafo += conexiones_vertical
    mi_grafo += '}\n'

    
    print(mi_grafo)
    contador_periodo += 1
    print(contador_periodo)
    
    
    mi_archivo = open("Nuevo_archivo.dot", mode='w', encoding='utf-8')
    mi_archivo.write(mi_grafo)
    mi_archivo.close()
    subprocess.run(['dot', '-Tsvg', "Nuevo_archivo.dot", '-o', "Nuevo_archivo.svg"])
    os.startfile("Nuevo_archivo.svg")