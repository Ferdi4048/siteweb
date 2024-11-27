import streamlit as st
from PIL import Image
import webbrowser
# Page configuration
st.set_page_config(page_title="DataDynamite Solution", layout="wide")

# Custom CSS for styling
st.markdown("""<style>
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
        url = "https://dashboard-adftzwppw9b6u7hnabiwmn.streamlit.app/"
        webbrowser.open(url)
        
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
            "automotive, and manufacturing. The company operates several state-of-the-art steel plants that utilize advanced technologies to ensure efficiency and sustainability.</p>",
            unsafe_allow_html=True
        )

        st.markdown("<h3 style='text-align: center;'>Objectives of Ternium</h3>", unsafe_allow_html=True)
        st.markdown(
            "<ul style='text-align: justify;'>"
            "<li><strong>Sustainability:</strong> Ternium aims to minimize its environmental impact by adopting eco-friendly practices and technologies throughout its production processes.</li>"
            "<li><strong>Innovation:</strong> The company is committed to investing in research and development to create new products that meet the evolving needs of its customers.</li>"
            "<li><strong>Quality:</strong> Ternium strives to maintain the highest quality standards in its products, ensuring customer satisfaction and loyalty.</li>"
            "<li><strong>Operational Excellence:</strong> The organization focuses on optimizing its operations to improve efficiency, reduce costs, and enhance productivity.</li>"
            "</ul>",
            unsafe_allow_html=True
        )

        st.markdown("<h3 style='text-align: center;'>Key Highlights</h3>", unsafe_allow_html=True)
        st.markdown(
            "<ul style='text-align: justify;'>"
            "<li><strong>Production Capacity:</strong> Ternium has a total production capacity of over 10 million tons of steel per year, making it one of the largest steel producers in the region.</li>"
            "<li><strong>Product Range:</strong> The company offers a wide range of steel products, including hot-rolled and cold-rolled sheets, galvanized sheets, and special steel grades.</li>"
            "<li><strong>Commitment to Community:</strong> Ternium actively engages with local communities through social responsibility programs aimed at education, health, and sustainable development.</li>"
            "</ul>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<p style='text-align: justify;'>In conclusion, Ternium is dedicated to providing high-quality steel products while promoting sustainability and innovation. "
            "Through its commitment to operational excellence and community engagement, Ternium continues to strengthen its position as a leader in the steel industry.</p>",
            unsafe_allow_html=True
        )

    # HistoricalDataAnalysis Page
    elif page == "Historical Data Analysis":
        st.markdown("<h2 style='text-align: center; color: white; background-color: black; padding: 10px;'>Detailed Summary of the Machine Learning Project</h2>", unsafe_allow_html=True)

        st.markdown(
        "<h3>Introduction</h3>"
        "<p style='text-align: justify;'>"
        "The project carried out by the <em>Data Dynamite</em> team focuses on analyzing and resolving dimensional defects in metal slabs produced at Ternium’s hot rolling mill. "
        "Using a methodological approach based on the CRISP-DM (Cross-Industry Standard Process for Data Mining) framework, the students explored and analyzed data to address "
        "industrial challenges by applying various machine learning models."
        "</p>",
        unsafe_allow_html=True
        )

        st.markdown(
        "<h3>Methodology and Predictive Models</h3>"
        "<p style='text-align: justify;'>"
        "The methodology combined supervised and unsupervised learning techniques:</p>"
        "<ul style='text-align: justify;'>"
        "<li><strong>K-Means Clustering:</strong> This algorithm grouped slabs into clusters based on their physical properties.</li>"
        "<li><strong>Supervised Validation:</strong> The clusters were compared to labeled data to verify their consistency with known defects.</li>"
        "</ul>"
        "<p style='text-align: justify;'>"
        "K-Means was chosen for its ability to group unlabeled data, revealing intrinsic patterns. The resulting clusters were interpreted and linked to defect categories through visualization tools and discussions with experts."
        "</p>",
        unsafe_allow_html=True
        )

        st.markdown(
        "<h3>Results and Analysis</h3>"
        "<h4>1. Clustering by Weight</h4>"
        "<p style='text-align: justify;'>"
        "Slabs were divided into three groups: lightweight, medium weight, and heavyweight. Lightweight slabs were more prone to dimensional defects."
        "</p>",
        unsafe_allow_html=True
        )
        st.image("image1.png", caption="K-Means Clustering on Slab Weight (Image 1)")
     

        st.markdown(
        "<h4>2. Clustering by Length</h4>"
        "<p style='text-align: justify;'>"
        "Shorter slabs exhibited greater variability and a higher risk of defects, whereas longer slabs displayed more consistent quality. "
        "</p>",
        unsafe_allow_html=True
        )
        st.image("image3.png", caption="K-Means Clustering on Slab Length (Image 3)")
        
        st.markdown(
        "<h4>3. Clustering by Thickness</h4>"
        "<p style='text-align: justify;'>"
        "Thinner slabs were more susceptible to production issues, while thicker slabs exhibited greater consistency."
        "</p>",
        unsafe_allow_html=True
        )
        st.image("image5.png", caption="K-Means Clustering on Slab Thickness (Image 5)")
        
        st.markdown(
        "<h4>4. Cluster Validation</h4>"
        "<p style='text-align: justify;'>"
        "Validation confirmed that certain clusters strongly correlated with specific defects, enabling prioritization of high-risk slab families. We identified three distinct weight-based groups: lightweight, medium weight, and heavyweight slabs. These clusters revealed clear patterns in slab weight distribution across the dataset. Lightweight slabs were associated with a higher frequency of dimensional inconsistencies, while heavyweight slabs demonstrated better overall quality."
        "</p>",
        unsafe_allow_html=True
        )

        st.markdown(
        "<h3>Actionable Insights</h3>"
        "<ul style='text-align: justify;'>"
        "<li><strong>Weight-Length Interactions:</strong> Lightweight and short slabs should be prioritized for quality checks.</li>"
        "<li><strong>Thickness Variability:</strong> Stricter controls for thinner slabs are necessary to reduce production inconsistencies.</li>"
        "<li><strong>Cluster-Driven Quality Management:</strong> Integrating clustering results into Ternium’s quality management system would enable more efficient prioritization.</li>"
        "</ul>",
        unsafe_allow_html=True
        )

        st.markdown(
        "<h3>Model Validation and Limitations</h3>"
        "<p style='text-align: justify;'>"
        "Validation was based on comparisons with labeled data and historical trend analysis. However, several limitations were identified:</p>"
        "<ul style='text-align: justify;'>"
        "<li><strong>High Dimensionality:</strong> The inclusion of additional variables, such as production temperature, could improve clustering accuracy.</li>"
        "<li><strong>Data Imbalance:</strong> Some slab categories were overrepresented, potentially biasing clustering results.</li>"
        "<li><strong>Lack of Dynamic Variables:</strong> Analysis was limited to static physical attributes, excluding dynamic process variables like rolling speed.</li>"
        "</ul>",
        unsafe_allow_html=True
        )
       

        st.markdown(
        "<h3>Future Directions</h3>"
        "<ul style='text-align: justify;'>"
        "<li>Incorporate dynamic process variables (e.g., rolling speed, temperature) into clustering analysis.</li>"
        "<li>Explore alternative algorithms, such as DBSCAN, to capture non-linear relationships.</li>"
        "<li>Apply resampling techniques to balance data and reduce biases.</li>"
        "</ul>",
        unsafe_allow_html=True
        )

        st.markdown(
        "<h3>Conclusion</h3>"
        "<p style='text-align: justify;'>"
        "This project established a scalable approach to identify and understand defects in the production process. By combining advanced algorithms and supervised validation, the team proposed actionable recommendations to optimize Ternium’s industrial processes. "
        "Future steps include integrating additional variables and exploring new algorithms for more refined analysis."
        "</p>",
        unsafe_allow_html=True
        )


    # Our Approach Page
    elif page == "Our Approach":
        st.markdown("<h2 style='text-align: center; background-color: black; color: white; padding: 10px;'>Our Approach</h2>", unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: justify;'>DataDynamite’s approach to solving dimensional defects in Ternium’s Hot Rolling Process is based on a combination of data science, machine learning, and process optimization. "
            "Our methodology involves the following steps:</p>"
            "<ul style='text-align: justify;'>"
            "<li><strong>Data Preprocessing:</strong> Cleaning, structuring, and transforming the data for further analysis.</li>"
            "<li><strong>Exploratory Data Analysis (EDA):</strong> Identifying key features and trends through statistical and visual analysis.</li>"
            "<li><strong>Machine Learning Implementation:</strong> Using supervised learning models to predict defect occurrences and fine-tune the process.</li>"
            "<li><strong>Model Evaluation and Optimization:</strong> Continuously improving the model for better prediction accuracy and operational efficiency.</li>"
            "</ul>",
            unsafe_allow_html=True
        )

    # Contact Us Page
    elif page == "Contact Us":
        st.markdown("<h2 style='text-align: center; background-color: black; color: white; padding: 10px;'>Contact Us</h2>", unsafe_allow_html=True)

        # Display image of the team
        st.image("team.png", caption="The DataDynamite Team", width=1350)

        st.markdown("<h3 style='text-align: center;'>Get in Touch</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>If you have any questions or need further information, feel free to reach out to us!</p>", unsafe_allow_html=True)

        st.markdown(
            "<h4 style='text-align: center;'>Email: info@datadynamite.com </h4>"
            "<h4 style='text-align: center;'>Phone: +184 245 658 </h4>"
            "<h4 style='text-align: center;' Address: TEC Monterrey, Monterrey, Mexico> </h4>",
            unsafe_allow_html=True
        )

# Main script to check session and display appropriate page
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'reset_password' not in st.session_state:
    st.session_state.reset_password = False

if st.session_state.logged_in:
    main_page()  # Appelez la fonction de la page principale
else:
    login_page()  # Appelez la fonction de la page de connexion
