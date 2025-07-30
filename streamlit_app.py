import streamlit as st
import re

st.set_page_config(page_title="Botones", page_icon="🎛️")

st.markdown('''
            # Formulario de usuario
            '''
            )
    
nombre = st.text_input('Escribe tu nombre:')
apellido = st.text_input('Escribe tus apellidos:')
movil = st.text_input('Escribe tu numero de movil:')
email = st.text_input('Escribe tu email:')  
cp = st.text_input('Escribe tu código postal:') 

if nombre:
    if nombre.isalpha():
        nombre += ' ha sido verificado'
    else:
        nombre = "Nombre no válido, usa solo letras"
else:
    nombre = 'Campo vacío'
        
if apellido:
    if apellido.isalpha():
        apellido += ' ha sido verificado'
    else:
        apellido = "Apellidos no válido, usa solo letras"
else:
    apellido = 'Campo vacío'
        
if movil:
    if movil.isdigit() and len(movil) == 9:
        movil += ' ha sido verificado'
    else:
        movil = "Móvil no válido, usa solo 9 números"
else:
    movil = 'Campo vacío'
        
regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if email:
    if re.match(regex, email):
        email += ' ha sido verificado'
    else:
        email = "Email no válido, usa una estructura correcta"
else:
    email = 'Campo vacío'

if cp:
    if cp.isdigit() and len(cp) == 5:
        cp += ' ha sido verificado'
    else:
        cp = "Código Postal no válido, usa solo 5 números"
else:
    cp = 'Campo vacío'

if st.button('Verificar Formulario'):
    with st.container():
        
        st.markdown('## Resultado verificación:')
        st.markdown(f'''
                    
                :grey-background[:red[Nombre:]]
                
                {nombre}
                
                :grey-background[:red[Apellido:]]
                
                {apellido}
                
                :grey-background[:red[Móvil:]]
                
                {movil}
                
                :grey-background[:red[Email:]]
                
                {email}
                
                :grey-background[:red[Código Postal:]]
                
                {cp}
                ''')