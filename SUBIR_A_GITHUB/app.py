import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Las 3 Clases | Daniel Antonanzas",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling to match the original brand
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&family=Caveat:wght@700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    .main-header {
        background: linear-gradient(135deg, #182848 0%, #4b6cb7 100%);
        padding: 2.2rem 2rem;
        border-radius: 14px;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.15);
    }
    .badge-tag {
        background-color: #ffd166;
        color: #1a1a1a;
        padding: 0.35rem 0.9rem;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.85rem;
        display: inline-block;
        margin-bottom: 0.8rem;
    }
    .card-box {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
    }
    .card-title {
        color: #1e293b;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <span class="badge-tag">Dani · Las Clases de TDAH Power</span>
    <h1 style="color:white; margin:0; font-size:2.2rem;">Las 3 Clases Completas & Testimonios</h1>
    <p style="color:#e2e8f0; margin-top:0.6rem; font-size:1.05rem;">Respaldo y reproductor completo de las sesiones y experiencias de las familias</p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
menu = st.sidebar.radio(
    "Navegación:",
    ["🏫 Índice de Clases", "1️⃣ Clase 1", "2️⃣ Clase 2", "3️⃣ Clase 3", "💬 Testimonios de Familias", "📥 Enlaces y Descargas Directas"]
)

if menu == "🏫 Índice de Clases":
    st.subheader("Selecciona una de las 3 clases para verla:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card-box">
            <span style="color:#ef4444; font-weight:700;">Clase 01 · Martes 3</span>
            <div class="card-title">Por qué tu hijo se bloquea, se olvida de todo y explota</div>
            <p style="color:#64748b; font-size:0.9rem;">...aunque sea listísimo. Las claves biológicas y emocionales del TDAH explicadas sin rodeos.</p>
        </div>
        """, unsafe_allow_html=True)
        st.image("https://i.ytimg.com/vi/ETXBHHTJ4JY/maxresdefault.jpg", use_container_width=True)
        st.info("Vídeo completo disponible en la pestaña 'Clase 1'.")

    with col2:
        st.markdown("""
        <div class="card-box">
            <span style="color:#3b82f6; font-weight:700;">Clase 02 · Miércoles 4</span>
            <div class="card-title">Cómo devolverle la calma y activar su motor</div>
            <p style="color:#64748b; font-size:0.9rem;">Sin premios eternos ni amenazas que destruyen la relación en casa.</p>
        </div>
        """, unsafe_allow_html=True)
        st.image("https://i.ytimg.com/vi/Vmgy6PYByIo/maxresdefault.jpg", use_container_width=True)
        st.info("Vídeo completo disponible en la pestaña 'Clase 2'.")

    with col3:
        st.markdown("""
        <div class="card-box">
            <span style="color:#10b981; font-weight:700;">Clase 03 · Jueves 5</span>
            <div class="card-title">La estructura que le da seguridad y su superpoder</div>
            <p style="color:#64748b; font-size:0.9rem;">El superpoder que esconde su TDAH y el método para convertirte en su copiloto.</p>
        </div>
        """, unsafe_allow_html=True)
        st.image("https://vz-668e1210-356.b-cdn.net/805d6528-9a0c-43fa-9756-d5fb9dc076a3/thumbnail.jpg", use_container_width=True)
        st.info("Vídeo alojado en Bunny Stream (~1.5 GB). Disponible en la pestaña 'Clase 3'.")

elif menu == "1️⃣ Clase 1":
    st.markdown("## Clase 01: Por qué tu hijo se bloquea, se olvida de todo y explota, *aunque sea listísimo*")
    st.caption("Martes 3 de noviembre · TDAH Power")
    
    components.html("""
    <div style="position:relative; width:100%; aspect-ratio:16/9;">
        <iframe width="100%" height="100%" src="https://www.youtube-nocookie.com/embed/ETXBHHTJ4JY?rel=0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius:12px;"></iframe>
    </div>
    """, height=500)
    
    st.markdown("### Lo que escriben las familias después de esta clase:")
    st.markdown("""
    > *"Dani, eres extraordinario! Has sacado todas mis emociones, he llorado mucho, me he reconocido en muchos momentos. Nadie me había explicado el TDAH como tú lo has hecho, ¡tú sí eres un FARERO! Gracias por tu luz."*  
    > **— Rebeca (@rebecatribaldos341)**
    """)

elif menu == "2️⃣ Clase 2":
    st.markdown("## Clase 02: Cómo devolverle la calma y activar su motor, *sin premios eternos ni amenazas*")
    st.caption("Miércoles 4 de noviembre · TDAH Power")
    
    components.html("""
    <div style="position:relative; width:100%; aspect-ratio:16/9;">
        <iframe width="100%" height="100%" src="https://www.youtube-nocookie.com/embed/Vmgy6PYByIo?rel=0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius:12px;"></iframe>
    </div>
    """, height=500)

elif menu == "3️⃣ Clase 3":
    st.markdown("## Clase 03: La estructura que le da seguridad y el superpoder que esconde su TDAH")
    st.caption("Jueves 5 de noviembre · Vídeo Original en Servidor Bunny Stream (1.52 GB)")
    
    components.html("""
    <div style="position:relative; width:100%; aspect-ratio:16/9;">
        <iframe width="100%" height="100%" src="https://iframe.mediadelivery.net/embed/780636/805d6528-9a0c-43fa-9756-d5fb9dc076a3" frameborder="0" allow="accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;" allowfullscreen="true" style="border-radius:12px;"></iframe>
    </div>
    """, height=500)
    
    st.markdown("---")
    st.success("💾 Enlace directo a la descarga del archivo MP4 (720p):")
    st.markdown("[👉 Descargar Clase 3 directamente (1.52 GB MP4)](https://vz-668e1210-356.b-cdn.net/805d6528-9a0c-43fa-9756-d5fb9dc076a3/play_720p.mp4)")

elif menu == "💬 Testimonios de Familias":
    st.subheader("Historias reales de familias y alumnos")
    st.write("Selecciona cualquiera de los testimonios para reproducir su experiencia:")
    
    testimonios = [
        {"nombre": "Marga", "rol": "Madre", "titulo": "De «no puedo, no me entero» a «tengo un Ferrari en mi cabeza»", "id": "44a5749f-57c1-465c-bca1-a9327b5dc9e6"},
        {"nombre": "Rafa", "rol": "Padre de un estudiante de Biotecnología", "titulo": "Hoy tiene las mejores notas de su curso en Biotecnología", "id": "bb898847-c09d-4d70-a167-2d278e867c15"},
        {"nombre": "Cristina", "rol": "Madre y profesora", "titulo": "«Por fin alguien que me entiende», me dijo mi hijo con 9 años", "id": "07120aa8-a944-4353-92ce-5145c6ae2cf9"},
        {"nombre": "Eugenia", "rol": "Madre de un adolescente", "titulo": "Pasó de repetir curso a entrar en la carrera que soñaba", "id": "61e8c3f0-f859-44b2-8be0-d45dd5f12fb8"},
        {"nombre": "Desy", "rol": "Madre de dos hijos con TDAH", "titulo": "Se acabaron las batallas diarias para hacer los deberes", "id": "7677bd43-80cf-4679-84e7-3e856ffab831"},
        {"nombre": "Ana", "rol": "Madre", "titulo": "La tranquilidad de saber que no estás solo en esto", "id": "f5630521-20f1-4e48-8b2c-1676183b6615"}
    ]
    
    seleccion = st.selectbox("Elige un testimonio:", [f"{t['nombre']} ({t['rol']}) - {t['titulo']}" for t in testimonios])
    elegido = next(t for t in testimonios if f"{t['nombre']} ({t['rol']}) - {t['titulo']}" == seleccion)
    
    st.markdown(f"### {elegido['nombre']} ({elegido['rol']})")
    st.markdown(f"**{elegido['titulo']}**")
    
    video_url = f"https://vz-668e1210-356.b-cdn.net/{elegido['id']}/play_720p.mp4"
    st.video(video_url)

elif menu == "📥 Enlaces y Descargas Directas":
    st.subheader("Índice de fuentes directas y copias de seguridad")
    st.markdown("""
    - **Clase 1 (YouTube):** [https://www.youtube.com/watch?v=ETXBHHTJ4JY](https://www.youtube.com/watch?v=ETXBHHTJ4JY)
    - **Clase 2 (YouTube):** [https://www.youtube.com/watch?v=Vmgy6PYByIo](https://www.youtube.com/watch?v=Vmgy6PYByIo)
    - **Clase 3 (Bunny Stream Direct MP4):** [Descargar MP4 720p (1.52 GB)](https://vz-668e1210-356.b-cdn.net/805d6528-9a0c-43fa-9756-d5fb9dc076a3/play_720p.mp4)
    - **Clase 3 (HLS Playlist):** `https://vz-668e1210-356.b-cdn.net/805d6528-9a0c-43fa-9756-d5fb9dc076a3/playlist.m3u8`
    """)
