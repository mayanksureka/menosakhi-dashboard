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

    html, body, [class*="css"] {{
        font-family: "Aptos", "Helvetica Neue", Arial, sans-serif;
    }}

    .stApp {{
        background:
            radial-gradient(circle at 4% 6%, rgba(213,164,86,0.08), transparent 20%),
            radial-gradient(circle at 96% 95%, rgba(201,127,88,0.07), transparent 20%),
            {CREAM};
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
        max-width: 1600px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }}

    h1, h2, h3, h4 {{
        color: {BROWN};
    }}

    .brand-row {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 8px;
    }}

    .eyebrow {{
        font-size: 0.72rem;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: {GOLD};
        font-weight: 700;
        margin-bottom: 0.25rem;
    }}

    .main-title {{
        font-size: 2.15rem;
        line-height: 1.0;
        font-weight: 800;
        color: {BROWN};
        margin-bottom: 0.35rem;
    }}

    .subtitle {{
        font-size: 0.96rem;
        color: {BROWN_2};
        max-width: 950px;
        line-height: 1.45;
        margin-bottom: 0.8rem;
    }}

    .kpi-card {{
        background: rgba(255,253,249,0.72);
        border: 1px solid {GOLD_LIGHT};
        border-radius: 16px;
        padding: 14px 15px 13px 15px;
        min-height: 108px;
        box-shadow: 0 4px 12px rgba(74,48,32,0.04);
    }}

    .kpi-label {{
        color: {MUTED};
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-size: 0.67rem;
        font-weight: 700;
        margin-bottom: 4px;
    }}

    .kpi-value {{
        color: {BROWN};
        font-size: 1.82rem;
        line-height: 1.0;
        font-weight: 800;
        margin-bottom: 7px;
    }}

    .kpi-sub {{
        color: {BROWN_2};
        font-size: 0.74rem;
        line-height: 1.25;
    }}

    .panel {{
        background: rgba(255,253,249,0.70);
        border: 1px solid {GOLD_LIGHT};
        border-radius: 18px;
        padding: 14px 16px 12px 16px;
        box-shadow: 0 4px 12px rgba(74,48,32,0.035);
        margin-bottom: 14px;
    }}

    .panel-title {{
        font-size: 0.86rem;
        font-weight: 800;
        color: {BROWN};
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 1px;
    }}

    .panel-sub {{
        font-size: 0.69rem;
        color: {MUTED};
        margin-bottom: 7px;
    }}

    .equation-box {{
        background: {BROWN};
        border-radius: 14px;
        padding: 14px 18px;
        color: {CREAM};
        text-align: center;
        margin-top: 8px;
    }}

    .equation-main {{
        font-size: 1.15rem;
        font-weight: 800;
        letter-spacing: 0.01em;
    }}

    .equation-sub {{
        font-size: 0.68rem;
        opacity: 0.83;
        margin-top: 4px;
    }}

    .impact-wrap {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-top: 8px;
    }}

    .impact-card {{
        background: {CREAM_2};
        border: 1px solid {GOLD_LIGHT};
        border-radius: 14px;
        padding: 14px 10px;
        text-align: center;
    }}

    .impact-number {{
        font-size: 1.65rem;
        line-height: 1;
        font-weight: 800;
        color: {BROWN};
    }}

    .impact-label {{
        color: {BROWN_2};
        margin-top: 5px;
        font-size: 0.66rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }}

    .timeline {{
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 7px;
        margin-top: 8px;
    }}

    .year-box {{
        background: {WHITE};
        border-top: 4px solid {GOLD};
        border-radius: 8px;
        padding: 9px 8px;
        min-height: 95px;
    }}

    .year-title {{
        color: {BROWN};
        font-size: 0.77rem;
        font-weight: 800;
        margin-bottom: 5px;
    }}

    .year-copy {{
        color: {BROWN_2};
        font-size: 0.62rem;
        line-height: 1.35;
    }}

    .small-note {{
        font-size: 0.64rem;
        color: {MUTED};
        margin-top: 4px;
    }}

    div[data-testid="stDataFrame"] {{
        border: 1px solid {GOLD_LIGHT};
        border-radius: 12px;
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

data = pd.DataFrame(
    {
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

        # Derived approximate AOV
        "AOV": [1183, 1104, 1047, 981, 946],

        "CAC": [1120, 1314.14, 1232.48, 1276.57, 1284.35],
        "LTV": [2488, 3053, 3672, 4250, 4703],
        "LTV CAC": [2.22, 2.32, 2.98, 3.33, 3.66],
        "CAC Payback": [8.44, 9.22, 8.06, 8.01, 7.80],

        "Gross Margin": [59.45, 62.11, 63.15, 63.82, 63.41],
        "CM1": [43.57, 43.41, 42.64, 41.57, 40.31],
        "CM2": [8.57, 12.41, 19.64, 23.57, 25.31],
        "EBITDA": [-2.707, -3.615, -1.050, 3.873, 9.420],
        "EBITDA Margin": [-67.68, -22.59, -2.50, 5.38, 9.06],
    }
)

# ============================================================
# PLOTLY DEFAULTS
# ============================================================

def clean_layout(fig, height=270, margin=None):
    if margin is None:
        margin = dict(l=20, r=15, t=15, b=20)

    fig.update_layout(
        height=height,
        margin=margin,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Arial",
            color=BROWN_2,
            size=11,
        ),
        hovermode=False,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
            font=dict(size=9),
        ),
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        showline=False,
        tickfont=dict(size=10, color=MUTED),
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor=GRID,
        gridwidth=0.7,
        zeroline=False,
        showline=False,
        tickfont=dict(size=9, color=MUTED),
    )

    return fig


def panel_header(title, subtitle=""):
    st.markdown(
        f"""
        <div>
            <div class="panel-title">{title}</div>
            <div class="panel-sub">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HEADER
# ============================================================

header_left, header_right = st.columns([5.7, 1.3])

with header_left:
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

with header_right:
    logo_path = Path("logo.png")
    if logo_path.exists():
        st.image(str(logo_path), use_container_width=True)
    else:
        st.markdown(
            f"""
            <div style="
                text-align:right;
                color:{BROWN};
                font-size:1.25rem;
                font-weight:800;
                padding-top:20px;">
                MenoSakhi
            </div>
            """,
            unsafe_allow_html=True,
        )

# ============================================================
# KPI CARDS
# ============================================================

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-label">Y5 Revenue</div>
            <div class="kpi-value">₹104 Cr</div>
            <div class="kpi-sub">Crosses the ₹100 Cr ambition by Year 5</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k2:
    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-label">Active customers</div>
            <div class="kpi-value">2.12 Lakh</div>
            <div class="kpi-sub">Scaled customer base supporting the revenue build</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k3:
    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-label">Y5 ARPU</div>
            <div class="kpi-value">₹4,900</div>
            <div class="kpi-sub">Driven by repeat and purchase frequency</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k4:
    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-label">Y5 EBITDA margin</div>
            <div class="kpi-value">9.1%</div>
            <div class="kpi-sub">EBITDA positive from Y4 at ₹72 Cr revenue</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")

# ============================================================
# ROW 1
# ============================================================

c1, c2, c3 = st.columns([1.42, 1.42, 0.86])

with c1:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Revenue by channel", "₹ Cr · digital-first through Y3")

    fig_channel = go.Figure()

    channel_series = {
        "D2C": BROWN,
        "Marketplace": GOLD,
        "Quick Commerce": TERRACOTTA,
        "Offline": SAND,
    }

    for channel, color in channel_series.items():
        vals = data[channel].tolist()

        labels = [
            "" if pd.isna(v) else f"{v:.1f}"
            for v in vals
        ]

        fig_channel.add_trace(
            go.Bar(
                x=years,
                y=vals,
                name=channel,
                marker_color=color,
                text=labels,
                textposition="inside",
                insidetextanchor="middle",
                textfont=dict(size=8, color=WHITE if channel == "D2C" else BROWN),
                hoverinfo="skip",
            )
        )

    fig_channel.update_layout(barmode="stack")

    # Total revenue labels
    fig_channel.add_trace(
        go.Scatter(
            x=years,
            y=[4.8, 18, 45, 76, 109],
            mode="text",
            text=[f"₹{x} Cr" for x in data["Revenue"]],
            textfont=dict(size=10, color=BROWN),
            showlegend=False,
            hoverinfo="skip",
        )
    )

    clean_layout(fig_channel, height=275)
    fig_channel.update_yaxes(range=[0, 115], title=None)

    st.plotly_chart(
        fig_channel,
        use_container_width=True,
        config={"displayModeBar": False, "staticPlot": True},
    )
    st.markdown('</div>', unsafe_allow_html=True)


with c2:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Revenue by SKU", "₹ Cr · portfolio mix evolves over time")

    fig_sku = go.Figure()

    sku_series = {
        "Morning Pancake Mix": GREENISH,
        "Night Core Capsule": BROWN,
        "Heat Relief Roll-on": TERRACOTTA,
        "Calm Infusion Tea": GOLD,
    }

    for sku, color in sku_series.items():
        fig_sku.add_trace(
            go.Bar(
                x=years,
                y=data[sku],
                name=sku,
                marker_color=color,
                hoverinfo="skip",
            )
        )

    fig_sku.update_layout(barmode="stack")
    clean_layout(fig_sku, height=275)
    fig_sku.update_yaxes(range=[0, 112])

    st.plotly_chart(
        fig_sku,
        use_container_width=True,
        config={"displayModeBar": False, "staticPlot": True},
    )
    st.markdown('</div>', unsafe_allow_html=True)


with c3:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Repeat rate", "Retention strengthens each year")

    fig_repeat = go.Figure()

    fig_repeat.add_trace(
        go.Scatter(
            x=years,
            y=data["Repeat Rate"],
            mode="lines+markers+text",
            line=dict(color=BROWN, width=3),
            marker=dict(size=8, color=GOLD, line=dict(width=1.5, color=BROWN)),
            text=[f"{x:.0f}%" for x in data["Repeat Rate"]],
            textposition="top center",
            textfont=dict(size=10, color=BROWN),
            hoverinfo="skip",
        )
    )

    clean_layout(fig_repeat, height=275)
    fig_repeat.update_layout(showlegend=False)
    fig_repeat.update_yaxes(range=[25, 65], ticksuffix="%")

    st.plotly_chart(
        fig_repeat,
        use_container_width=True,
        config={"displayModeBar": False, "staticPlot": True},
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# ROW 2
# ============================================================

r2c1, r2c2, r2c3 = st.columns([0.92, 1.30, 1.48])

with r2c1:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Purchase frequency", "Units per active customer per year")

    fig_freq = go.Figure()

    fig_freq.add_trace(
        go.Scatter(
            x=years,
            y=data["Purchase Frequency"],
            mode="lines+markers+text",
            line=dict(color=TERRACOTTA, width=3),
            marker=dict(size=8, color=PEACH, line=dict(width=1.5, color=TERRACOTTA)),
            text=[f"{x:.1f}×" for x in data["Purchase Frequency"]],
            textposition="top center",
            textfont=dict(size=10, color=BROWN),
            hoverinfo="skip",
        )
    )

    clean_layout(fig_freq, height=245)
    fig_freq.update_layout(showlegend=False)
    fig_freq.update_yaxes(range=[4.5, 10])

    st.plotly_chart(
        fig_freq,
        use_container_width=True,
        config={"displayModeBar": False, "staticPlot": True},
    )
    st.markdown('</div>', unsafe_allow_html=True)


with r2c2:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Customer base + ARPU", "Scale and monetisation grow together")

    active_lakh = data["Active Customers"] / 100000

    fig_customer = go.Figure()

    fig_customer.add_trace(
        go.Bar(
            x=years,
            y=active_lakh,
            name="Active customers",
            marker_color=GOLD_LIGHT,
            text=[f"{x:.2f}L" for x in active_lakh],
            textposition="outside",
            textfont=dict(size=9, color=BROWN),
            hoverinfo="skip",
        )
    )

    fig_customer.add_trace(
        go.Scatter(
            x=years,
            y=data["ARPU"],
            name="ARPU",
            yaxis="y2",
            mode="lines+markers+text",
            line=dict(color=BROWN, width=3),
            marker=dict(color=BROWN, size=7),
            text=[f"₹{x:,}" for x in data["ARPU"]],
            textposition="top center",
            textfont=dict(size=9, color=BROWN),
            hoverinfo="skip",
        )
    )

    fig_customer.update_layout(
        yaxis=dict(
            title="Customers (Lakh)",
            range=[0, 2.45],
            gridcolor=GRID,
            zeroline=False,
        ),
        yaxis2=dict(
            title="",
            overlaying="y",
            side="right",
            range=[2500, 5400],
            showgrid=False,
            showticklabels=False,
            zeroline=False,
        ),
    )

    clean_layout(fig_customer, height=245)

    st.plotly_chart(
        fig_customer,
        use_container_width=True,
        config={"displayModeBar": False, "staticPlot": True},
    )

    st.markdown(
        """
        <div class="equation-box">
            <div class="equation-main">2.12 Lakh × ₹4,900 ≈ ₹104 Crore</div>
            <div class="equation-sub">Active customers × annual revenue per customer</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)


with r2c3:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("LTV:CAC + EBITDA", "Customer economics mature before profitability")

    fig_quality = go.Figure()

    fig_quality.add_trace(
        go.Scatter(
            x=years,
            y=data["LTV CAC"],
            name="LTV:CAC",
            mode="lines+markers+text",
            line=dict(color=BROWN, width=3),
            marker=dict(color=BROWN, size=7),
            text=[f"{x:.2f}×" for x in data["LTV CAC"]],
            textposition="top center",
            textfont=dict(size=9, color=BROWN),
            hoverinfo="skip",
        )
    )

    fig_quality.add_trace(
        go.Bar(
            x=years,
            y=data["EBITDA Margin"],
            name="EBITDA margin",
            yaxis="y2",
            marker_color=[
                PEACH if x < 0 else GOLD
                for x in data["EBITDA Margin"]
            ],
            opacity=0.72,
            hoverinfo="skip",
        )
    )

    fig_quality.update_layout(
        yaxis=dict(
            range=[1.5, 4.2],
            gridcolor=GRID,
            zeroline=False,
        ),
        yaxis2=dict(
            overlaying="y",
            side="right",
            range=[-80, 20],
            ticksuffix="%",
            showgrid=False,
            zeroline=True,
            zerolinecolor=BROWN_2,
            zerolinewidth=1,
        ),
    )

    clean_layout(fig_quality, height=245)

    st.plotly_chart(
        fig_quality,
        use_container_width=True,
        config={"displayModeBar": False, "staticPlot": True},
    )

    st.markdown(
        f"""
        <div style="
            background:{CREAM_2};
            border:1px solid {GOLD_LIGHT};
            border-radius:10px;
            padding:8px 10px;
            color:{BROWN};
            font-size:0.71rem;
            margin-top:4px;">
            <b>EBITDA positive in Y4 at ₹72 Cr revenue</b><br>
            CM1 compresses with channel mix, while lower marketing intensity expands CM2.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# ROW 3 TABLES
# ============================================================

t1, t2, t3 = st.columns([1.15, 1.2, 0.85])

with t1:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Growth engine", "Core quantified levers behind the revenue build")

    growth_table = pd.DataFrame(
        {
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
        }
    )

    st.dataframe(
        growth_table,
        hide_index=True,
        use_container_width=True,
        height=224,
    )

    st.markdown(
        f"""
        <div class="small-note">
        Derived AOV is based on ARPU, purchase frequency and channel-level units/order assumptions.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)


with t2:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Financial quality", "Economics at launch, scale and maturity")

    fin_table = pd.DataFrame(
        {
            "Metric": [
                "CAC",
                "LTV",
                "LTV:CAC",
                "CAC payback",
                "Gross margin",
                "CM1",
                "CM2",
                "EBITDA margin",
            ],
            "Y1": [
                "₹1,120",
                "₹2,488",
                "2.22×",
                "8.4m",
                "59.4%",
                "43.6%",
                "8.6%",
                "-67.7%",
            ],
            "Y3": [
                "₹1,232",
                "₹3,672",
                "2.98×",
                "8.1m",
                "63.2%",
                "42.6%",
                "19.6%",
                "-2.5%",
            ],
            "Y5": [
                "₹1,284",
                "₹4,703",
                "3.66×",
                "7.8m",
                "63.4%",
                "40.3%",
                "25.3%",
                "9.1%",
            ],
        }
    )

    st.dataframe(
        fin_table,
        hide_index=True,
        use_container_width=True,
        height=298,
    )
    st.markdown('</div>', unsafe_allow_html=True)


with t3:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("Personalization pays", "Y5 versus no-quiz counterfactual")

    st.markdown(
        """
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
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div style="
            margin-top:10px;
            background:{WHITE};
            border-left:4px solid {GOLD};
            padding:10px 11px;
            font-size:0.70rem;
            line-height:1.45;
            color:{BROWN_2};
            border-radius:8px;">
            Quiz-led personalization improves acquisition efficiency and strengthens
            repeat behaviour, compounding customer value over time.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# TIMELINE
# ============================================================

st.markdown('<div class="panel">', unsafe_allow_html=True)
panel_header("Five-year scale path", "What changes economically as MenoSakhi grows")

st.markdown(
    """
    <div class="timeline">

        <div class="year-box">
            <div class="year-title">Y1 · Prove</div>
            <div class="year-copy">
                ₹4 Cr revenue<br>
                12.5K customers<br>
                36% repeat<br>
                Digital-only revenue
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
                EBITDA turns positive<br>
                55% repeat<br>
                Offline selectively enters
            </div>
        </div>

        <div class="year-box">
            <div class="year-title">Y5 · ₹100 Cr+</div>
            <div class="year-copy">
                ₹104 Cr revenue<br>
                2.12L customers<br>
                58% repeat<br>
                9.1% EBITDA margin
            </div>
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# FOOTNOTE
# ============================================================

st.markdown(
    f"""
    <div style="
        text-align:right;
        color:{MUTED};
        font-size:0.58rem;
        padding:4px 2px 12px 2px;">
        MenoSakhi financial model · ₹ Cr unless otherwise stated
    </div>
    """,
    unsafe_allow_html=True,
)
