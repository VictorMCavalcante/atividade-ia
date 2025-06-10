import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDW4oOCPtuh0Sqb5rYCNVn7j6XSR-eTQm4")
model = genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(
    page_title="Exercícios Streamlit + IA",
    page_icon="🚀",
    layout="wide"
)


def gerar_resposta_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"


st.sidebar.title("📚 Menu de Exercícios")
st.sidebar.write("Escolha um exercício para praticar:")

exercicio_selecionado = st.sidebar.selectbox(
    "Selecione o exercício:",
    [
        "🏠 Página Inicial",
        "👋 Exercício 1 - Saudação",
        "🎨 Exercício 2 - Cores",
        "🤖 Exercício 3 - Chat IA",
        "📚 Exercício IA 1 - Histórias",
        "🧑‍🍳 Exercício IA 2 - Receitas"
    ]
)

st.sidebar.divider()
st.sidebar.info("💡 **Dica:** Navegue pelos exercícios usando o menu acima!")
st.sidebar.caption("Criado com ❤️ usando Streamlit + Gemini AI")

if exercicio_selecionado == "🏠 Página Inicial":
    st.title("🚀 Exercícios de Streamlit + IA")

    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
        color: white;
    ">
        <h1 style="color: white; margin-bottom: 10px;">👨‍💻 Victor Medeiros Cavalcante</h1>
        <h3 style="color: #f8f9fa; margin-bottom: 0;">Entrega dos Exercícios de IA</h3>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.header("📋 Instruções para Navegação")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("""
        ### 🎯 Como Usar:
        1. **Use o menu lateral** para navegar
        2. **Selecione um exercício** da lista
        3. **Siga as instruções** de cada página
        4. **Preencha os campos** solicitados
        5. **Clique nos botões** para ver os resultados
        """)

    with col2:
        st.markdown("""
        ### 📚 Exercícios Disponíveis:
        
        **🔰 Exercícios Básicos:**
        - **Exercício 1:** Saudação personalizada com entrada de texto
        - **Exercício 2:** Seletor de cores interativo
        - **Exercício 3:** Chat básico com inteligência artificial
        
        **🚀 Exercícios Avançados com IA:**
        - **Exercício IA 1:** Criador de histórias personalizadas
        - **Exercício IA 2:** Gerador de receitas culinárias inteligente
        """)

    st.info("👈 **Comece agora!** Use o menu lateral para selecionar um exercício e começar a praticar.")

    st.success(
        "✨ **Projeto desenvolvido com:** Python, Streamlit e Google Gemini AI")

elif exercicio_selecionado == "👋 Exercício 1 - Saudação":
    st.title("👋 Exercício 1 - Saudação Personalizada")
    st.write("Digite seu nome e receba uma saudação personalizada!")

    nome = st.text_input(
        "Digite seu nome:",
        placeholder="Ex: Maria, João, Ana...",
        help="Digite seu nome completo ou apenas o primeiro nome"
    )

    if nome:
        nome_limpo = nome.strip()

        if nome_limpo:
            st.success(f"Olá, {nome_limpo}! Boas-vindas ao Streamlit! 🎉")
            st.info("✨ Que bom ter você aqui! Esperamos que aproveite a experiência.")
        else:
            st.warning("Por favor, digite um nome válido.")
    else:
        st.write("👆 Digite seu nome acima para receber uma saudação personalizada!")

elif exercicio_selecionado == "🎨 Exercício 2 - Cores":
    st.title("🎨 Exercício 2 - Seletor de Cores")
    st.write("Escolha sua cor favorita e veja uma mensagem personalizada!")

    cor_selecionada = st.selectbox(
        "Escolha uma cor:",
        ["Vermelho", "Verde", "Azul"],
        index=None,
        placeholder="Selecione uma cor..."
    )

    if cor_selecionada:
        cores_info = {
            "Vermelho": {"emoji": "🔴", "hex": "#FF0000", "rgb": "rgb(255, 0, 0)"},
            "Verde": {"emoji": "🟢", "hex": "#00FF00", "rgb": "rgb(0, 255, 0)"},
            "Azul": {"emoji": "🔵", "hex": "#0000FF", "rgb": "rgb(0, 0, 255)"}
        }

        info_cor = cores_info[cor_selecionada]

        st.success(
            f"Você selecionou a cor {cor_selecionada}! {info_cor['emoji']}")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Cor Escolhida", cor_selecionada)

        with col2:
            st.metric("Código HEX", info_cor['hex'])

        with col3:
            st.metric("Código RGB", info_cor['rgb'])

        st.markdown(f"""
            <div style="
                width: 100px; 
                height: 100px; 
                background-color: {info_cor['hex']}; 
                margin: 20px auto;
                border-radius: 10px;
                border: 2px solid #333;
            "></div>
        """, unsafe_allow_html=True)

        mensagens_cores = {
            "Vermelho": "Uma cor vibrante e cheia de energia! ❤️",
            "Verde": "A cor da natureza e da tranquilidade! 🌿",
            "Azul": "A cor do céu e do mar, muito relaxante! 🌊"
        }

        st.info(mensagens_cores[cor_selecionada])

    else:
        st.write("👆 Selecione uma cor acima para ver uma mensagem personalizada!")

        st.write("**Cores disponíveis:**")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("🔴 Vermelho")
        with col2:
            st.write("🟢 Verde")
        with col3:
            st.write("🔵 Azul")

elif exercicio_selecionado == "🤖 Exercício 3 - Chat IA":
    st.title("🤖 Exercício 3 - Chat com Gemini AI")
    st.write("Faça uma pergunta e obtenha uma resposta inteligente usando IA!")

    pergunta = st.text_area(
        "Digite sua pergunta:",
        placeholder="Ex: Qual é a capital do Brasil? Como funciona a inteligência artificial?",
        help="Faça qualquer pergunta e a IA irá responder!"
    )

    if st.button("🚀 Gerar Resposta com IA", type="primary"):
        if pergunta and pergunta.strip():
            with st.spinner("🤔 Pensando... Gerando resposta..."):
                resposta = gerar_resposta_gemini(pergunta.strip())

                st.write("**🤖 Resposta da IA:**")
                st.markdown(f"""
                    <div style="
                        background: linear-gradient(135deg, #f0f8ff, #e6f3ff);
                        padding: 20px;
                        border-radius: 10px;
                        border-left: 4px solid #4169e1;
                        margin: 15px 0;
                    ">
                        {resposta}
                    </div>
                """, unsafe_allow_html=True)

                st.success("✅ Resposta gerada com sucesso!")

        else:
            st.warning("⚠️ Por favor, digite uma pergunta válida.")

    with st.expander("💡 Sugestões de Perguntas"):
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Perguntas Gerais:**")
            st.write("• Qual é a capital do Brasil?")
            st.write("• Como funciona a fotossíntese?")
            st.write("• Explique o que é inteligência artificial")

        with col2:
            st.write("**Perguntas sobre Programação:**")
            st.write("• O que é Python?")
            st.write("• Como criar uma função em JavaScript?")
            st.write("• Explique o que é Streamlit")

elif exercicio_selecionado == "📚 Exercício IA 1 - Histórias":
    st.title("📚 Criador de Histórias Interativas com IA")
    st.write("Crie histórias únicas e personalizadas usando inteligência artificial!")

    st.header("🎭 Configure sua História")

    nome_protagonista = st.text_input(
        "Nome do Protagonista:",
        placeholder="Ex: Sofia, João, Aria, Draven...",
        help="Digite o nome do personagem principal da sua história"
    )

    genero_literario = st.selectbox(
        "Gênero Literário:",
        ["Fantasia", "Ficção Científica", "Mistério", "Aventura"],
        index=None,
        placeholder="Escolha o gênero da história..."
    )

    local_inicial = st.radio(
        "Local Inicial da História:",
        [
            "Uma floresta antiga",
            "Uma cidade futurista",
            "Um castelo assombrado",
            "Uma nave espacial à deriva"
        ]
    )

    frase_desafio = st.text_area(
        "Frase de Efeito ou Desafio Inicial:",
        placeholder="Ex: E de repente, tudo ficou escuro.\nO mapa indicava um perigo iminente.\nUm estranho ruído ecoou pela noite...",
        help="Esta frase será incorporada no início da história para criar suspense"
    )

    if st.button("📖 Gerar Início da História", type="primary"):
        if nome_protagonista and genero_literario and local_inicial and frase_desafio:
            nome_limpo = nome_protagonista.strip()
            frase_limpa = frase_desafio.strip()

            prompt = f"""Crie o início envolvente de uma história de '{genero_literario}' com o protagonista chamado '{nome_limpo}'. 
            A história começa em '{local_inicial}'. 
            Incorpore a seguinte frase ou desafio no início da narrativa: '{frase_limpa}'.
            
            Escreva 2-3 parágrafos que estabeleçam a atmosfera, apresentem o protagonista e criem suspense. 
            Use uma linguagem rica e descritiva que capture a essência do gênero escolhido."""

            with st.spinner("✨ A IA está criando sua história..."):
                historia_gerada = gerar_resposta_gemini(prompt)

                st.success("🎉 História criada com sucesso!")

                st.markdown("### 📜 Sua História:")
                st.markdown(f"""
                    <div style="
                        background: linear-gradient(135deg, #f6f8ff, #e8f0fe);
                        padding: 25px;
                        border-radius: 15px;
                        border-left: 5px solid #4a90e2;
                        margin: 20px 0;
                        font-family: Georgia, serif;
                        line-height: 1.6;
                    ">
                        <h4 style="color: #2c3e50; margin-bottom: 15px;">
                            🌟 {genero_literario}: A História de {nome_limpo}
                        </h4>
                        <div style="font-size: 1.1em; color: #34495e;">
                            {historia_gerada.replace(chr(10), '<br>')}
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                st.info(
                    "💡 Gostou da história? Experimente mudar alguns elementos e gerar uma nova versão!")

        else:
            campos_faltando = []
            if not nome_protagonista:
                campos_faltando.append("Nome do Protagonista")
            if not genero_literario:
                campos_faltando.append("Gênero Literário")
            if not local_inicial:
                campos_faltando.append("Local Inicial")
            if not frase_desafio:
                campos_faltando.append("Frase de Efeito")

            st.warning(
                f"⚠️ Por favor, preencha os seguintes campos: {', '.join(campos_faltando)}")

    with st.expander("💡 Dicas para Criar Histórias Incríveis"):
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Nomes de Protagonistas:**")
            st.write("• Fantasia: Aragorn, Lyanna, Thorin")
            st.write("• Ficção Científica: Zara, Neo, Ripley")
            st.write("• Mistério: Holmes, Watson, Marlowe")
            st.write("• Aventura: Indiana, Lara, Jack")

        with col2:
            st.write("**Frases de Efeito Sugeridas:**")
            st.write("• 'A chave brilhou com uma luz estranha'")
            st.write("• 'O último sinal de vida foi há 3 dias'")
            st.write("• 'As pegadas levavam ao impossível'")
            st.write("• 'O eco revelou que não estavam sozinhos'")

elif exercicio_selecionado == "🧑‍🍳 Exercício IA 2 - Receitas":
    st.title("🧑‍🍳 Gerador de Receitas Culinárias Personalizadas com IA")
    st.write(
        "Descubra receitas incríveis baseadas nos seus ingredientes e preferências!")

    st.header("🥘 Configure sua Receita Ideal")

    ingredientes_principais = st.text_area(
        "Ingredientes Principais que você possui:",
        placeholder="Ex: frango, tomate, cebola, arroz, batata, queijo...",
        help="Liste os ingredientes separados por vírgula"
    )

    tipo_culinaria = st.selectbox(
        "Tipo de Culinária:",
        ["Italiana", "Brasileira", "Asiática", "Mexicana", "Qualquer uma"],
        index=None,
        placeholder="Escolha o estilo culinário..."
    )

    nivel_dificuldade = st.slider(
        "Nível de Dificuldade:",
        min_value=1,
        max_value=5,
        value=3,
        help="1 = Muito Fácil | 5 = Desafiador"
    )

    niveis_texto = {
        1: "Muito Fácil 😊",
        2: "Fácil 🙂",
        3: "Médio 😐",
        4: "Difícil 😤",
        5: "Desafiador 🔥"
    }

    st.write(f"**Nível selecionado:** {niveis_texto[nivel_dificuldade]}")

    tem_restricao = st.checkbox("Possui Restrição Alimentar?")

    restricao_alimentar = ""
    if tem_restricao:
        restricao_alimentar = st.text_input(
            "Especifique sua restrição alimentar:",
            placeholder="Ex: sem glúten, vegetariana, sem lactose, vegana...",
            help="Descreva suas restrições alimentares"
        )

    if st.button("🍽️ Sugerir Receita", type="primary"):
        if ingredientes_principais and tipo_culinaria:
            ingredientes_limpos = ingredientes_principais.strip()

            restricao_str = ""
            if tem_restricao and restricao_alimentar:
                restricao_str = f"A receita deve ser {restricao_alimentar.strip()}."
            elif tem_restricao:
                restricao_str = "Considere que há restrições alimentares."

            prompt = f"""Sugira uma receita {tipo_culinaria} com nível de dificuldade {nivel_dificuldade} (sendo 1 muito fácil e 5 desafiador). 
            Deve usar principalmente os seguintes ingredientes: '{ingredientes_limpos}'. 
            {restricao_str}
            
            Apresente a resposta no seguinte formato:
            
            **Nome da Receita:** [nome criativo e apetitoso]
            
            **Ingredientes Completos:**
            - [liste todos os ingredientes necessários com quantidades]
            
            **Modo de Preparo:**
            [passo a passo detalhado mas conciso]
            
            **Tempo de Preparo:** [tempo estimado]
            
            **Dica Extra:** [uma dica especial para o sucesso da receita]
            
            Certifique-se de que a receita seja prática e saborosa!"""

            with st.spinner("👨‍🍳 A IA está criando sua receita personalizada..."):
                receita_gerada = gerar_resposta_gemini(prompt)

                st.success("🎉 Receita criada com sucesso!")

                culinaria_emojis = {
                    "Italiana": "🇮🇹",
                    "Brasileira": "🇧🇷",
                    "Asiática": "🥢",
                    "Mexicana": "🇲🇽",
                    "Qualquer uma": "🌍"
                }

                emoji_culinaria = culinaria_emojis.get(tipo_culinaria, "🍽️")

                st.markdown("### 🍽️ Sua Receita Personalizada:")
                st.markdown(f"""
                    <div style="
                        background: linear-gradient(135deg, #fff8f0, #fef7ed);
                        padding: 25px;
                        border-radius: 15px;
                        border-left: 5px solid #f97316;
                        margin: 20px 0;
                        line-height: 1.6;
                    ">
                        <h4 style="color: #ea580c; margin-bottom: 15px;">
                            {emoji_culinaria} Receita {tipo_culinaria} - Nível {nivel_dificuldade}
                        </h4>
                        <div style="font-size: 1.05em; color: #431407;">
                            {receita_gerada.replace(chr(10), '<br>')}
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Ingredientes Usados", len(
                        ingredientes_limpos.split(',')))
                with col2:
                    st.metric("Culinária", tipo_culinaria)
                with col3:
                    st.metric("Dificuldade", f"{nivel_dificuldade}/5")

                if restricao_str:
                    st.info(f"✅ Receita adaptada para: {restricao_alimentar}")

                st.success(
                    "🍴 Bom apetite! Esperamos que você aproveite sua refeição!")

        else:
            campos_faltando = []
            if not ingredientes_principais:
                campos_faltando.append("Ingredientes Principais")
            if not tipo_culinaria:
                campos_faltando.append("Tipo de Culinária")

            st.warning(
                f"⚠️ Por favor, preencha os seguintes campos: {', '.join(campos_faltando)}")

    with st.expander("💡 Dicas para Melhores Receitas"):
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Como listar ingredientes:**")
            st.write("• Seja específico: 'peito de frango' ao invés de 'frango'")
            st.write("• Inclua temperos que você tem")
            st.write("• Mencione vegetais e proteínas disponíveis")
            st.write("• Separe os ingredientes por vírgula")

        with col2:
            st.write("**Níveis de Dificuldade:**")
            st.write("• **Nível 1-2:** Receitas rápidas, poucos passos")
            st.write("• **Nível 3:** Receitas tradicionais, tempo médio")
            st.write("• **Nível 4-5:** Técnicas elaboradas, mais tempo")
