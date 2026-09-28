import streamlit as st

st.set_page_config(
    page_title="About me",
    page_icon="✳️",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700;800;900&display=swap');

    :root {
        --paper: #f4f3ed;
        --ink: #20221d;
        --muted: #70736a;
        --line: #d9d9cf;
        --acid: #d8fa4b;
        --orange: #f27652;
    }

    .stApp {
        background-color: var(--paper);
        background-image:
            linear-gradient(rgba(32, 34, 29, .035) 1px, transparent 1px),
            linear-gradient(90deg, rgba(32, 34, 29, .035) 1px, transparent 1px);
        background-size: 36px 36px;
        color: var(--ink);
        font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1080px;
        padding-top: 3rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, p, label, [data-testid="stMetricLabel"], [data-testid="stMetricValue"] {
        font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
        color: var(--ink);
    }

    .masthead {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 16px;
        border-bottom: 1px solid var(--line);
        color: var(--muted);
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1.2px;
    }

    .masthead-mark { color: var(--orange); font-size: 18px; }

    .hero {
        display: grid;
        grid-template-columns: minmax(0, 1.65fr) minmax(230px, .75fr);
        gap: 48px;
        align-items: end;
        padding: 70px 0 62px;
    }

    .eyebrow {
        margin: 0 0 22px;
        color: #55594e;
        font-size: 13px;
        font-weight: 700;
    }

    .hero h1 {
        max-width: 720px;
        margin: 0;
        font-size: 60px;
        font-weight: 900;
        line-height: 1.2;
        letter-spacing: 0;
        word-break: keep-all;
    }

    .hero h1 span {
        text-decoration: underline;
        text-decoration-color: var(--orange);
        text-decoration-thickness: 7px;
        text-underline-offset: 8px;
    }

    .hero-copy {
        max-width: 570px;
        margin: 26px 0 0;
        color: #62655c;
        font-size: 17px;
        line-height: 1.9;
        word-break: keep-all;
    }

    .side-note {
        min-height: 224px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 23px;
        background: var(--ink);
        color: white;
    }

    .side-note-label {
        color: var(--acid);
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.4px;
    }

    .side-note-mark {
        color: var(--acid);
        font-size: 52px;
        font-weight: 700;
        line-height: 1;
    }

    .side-note p {
        margin: 0;
        color: #f3f3eb;
        font-size: 14px;
        line-height: 1.7;
        word-break: keep-all;
    }

    .section-label {
        margin: 0 0 14px;
        color: var(--muted);
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.4px;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 28px;
        border-bottom: 1px solid var(--line);
    }

    .stTabs [data-baseweb="tab"] {
        height: 48px;
        padding: 0 2px;
        color: var(--muted);
        font-weight: 600;
    }

    .stTabs [aria-selected="true"] {
        color: var(--ink) !important;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        background-color: var(--orange);
    }

    .stMetric {
        padding: 18px 0 10px;
        border-top: 2px solid var(--ink);
    }

    [data-testid="stMetricLabel"] { color: var(--muted); font-size: 13px; }
    [data-testid="stMetricValue"] { font-size: 25px; font-weight: 800; }

    .principle {
        min-height: 155px;
        padding: 20px;
        border: 1px solid var(--line);
        background: rgba(255, 255, 255, .45);
    }

    .principle-number {
        color: var(--orange);
        font-size: 12px;
        font-weight: 700;
    }

    .principle h3 { margin: 22px 0 8px; font-size: 18px; }
    .principle p { margin: 0; color: var(--muted); font-size: 13px; line-height: 1.7; }

    .footer {
        margin-top: 58px;
        padding-top: 16px;
        border-top: 1px solid var(--line);
        color: var(--muted);
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1px;
    }

    @media (max-width: 700px) {
        [data-testid="stMainBlockContainer"] { padding-top: 1.5rem; }
        .hero { grid-template-columns: 1fr; gap: 30px; padding: 48px 0 42px; }
        .hero h1 { font-size: 42px; }
        .side-note { min-height: 180px; }
        .stTabs [data-baseweb="tab-list"] { gap: 16px; }
    }
    </style>

    <div class="masthead">
        <span>PERSONAL PROFILE</span>
        <span class="masthead-mark">✳</span>
        <span>CURIOUS BY DEFAULT</span>
    </div>

    <section class="hero">
        <div>
            <p class="eyebrow">안녕하세요, 저를 소개합니다.</p>
            <h1>호기심을 <span>실행</span>으로<br>옮기는 사람.</h1>
            <p class="hero-copy">
                좋은 질문에서 시작해 직접 부딪히며 답을 찾아갑니다.<br>
                생각을 작은 시도로 바꾸고, 그 과정에서 계속 배웁니다.
            </p>
        </div>
        <aside class="side-note">
            <span class="side-note-label">A LITTLE ABOUT ME</span>
            <span class="side-note-mark">01</span>
            <p>관찰하고, 만들어보고,<br>다음 가능성을 발견합니다.</p>
        </aside>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="section-label">GET TO KNOW ME</p>', unsafe_allow_html=True)

intro_tab, approach_tab, values_tab = st.tabs(["한눈에 보기", "일하는 방식", "중요하게 여기는 것"])

with intro_tab:
    st.subheader("배움은 직접 해볼 때 가장 선명해집니다.")
    st.write(
        "익숙한 답에 머무르기보다 더 나은 질문을 찾습니다. "
        "작게 시작하고, 결과를 살피고, 다음 시도에 반영하는 과정을 좋아합니다."
    )
    first, second, third = st.columns(3)
    first.metric("먼저", "질문하기")
    second.metric("그다음", "직접 해보기")
    third.metric("계속", "배우고 나누기")

with approach_tab:
    st.subheader("작게 시작해, 제대로 마무리합니다.")
    st.write(
        "막연한 아이디어를 실행할 수 있는 크기로 나눕니다. "
        "만들어 본 뒤에는 무엇이 통했고 무엇을 바꿀지 돌아봅니다."
    )
    st.markdown(
        """
        <div class="principle">
            <span class="principle-number">01 — NOTICE</span>
            <h3>문제를 자세히 봅니다</h3>
            <p>무엇이 필요한지 먼저 관찰하고 질문합니다.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown(
        """
        <div class="principle">
            <span class="principle-number">02 — MAKE</span>
            <h3>작은 시도로 확인합니다</h3>
            <p>생각을 실제 결과물로 옮겨 가능성을 살핍니다.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown(
        """
        <div class="principle">
            <span class="principle-number">03 — LEARN</span>
            <h3>다음 시도에 반영합니다</h3>
            <p>배운 것을 정리하고 더 나은 방향을 찾습니다.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with values_tab:
    st.subheader("계속 지키고 싶은 태도")
    left, right = st.columns(2)
    with left:
        st.markdown(
            """
            <div class="principle">
                <span class="principle-number">STAY OPEN</span>
                <h3>열린 마음</h3>
                <p>다른 관점에서 배우고, 모르는 것을 편하게 인정합니다.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown(
            """
            <div class="principle">
                <span class="principle-number">KEEP GOING</span>
                <h3>꾸준한 실행</h3>
                <p>완벽한 순간을 기다리기보다 오늘 할 수 있는 것을 시작합니다.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="footer">MADE WITH CURIOSITY <span style="color:#f27652">✳</span></div>', unsafe_allow_html=True)