st = '     eu      adoro    python     '

st = st.strip()

while ('  ' in st):
    st = st.replace('  ', ' ')

print('[',st, ']', sep='')