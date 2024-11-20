
import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(page_title="DataDynamite Solution", layout="wide")

def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

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
        dashboard_image = Image.open("dashboard.jpg")
        st.image(dashboard_image, use_container_width=True)

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
        st.markdown("<h2 style='text-align: center; background-color: black; color: white; padding: 10px;'>Historical Data Analysis</h2>", unsafe_allow_html=True)

        st.markdown(
            "<h3>Understanding the Context of Dimensional Defects</h3>"
            "<p style='text-align: justify;'>In the Hot Rolling Process of Mill 4 at Ternium, the occurrence of dimensional defects has "
            "presented significant challenges in maintaining product quality and operational efficiency. Dimensional defects impact the precision and usability of sheet metal, "
            "leading to increased costs and inefficiencies. This section explores the historical data we analyzed to identify root causes and patterns.</p>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<h3>Data Collection and Initial Analysis</h3>"
            "<p style='text-align: justify;'>Our team at DataDynamite conducted a descriptive analysis of the available historical "
            "data. This involved:</p>"
            "<ul style='text-align: justify;'>"
            "<li><strong>Data Exploration and Cleaning:</strong> Initial examination focused on identifying data types and structuring the information effectively, setting a solid foundation for deeper analysis.</li>"
            "<li><strong>Meeting with Ternium:</strong> Discussions with Ternium stakeholders guided our understanding of process nuances and allowed us to align our analytical approach with the company’s operational realities.</li>"
            "</ul>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<h3>Historical Trends and Patterns</h3>"
            "<p style='text-align: justify;'>Based on our analysis of historical production data, we identified several recurring patterns in defects, "
            "such as the influence of material thickness, and machine settings. By identifying patterns in the data, we could propose process optimizations and predictive analytics solutions for improving product quality.</p>",
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