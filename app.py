import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title="MenoSakhi | Path to ₹100 Crore",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# COLORS
# ============================================================

CREAM = "#FBF3E7"
CREAM_2 = "#F8EBDD"
BROWN = "#4A3020"
BROWN_2 = "#765A43"
GOLD = "#D5A456"
GOLD_LIGHT = "#E6C999"
TERRACOTTA = "#C97F58"
PEACH = "#E9B78E"
SAND = "#E9D5B6"
OLIVE = "#8B8A6A"
MUTED = "#8A705B"
WHITE = "#FFFDF9"
GRID = "#E8D9C6"

# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
<style>

html {{
    zoom: 0.90;
}}

.stApp {{
    background: {CREAM};
    color: {BROWN};
}}

header[data-testid="stHeader"] {{
    height: 0px;
    background: transparent;
}}

#MainMenu, footer {{
    visibility: hidden;
}}

.block-container {{
    width: 100% !important;
    max-width: 100% !important;
    padding: 0.35rem 1.1rem 0.25rem 1.1rem !important;
}}

[data-testid="stHorizontalBlock"] {{
    gap: 0.55rem !important;
}}

[data-testid="stVerticalBlock"] {{
    gap: 0.35rem !important;
}}

/* Real Streamlit bordered containers */
div[data-testid="stVerticalBlockBorderWrapper"] {

    border: 1.5px solid #D9AD69 !important;

    border-radius: 14px !important;

    background: #FFFDF9 !important;

    box-shadow: 0 2px 8px rgba(74,48,32,0.06) !important;

}

div[data-testid="stVerticalBlockBorderWrapper"] > div {

    padding: 0.65rem 0.75rem !important;

}

.eyebrow {{
    font-size: 0.56rem;
    color: {GOLD};
    font-weight: 800;
    letter-spacing: 0.11em;
    text-transform: uppercase;
}}

.main-title {{
    color: {BROWN};
    font-size: 1.72rem;
    line-height: 1;
    font-weight: 850;
    margin: 0.08rem 0 0.16rem 0;
}}

.subtitle {{
    color: {BROWN_2};
    font-size: 0.66rem;
    line-height: 1.25;
    margin: 0;
}}

.section-title {{
    color: {BROWN};
    font-size: 0.66rem;
    line-height: 1;
    font-weight: 850;
    text-transform: uppercase;
    letter-spacing: 0.045em;
    margin: 0 0 2px 0;
}}

.section-sub {{
    color: {MUTED};
    font-size: 0.49rem;
    line-height: 1.15;
    margin-bottom: 1px;
}}

.kpi-label {{
    color: {MUTED};
    font-size: 0.48rem;
    font-weight: 800;
    text-transform: uppercase;
}}

.kpi-value {{
    color: {BROWN};
    font-size: 1.28rem;
    line-height: 1.05;
    font-weight: 850;
    margin: 3px 0;
}}

.kpi-sub {{
    color: {BROWN_2};
    font-size: 0.49rem;
    line-height: 1.15;
}}

.eq {{
    background: {BROWN};
    color: {CREAM};
    border-radius: 8px;
    padding: 6px 8px;
    text-align: center;
    font-size: 0.68rem;
    font-weight: 800;
    margin-top: 2px;
}}

.eq-small {{
    font-size: 0.43rem;
    opacity: 0.8;
    font-weight: 400;
}}

.impact-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
}}

.impact {{
    background: {CREAM_2};
    border: 1px solid {GOLD_LIGHT};
    border-radius: 8px;
    text-align: center;
    padding: 7px 4px;
}}

.impact-num {{
    color: {BROWN};
    font-size: 1.1rem;
    font-weight: 850;
}}

.impact-text {{
    color: {BROWN_2};
    font-size: 0.48rem;
    font-weight: 750;
    text-transform: uppercase;
}}

table.fin {{
    width: 100%;
    border-collapse: collapse;
    color: {BROWN};
    font-size: 0.46rem;
    line-height: 1.1;
}}

table.fin th {{
    background: {BROWN};
    color: {CREAM};
    padding: 3px 4px;
    border: 1px solid {GOLD_LIGHT};
    font-weight: 700;
}}

table.fin td {{
    padding: 3px 4px;
    border: 1px solid {GOLD_LIGHT};
    text-align: center;
}}

table.fin td:first-child {{
    text-align: left;
    font-weight: 650;
}}

.timeline {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 4px;
}}

.year {{
    border: 1px solid {GOLD_LIGHT};
    border-top: 3px solid {GOLD};
    border-radius: 7px;
    background: {WHITE};
    padding: 5px;
    min-height: 64px;
}}

.year-head {{
    color: {BROWN};
    font-size: 0.52rem;
    font-weight: 850;
    margin-bottom: 3px;
}}

.year-body {{
    color: {BROWN_2};
    font-size: 0.42rem;
    line-height: 1.25;
}}

</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# DATA
# ============================================================

years = ["Y1", "Y2", "Y3", "Y4", "Y5"]

df = pd.DataFrame({
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
    "Frequency": [5.54, 6.49, 7.51, 8.32, 8.97],

    "Customers Lakh": [0.125, 0.43243, 1.00, 1.56522, 2.12245],
    "ARPU": [3200, 3700, 4200, 4600, 4900],

    "LTV CAC": [2.22, 2.32, 2.98, 3.33, 3.66],
    "EBITDA Margin": [-67.68, -22.59, -2.50, 5.38, 9.06],
})

# ============================================================
# HELPERS
# ============================================================

def title(text, sub=""):
    st.markdown(
        f"""
<div class="section-title">{text}</div>
<div class="section-sub">{sub}</div>
""",
        unsafe_allow_html=True,
    )


def clean_chart(fig, height=150):
    fig.update_layout(
        height=height,
        margin=dict(l=8, r=8, t=13, b=8),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        hovermode=False,
        font=dict(
            family="Arial",
            size=7,
            color=BROWN_2
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            x=0,
            font=dict(size=6),
        ),
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        tickfont=dict(size=7, color=MUTED),
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        tickfont=dict(size=6, color=MUTED),
    )

    return fig


config = {
    "displayModeBar": False,
    "staticPlot": True,
}

# ============================================================
# HEADER
# ============================================================

left, logo = st.columns([6.8, 1.2])

with left:
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

with logo:
    if Path("logo.png").exists():
        st.image("logo.png", use_container_width=True)

# ============================================================
# KPI ROW
# ============================================================

k1, k2, k3, k4 = st.columns(4)

for col, label, value, sub in [
    (k1, "Y5 Revenue", "₹104 Cr", "Crosses ₹100 Cr by Year 5"),
    (k2, "Active Customers", "2.12 Lakh", "Scaled customer base"),
    (k3, "Y5 ARPU", "₹4,900", "Repeat + purchase frequency"),
    (k4, "Y5 EBITDA Margin", "9.1%", "Positive from Y4 @ ₹72 Cr"),
]:
    with col:
        with st.container(border=True):
            st.markdown(
                f"""
<div class="kpi-label">{label}</div>
<div class="kpi-value">{value}</div>
<div class="kpi-sub">{sub}</div>
""",
                unsafe_allow_html=True,
            )

# ============================================================
# ROW 1
# ============================================================

c1, c2, c3 = st.columns([1.25, 1.25, 0.9])

# CHANNEL
with c1:
    with st.container(border=True):
        title("Revenue by channel", "₹ Cr · digital-first through Y3")

        fig = go.Figure()

        channel_colors = {
            "D2C": BROWN,
            "Marketplace": GOLD,
            "Quick Commerce": TERRACOTTA,
            "Offline": SAND,
        }

        for name, color in channel_colors.items():

            labels = [
                "" if pd.isna(x) else f"{x:.1f}"
                for x in df[name]
            ]

            fig.add_trace(
                go.Bar(
                    x=years,
                    y=df[name],
                    name=name,
                    marker_color=color,
                    text=labels,
                    textposition="inside",
                    textfont=dict(size=6),
                    hoverinfo="skip",
                )
            )

        fig.update_layout(barmode="stack")
        clean_chart(fig, 158)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config=config,
        )

# SKU
with c2:
    with st.container(border=True):
        title("Revenue by SKU", "₹ Cr · portfolio mix evolves")

        fig = go.Figure()

        sku_colors = {
            "Morning Pancake Mix": OLIVE,
            "Night Core Capsule": BROWN,
            "Heat Relief Roll-on": TERRACOTTA,
            "Calm Infusion Tea": GOLD,
        }

        for name, color in sku_colors.items():
            fig.add_trace(
                go.Bar(
                    x=years,
                    y=df[name],
                    name=name,
                    marker_color=color,
                    hoverinfo="skip",
                )
            )

        fig.update_layout(barmode="stack")
        clean_chart(fig, 158)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config=config,
        )

# REPEAT
with c3:
    with st.container(border=True):
        title("Repeat rate", "Retention strengthens each year")

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=years,
                y=df["Repeat Rate"],
                mode="lines+markers+text",
                line=dict(color=BROWN, width=2.4),
                marker=dict(
                    size=6,
                    color=GOLD,
                    line=dict(color=BROWN, width=1)
                ),
                text=[f"{x}%" for x in df["Repeat Rate"]],
                textposition="top center",
                textfont=dict(size=7, color=BROWN),
                hoverinfo="skip",
            )
        )

        clean_chart(fig, 158)
        fig.update_layout(showlegend=False)
        fig.update_yaxes(range=[30, 63])

        st.plotly_chart(
            fig,
            use_container_width=True,
            config=config,
        )

# ============================================================
# ROW 2
# ============================================================

c1, c2, c3 = st.columns([0.9, 1.25, 1.25])

# FREQUENCY
with c1:
    with st.container(border=True):
        title("Purchase frequency", "Units / customer / year")

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=years,
                y=df["Frequency"],
                mode="lines+markers+text",
                line=dict(color=TERRACOTTA, width=2.4),
                marker=dict(
                    size=6,
                    color=PEACH,
                    line=dict(color=TERRACOTTA, width=1)
                ),
                text=[f"{x:.1f}×" for x in df["Frequency"]],
                textposition="top center",
                textfont=dict(size=7, color=BROWN),
                hoverinfo="skip",
            )
        )

        clean_chart(fig, 140)
        fig.update_layout(showlegend=False)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config=config,
        )

# CUSTOMERS + ARPU
with c2:
    with st.container(border=True):
        title("Customer base + ARPU", "Scale and monetisation grow together")

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=years,
                y=df["Customers Lakh"],
                name="Customers",
                marker_color=GOLD_LIGHT,
                text=[
                    "0.13L",
                    "0.43L",
                    "1.00L",
                    "1.57L",
                    "2.12L"
                ],
                textposition="outside",
                textfont=dict(size=6, color=BROWN),
                hoverinfo="skip",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=years,
                y=df["ARPU"],
                yaxis="y2",
                name="ARPU",
                mode="lines+markers+text",
                line=dict(color=BROWN, width=2.3),
                marker=dict(size=5, color=BROWN),
                text=[f"₹{x:,}" for x in df["ARPU"]],
                textposition="top center",
                textfont=dict(size=6, color=BROWN),
                hoverinfo="skip",
            )
        )

        fig.update_layout(
            yaxis2=dict(
                overlaying="y",
                side="right",
                showgrid=False,
                showticklabels=False,
            )
        )

        clean_chart(fig, 122)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config=config,
        )

        st.markdown(
            """
<div class="eq">
2.12 Lakh × ₹4,900 ≈ ₹104 Crore
<div class="eq-small">Active customers × ARPU</div>
</div>
""",
            unsafe_allow_html=True,
        )

# LTV CAC + EBITDA
with c3:
    with st.container(border=True):
        title("LTV:CAC + EBITDA", "Customer economics mature before profitability")

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=years,
                y=df["LTV CAC"],
                mode="lines+markers+text",
                name="LTV:CAC",
                line=dict(color=BROWN, width=2.3),
                marker=dict(size=6, color=BROWN),
                text=[f"{x:.2f}×" for x in df["LTV CAC"]],
                textposition="top center",
                textfont=dict(size=6, color=BROWN),
                hoverinfo="skip",
            )
        )

        fig.add_trace(
            go.Bar(
                x=years,
                y=df["EBITDA Margin"],
                yaxis="y2",
                name="EBITDA margin",
                marker_color=PEACH,
                opacity=0.65,
                hoverinfo="skip",
            )
        )

        fig.update_layout(
            yaxis2=dict(
                overlaying="y",
                side="right",
                showgrid=False,
                ticksuffix="%",
            )
        )

        clean_chart(fig, 155)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config=config,
        )

# ============================================================
# BOTTOM ROW
# ============================================================

b1, b2, b3 = st.columns([1.18, 1.02, 1.8])

# GROWTH ENGINE
with b1:
    with st.container(border=True):
        title("Growth engine", "Core quantified levers")

        growth_html = """
<table class="fin">
<tr>
<th>Metric</th><th>Y1</th><th>Y2</th><th>Y3</th><th>Y4</th><th>Y5</th>
</tr>
<tr>
<td>Customers</td><td>12.5K</td><td>43.2K</td><td>100K</td><td>156.5K</td><td>212.2K</td>
</tr>
<tr>
<td>Repeat</td><td>36%</td><td>44%</td><td>50%</td><td>55%</td><td>58%</td>
</tr>
<tr>
<td>Derived AOV</td><td>₹1,183</td><td>₹1,104</td><td>₹1,047</td><td>₹981</td><td>₹946</td>
</tr>
<tr>
<td>Frequency</td><td>5.5×</td><td>6.5×</td><td>7.5×</td><td>8.3×</td><td>9.0×</td>
</tr>
<tr>
<td>ARPU</td><td>₹3,200</td><td>₹3,700</td><td>₹4,200</td><td>₹4,600</td><td>₹4,900</td>
</tr>
</table>
"""

        st.markdown(
            growth_html,
            unsafe_allow_html=True,
        )

# FINANCIAL QUALITY
with b2:
    with st.container(border=True):
        title("Financial quality", "Launch → scale → maturity")

        fin_html = """
<table class="fin">
<tr>
<th>Metric</th><th>Y1</th><th>Y3</th><th>Y5</th>
</tr>
<tr>
<td>CAC</td><td>₹1,120</td><td>₹1,232</td><td>₹1,284</td>
</tr>
<tr>
<td>LTV</td><td>₹2,488</td><td>₹3,672</td><td>₹4,703</td>
</tr>
<tr>
<td>LTV:CAC</td><td>2.22×</td><td>2.98×</td><td>3.66×</td>
</tr>
<tr>
<td>Gross Margin</td><td>59.4%</td><td>63.2%</td><td>63.4%</td>
</tr>
<tr>
<td>CM1</td><td>43.6%</td><td>42.6%</td><td>40.3%</td>
</tr>
<tr>
<td>CM2</td><td>8.6%</td><td>19.6%</td><td>25.3%</td>
</tr>
<tr>
<td>EBITDA</td><td>-67.7%</td><td>-2.5%</td><td>9.1%</td>
</tr>
</table>
"""

        st.markdown(
            fin_html,
            unsafe_allow_html=True,
        )

# PERSONALIZATION + TIMELINE IN SAME BOX
with b3:
    with st.container(border=True):

        topa, topb = st.columns([0.7, 1.3])

        with topa:
            title("Personalization pays", "Y5 vs no-quiz")

        with topb:
            impact_html = """
<div class="impact-grid">
<div class="impact">
<div class="impact-num">23%</div>
<div class="impact-text">Lower CAC</div>
</div>
<div class="impact">
<div class="impact-num">25%</div>
<div class="impact-text">Higher LTV</div>
</div>
</div>
"""
            st.markdown(
                impact_html,
                unsafe_allow_html=True,
            )

        st.markdown(
            """
<div style="
border-top:1px solid #E6C999;
margin:5px 0 5px 0;
"></div>
""",
            unsafe_allow_html=True,
        )

        title(
            "Five-year scale path",
            "What changes economically as MenoSakhi grows"
        )

        timeline = """
<div class="timeline">

<div class="year">
<div class="year-head">Y1 · Prove</div>
<div class="year-body">
₹4 Cr revenue<br>
12.5K customers<br>
36% repeat<br>
Digital-only
</div>
</div>

<div class="year">
<div class="year-head">Y2 · Build</div>
<div class="year-body">
₹16 Cr revenue<br>
43.2K customers<br>
44% repeat<br>
Q-commerce scales
</div>
</div>

<div class="year">
<div class="year-head">Y3 · Scale</div>
<div class="year-body">
₹42 Cr revenue<br>
1.0L customers<br>
50% repeat<br>
2.98× LTV:CAC
</div>
</div>

<div class="year">
<div class="year-head">Y4 · Break even</div>
<div class="year-body">
₹72 Cr revenue<br>
EBITDA positive<br>
55% repeat<br>
Offline enters
</div>
</div>

<div class="year">
<div class="year-head">Y5 · ₹100 Cr+</div>
<div class="year-body">
₹104 Cr revenue<br>
2.12L customers<br>
58% repeat<br>
9.1% EBITDA
</div>
</div>

</div>
"""

        st.markdown(
            timeline,
            unsafe_allow_html=True,
        )

st.markdown(
    """
<style>

/* Make dashboard occupy the visible screen */
section.main {
    min-height: auto !important;
}

[data-testid="stAppViewContainer"] {
    min-height: auto !important;
}

.stApp {
    min-height: auto !important;
}

/* Slightly enlarge the bottom section */
table.fin {
    font-size: 0.56rem !important;
}

.year-head {
    font-size: 0.62rem !important;
}

.year-body {
    font-size: 0.50rem !important;
    line-height: 1.35 !important;
}

.impact-num {
    font-size: 1.35rem !important;
}

.impact-text {
    font-size: 0.56rem !important;
}

</style>
""",
    unsafe_allow_html=True,
)
