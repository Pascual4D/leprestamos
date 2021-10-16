import streamlit as st
import pandas as pd
import joblib 

# cargar el modelo
modelo_cargado = joblib.load('modelo_prestamos.joblib')
# parametros de configuración
p1=0
p2=0
p3=0
p4=0
#credit = pd.read_csv('credit-approval.csv')

#campo=credit["TiempoEmpleado"].values
#media=campo.mean()
#ancho=campo.std()
#st.write(ancho,media)
ancho2=3.344087470333537
media2=2.223405797101449
#minimo=campo.min()
#st.write(minimo)

#campo=credit["PuntajeCredito"].values
#media=campo.mean()
#ancho=campo.std()
#st.write(ancho,media)
ancho3=4.8594148869466025
media3=2.4
#minimo=campo.min()
#st.write(minimo)

#campo=credit["Ingresos"].values
#media=campo.mean()
#ancho=campo.std()
#st.write(ancho,media)
ancho4=5206.325792733279
media4=1017.3855072463768
#maxp1=credit["Ingresos"].max()
#st.write(maxp1)
#minimo=campo.min()
#st.write(minimo)

st.write("## LE PRESTAMOS")

exp = ["No", "Si"]
opcion = st.selectbox("Has incumplido algún préstamo alguna vez?", exp)
if (opcion=="Si"):
    p1=1
else:
    p1=0

p2 = st.slider('Tiempo que ha estado Empleado en años ',0,30) 
p2= (p2-media2)/ancho2
p3 = st.slider('Puntaje de Credito',0,100) 
p3= (p3-media3)/ancho3
p4 = st.slider('Ingresos en dólares al año ',0,100000) 
p4 = (p4-media4)/ancho4

entrada=pd.DataFrame({'IncumplimientosPrevios': [p1], 'TiempoEmpleado': [p2], 'PuntajeCredito': [p3], 'Ingresos': [p4]})
datos=entrada.values
y_pred = modelo_cargado.predict(datos)
if (y_pred[0]==1):
    st.markdown("<p style='font-family:Courier; color:Green; font-size: 20px;'>OPCIONADO para préstamo</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='font-family:Courier; color:Red; font-size: 20px;'>No Opcionado para préstamo</p>", unsafe_allow_html=True)

#st.write(datos)    
st.write("##### Inteligencia Artificial")
st.write("##### Proyecto Productivo I.U. Pascual Bravo")
st.write("##### jorgejuliansanchezvelez@pascualbravo.edu.co")