import streamlit as st
from PIL import Image
import os
import matplotlib

# Page configuration
st.set_page_config(page_title="DataDynamite Solution", layout="wide")

# Custom CSS for styling
st.markdown("""
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
    background-color: #D32F2F; /* Rouge vif */
    border-radius: 0.5em;
}
.stRadio > div > label:hover {
    background-color: #C62828; /* Rouge légèrement plus foncé */
    border-radius: 0.3em;
}
.stButton > button {
    background-color: #D32F2F; /* Rouge vif */
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
    background-color: #D32F2F; /* Rouge vif */
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
</style>""", unsafe_allow_html=True)

# Reset password page
def reset_password_page():
    st.markdown("<h2 style='text-align: center;'>Réinitialisation de mot de passe</h2>", unsafe_allow_html=True)
    email = st.text_input("Entrez votre email", "")

    if st.button("Envoyer la demande de réinitialisation"):
        if email:
            st.success("Un lien de réinitialisation de mot de passe a été envoyé à votre adresse e-mail.")
            # Ici vous pouvez intégrer une logique pour envoyer réellement un e-mail de réinitialisation
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

    # "Forgot Password" link
    st.markdown("<p style='text-align: center;'><a href='#' style='color: #D32F2F;' onclick='show_reset_password();'>Forgot Password ?</a></p>", unsafe_allow_html=True)

    # Show reset password form when link is clicked
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
            'Cluster': '/content/Cluster',
            'Cluster1': '/content/Cluster1',
            'Cluster2': '/content/Cluster2',
            'GoodCluster': '/content/GoodCluster',
            'GoodCluster1': '/content/GoodCluster1',
            'GoodCluster2': '/content/GoodCluster2'
        }

        # Vérification de l'existence des dossiers
        for folder in folders.values():
            if not os.path.exists(folder):
                st.write(f"Le dossier {folder} n'est pas trouvé.")

        # Fonction pour afficher l'image
        def display_image(cluster_folder, goodcluster_folder, selected_image):
            cluster_image_path = os.path.join(cluster_folder, selected_image)
            goodcluster_image_path = os.path.join(goodcluster_folder, selected_image)

            # Vérification si l'image existe dans 'goodcluster'
            if os.path.exists(goodcluster_image_path):
                # Chargement des deux images
                cluster_img = mpimg.imread(cluster_image_path)
                goodcluster_img = mpimg.imread(goodcluster_image_path)

                # Affichage des deux images côte à côte
                fig, axes = plt.subplots(1, 2, figsize=(12, 6))

                # Affichage de l'image du dossier 'cluster'
                axes[0].imshow(cluster_img)
                axes[0].set_title(f"Cluster: {selected_image}")
                axes[0].axis('off')

                # Affichage de l'image du dossier 'goodcluster'
                axes[1].imshow(goodcluster_img)
                axes[1].set_title(f"GoodCluster: {selected_image}")
                axes[1].axis('off')

                st.pyplot(fig)  # Affichage avec Streamlit
            else:
                st.write(f"L'image {selected_image} n'existe pas dans '{goodcluster_folder}'.")

        # Interface utilisateur avec Streamlit
        st.title("Sélectionnez un dossier et une image")

        # Sélectionner un dossier Cluster et GoodCluster
        cluster_choice = st.selectbox('Choisir un dossier Cluster:', ['Cluster', 'Cluster1', 'Cluster2'])
        goodcluster_choice = st.selectbox('Choisir un dossier GoodCluster:', ['GoodCluster', 'GoodCluster1', 'GoodCluster2'])

        # Déterminer les dossiers correspondants
        cluster_folder = folders[cluster_choice]
        goodcluster_folder = folders[goodcluster_choice]

        # Liste des images disponibles dans le dossier sélectionné
        cluster_images = [f for f in os.listdir(cluster_folder) if os.path.isfile(os.path.join(cluster_folder, f))]

        # Sélectionner l'image à afficher
        selected_image = st.selectbox('Sélectionner une image:', cluster_images)

        # Afficher l'image
        if selected_image:
            display_image(cluster_folder, goodcluster_folder, selected_image)
            page = st.radio(
                label="",
                options=["Welcome", "Our Client", "Historical Data Analysis", "Our Approach", "Contact Us"],
                horizontal=True
            )

    # Welcome Page
    if page == "Welcome":
        st.markdown("<h2 style='text-align: center;'>Welcome to DataDynamite Solution!</h2>", unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: center;'>At DataDynamite, we provide cutting-edge data solutions for manufacturing industries. "
            "Explore our approach to solving dimensional defects and improving production processes at Ternium.</p>", unsafe_allow_html=True)

    # OurClient Page
    elif page == "Our Client":
        st.markdown("<h2 style='text-align: center; background-color: black; color: white; padding: 10px;'>Our Client: Ternium</h2>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 3, 1])  # Crée 3 colonnes avec la colonne du milieu plus large
        with col2:
            st.image("usine.jpeg", caption="", width=800)

        st.markdown(
            "<p style='text-align: justify;'>Ternium is a leading steel producer in Latin America, with a strong presence in Mexico, Argentina, Brazil, and the United States. "
            "Founded in 2005, Ternium focuses on providing high-quality steel products and solutions for various industries, including construction, "
            "automotive, and manufacturing. The company operates several state-of-the-art steel plants that utilize advanced technologies to ensure efficiency and sustainability.</p>", unsafe_allow_html=True)

    # Historical Data Analysis Page
    elif page == "Historical Data Analysis":
        st.markdown("<h2 style='text-align: center; background-color: black; color: white; padding: 10px;'>Historical Data Analysis</h2>", unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: justify;'>Our team has analyzed historical data from Ternium's production processes to identify patterns and predict dimensional defects in steel coils. "
            "By using advanced statistical models and machine learning algorithms, we aim to improve production quality and reduce defects, ensuring the delivery of high-quality steel products.</p>", unsafe_allow_html=True)

    # Our Approach Page
    elif page == "Our Approach":
        st.markdown("<h2 style='text-align: center; background-color: black; color: white; padding: 10px;'>Our Approach</h2>", unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: justify;'>At DataDynamite, we utilize state-of-the-art machine learning algorithms and advanced data analytics techniques to tackle complex challenges in manufacturing. "
            "Our approach involves understanding the underlying data, identifying key factors contributing to defects, and developing predictive models to optimize production processes.</p>", unsafe_allow_html=True)

    # Contact Us Page
    elif page == "Contact Us":
        st.markdown("<h2 style='text-align: center; background-color: black; color: white; padding: 10px;'>Contact Us</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>For more information, feel free to reach out to us:</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Email: info@datadynamite.com</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Phone: +1-800-555-1234</p>", unsafe_allow_html=True)

# Main logic to check if user is logged in
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    main_page()
else:
    login_page()
