import streamlit as st

# MBTI로 단짝 포켓몬 찾기
# 추가 패키지 없이 Streamlit만 사용합니다.
# 포켓몬 이미지는 PokeAPI의 공개 스프라이트 저장소에서 불러옵니다.
# 이미지 주소: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{번호}.png

st.set_page_config(
    page_title="MBTI로 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered",
)

POKEMON = {
    "ISTJ": {
        "ko": "거북왕", "en": "Blastoise", "id": 9,
        "types": "물 (Water)", "traits": "침착함 · 책임감 · 든든함",
        "reason": "차분하게 상황을 살피고 맡은 일을 꾸준히 해내는 모습이 닮았어요.",
        "reason2": "필요할 때 든든하게 힘을 보태 주는 믿음직한 단짝이에요.",
        "emoji": "🐢", "match": "ESFP",
    },
    "ISFJ": {
        "ko": "럭키", "en": "Chansey", "id": 113,
        "types": "노말 (Normal)", "traits": "배려심 · 다정함 · 돌봄",
        "reason": "주변을 세심하게 살피고 친구가 편안하도록 도와주는 성격과 잘 어울려요.",
        "reason2": "작은 친절도 소중히 여기는 따뜻한 단짝을 떠올리게 해요.",
        "emoji": "💗", "match": "ESFP",
    },
    "INFJ": {
        "ko": "가디안", "en": "Gardevoir", "id": 282,
        "types": "에스퍼 / 페어리 (Psychic / Fairy)", "traits": "공감 · 직관 · 다정함",
        "reason": "다른 사람의 마음을 헤아리고 소중한 관계를 지키려는 모습이 어울려요.",
        "reason2": "조용하지만 깊은 마음으로 곁을 지켜 주는 단짝이에요.",
        "emoji": "🌙", "match": "ENFP",
    },
    "INTJ": {
        "ko": "뮤츠", "en": "Mewtwo", "id": 150,
        "types": "에스퍼 (Psychic)", "traits": "전략적 사고 · 독립성 · 집중력",
        "reason": "큰 그림을 생각하고 자신만의 방식으로 문제를 해결하는 모습이 닮았어요.",
        "reason2": "목표를 향해 깊이 생각하며 나아가는 멋진 파트너예요.",
        "emoji": "🔮", "match": "ENFP",
    },
    "ISTP": {
        "ko": "팬텀", "en": "Gengar", "id": 94,
        "types": "고스트 / 독 (Ghost / Poison)", "traits": "재치 · 관찰력 · 문제 해결",
        "reason": "상황을 빠르게 파악하고 예상 밖의 방법을 찾아내는 점이 잘 어울려요.",
        "reason2": "필요할 때 재치 있게 해결책을 찾아 주는 단짝이에요.",
        "emoji": "👻", "match": "ESTJ",
    },
    "ISFP": {
        "ko": "치코리타", "en": "Chikorita", "id": 152,
        "types": "풀 (Grass)", "traits": "섬세함 · 온화함 · 자기만의 취향",
        "reason": "자신만의 감성과 속도를 소중히 여기고 주변에 편안함을 주는 모습이 닮았어요.",
        "reason2": "함께 조용한 순간도 즐길 수 있는 포근한 단짝이에요.",
        "emoji": "🌿", "match": "ESFJ",
    },
    "INFP": {
        "ko": "이브이", "en": "Eevee", "id": 133,
        "types": "노말 (Normal)", "traits": "상상력 · 호기심 · 다양한 가능성",
        "reason": "풍부한 상상력과 자기만의 소중한 세계를 가진 모습이 어울려요.",
        "reason2": "앞으로 어떤 모습으로 성장할지 기대되는 가능성 가득한 단짝이에요.",
        "emoji": "🌸", "match": "ENFJ",
    },
    "INTP": {
        "ko": "폴리곤", "en": "Porygon", "id": 137,
        "types": "노말 (Normal)", "traits": "논리 · 탐구심 · 분석력",
        "reason": "궁금한 것이 생기면 원리를 알아보고 논리적으로 생각하는 모습이 닮았어요.",
        "reason2": "새로운 질문을 함께 탐구하기 좋은 똑똑한 단짝이에요.",
        "emoji": "🧩", "match": "ENTJ",
    },
    "ESTP": {
        "ko": "리자몽", "en": "Charizard", "id": 6,
        "types": "불꽃 / 비행 (Fire / Flying)", "traits": "도전 정신 · 행동력 · 에너지",
        "reason": "새로운 경험을 두려워하지 않고 직접 부딪쳐 보는 활력이 잘 어울려요.",
        "reason2": "함께 모험하고 신나는 추억을 만들기 좋은 단짝이에요.",
        "emoji": "🔥", "match": "ISFJ",
    },
    "ESFP": {
        "ko": "피카츄", "en": "Pikachu", "id": 25,
        "types": "전기 (Electric)", "traits": "밝음 · 사교성 · 활기",
        "reason": "밝은 에너지로 주변을 즐겁게 하고 친구들과 순간을 나누는 모습이 닮았어요.",
        "reason2": "함께 있으면 평범한 하루도 신나는 모험처럼 느껴지는 단짝이에요.",
        "emoji": "⚡", "match": "ISTJ",
    },
    "ENFP": {
        "ko": "파치리스", "en": "Pachirisu", "id": 417,
        "types": "전기 (Electric)", "traits": "호기심 · 낙천성 · 아이디어",
        "reason": "호기심이 많고 새로운 가능성을 발견하는 것을 좋아하는 모습이 어울려요.",
        "reason2": "톡톡 튀는 아이디어와 즐거운 에너지를 나눌 수 있는 단짝이에요.",
        "emoji": "✨", "match": "INFJ",
    },
    "ENTP": {
        "ko": "파오리", "en": "Farfetch’d", "id": 83,
        "types": "노말 / 비행 (Normal / Flying)", "traits": "재치 · 독창성 · 호기심",
        "reason": "남다른 관점으로 생각하고 재치 있는 방법을 찾아내는 모습이 잘 어울려요.",
        "reason2": "새로운 생각을 주고받으며 지루할 틈이 없는 단짝이에요.",
        "emoji": "🦆", "match": "INFJ",
    },
    "ESTJ": {
        "ko": "코뿌리", "en": "Rhydon", "id": 112,
        "types": "땅 / 바위 (Ground / Rock)", "traits": "추진력 · 책임감 · 실천",
        "reason": "해야 할 일을 정리하고 계획을 실제 행동으로 옮기는 모습이 닮았어요.",
        "reason2": "함께 목표를 세우고 끝까지 도전하기 좋은 든든한 단짝이에요.",
        "emoji": "💪", "match": "ISTP",
    },
    "ESFJ": {
        "ko": "푸린", "en": "Jigglypuff", "id": 39,
        "types": "노말 / 페어리 (Normal / Fairy)", "traits": "친화력 · 배려 · 분위기 메이커",
        "reason": "사람들과 어울리고 모두가 즐거운 분위기를 만드는 모습이 어울려요.",
        "reason2": "친구들과 웃고 노래하며 따뜻한 추억을 만드는 단짝이에요.",
        "emoji": "🎤", "match": "ISFP",
    },
    "ENFJ": {
        "ko": "이상해꽃", "en": "Venusaur", "id": 3,
        "types": "풀 / 독 (Grass / Poison)", "traits": "응원 · 협력 · 따뜻한 리더십",
        "reason": "주변 사람의 장점을 발견하고 함께 성장하도록 돕는 모습이 닮았어요.",
        "reason2": "팀에 힘을 불어넣고 함께 앞으로 나아가는 든든한 단짝이에요.",
        "emoji": "🌻", "match": "INFP",
    },
    "ENTJ": {
        "ko": "갸라도스", "en": "Gyarados", "id": 130,
        "types": "물 / 비행 (Water / Flying)", "traits": "결단력 · 자신감 · 추진력",
        "reason": "목표를 향해 과감하게 나아가고 어려운 상황에서도 추진력을 발휘하는 모습이 어울려요.",
        "reason2": "큰 도전을 함께 해낼 수 있는 강렬한 파트너예요.",
        "emoji": "🌊", "match": "INTP",
    },
}

# 페이지 디자인
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #fff9e9 0%, #fffdf7 100%);
        color: #493a25;
    }
    .block-container {
        max-width: 850px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    h1, h2, h3 { color: #81551c !important; }
    .hero {
        background: #ffedb8;
        border: 2px solid #f0d27e;
        border-radius: 26px;
        padding: 26px 20px;
        text-align: center;
        margin-bottom: 18px;
    }
    .hero-icon { font-size: 3.6rem; line-height: 1.2; }
    .hero-title { font-size: clamp(1.8rem, 5vw, 2.7rem); font-weight: 900; margin: 8px 0; }
    .hero-sub { font-size: 1.12rem; line-height: 1.7; }
    div.stButton > button {
        background: #fffdf6;
        color: #654b2a;
        border: 2px solid #ecd18d;
        border-radius: 14px;
        min-height: 3.1rem;
        font-size: 1.08rem;
        font-weight: 800;
        transition: all .15s ease;
    }
    div.stButton > button:hover {
        border-color: #dfa52d;
        background: #fff0bd;
        color: #654b2a;
    }
    .result-card {
        background: #fffdf7;
        border: 3px solid #f0d58f;
        border-radius: 24px;
        padding: 24px 22px;
        text-align: center;
        margin-top: 18px;
        box-shadow: 0 8px 22px rgba(130, 91, 24, .08);
    }
    .mbti-pill {
        display: inline-block;
        background: #ffedb8;
        color: #79511c;
        border-radius: 30px;
        padding: 6px 16px;
        font-weight: 800;
        font-size: 1.05rem;
    }
    .pokemon-title { font-size: clamp(1.7rem, 4vw, 2.2rem); font-weight: 900; color: #d58b0a; margin: 6px 0; }
    .pokemon-en { color: #8b785e; font-size: 1.08rem; }
    .info-box {
        background: #fff4d7;
        border-radius: 15px;
        padding: 13px 16px;
        margin-top: 12px;
        text-align: left;
        font-size: 1.05rem;
        line-height: 1.8;
    }
    .reason-box {
        background: #fff9ea;
        border: 1px solid #f3e3b8;
        border-radius: 15px;
        padding: 15px 17px;
        margin-top: 12px;
        text-align: left;
        font-size: 1.08rem;
        line-height: 1.85;
    }
    .match-box {
        background: #ffefbd;
        border-radius: 16px;
        padding: 15px;
        margin-top: 15px;
        font-size: 1.08rem;
        line-height: 1.7;
    }
    .footnote { color: #8b795e; font-size: .88rem; text-align: center; margin-top: 24px; }
    @media (max-width: 520px) {
        .hero { padding: 22px 13px; }
        .result-card { padding: 19px 13px; }
    }
    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after { animation: none !important; transition: none !important; }
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="hero-icon">⚡ 🐣 🌼</div>
  <div class="hero-title">MBTI로 단짝 포켓몬 찾기!</div>
  <div class="hero-sub">내 성격과 잘 어울리는 포켓몬은 누구일까요?<br>MBTI를 선택하고 나만의 단짝을 만나 보세요!</div>
</div>
""", unsafe_allow_html=True)

st.subheader("🌟 나의 MBTI를 선택해 주세요")
st.caption("아래 16가지 유형 중 하나를 눌러 보세요.")

types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ",
]

# 선택한 MBTI를 세션에 보관
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

cols = st.columns(4)
for index, mbti in enumerate(types):
    with cols[index % 4]:
        if st.button(mbti, key=f"mbti_{mbti}", use_container_width=True):
            st.session_state.selected_mbti = mbti

selected = st.session_state.selected_mbti

if selected:
    p = POKEMON[selected]
    st.balloons()

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="mbti-pill">🎉 나의 MBTI: {selected}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="pokemon-title">{p["ko"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="pokemon-en">({p["en"]})</div>', unsafe_allow_html=True)

    image_url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{p["id"]}.png'
    st.image(image_url, width=220, caption=f'{p["ko"]} · {p["en"]}')

    st.markdown(f"""
    <div class="info-box">
      <b>🔎 타입</b><br>{p["types"]}<br><br>
      <b>✨ 특징</b><br>{p["traits"]}
    </div>
    <div class="reason-box">
      <b>💛 당신과 잘 어울리는 이유</b><br>
      {p["reason"]}<br>
      {p["reason2"]}
    </div>
    <div class="match-box">
      <b>🤝 잘 맞을 수 있는 MBTI</b><br>
      <span style="font-size:1.5rem;font-weight:900;color:#9a681a">{p["match"]}</span><br>
      서로 다른 장점을 나누며 즐거운 팀이 될 수 있어요!
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("↩️ 다시 고르기", use_container_width=True):
        st.session_state.selected_mbti = None
        st.rerun()
else:
    st.info("💡 MBTI 버튼을 누르면 단짝 포켓몬과 축하 효과가 나타나요!")

st.markdown("""
<div class="footnote">
  포켓몬 이미지는 인터넷에서 불러옵니다. 이미지가 보이지 않으면 연결 상태를 확인해 주세요.<br>
  MBTI와 포켓몬의 연결 및 궁합은 재미를 위한 창작 추천이며, 과학적인 성격 검사 결과가 아니에요.
</div>
""", unsafe_allow_html=True)
