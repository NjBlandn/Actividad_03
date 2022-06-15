# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 11:05:18 2022

@author: Dell
"""

import tkinter as tk
from tkinter.messagebox import showinfo

 #crear ventana
vent = tk.Tk()                 
vent.geometry('700x600')
#agregar titulo
vent.title('Plan de Vuelo Fotogramétrico')    
vent.config(bg= 'silver')

###########################################################################
#Agregar etiqueta 1
etiq1 = tk.Label(vent, text='Distancia focal (mm)', bg='silver',  fg='black')
etiq1.grid(row = 0, column = 0)

  #Agregar caja 1
df = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
df.grid(row = 1, column = 0)

############################################################################
#Agregar etiqueta 2
etiq2 = tk.Label(vent, text='Ancho de imagen (pixel)', bg='silver',  fg='black')
etiq2.grid(row = 0, column = 1)

   #Agregar caja 2
ani = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
ani.grid(row = 1, column = 1)

#############################################################################
#Agregar etiqueta 3
etiq3 = tk.Label(vent, text='Alto de imagen (pixel)', bg='silver',  fg='black')
etiq3.grid(row = 0, column = 2)

   #Agregar caja 3
ali = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
ali.grid(row = 1, column = 2)

#############################################################################
#Agregar etiqueta 4
etiq4 = tk.Label(vent, text='Ancho del sensor (mm)', bg='silver',  fg='black')
etiq4.grid(row = 2, column = 0)

   #Agregar caja 4
ans = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
ans.grid(row = 3, column = 0)

############################################################################
#Agregar etiqueta 5
etiq5 = tk.Label(vent, text='Alto del sensor (mm)', bg='silver',  fg='black')
etiq5.grid(row = 2, column = 1)

   #Agregar caja 5
als = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
als.grid(row = 3, column = 1)

############################################################################
#Agregar etiqueta 6
etiq6 = tk.Label(vent, text='Altura de vuelo (m)', bg='silver',  fg='black')
etiq6.grid(row = 2, column = 2)

#Agregar caja 6
alv = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
alv.grid(row = 3, column = 2)

############################################################################
#Agregar etiqueta 7
etiq7 = tk.Label(vent, text='Solape longitudinal (%)', bg='silver',  fg='black')
etiq7.grid(row = 4, column = 0)

#Agregar caja 7
sl = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
sl.grid(row = 5, column = 0)

#############################################################################
#Agregar etiqueta 8
etiq8 = tk.Label(vent, text='Solape transversal (%)', bg='silver',  fg='black')
etiq8.grid(row = 4, column = 1)

   #Agregar caja 8
st = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
st.grid(row = 5, column = 1)

#############################################################################
#Agregar etiqueta 9
etiq9 = tk.Label(vent, text='Largo parcela (m)', bg='silver',  fg='black')
etiq9.grid(row = 4, column = 2)

#Agregar caja 9
lp = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
lp.grid(row = 5, column = 2)

##############################################################################
#Agregar etiqueta 10
etiq10 = tk.Label(vent, text='Ancho parcela (m)', bg='silver',  fg='black')
etiq10.grid(row = 6, column = 0)

#Agregar caja 10
ap = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
ap.grid(row = 7, column = 0)

##############################################################################
#Agregar etiqueta 11
etiq11 = tk.Label(vent, text='Velocidad de vuelo (m/s)', bg='silver',  fg='black')
etiq11.grid(row = 6, column = 1)

   #Agregar caja 11
vv = tk.Entry(vent, font= 'Helvetica 10', justify = 'center')
vv.grid(row = 7, column = 1)

##############################################################################

textResult = tk.Text(vent, font = 'Helvetica 10', bg = 'black', fg = 'yellow')         #cuadro de texto                                
textResult.grid(row = 9, column = 0, columnspan = 3, padx = (50,50))


def calcular():
    ALV = float (alv.get())
    DF = float (df.get())
    ALIT = float (ali.get())
    ANS = float (ans.get())
    ANI = float (ani.get())
    ALS = float (als.get())
    SL = float (sl.get())
    ST = float (st.get())
    LP = float (lp.get())
    AP = float (ap.get())
    VV = float (vv.get())
    
    textResult.delete(1.0, tk.END)
    gds = (ALV*100/DF)*(ANS/ANI)
    GDS = 'GSD = 'f'{gds:.4} cm/ pixel\n=======================================\n'
    textResult.insert(tk.END, GDS)
  #convirtiendo en entero el resultado de la formula
    ev = int(1/((DF/1000)/ALV))      
    EV = 'Escala de Vuelo = 'f'{ev}\n=======================================\n'
    textResult.insert(tk.END, EV)
  #redondeando el resultado de la formula  
    anit = round((ANS*ev)/1000, 2)   
    ANIT = 'Ancho de imagen sobre terreno = 'f'{anit} m\n=======================================\n'
    textResult.insert(tk.END, ANIT)
 #redondeando el resultado de la formula
    alit = round((ALS*ev)/1000, 2)    
    ALIT = 'Altura de imagen sobre terreno = 'f'{alit} m\n=======================================\n'
    textResult.insert(tk.END, ALIT)
 #redondeando el resultado de la formula   
    ba = round(anit*(1-(SL/100)), 2)   
    BA = 'Base aerea = 'f'{ba} m\n=======================================\n'
    textResult.insert(tk.END, BA)
 #redondeando el resultado de la formula  
    dp = round(alit*(1-(ST/100)), 2)   
    DP = 'Distancia entre pasadas = 'f'{dp} m\n=======================================\n'
    textResult.insert(tk.END, DP)
 #redondeando el resultado de la formula   
    ief = round(ba/VV, 2)                 
    IEF = 'Tiempo entre fotos = 'f'{ief} s\n=======================================\n'
    textResult.insert(tk.END, IEF)
    
    np = round(AP/dp)                     #redondeando el resultado de la formula
    NP = 'Numero de pasadas = 'f'{np}\n=======================================\n'
    textResult.insert(tk.END, NP)
    
    nfp = round((LP/ba)+1)                 #redondeando el resultado de la formula
    NFP = 'Numero de fotos por pasada = 'f'{nfp}\n=======================================\n'
    textResult.insert(tk.END, NFP)
    
    nfv = round(nfp*np, 2)                     #redondeando el resultado de la formula
    NFV = 'Numero de fotos por vuelo = 'f'{nfv}\n=======================================\n'
    textResult.insert(tk.END, NFV)
    
    div = round((np*LP)+AP, 2)
    DIV = 'Distancia de vuelo = 'f'{div} m\n=======================================\n'
    textResult.insert(tk.END, DIV)
    
    duv = round((nfv*ief)/60, 2)
    DUV = 'Duracion del vuelo = 'f'{duv} min\n=======================================\n'
    textResult.insert(tk.END, DUV)
    
    message = 'Proceso finalizado con exito'
    showinfo('¡Finish!', message)
    
            
botoncal = tk.Button(text = 'Calcular', font = 'Helvetica 10', command = calcular)
botoncal.grid(row = 8, column = 1, pady = (10,10))


vent.mainloop()
