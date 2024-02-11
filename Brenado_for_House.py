import streamlit as st
from datetime import datetime, timedelta

# Setări inițiale
titlu_proiect = "Numele Proiectului"
descriere_proiect = "Acesta este un scurt rezumat al proiectului."
url_github = "https://github.com/username/proiect"
data_inceput = datetime(2024, 2, 9)
data_limita = datetime(2024, 3, 20)
data_curenta = datetime.now()

# Calcularea progresului
total_zile_proiect = (data_limita - data_inceput).days
zile_trecute = (data_curenta - data_inceput).days
progres = min(max(zile_trecute / total_zile_proiect, 0), 1)  # Asigură că progresul este între 0 și 1

# Construirea paginii Streamlit
st.title(titlu_proiect)
st.write(descriere_proiect)
st.progress(progres)

if progres < 1.0:
    st.write(f"Mai sunt {total_zile_proiect - zile_trecute} zile până la data limită.")
else:
    st.write("Proiectul a atins data limită!")

st.markdown(f"[*Repository GitHub*]({url_github})")

# Dacă dorești să adaugi mai multe elemente, poți continua cu st.write() sau alte funcții Streamlit
