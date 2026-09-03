import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="MenoSakhi | Path to ₹100 Crore",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# BRAND COLORS
# ============================================================

CREAM = "#FBF3E7"
CREAM_2 = "#F7ECDD"
BROWN = "#4A3020"
BROWN_2 = "#765A43"
GOLD = "#D5A456"
GOLD_LIGHT = "#E7C995"
TERRACOTTA = "#C97F58"
PEACH = "#E9B78E"
SAND = "#E9D5B6"
MUTED = "#8B735D"
WHITE = "#FFFDF9"
GRID = "#E5D6C1"
GREENISH = "#89886A"

# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
<style>

html {{
    zoom: 0.80;
}}

html, body, [class*="css"] {{
    font-family: Arial, sans-serif;
}}

.stApp {{
    background: {CREAM};
    color: {BROWN};
}}

header[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

footer {{
    visibility: hidden;
}}

#MainMenu {{
    visibility: hidden;
}}

.block-container {{
    width: 100vw !important;
    max-width: 100vw !important;
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
    padding-left: 1.2vw !important;
    padding-right: 1.2vw !important;
}}

[data-testid="stMain"] {{
    width: 100% !important;
}}

[data-testid="stHorizontalBlock"] {{
    gap: 0.6rem !important;
}}

.eyebrow {{
    font-size: 0.62rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: {GOLD};
    font-weight: 700;
}}

.main-title {{
    font-size: 1.8rem;
    line-height: 1.0;
    font-weight: 800;
    color: {BROWN};
    margin-bottom: 0.2rem;
}}

.subtitle {{
    font-size: 0.75rem;
    color: {BROWN_2};
    line-height: 1.35;
    margin-bottom: 0.4rem;
}}

.kpi-card {{
    background: rgba(255,253,249,0.75);
    border: 1px solid {GOLD_LIGHT};
    border-radius: 13px;
    padding: 9px 11px;
    min-height: 82px;
}}

.kpi-label {{
    color: {MUTED};
    text-transform: uppercase;
    font-size: 0.56rem;
    font-weight: 700;
    margin-bottom: 3px;
}}

.kpi-value {{
    color: {BROWN};
    font-size: 1.45rem;
    font-weight: 800;
    margin-bottom: 4px;
}}

.kpi-sub {{
    color: {BROWN_2};
    font-size: 0.58rem;
    line-height: 1.25;
}}

.panel {{
    background: rgba(255,253,249,0.72);
    border: 1px solid {GOLD_LIGHT};
    border-radius: 14px;
    padding: 8px 10px 7px 10px;
    margin-bottom: 7px;
}}

.panel-title {{
    font-size: 0.70rem;
    font-weight: 800;
    color: {BROWN};
    text-transform: uppercase;
    letter-spacing: 0.05em;
}}

.panel-sub {{
    font-size: 0.56rem;
    color: {MUTED};
    margin-bottom: 2px;
}}

.equation-box {{
    background: {BROWN};
    border-radius: 10px;
    padding: 8px 12px;
    color: {CREAM};
    text-align: center;
    margin-top: 4px;
}}

.equation-main {{
    font-size: 0.92rem;
    font-weight: 800;
}}

.equation-sub {{
    font-size: 0.54rem;
    opacity: 0.85;
    margin-top: 2px;
}}

.impact-wrap {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 7px;
    margin-top: 6px;
}}

.impact-card {{
    background: {CREAM_2};
    border: 1px solid {GOLD_LIGHT};
    border-radius: 11px;
    padding: 9px 7px;
    text-align: center;
}}

.impact-number {{
    font-size: 1.35rem;
    font-weight: 800;
    color: {BROWN};
}}

.impact-label {{
    color: {BROWN_2};
    margin-top: 3px;
    font-size: 0.56rem;
    font-weight: 700;
    text-transform: uppercase;
}}

.timeline {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 5px;
    margin-top: 6px;
}}

.year-box {{
    background: {WHITE};
    border-top: 3px solid {GOLD};
    border-radius: 7px;
    padding: 6px;
    min-height: 72px;
}}

.year-title {{
    color: {BROWN};
    font-size: 0.63rem;
    font-weight: 800;
    margin-bottom: 3px;
}}

.year-copy {{
    color: {BROWN_2};
    font-size: 0.50rem;
    line-height: 1.3;
}}

div[data-testid="stDataFrame"] {{
    border: 1px solid {GOLD_LIGHT};
    border-radius: 9px;
    overflow: hidden;
}}

</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# DATA
# ============================================================

years = ["Y1", "Y2", "Y3", "Y4", "Y5"]

data = pd.DataFrame({
    "Year": years,
    "Revenue": [4, 16, 42, 72, 104],
    "D2C": [2.4, 8.0, 18.9, 28.8, 39.52],
    "Marketplace": [1.2, 4.48, 10.5, 15.84, 20.8],
    "Quick Commerce": [0.4, 3.52, 12.6, 20.16, 28.08],
    "Offline": [None, None, None, 7.2, 15.6],

    "Morning Pancake Mix": [0.64, 2.88, 8.40, 15.12, 22.88],
    "Night Core Capsule": [2.08, 8.00, 19.74, 32.40, 44.72],
    "Heat Relief Roll-on": [0.80, 2.72, 6.30, 10.08, 13.52],
    "Calm Infusion Tea": [0.48, 2.40, 7.56, 14.40, 22.88],

    "Repeat Rate": [36, 44, 50, 55, 58],
    "Purchase Frequency": [5.54, 6.49, 7.51, 8.32, 8.97],
    "Active Customers": [12500, 43243, 100000, 156522, 212245],
    "ARPU": [3200, 3700, 4200, 4600, 4900],
    "AOV": [1183, 1104, 1047, 981, 946],

    "CAC": [1120, 1314.14, 1232.48, 1276.57, 1284.35],
    "LTV": [2488, 3053, 3672, 4250, 4703],
    "LTV CAC": [2.22, 2.32, 2.98, 3.33, 3.66],

    "Gross Margin": [59.45, 62.11, 63.15, 63.82, 63.41],
    "CM1": [43.57, 43.41, 42.64, 41.57, 40.31],
    "CM2": [8.57, 12.41, 19.64, 23.57, 25.31],
    "EBITDA Margin": [-67.68, -22.59, -2.50, 5.38, 9.06],
})

# ============================================================
# HELPERS
# ============================================================

def clean_layout(fig, height=190):
    fig.update_layout(
        height=height,
        margin=dict(l=15, r=10, t=10, b=15),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Arial", color=BROWN_2, size=9),
        hovermode=False,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
            font=dict(size=7),
        ),
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        tickfont=dict(size=8, color=MUTED),
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        tickfont=dict(size=7, color=MUTED),
    )

    return fig


def panel_header(title, subtitle=""):
    st.markdown(
        f"""
<div class="panel-title">{title}</div>
<div class="panel-sub">{subtitle}</div>
""",
        unsafe_allow_html=True,
    )

# ============================================================
# HEADER
# ============================================================

h1, h2 = st.columns([6, 1.2])

with h1:
    st.markdown(
        """
<div class="eyebrow">05 · Financial roadmap</div>
<div class="main-title">PATH TO ₹100 CRORE</div>
<div class="subtitle">
MenoSakhi scales through a digital-first revenue engine, stronger repeat behaviour,
improving customer economics and disciplined operating leverage.
</div>
""",
        unsafe_allow_html=True,
    )

with h2:
    if Path("logo.png").exists():
        st.image("logo.png", use_container_width=True)

# ============================================================
# KPI CARDS
# ============================================================

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown("""
<div class="kpi-card">
<div class="kpi-label">Y5 Revenue</div>
<div class="kpi-value">₹104 Cr</div>
<div class="kpi-sub">Crosses the ₹100 Cr ambition by Year 5</div>
</div>
""", unsafe_allow_html=True)

with k2:
    st.markdown("""
<div class="kpi-card">
<div class="kpi-label">Active Customers</div>
<div class="kpi-value">2.12 Lakh</div>
<div class="kpi-sub">Scaled customer base supporting revenue build</div>
</div>
""", unsafe_allow_html=True)

with k3:
    st.markdown("""
<div class="kpi-card">
<div class="kpi-label">Y5 ARPU</div>
<div class="kpi-value">₹4,900</div>
<div class="kpi-sub">Driven by repeat and purchase frequency</div>
</div>
""", unsafe_allow_html=True)

with k4:
    st.markdown("""
<div class="kpi-card">
<div class="kpi-label">Y5 EBITDA Margin</div>
<div class="kpi-value">9.1%</div>
<div class="kpi-sub">EBITDA positive from Y4 at ₹72 Cr</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# ROW 1
# ============================================================

c1, c2, c3 = st.columns([1.4, 1.4, 0.9])

with c1:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Revenue by channel", "₹ Cr")

    fig = go.Figure()

    colors = {
        "D2C": BROWN,
        "Marketplace": GOLD,
        "Quick Commerce": TERRACOTTA,
        "Offline": SAND,
    }

    for col, color in colors.items():
        labels = ["" if pd.isna(v) else f"{v:.1f}" for v in data[col]]
        fig.add_trace(go.Bar(
            x=years,
            y=data[col],
            name=col,
            marker_color=color,
            text=labels,
            textposition="inside",
            hoverinfo="skip",
        ))

    fig.update_layout(barmode="stack")
    clean_layout(fig, 200)

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False, "staticPlot": True},
    )

    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Revenue by SKU", "₹ Cr")

    fig = go.Figure()

    sku_colors = {
        "Morning Pancake Mix": GREENISH,
        "Night Core Capsule": BROWN,
        "Heat Relief Roll-on": TERRACOTTA,
        "Calm Infusion Tea": GOLD,
    }

    for col, color in sku_colors.items():
        fig.add_trace(go.Bar(
            x=years,
            y=data[col],
            name=col,
            marker_color=color,
            hoverinfo="skip",
        ))

    fig.update_layout(barmode="stack")
    clean_layout(fig, 200)

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False, "staticPlot": True},
    )

    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Repeat rate", "Retention strengthens")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=years,
        y=data["Repeat Rate"],
        mode="lines+markers+text",
        line=dict(color=BROWN, width=3),
        marker=dict(size=7, color=GOLD),
        text=[f"{x}%" for x in data["Repeat Rate"]],
        textposition="top center",
        hoverinfo="skip",
    ))

    clean_layout(fig, 200)
    fig.update_layout(showlegend=False)
    fig.update_yaxes(range=[30, 62])

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False, "staticPlot": True},
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# ROW 2
# ============================================================

r1, r2, r3 = st.columns([0.9, 1.3, 1.5])

with r1:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Purchase frequency", "Units per customer per year")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=years,
        y=data["Purchase Frequency"],
        mode="lines+markers+text",
        line=dict(color=TERRACOTTA, width=3),
        marker=dict(size=7, color=PEACH),
        text=[f"{x:.1f}×" for x in data["Purchase Frequency"]],
        textposition="top center",
        hoverinfo="skip",
    ))

    clean_layout(fig, 180)
    fig.update_layout(showlegend=False)

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False, "staticPlot": True},
    )

    st.markdown('</div>', unsafe_allow_html=True)

with r2:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Customer base + ARPU", "Scale and monetisation")

    fig = go.Figure()

    active_lakh = data["Active Customers"] / 100000

    fig.add_trace(go.Bar(
        x=years,
        y=active_lakh,
        name="Customers",
        marker_color=GOLD_LIGHT,
        hoverinfo="skip",
    ))

    fig.add_trace(go.Scatter(
        x=years,
        y=data["ARPU"],
        yaxis="y2",
        name="ARPU",
        mode="lines+markers",
        line=dict(color=BROWN, width=3),
        marker=dict(size=6, color=BROWN),
        hoverinfo="skip",
    ))

    fig.update_layout(
        yaxis2=dict(
            overlaying="y",
            side="right",
            showgrid=False,
            showticklabels=False,
        )
    )

    clean_layout(fig, 180)

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False, "staticPlot": True},
    )

    st.markdown("""
<div class="equation-box">
<div class="equation-main">2.12 Lakh × ₹4,900 ≈ ₹104 Crore</div>
<div class="equation-sub">Active customers × ARPU</div>
</div>
""", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with r3:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("LTV:CAC + EBITDA", "Economics mature before profitability")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=years,
        y=data["LTV CAC"],
        mode="lines+markers+text",
        name="LTV:CAC",
        line=dict(color=BROWN, width=3),
        marker=dict(size=7, color=BROWN),
        text=[f"{x:.2f}×" for x in data["LTV CAC"]],
        textposition="top center",
        hoverinfo="skip",
    ))

    fig.add_trace(go.Bar(
        x=years,
        y=data["EBITDA Margin"],
        yaxis="y2",
        name="EBITDA Margin",
        marker_color=PEACH,
        opacity=0.7,
        hoverinfo="skip",
    ))

    fig.update_layout(
        yaxis2=dict(
            overlaying="y",
            side="right",
            ticksuffix="%",
            showgrid=False,
        )
    )

    clean_layout(fig, 180)

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False, "staticPlot": True},
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# ROW 3
# ============================================================

a, b, c = st.columns([1.15, 1.15, 0.9])

with a:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Growth engine", "Core quantified levers")

    growth = pd.DataFrame({
        "Metric": [
            "Active customers",
            "Repeat rate",
            "Derived AOV",
            "Purchase frequency",
            "ARPU",
        ],
        "Y1": ["12.5K", "36%", "₹1,183", "5.5×", "₹3,200"],
        "Y2": ["43.2K", "44%", "₹1,104", "6.5×", "₹3,700"],
        "Y3": ["100K", "50%", "₹1,047", "7.5×", "₹4,200"],
        "Y4": ["156.5K", "55%", "₹981", "8.3×", "₹4,600"],
        "Y5": ["212.2K", "58%", "₹946", "9.0×", "₹4,900"],
    })

    st.dataframe(
        growth,
        hide_index=True,
        use_container_width=True,
        height=185,
    )

    st.markdown('</div>', unsafe_allow_html=True)

with b:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Financial quality", "Economics at scale")

    fin = pd.DataFrame({
        "Metric": [
            "CAC",
            "LTV",
            "LTV:CAC",
            "Gross Margin",
            "CM1",
            "CM2",
            "EBITDA Margin",
        ],
        "Y1": ["₹1,120", "₹2,488", "2.22×", "59.4%", "43.6%", "8.6%", "-67.7%"],
        "Y3": ["₹1,232", "₹3,672", "2.98×", "63.2%", "42.6%", "19.6%", "-2.5%"],
        "Y5": ["₹1,284", "₹4,703", "3.66×", "63.4%", "40.3%", "25.3%", "9.1%"],
    })

    st.dataframe(
        fin,
        hide_index=True,
        use_container_width=True,
        height=225,
    )

    st.markdown('</div>', unsafe_allow_html=True)

with c:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Personalization pays", "Y5 vs no-quiz")

    impact_html = """
<div class="impact-wrap">
<div class="impact-card">
<div class="impact-number">23%</div>
<div class="impact-label">Lower CAC</div>
</div>
<div class="impact-card">
<div class="impact-number">25%</div>
<div class="impact-label">Higher LTV</div>
</div>
</div>
"""

    st.markdown(impact_html, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# FIVE YEAR PATH
# ============================================================

st.markdown('<div class="panel">', unsafe_allow_html=True)
panel_header("Five-year scale path", "What changes economically as MenoSakhi grows")

timeline_html = """
<div class="timeline">
<div class="year-box">
<div class="year-title">Y1 · Prove</div>
<div class="year-copy">
₹4 Cr revenue<br>
12.5K customers<br>
36% repeat<br>
Digital-only
</div>
</div>

<div class="year-box">
<div class="year-title">Y2 · Build</div>
<div class="year-copy">
₹16 Cr revenue<br>
43.2K customers<br>
44% repeat<br>
Q-commerce scales
</div>
</div>

<div class="year-box">
<div class="year-title">Y3 · Scale</div>
<div class="year-copy">
₹42 Cr revenue<br>
1.0L customers<br>
50% repeat<br>
2.98× LTV:CAC
</div>
</div>

<div class="year-box">
<div class="year-title">Y4 · Break even</div>
<div class="year-copy">
₹72 Cr revenue<br>
EBITDA positive<br>
55% repeat<br>
Offline enters
</div>
</div>

<div class="year-box">
<div class="year-title">Y5 · ₹100 Cr+</div>
<div class="year-copy">
₹104 Cr revenue<br>
2.12L customers<br>
58% repeat<br>
9.1% EBITDA
</div>
</div>
</div>
"""

st.markdown(timeline_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
