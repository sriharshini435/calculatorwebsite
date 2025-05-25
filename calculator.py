import streamlit as st
a=st.number_input('first number',value=0)
b=st.number_input('second number',value=0)
operator =st.text_input('enter the operator symbol')
if st.button('display:'):
    if operator=='+':
        ans=a+b
        st.write(f"the additionof{a} and {b}is :{ans}")

    elif operator == '-':
        ans = a - b
        st.write(f"the subtraction of{a} and {b}is :{ans}")
    
    elif operator == '*':
        ans = a * b
        st.write(f"the multiplication of{a} and {b}is :{ans}")

    elif operator == '/':
        ans = a / b
        st.write(f"the division of{a} and {b}is :{ans}")

    elif operator == '%':
        ans = a % b
        st.write(f"the modulus of{a} and {b}is :{ans}")

    elif operator == '//':
        ans = a // b
        st.write(f"the  of{a} floordivision and {b}is :{ans}")

    elif operator == '**':
        ans = a ** b
        st.write(f"the  of{a} exponents and {b}is :{ans}")
    else :
        st.error('pls enter a valid operator symbol')

      
