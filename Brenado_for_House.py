import streamlit as st
from datetime import datetime, timedelta

# Setări inițiale
titlu_proiect = "Brenado for House"
descriere_proiect = "Acesta este un scurt rezumat al proiectului."
url_github = "https://castemill.com"
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

st.markdown(f"[*Partener app*]({url_github})")


# Secțiunea pentru documente
st.header(":blue[Documente Încărcate]", divider="rainbow")
# Lista de documente de exemplu
documente = [
    {"nume": "Document 1", "stadiu": "Încărcat"},
    {"nume": "Document 2", "stadiu": "În procesare"},
    {"nume": "Document 3", "stadiu": "Finalizat"}
]

for doc in documente:
    # Logica pentru a afișa fiecare document și stadiul său
    st.subheader(doc["nume"])
    st.write(f"Stadiu: {doc['stadiu']}")


# Încărcarea de noi documente
st.header("Încărcare Documente Noi")
uploaded_file = st.file_uploader("Alege un document", type=["pdf", "docx", "txt"])
if uploaded_file is not None:
    # Aici poți adăuga logica pentru procesarea și salvarea documentului încărcat
    st.write("Document încărcat cu succes!")
