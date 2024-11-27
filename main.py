import streamlit as st
from PIL import Image
import os

# Page configuration
st.set_page_config(page_title="DataDynamite Solution", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    header, footer {visibility: hidden;}
    .main {background-color: #f5f5f5; padding: 2rem;}
    .stRadio > div {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-bottom: 2rem;
    }
    .stRadio > div > label {
        color: white;
        font-size: 1.2em;
        padding: 0.5em;
        cursor: pointer;
        background-color: #D32F2F;
        border-radius: 0.5em;
    }
    .stRadio > div > label:hover {
        background-color: #C62828;
        border-radius: 0.3em;
    }
    .stButton > button {
        background-color: #D32F2F;
        color: white;
        font-size: 1.2em;
        border-radius: 0.5em;
        padding: 1em 2em;
        width: 100%;
        display: block;
        margin: 0 auto;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border: none;
        transition: background-color 0.3s, transform 0.2s;
    }
    .logo {width: 150px; height: auto;}
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #D32F2F;
        color: white;
        text-align: center;
        padding: 1rem 0;
        font-size: 0.9em;
    }
    .footer a {
        color: white;
        text-decoration: none;
        margin: 0 10px;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="footer">
        © 2023 DataDynamite Solutions. All rights reserved.
        <br>
        <a href="#">Privacy Policy</a> |
        <a href="#">Terms of Service</a> |
        <a href="mailto:info@datadynamite.com">Contact Us</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Reset password page
def reset_password_page():
    st.markdown("<h2 style='text-align: center;'>Réinitialisation de mot de passe</h2>", unsafe_allow_html=True)
    email = st.text_input("Entrez votre email", "")
    if st.button("Envoyer la demande de réinitialisation"):
        if email:
            st.success("Un lien de réinitialisation de mot de passe a été envoyé à votre adresse e-mail.")
            # Ajoutez ici la logique pour envoyer réellement un e-mail de réinitialisation
        else:
            st.error("Veuillez entrer une adresse e-mail valide.")

# Login page with "Forgot Password" link
def login_page():
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col1:
        st.image("ternium.png", width=150)
    with col3:
        st.image("dynamite.png", width=120)
    with col5:
        st.image("tec.png", width=80)

    email = st.text_input("Email", "")
    password = st.text_input("Password", "", type="password")

    if st.button("Login"):
        if email == "admin@ternium.com" and password == "datadynamite":
            st.session_state.logged_in = True
            st.success("Login successful! Redirecting to the dashboard...")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials. Please try again.")

    st.markdown(
        "<p style='text-align: center;'>"
        "<a href='#' style='color: #D32F2F;' onclick='show_reset_password();'>Forgot Password ?</a>"
        "</p>",
        unsafe_allow_html=True
    )

    if 'reset_password' in st.session_state and st.session_state.reset_password:
        reset_password_page()

# Main page content when logged in
def main_page():
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col1:
        st.image("ternium.png", width=150)
    with col3:
        st.image("dynamite.png", width=120)
    with col5:
        st.image("tec.png", width=80)

    st.markdown("<h1 style='text-align: center;'>DataDynamite Solution</h1>", unsafe_allow_html=True)

    if st.button("Click here to view the dashboard"):
        folders = {
            'Cluster': 'Cluster',
            'Cluster1': 'Cluster1',
            'Cluster2': 'Cluster2',
            'GoodCluster': 'GoodCluster',
            'GoodCluster1': 'GoodCluster1',
            'GoodCluster2': 'GoodCluster2'
        }

        for folder in folders.values():
            if not os.path.exists(folder):
                st.warning(f"Le dossier {folder} n'est pas trouvé.")

        def display_image(cluster_folder, goodcluster_folder, selected_image):
            cluster_image_path = os.path.join(cluster_folder, selected_image)
            goodcluster_image_path = os.path.join(goodcluster_folder, selected_image)

            if os.path.exists(goodcluster_image_path):
                col1, col2 = st.columns(2)
                with col1:
                    st.image(cluster_image_path, caption=f"Cluster: {selected_image}", use_container_width=True)
                with col2:
                    st.image(goodcluster_image_path, caption=f"GoodCluster: {selected_image}", use_container_width=True)
            else:
                st.warning(f"L'image {selected_image} n'existe pas dans '{goodcluster_folder}'.")

        cluster_choice = st.selectbox('Choisir un dossier Cluster:', ['Cluster', 'Cluster1', 'Cluster2'])
        goodcluster_choice = st.selectbox('Choisir un dossier GoodCluster:', ['GoodCluster', 'GoodCluster1', 'GoodCluster2'])

        cluster_folder = folders[cluster_choice]
        goodcluster_folder = folders[goodcluster_choice]
        cluster_images = [f for f in os.listdir(cluster_folder) if os.path.isfile(os.path.join(cluster_folder, f))]
        selected_image = st.selectbox('Sélectionner une image:', cluster_images)

        if selected_image:
            display_image(cluster_folder, goodcluster_folder, selected_image)

# Application logic
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    main_page()
else:
    login_page()
