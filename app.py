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

html, body, [class*="css"] {{
    font-family: Arial, sans-serif;
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
    padding: 0.45rem 0.8rem 0.3rem 0.8rem !important;
}}

[data-testid="stHorizontalBlock"] {{
    gap: 0.55rem !important;
}}

[data-testid="stVerticalBlock"] {{
    gap: 0.35rem !important;
}}

/* CARD BORDERS */
div[data-testid="stVerticalBlockBorderWrapper"] {{
    border: 1.3px solid {GOLD_LIGHT} !important;
    border-radius: 12px !important;
    background: rgba(255,253,249,0.88) !important;
    box-shadow: 0 2px 7px rgba(74,48,32,0.04) !important;
}}

div[data-testid="stVerticalBlockBorderWrapper"] > div {{
    padding: 0.55rem 0.65rem !important;
}}

/* HEADER */
.eyebrow {{
    font-size: 0.68rem;
    color: {GOLD};
    font-weight: 800;
    letter-spacing: 0.11em;
    text-transform: uppercase;
}}

.main-title {{
    font-size: 2.05rem;
    line-height: 1;
    color: {BROWN};
    font-weight: 850;
    margin: 0.08rem 0 0.18rem 0;
}}

.subtitle {{
    font-size: 0.80rem;
    line-height: 1.30;
    color: {BROWN_2};
    max-width: 920px;
}}

/* SECTION TITLES */
.section-title {{
    font-size: 0.82rem;
    font-weight: 850;
    color: {BROWN};
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 1px;
}}

.section-sub {{
    font-size: 0.60rem;
    color: {MUTED};
    margin-bottom: 2px;
}}

/* KPI */
.kpi-label {{
    font-size: 0.57rem;
    text-transform: uppercase;
    font-weight: 800;
    color: {MUTED};
}}

.kpi-value {{
    font-size: 1.48rem;
    font-weight: 850;
    color: {BROWN};
    margin: 3px 0;
}}

.kpi-sub {{
    font-size: 0.56rem;
    color: {BROWN_2};
    line-height: 1.2;
}}

/* EQUATION */
.eq {{
    background: {BROWN};
    color: {CREAM};
    border-radius: 8px;
    padding: 7px 8px;
    text-align: center;
    margin-top: 4px;
}}

.eq-main {{
    font-size: 0.85rem;
    font-weight: 850;
}}

.eq-sub {{
    font-size: 0.48rem;
    opacity: 0.82;
}}

/* IMPACT */
.impact-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
}}

.impact {{
    background: {CREAM_2};
    border: 1px solid {GOLD_LIGHT};
    border-radius: 9px;
    padding: 8px 5px;
    text-align: center;
}}

.impact-num {{
    font-size: 1.35rem;
    font-weight: 850;
    color: {BROWN};
}}

.impact-text {{
    font-size: 0.58rem;
    text-transform: uppercase;
    font-weight: 750;
    color: {BROWN_2};
}}

/* TABLES */
table.fin {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.56rem;
    line-height: 1.16;
    color: {BROWN};
}}

table.fin th {{
    background: {BROWN};
    color: {CREAM};
    border: 1px solid {GOLD_LIGHT};
    padding: 4px 5px;
    font-weight: 750;
}}

table.fin td {{
    border: 1px solid {GOLD_LIGHT};
    padding: 4px 5px;
    text-align: center;
}}

table.fin td:first-child {{
    text-align: left;
    font-weight: 650;
}}

/* TIMELINE */
.timeline {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 5px;
}}

.year {{
    background: {WHITE};
    border: 1px solid {GOLD_LIGHT};
    border-top: 3px solid {GOLD};
    border-radius: 7px;
    padding: 6px;
    min-height: 78px;
}}

.year-head {{
    font-size: 0.63rem;
    font-weight: 850;
    color: {BROWN};
    margin-bottom: 3px;
}}

.year-body {{
    font-size: 0.51rem;
    line-height: 1.34;
    color: {BROWN_2};
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

def section_title(title, sub=""):
    st.markdown(
        f"""
<div class="section-title">{title}</div>
<div class="section-sub">{sub}</div>
""",
        unsafe_allow_html=True,
    )


def clean_chart(fig, height=175):

    fig.update_layout(
        height=height,
        margin=dict(l=10, r=10, t=24, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        hovermode=False,

        font=dict(
            family="Arial",
            size=10,
            color=BROWN_2,
        ),

        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.03,
            xanchor="left",
            x=0,
            font=dict(size=9),
        ),
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        tickfont=dict(size=9, color=MUTED),
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        tickfont=dict(size=8, color=MUTED),
    )

    return fig


chart_config = {
    "displayModeBar": False,
    "staticPlot": True,
}

# ============================================================
# HEADER
# ============================================================

logo_col, text_col = st.columns([0.75, 6.25])

with logo_col:
    if Path("logo.png").exists():
        st.image("logo.png", width=120)

with text_col:
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

# ============================================================
# KPI ROW
# ============================================================

k1, k2, k3, k4 = st.columns(4)

kpis = [
    (k1, "Y5 Revenue", "₹104 Cr", "Crosses the ₹100 Cr ambition by Year 5"),
    (k2, "Active Customers", "2.12 Lakh", "Scaled customer base"),
    (k3, "Y5 ARPU", "₹4,900", "Driven by repeat and purchase frequency"),
    (k4, "Y5 EBITDA Margin", "9.1%", "EBITDA positive from Y4 at ₹72 Cr"),
]

for col, label, value, sub in kpis:

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
# TOP ROW
# ============================================================

c1, c2, c3 = st.columns([1.25, 1.25, 0.9])

# CHANNEL
with c1:

    with st.container(border=True):

        section_title(
            "Revenue by channel",
            "₹ Cr · digital-first through Y3"
        )

        fig = go.Figure()

        channel_colors = {
            "D2C": BROWN,
            "Marketplace": GOLD,
            "Quick Commerce": TERRACOTTA,
            "Offline": SAND,
        }

        for name, color in channel_colors.items():

            labels = [
                "" if pd.isna(v) else f"{v:.1f}"
                for v in df[name]
            ]

            fig.add_trace(
                go.Bar(
                    x=years,
                    y=df[name],
                    name=name,
                    marker_color=color,
                    text=labels,
                    textposition="inside",
                    textfont=dict(size=9),
                    hoverinfo="skip",
                )
            )

        fig.update_layout(barmode="stack")

        fig.add_trace(
            go.Scatter(
                x=years,
                y=[7, 20, 47, 79, 111],
                mode="text",
                text=[
                    "₹4 Cr",
                    "₹16 Cr",
                    "₹42 Cr",
                    "₹72 Cr",
                    "₹104 Cr"
                ],
                textfont=dict(size=9, color=BROWN),
                showlegend=False,
                hoverinfo="skip",
            )
        )

        clean_chart(fig, 190)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config=chart_config,
        )

# SKU
with c2:

    with st.container(border=True):

        section_title(
            "Revenue by SKU",
            "₹ Cr · portfolio mix evolves over time"
        )

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

        clean_chart(fig, 190)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config=chart_config,
        )

# REPEAT
with c3:

    with st.container(border=True):

        section_title(
            "Repeat rate",
            "Retention strengthens each year"
        )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=years,
                y=df["Repeat Rate"],
                mode="lines+markers+text",
                line=dict(
                    color=BROWN,
                    width=2.8
                ),
                marker=dict(
                    size=8,
                    color=GOLD,
                    line=dict(
                        color=BROWN,
                        width=1
                    )
                ),
                text=[
                    f"{x}%"
                    for x in df["Repeat Rate"]
                ],
                textposition="top center",
                textfont=dict(
                    size=10,
                    color=BROWN
                ),
                hoverinfo="skip",
            )
        )

        clean_chart(fig, 190)

        fig.update_layout(showlegend=False)

        fig.update_yaxes(
            range=[30, 63],
            ticksuffix="%"
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config=chart_config,
        )

# ============================================================
# MIDDLE ROW
# ============================================================

m1, m2, m3 = st.columns([0.9, 1.25, 1.25])

# PURCHASE FREQUENCY
with m1:

    with st.container(border=True):

        section_title(
            "Purchase frequency",
            "Units per customer per year"
        )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=years,
                y=df["Frequency"],
                mode="lines+markers+text",
                line=dict(
                    color=TERRACOTTA,
                    width=2.8
                ),
                marker=dict(
                    size=8,
                    color=PEACH,
                    line=dict(
                        color=TERRACOTTA,
                        width=1
                    )
                ),
                text=[
                    f"{x:.1f}×"
                    for x in df["Frequency"]
                ],
                textposition="top center",
                textfont=dict(
                    size=10,
                    color=BROWN
                ),
                hoverinfo="skip",
            )
        )

        clean_chart(fig, 165)

        fig.update_layout(showlegend=False)

        fig.update_yaxes(
            range=[4.5, 9.8]
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config=chart_config,
        )

# CUSTOMER + ARPU
with m2:

    with st.container(border=True):

        section_title(
            "Customer base + ARPU",
            "Scale and monetisation grow together"
        )

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=years,
                y=df["Customers Lakh"],
                name="Active Customers",
                marker_color=GOLD_LIGHT,
                text=[
                    "0.13L",
                    "0.43L",
                    "1.00L",
                    "1.57L",
                    "2.12L"
                ],
                textposition="outside",
                textfont=dict(
                    size=9,
                    color=BROWN
                ),
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
                line=dict(
                    color=BROWN,
                    width=2.6
                ),
                marker=dict(
                    size=7,
                    color=BROWN
                ),
                text=[
                    f"₹{x:,}"
                    for x in df["ARPU"]
                ],
                textposition="top center",
                textfont=dict(
                    size=9,
                    color=BROWN
                ),
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

        clean_chart(fig, 142)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config=chart_config,
        )

        st.markdown(
            """
<div class="eq">
<div class="eq-main">2.12 Lakh × ₹4,900 ≈ ₹104 Crore</div>
<div class="eq-sub">Active customers × ARPU</div>
</div>
""",
            unsafe_allow_html=True,
        )

# LTV CAC + EBITDA
with m3:

    with st.container(border=True):

        section_title(
            "LTV:CAC + EBITDA",
            "Customer economics mature before profitability"
        )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=years,
                y=df["LTV CAC"],
                mode="lines+markers+text",
                name="LTV:CAC",
                line=dict(
                    color=BROWN,
                    width=2.6
                ),
                marker=dict(
                    size=8,
                    color=BROWN
                ),
                text=[
                    f"{x:.2f}×"
                    for x in df["LTV CAC"]
                ],
                textposition="top center",
                textfont=dict(
                    size=9,
                    color=BROWN
                ),
                hoverinfo="skip",
            )
        )

        fig.add_trace(
            go.Bar(
                x=years,
                y=df["EBITDA Margin"],
                yaxis="y2",
                name="EBITDA Margin",
                marker_color=PEACH,
                opacity=0.68,
                hoverinfo="skip",
            )
        )

        fig.update_layout(
            yaxis2=dict(
                overlaying="y",
                side="right",
                ticksuffix="%",
                showgrid=False,
                range=[-80, 20],
            )
        )

        clean_chart(fig, 172)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config=chart_config,
        )

# ============================================================
# BOTTOM ROW
# ============================================================

b1, b2, b3 = st.columns([1.15, 1.0, 1.85])

# GROWTH ENGINE
with b1:

    with st.container(border=True):

        section_title(
            "Growth engine",
            "Core quantified levers"
        )

        st.markdown(
            """
<table class="fin">

<tr>
<th>Metric</th>
<th>Y1</th>
<th>Y2</th>
<th>Y3</th>
<th>Y4</th>
<th>Y5</th>
</tr>

<tr>
<td>Customers</td>
<td>12.5K</td>
<td>43.2K</td>
<td>100K</td>
<td>156.5K</td>
<td>212.2K</td>
</tr>

<tr>
<td>Repeat rate</td>
<td>36%</td>
<td>44%</td>
<td>50%</td>
<td>55%</td>
<td>58%</td>
</tr>

<tr>
<td>Derived AOV</td>
<td>₹1,183</td>
<td>₹1,104</td>
<td>₹1,047</td>
<td>₹981</td>
<td>₹946</td>
</tr>

<tr>
<td>Purchase frequency</td>
<td>5.5×</td>
<td>6.5×</td>
<td>7.5×</td>
<td>8.3×</td>
<td>9.0×</td>
</tr>

<tr>
<td>ARPU</td>
<td>₹3,200</td>
<td>₹3,700</td>
<td>₹4,200</td>
<td>₹4,600</td>
<td>₹4,900</td>
</tr>

</table>
""",
            unsafe_allow_html=True,
        )

# FINANCIAL QUALITY
with b2:

    with st.container(border=True):

        section_title(
            "Financial quality",
            "Launch → scale → maturity"
        )

        st.markdown(
            """
<table class="fin">

<tr>
<th>Metric</th>
<th>Y1</th>
<th>Y3</th>
<th>Y5</th>
</tr>

<tr>
<td>CAC</td>
<td>₹1,120</td>
<td>₹1,232</td>
<td>₹1,284</td>
</tr>

<tr>
<td>LTV</td>
<td>₹2,488</td>
<td>₹3,672</td>
<td>₹4,703</td>
</tr>

<tr>
<td>LTV:CAC</td>
<td>2.22×</td>
<td>2.98×</td>
<td>3.66×</td>
</tr>

<tr>
<td>Gross Margin</td>
<td>59.4%</td>
<td>63.2%</td>
<td>63.4%</td>
</tr>

<tr>
<td>CM1</td>
<td>43.6%</td>
<td>42.6%</td>
<td>40.3%</td>
</tr>

<tr>
<td>CM2</td>
<td>8.6%</td>
<td>19.6%</td>
<td>25.3%</td>
</tr>

<tr>
<td>EBITDA Margin</td>
<td>-67.7%</td>
<td>-2.5%</td>
<td>9.1%</td>
</tr>

</table>
""",
            unsafe_allow_html=True,
        )

# PERSONALIZATION + ROADMAP
with b3:

    with st.container(border=True):

        p1, p2 = st.columns([0.75, 1.25])

        with p1:

            section_title(
                "Personalization pays",
                "Y5 vs no-quiz"
            )

        with p2:

            st.markdown(
                """
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
""",
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
<div style="
border-top:1px solid {GOLD_LIGHT};
margin:7px 0 6px 0;">
</div>
""",
            unsafe_allow_html=True,
        )

        section_title(
            "Five-year scale path",
            "What changes economically as MenoSakhi grows"
        )

        st.markdown(
            """
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
""",
            unsafe_allow_html=True,
        )
