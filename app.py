import os
import streamlit as st
import streamlit.components.v1 as components

def mostrar_presente():

    # 1. O código JavaScript do "Improviso" (Scroll Reveal Dinâmico)
    scroll_reveal_js = """
    <script>
        const doc = window.parent.document;
        const elementos = doc.querySelectorAll('div[data-testid="stVerticalBlock"] > div');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
                // O "else" foi removido. Agora, uma vez que a foto aparece, ela fica fixa!
            });
        }, { threshold: 0.01 }); // Aciona logo que 1% do elemento aparecer

        elementos.forEach(el => {
            if (el.innerHTML.includes('heart')) return;
            el.style.transition = 'opacity 0.8s ease-out, transform 0.8s ease-out';
            
            // 0.05 é o segredo: quase invisível, mas obriga o celular a carregar as fotos!
            el.style.opacity = '0.05'; 
            el.style.transform = 'translateY(40px)';
            
            observer.observe(el);
        });
    </script>
    """
    components.html(scroll_reveal_js, height=0, width=0)

    # 2. Fundo do site e esconder os menus
    fundo_css = """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
    st.markdown(fundo_css, unsafe_allow_html=True)

    # 3. Corações injetados no Body
    coracoes_js = """
    <script>
        const doc = window.parent.document;
        if (!doc.getElementById("chuva-coracoes")) {
            const divCoracoes = doc.createElement('div');
            divCoracoes.id = "chuva-coracoes";
            divCoracoes.innerHTML = `
                <style>
                .heart {
                    position: fixed;
                    bottom: -10vh;
                    font-size: 30px;
                    z-index: 999999;
                    animation: floatUp 5s linear infinite;
                    pointer-events: none;
                }
                @keyframes floatUp {
                    0% { transform: translateY(0) scale(1); opacity: 1; }
                    100% { transform: translateY(-110vh) scale(1.5); opacity: 0; }
                }
                .h1 { left: 10%; animation-delay: 0s; }
                .h2 { left: 30%; animation-delay: 1.5s; }
                .h3 { left: 50%; animation-delay: 3s; }
                .h4 { left: 70%; animation-delay: 0.5s; }
                .h5 { left: 90%; animation-delay: 2s; }
                .h6 { left: 20%; animation-delay: 1s; }
                .h7 { left: 40%; animation-delay: 2.5s; }
                .h8 { left: 60%; animation-delay: 1.2s; }
                .h9 { left: 80%; animation-delay: 3.5s; }
                .h10 { left: 15%; animation-delay: 4s; }
                .h11 { left: 85%; animation-delay: 0.8s; }
                .h12 { left: 55%; animation-delay: 4.5s; }
                </style>
                <div class="heart h1">❤️</div>
                <div class="heart h2">💖</div>
                <div class="heart h3">❤️</div>
                <div class="heart h4">💖</div>
                <div class="heart h5">❤️</div>
                <div class="heart h6">💕</div>
                <div class="heart h7">❤️</div>
                <div class="heart h8">💗</div>
                <div class="heart h9">💖</div>
                <div class="heart h10">❤️</div>
                <div class="heart h11">💞</div>
                <div class="heart h12">💘</div>
            `;
            doc.body.appendChild(divCoracoes);
        }
    </script>
    """
    components.html(coracoes_js, height=0, width=0)

    # TITULOS CENTRALIZADOS DE FORMA RESPONSIVA (Sem usar colunas)
    st.markdown("<h1 style='text-align: center; color: #333;'>Anthony & Giovana ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #555;'>01 de Agosto de 2026</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #333; margin-top: 30px;'>Moments</h3>", unsafe_allow_html=True)

    # FOTOS (Usando 3 colunas padrão que se adaptam no celular)
    pasta_fotos = ".streamlit/images"
    if os.path.exists(pasta_fotos):
        arquivos = [f for f in os.listdir(pasta_fotos) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        if len(arquivos) > 0:
            col1, col2, col3 = st.columns(3)
            for i, arquivo in enumerate(arquivos):
                caminho_completo = os.path.join(pasta_fotos, arquivo)
                if i % 3 == 0:
                    with col1: st.image(caminho_completo, use_container_width=True)
                elif i % 3 == 1:
                    with col2: st.image(caminho_completo, use_container_width=True)
                else:
                    with col3: st.image(caminho_completo, use_container_width=True)
        else:
            st.warning("A pasta 'fotos' está vazia.")
    else:
        st.warning("A pasta 'fotos' não foi encontrada.")

    st.write("")
    st.write("")
    st.markdown("<h3 style='text-align: center; color: #333;'>Nossa Música 🎵</h3>", unsafe_allow_html=True)

    # MÚSICA (Usamos proporção 1:2:1 para não ficar gigante no PC, mas no celular ele arruma)
    msc1, msc2, msc3 = st.columns([1, 2, 1])
    with msc2:
        spotify_codigo = """
        <div style="
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            padding: 20px;
            border-radius: 24px;
            box-shadow: 0 10px 30px rgba(255, 75, 75, 0.4);
            border: 2px solid rgba(255, 255, 255, 0.5);
        ">
            <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/4PxTFojApbNeeIwiEEx2QX?utm_source=generator&si=7c0c6a58fe8f4b9f" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>
        """
        components.html(spotify_codigo, height=230)

    st.write("")
    st.markdown("<h2 style='text-align: center; color: #333;'>Sendo felizes juntos há...</h2>", unsafe_allow_html=True)

    # CRONÔMETRO
    crt1, crt2, crt3 = st.columns([1, 2, 1])
    with crt2:
        data_passada_js = "new Date(2026, 7, 1, 0, 0, 0).getTime()"
        contador_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body {{
                margin: 0; display: flex; justify-content: center; align-items: center;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #FF4B4B; 
            }}
            .timer-box {{
                text-align: center; background-color: #f0f2f6; padding: 20px 40px;
                border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); width: 100%;
            }}
            .numbers {{ font-size: 40px; font-weight: bold; margin: 0; }}
            .labels {{ font-size: 14px; color: #555; margin-top: -5px; }}
            
            /* AQUI ESTÁ A MÁGICA PARA O CELULAR! */
            @media (max-width: 600px) {{
                .numbers {{ font-size: 25px; }}
                .labels {{ font-size: 11px; }}
                .timer-box {{ padding: 15px 10px; }}
            }}
        </style>
        </head>
        <body>
        <div class="timer-box">
            <p class="numbers" id="relogio">Calculando...</p>
            <p class="labels">Dias : Horas : Minutos : Segundos</p>
        </div>  
        <script>
            var startDate = {data_passada_js};
            setInterval(function() {{
                var now = new Date().getTime();
                var distance = now - startDate;
                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);
                hours = hours < 10 ? "0" + hours : hours;
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;
                document.getElementById("relogio").innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
            }}, 1000);
        </script>
        </body>
        </html>
        """
        components.html(contador_html, height=150)

    # CARTINHA
    msg1, msg2, msg3 = st.columns([1, 2, 1])
    with msg2:
        quadro_mensagens = """
        <div style="
            background-color: #ffffff; padding: 30px; border-radius: 15px; 
            border-left: 8px solid #FF4B4B; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            margin-top: 20px; margin-bottom: 20px;
        ">
            <p style="font-size: 18px; color: #333; line-height: 1.6; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                <strong>Minha princesa,</strong><br><br>
                Desde o dia que você entrou na minha vida, ela tem mais cores, é mais viva, mais divertida, e a cada momento que passa
                eu tenho mais certeza que é você que eu quero para o resto da minha vida. Todos os nossos momentos são especiais e amo
                todos, quero ter uma família com a mulher mais incrível do mundo. Obrigado por me dar a oportunidade de fazer você feliz
                e cuidar de você, eu te amo ❤️<br>
                <strong>Anthony</strong>
            </p>
        </div>
        """
        st.markdown(quadro_mensagens, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: #333; padding-bottom: 50px;'>Eu te amo daqui até a eternidade</h2>", unsafe_allow_html=True)
