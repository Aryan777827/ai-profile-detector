import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from src.detector import full_profile_analysis

st.set_page_config(
    page_title="Veridian — AI Profile Detector",
    page_icon="●",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cabinet+Grotesk:wght@300;400;500;700;800&family=Instrument+Serif:ital@0;1&display=swap');

:root {
    --bg:       #F7F5F0;
    --surface:  #FFFFFF;
    --surface2: #F2EFE9;
    --border:   #D6D1C8;
    --border2:  #C4BEB4;

    --forest:   #1A2416;
    --forest2:  #2C3E28;
    --sage:     #2E5740;
    --sage-lt:  #5A8A6A;
    --sage-bg:  #DCE9E0;

    --amber:    #A85C1A;
    --amber-bg: #FDF0E4;
    --amber-bd: #E8C49A;

    --ok-bg:    #E4F0E8;
    --ok-bd:    #A8CEB5;

    --ink:      #1A2416;
    --ink2:     #3A4A3C;
    --ink3:     #5A6A5C;
    --muted:    #8A9A8C;
}

html, body, [class*="css"] {
    font-family: 'Cabinet Grotesk', sans-serif !important;
    background: var(--bg) !important;
    color: var(--ink) !important;
}
.stApp { background: var(--bg); }
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* ── Nav ── */
.app-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 0 1.2rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 0;
}
.nav-brand { display: flex; align-items: center; gap: 0.5rem; }
.nav-dot { width: 9px; height: 9px; border-radius: 50%; background: var(--sage); }
.nav-name { font-size: 1rem; font-weight: 800; letter-spacing: -0.01em; color: var(--forest); }
.nav-badge {
    font-size: 0.58rem; letter-spacing: 0.14em; text-transform: uppercase;
    color: var(--sage); border: 1px solid var(--sage-bg);
    border-radius: 20px; padding: 0.2rem 0.75rem;
    background: var(--sage-bg);
}

/* ── Hero ── */
.hero {
    display: flex; align-items: flex-end; justify-content: space-between;
    padding: 2.5rem 0 2rem; border-bottom: 1px solid var(--border);
    margin-bottom: 2rem; gap: 2rem;
}
.hero-eyebrow { display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.7rem; }
.eyebrow-line { width: 20px; height: 1px; background: var(--sage); }
.eyebrow-txt {
    font-size: 0.62rem; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--sage); font-weight: 700;
}
.hero-title {
    font-family: 'Instrument Serif', serif; font-size: 2.6rem;
    line-height: 1.05; color: var(--forest); letter-spacing: -0.01em; margin-bottom: 0.5rem;
}
.hero-title em { font-style: italic; color: var(--sage); }
.hero-sub { font-size: 0.78rem; color: var(--ink3); font-weight: 500; letter-spacing: 0.04em; }
.hero-stat { text-align: right; }
.hero-stat-num {
    font-family: 'Instrument Serif', serif; font-size: 3rem;
    color: var(--border2); line-height: 1;
}
.hero-stat-label {
    font-size: 0.6rem; letter-spacing: 0.12em; text-transform: uppercase;
    color: var(--muted); margin-top: 0.25rem;
}

/* ── Section headers ── */
.sec-header { display: flex; align-items: center; gap: 0.7rem; margin-bottom: 1rem; }
.sec-num {
    font-size: 0.58rem; font-weight: 700; letter-spacing: 0.12em;
    color: var(--ink3); background: var(--surface2);
    border: 1px solid var(--border); border-radius: 20px; padding: 0.18rem 0.6rem;
}
.sec-title {
    font-size: 0.72rem; font-weight: 700; letter-spacing: 0.1em;
    text-transform: uppercase; color: var(--forest);
}

/* ── Inputs ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input {
    background: #FFFFFF !important;
    border: 1.5px solid #D6D1C8 !important;
    border-radius: 7px !important;
    color: #1A2416 !important;
    font-family: 'Cabinet Grotesk', sans-serif !important;
    font-size: 0.85rem !important;
    padding: 0.55rem 0.85rem !important;
    transition: border-color 0.15s;
    -webkit-text-fill-color: #1A2416 !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus,
.stNumberInput > div > div > input:focus {
    border-color: #2E5740 !important;
    box-shadow: 0 0 0 3px rgba(46,87,64,0.1) !important;
    outline: none !important;
    background: #FFFFFF !important;
}
.stTextInput > div > div > input::placeholder,
.stTextArea > div > div > textarea::placeholder {
    color: #8A9A8C !important;
    -webkit-text-fill-color: #8A9A8C !important;
}
/* Full number input wrapper — Streamlit wraps input+steppers together */
.stNumberInput > div > div {
    background: #FFFFFF !important;
    border: 1.5px solid #D6D1C8 !important;
    border-radius: 7px !important;
    overflow: hidden;
}
.stNumberInput > div > div > input {
    border: none !important;
    box-shadow: none !important;
}

/* ── Labels ── */
.stTextInput label, .stTextArea label,
.stNumberInput label, .stFileUploader label,
.stRadio label, .stRadio > label {
    font-size: 0.62rem !important; font-weight: 700 !important;
    letter-spacing: 0.1em !important; text-transform: uppercase !important;
    color: var(--ink3) !important;
    font-family: 'Cabinet Grotesk', sans-serif !important;
}

/* ── Radio ── */
.stRadio > div > label {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 5px !important;
    padding: 0.32rem 0.9rem !important;
    font-size: 0.75rem !important;
    text-transform: none !important;
    letter-spacing: 0 !important;
    color: var(--ink3) !important;
    font-weight: 500 !important;
    transition: all 0.12s;
}
.stRadio > div > label:has(input:checked) {
    background: var(--surface) !important;
    color: var(--forest) !important;
    border-color: var(--border2) !important;
    font-weight: 700 !important;
}

/* ── File uploader ── */
.stFileUploader > div {
    background: var(--surface) !important;
    border: 1.5px dashed var(--border2) !important;
    border-radius: 10px !important;
    transition: border-color 0.15s;
}
.stFileUploader > div:hover { border-color: var(--sage) !important; }
.stFileUploader p, .stFileUploader span { color: var(--ink3) !important; }

/* ── Button ── */
.stButton > button {
    background: #1A2416 !important;
    color: #F7F5F0 !important;
    -webkit-text-fill-color: #F7F5F0 !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Cabinet Grotesk', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    padding: 0.85rem 2rem !important;
    width: 100% !important;
    margin-top: 0.8rem !important;
    transition: all 0.15s !important;
}
.stButton > button p {
    color: #F7F5F0 !important;
    -webkit-text-fill-color: #F7F5F0 !important;
}
.stButton > button:hover {
    background: #2C3E28 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 16px rgba(26,36,22,0.18) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Metrics ── */
[data-testid="metric-container"] {
    background: var(--surface);
    border: 1.5px solid var(--border);
    border-radius: 8px;
    padding: 0.9rem 1rem;
}
[data-testid="metric-container"] label {
    font-size: 0.58rem !important; font-weight: 700 !important;
    letter-spacing: 0.1em !important; text-transform: uppercase !important;
    color: var(--ink3) !important;
    font-family: 'Cabinet Grotesk', sans-serif !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-family: 'Instrument Serif', serif !important;
    font-size: 1.6rem !important; font-weight: 400 !important;
    color: var(--forest) !important;
}

/* ── Progress ── */
.stProgress > div > div {
    background: var(--surface2) !important;
    height: 4px !important; border-radius: 2px !important;
}
.stProgress > div > div > div {
    background: var(--sage) !important; border-radius: 2px !important;
}

/* ── Alerts ── */
.stAlert {
    font-family: 'Cabinet Grotesk', sans-serif !important;
    font-size: 0.78rem !important; border-radius: 7px !important;
}
.stWarning {
    background: var(--amber-bg) !important;
    border: 1px solid var(--amber-bd) !important;
    border-left: 3px solid var(--amber) !important;
    color: var(--ink) !important;
}
.stSuccess {
    background: var(--ok-bg) !important;
    border: 1px solid var(--ok-bd) !important;
    border-left: 3px solid var(--sage) !important;
    color: var(--ink) !important;
}

/* ── Score block ── */
.score-block {
    background: var(--forest);
    border-radius: 12px;
    padding: 1.8rem;
    margin-bottom: 1.2rem;
    position: relative;
    overflow: hidden;
}
.score-block::before {
    content: ''; position: absolute; top: -70px; right: -70px;
    width: 200px; height: 200px; border-radius: 50%;
    border: 1px solid rgba(255,255,255,0.06);
}
.score-block::after {
    content: ''; position: absolute; top: -30px; right: -30px;
    width: 110px; height: 110px; border-radius: 50%;
    border: 1px solid rgba(255,255,255,0.04);
}
.score-lbl {
    font-size: 0.58rem; letter-spacing: 0.18em; text-transform: uppercase;
    color: rgba(247,245,240,0.45); margin-bottom: 0.45rem;
}
.score-row { display: flex; align-items: baseline; gap: 0.4rem; margin-bottom: 0.9rem; }
.score-big {
    font-family: 'Instrument Serif', serif;
    font-size: 5rem; line-height: 1; font-weight: 400;
}
.score-den { font-size: 1rem; color: rgba(247,245,240,0.28); font-weight: 300; }
.verdict-chip {
    display: inline-flex; align-items: center; gap: 0.5rem;
    border-radius: 20px; padding: 0.35rem 0.9rem;
}
.v-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }
.v-txt { font-size: 0.65rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }

/* ── Model breakdown table ── */
.model-table {
    background: var(--surface); border: 1.5px solid var(--border);
    border-radius: 8px; overflow: hidden; margin-bottom: 1.2rem;
}
.model-thead {
    background: var(--surface2); padding: 0.55rem 1rem;
    font-size: 0.6rem; font-weight: 700; letter-spacing: 0.12em;
    text-transform: uppercase; color: var(--ink3);
    border-bottom: 1px solid var(--border);
}
.model-row {
    display: flex; align-items: center; gap: 0.75rem;
    padding: 0.65rem 1rem; border-bottom: 1px solid var(--surface2);
}
.model-row:last-child { border-bottom: none; }
.m-name { font-size: 0.75rem; font-weight: 600; color: var(--ink2); min-width: 110px; }
.m-track { flex: 1; height: 4px; background: var(--surface2); border-radius: 2px; }
.m-fill { height: 4px; border-radius: 2px; }
.m-pct { font-size: 0.72rem; font-weight: 700; min-width: 38px; text-align: right; }

/* ── Flags ── */
.flag-item {
    display: flex; align-items: flex-start; gap: 0.65rem;
    padding: 0.65rem 0.9rem; border-radius: 7px; margin-bottom: 0.5rem;
}
.flag-pip { width: 5px; height: 5px; border-radius: 50%; margin-top: 5px; flex-shrink: 0; }
.flag-txt { font-size: 0.74rem; color: var(--ink2); line-height: 1.5; }

/* ── Empty state ── */
.empty-state { padding: 4rem 0; text-align: center; }
.empty-icon {
    font-family: 'Instrument Serif', serif;
    font-size: 2.5rem; color: var(--border); margin-bottom: 0.75rem;
}
.empty-txt {
    font-size: 0.68rem; letter-spacing: 0.14em;
    text-transform: uppercase; color: var(--muted);
}

/* ── Image ── */
[data-testid="stImage"] {
    border-radius: 8px; overflow: hidden;
    border: 1.5px solid var(--border);
}

/* ── Column layout ── */
[data-testid="column"]:first-child { padding-right: 2rem; }
[data-testid="column"]:last-child {
    border-left: 1px solid var(--border);
    padding-left: 2rem;
    background: var(--surface);
    border-radius: 0 8px 8px 0;
}

/* ── Number input stepper buttons ── */
.stNumberInput button,
.stNumberInput [data-testid="stNumberInputStepDown"],
.stNumberInput [data-testid="stNumberInputStepUp"] {
    background: #F2EFE9 !important;
    border: none !important;
    border-left: 1px solid #D6D1C8 !important;
    color: #3A4A3C !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    -webkit-text-fill-color: #3A4A3C !important;
    min-width: 36px !important;
}
.stNumberInput button:hover {
    background: #DCE9E0 !important;
    color: #1A2416 !important;
    -webkit-text-fill-color: #1A2416 !important;
}
    border-color: var(--sage) transparent transparent transparent !important;
}
/* stNumberInput button styles consolidated above */
.stCaption {
    color: var(--muted) !important;
    font-family: 'Cabinet Grotesk', sans-serif !important;
    font-size: 0.65rem !important; letter-spacing: 0.06em !important;
}
p, span, div, li { color: var(--ink); }
</style>
""", unsafe_allow_html=True)

# ─── Nav ───
st.markdown("""
<div class="app-nav">
    <div class="nav-brand">
        <div class="nav-dot"></div>
        <span class="nav-name">Veridian</span>
    </div>
    <span class="nav-badge">AI Profile Detector · V2</span>
</div>
""", unsafe_allow_html=True)

# ─── Hero ───
st.markdown("""
<div class="hero">
    <div>
        <div class="hero-eyebrow">
            <div class="eyebrow-line"></div>
            <span class="eyebrow-txt">Identity Verification</span>
        </div>
        <div class="hero-title">Detect the <em>synthetic</em><br>from the real.</div>
        <div class="hero-sub">CLIP Ensemble &nbsp;·&nbsp; ViT Models &nbsp;·&nbsp; Metadata Heuristics</div>
    </div>
    <div class="hero-stat">
        <div class="hero-stat-num">99%</div>
        <div class="hero-stat-label">Detection Accuracy</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Columns ───
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="sec-header"><span class="sec-num">01</span><span class="sec-title">Image Input</span></div>', unsafe_allow_html=True)
    method = st.radio("Method", ["Upload file", "Paste URL"], horizontal=True, label_visibility="collapsed")
    image = None

    if method == "Upload file":
        file = st.file_uploader("Image", type=["png", "jpg", "jpeg", "webp"], label_visibility="collapsed")
        if file:
            image = Image.open(file).convert("RGB")
            st.image(image, use_container_width=True)
    else:
        url = st.text_input("URL", placeholder="https://example.com/profile.jpg", label_visibility="collapsed")
        if url:
            try:
                resp  = requests.get(url, timeout=10)
                image = Image.open(BytesIO(resp.content)).convert("RGB")
                st.image(image, use_container_width=True)
            except Exception:
                st.error("Could not load image from that URL.")

    st.markdown("<div style='height:1.4rem'></div>", unsafe_allow_html=True)
    st.markdown('<div class="sec-header"><span class="sec-num">02</span><span class="sec-title">Profile Metadata</span></div>', unsafe_allow_html=True)

    mc1, mc2 = st.columns(2)
    with mc1:
        username  = st.text_input("Username", placeholder="@handle")
        followers = st.number_input("Followers", min_value=0, value=0)
        posts     = st.number_input("Posts", min_value=0, value=0)
    with mc2:
        bio       = st.text_area("Bio", placeholder="Profile bio...", height=72)
        following = st.number_input("Following", min_value=0, value=0)
        age       = st.number_input("Account age (days)", min_value=0, value=0)

    st.markdown("<div style='height:0.2rem'></div>", unsafe_allow_html=True)
    analyze = st.button("Run Analysis →")

with col2:
    st.markdown('<div class="sec-header"><span class="sec-num">03</span><span class="sec-title">Results</span></div>', unsafe_allow_html=True)

    if analyze:
        if image is None:
            st.warning("Please provide an image to begin analysis.")
        else:
            with st.spinner("Analyzing..."):
                result = full_profile_analysis(
                    image_source=image,
                    username=username,
                    bio=bio,
                    followers=followers,
                    following=following,
                    posts=posts,
                    account_age_days=age,
                )

            score   = result["overall_suspicion_score"]
            verdict = result["overall_verdict"]
            img_r   = result["image_analysis"]
            meta    = result["metadata_analysis"]

            # Colour-code by risk level — all on dark bg so must stay bright enough
            if score >= 65:
                sc      = "#E8956A"           # warm orange — readable on dark forest bg
                chip_bg = "rgba(232,149,106,0.15)"
                chip_bd = "rgba(232,149,106,0.35)"
            elif score >= 40:
                sc      = "#D4B86A"           # gold — readable on dark
                chip_bg = "rgba(212,184,106,0.15)"
                chip_bd = "rgba(212,184,106,0.35)"
            else:
                sc      = "#6DBF8A"           # light sage — readable on dark
                chip_bg = "rgba(109,191,138,0.15)"
                chip_bd = "rgba(109,191,138,0.35)"

            st.markdown(f"""
            <div class="score-block">
                <div class="score-lbl">Suspicion Score</div>
                <div class="score-row">
                    <span class="score-big" style="color:{sc}">{score:.0f}</span>
                    <span class="score-den">/ 100</span>
                </div>
                <div class="verdict-chip" style="background:{chip_bg};border:1px solid {chip_bd};">
                    <div class="v-dot" style="background:{sc}"></div>
                    <span class="v-txt" style="color:{sc}">{verdict}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.progress(int(score) / 100)

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("AI Generated", "Yes" if img_r["is_ai_generated"] else "No")
            m2.metric("Confidence",   img_r["confidence_level"].upper())
            m3.metric("CLIP Score",   f"{result.get('clip_score', 0):.1f}")
            m4.metric("Artifact",     f"{result.get('artifact_score', 0):.1f}")

            if img_r.get("individual_results"):
                st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)
                rows = '<div class="model-table"><div class="model-thead">Model Breakdown</div>'
                for name, r in img_r["individual_results"].items():
                    pct   = r["ai_probability"] * 100
                    # Bar colour: amber for high risk, sage for low — on white surface so darker shades
                    bar_c = "#A85C1A" if pct >= 65 else ("#9E7A20" if pct >= 40 else "#2E5740")
                    rows += f"""
                    <div class="model-row">
                        <span class="m-name">{name}</span>
                        <div class="m-track">
                            <div class="m-fill" style="width:{pct:.0f}%;background:{bar_c};"></div>
                        </div>
                        <span class="m-pct" style="color:{bar_c};">{pct:.1f}%</span>
                    </div>"""
                rows += "</div>"
                st.markdown(rows, unsafe_allow_html=True)

            flags = meta.get("red_flags", [])
            st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)

            if flags:
                for f in flags:
                    st.markdown(f"""
                    <div class="flag-item" style="background:#FDF0E4;border:1px solid #E8C49A;">
                        <div class="flag-pip" style="background:#A85C1A;"></div>
                        <span class="flag-txt">{f}</span>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="flag-item" style="background:#E4F0E8;border:1px solid #A8CEB5;">
                    <div class="flag-pip" style="background:#2E5740;"></div>
                    <span class="flag-txt">No metadata red flags detected.</span>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-icon">◉</div>
            <div class="empty-txt">Upload an image &amp; run analysis</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
st.caption("Veridian · AI Profile Detector V2 · CLIP + Ensemble Models · For research purposes only")
