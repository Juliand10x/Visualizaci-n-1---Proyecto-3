# -*- coding: utf-8 -*-
"""
Script de generación del Notebook Jupyter oficial y figuras del Proyecto 3
Visualización I — Universidad Externado de Colombia
Autores: Julián Steven Duarte & Julián Camilo Jiménez
"""

import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Configuración de carpetas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATOS_DIR = os.path.join(BASE_DIR, "..", "Datos")
FIG_DIR = os.path.join(BASE_DIR, "..", "figuras")
NB_DIR = os.path.join(BASE_DIR, "..", "notebooks")
os.makedirs(FIG_DIR, exist_ok=True)
os.makedirs(NB_DIR, exist_ok=True)

# 1. Cargar datos
df_edu_edad = pd.read_csv(os.path.join(DATOS_DIR, "geih_2026_educacion_edad.csv"))
df_sex_edu = pd.read_csv(os.path.join(DATOS_DIR, "geih_2026_sexo_educacion.csv"))
df_dep = pd.read_csv(os.path.join(DATOS_DIR, "geih_2026_departamentos.csv"))
df_m = pd.read_csv(os.path.join(DATOS_DIR, "geih_2026_tendencia_mensual.csv"))

# Configuración de estilo global Matplotlib / Seaborn
plt.rcParams['font.sans-serif'] = 'Segoe UI, DejaVu Sans, Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300
sns.set_theme(style="whitegrid", font='Segoe UI')

# ==============================================================================
# GRÁFICO 1 (SEABORN): LA PARADOJA EDUCATIVA EN COLOMBIA
# ==============================================================================
print("Generando Gráfico 1 (Seaborn)...")
# Agrupar solo por nivel educativo
df_edu_tot = df_sex_edu.groupby("Nivel Educativo").agg({
    "FEX_Ocupado": "sum",
    "FEX_Informal": "sum"
}).reset_index()
df_edu_tot = df_edu_tot[df_edu_tot["Nivel Educativo"] != "Sin informació"].copy()
df_edu_tot["Tasa_Informalidad"] = (df_edu_tot["FEX_Informal"] / df_edu_tot["FEX_Ocupado"]) * 100
df_edu_tot = df_edu_tot.sort_values(by="Tasa_Informalidad", ascending=True)

fig, ax = plt.subplots(figsize=(10, 5.5))
colores = ["#94A3B8" if edu != "Educación Superior" else "#E11D48" for edu in df_edu_tot["Nivel Educativo"]]

bars = ax.barh(df_edu_tot["Nivel Educativo"], df_edu_tot["Tasa_Informalidad"], color=colores, height=0.55, edgecolor="none")

# Etiquetas directas de datos (Gestalt: reducción de carga cognitiva)
for bar in bars:
    w = bar.get_width()
    y = bar.get_y() + bar.get_height() / 2
    ax.text(w + 1.2, y, f"{w:.1f}%", va='center', ha='left', fontsize=11, fontweight='bold', color="#1E293B")

# Línea de referencia nacional (54.64%)
ax.axvline(54.64, color="#475569", linestyle="--", linewidth=1.5, alpha=0.8)
ax.text(54.64, -0.6, "Tasa Nacional Promedio (54.6%)", ha="center", va="top", fontsize=9.5, fontweight="semibold", color="#475569")

# Anotación explicativa ciudadana
ax.annotate(
    "¡La Paradoja Colombiana!\n6 de cada 10 graduados con educación\nsuperior están atrapados en contratos\ninformales o prestación de servicios.",
    xy=(61.26, 3), xytext=(35, 2.3),
    arrowprops=dict(facecolor="#E11D48", shrink=0.08, width=1.5, headwidth=7),
    fontsize=9.5, fontweight="medium", color="#9F1239",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#FFE4E6", edgecolor="#FDA4AF", alpha=0.9)
)

ax.set_title("La Paradoja Educativa: Estudiar Más Ya No Garantiza Formalidad en Colombia", fontsize=13, fontweight='bold', color="#0F172A", pad=15, loc='left')
ax.set_xlabel("Tasa de Informalidad Laboral (%)", fontsize=10.5, color="#334155", labelpad=10)
ax.set_ylabel("", fontsize=10)
ax.set_xlim(0, 75)
ax.tick_params(colors="#334155", labelsize=10.5)
sns.despine(left=True, bottom=True)
ax.xaxis.grid(True, linestyle=":", alpha=0.6, color="#CBD5E1")
ax.yaxis.grid(False)

plt.tight_layout()
fig1_path = os.path.join(FIG_DIR, "fig1_paradoja_educativa_seaborn.png")
plt.savefig(fig1_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"Gráfico 1 guardado en: {fig1_path}")

# ==============================================================================
# GRÁFICO 2 (SEABORN): LA BRECHA DE GÉNERO SEGÚN NIVEL EDUCATIVO
# ==============================================================================
print("Generando Gráfico 2 (Seaborn)...")
df_pvt = df_sex_edu[df_sex_edu["Nivel Educativo"] != "Sin informació"].pivot(
    index="Nivel Educativo", columns="Sexo", values="Tasa_Informalidad"
).loc[["Ninguno / Preescolar", "Primaria", "Secundaria / Media", "Educación Superior"]]

fig, ax = plt.subplots(figsize=(10, 6))
y_pos = np.arange(len(df_pvt))

# Dibujar líneas conectoras (Dumbbell chart)
for i, (idx, row) in enumerate(df_pvt.iterrows()):
    ax.plot([row["Mujer"], row["Hombre"]], [i, i], color="#CBD5E1", linewidth=3.5, zorder=1)

# Puntos para Mujeres y Hombres
ax.scatter(df_pvt["Mujer"], y_pos, color="#9333EA", s=180, label="Mujeres", zorder=2, edgecolors="white", linewidths=1.5)
ax.scatter(df_pvt["Hombre"], y_pos, color="#2563EB", s=180, label="Hombres", zorder=2, edgecolors="white", linewidths=1.5)

# Etiquetas de datos en cada punto
for i, (idx, row) in enumerate(df_pvt.iterrows()):
    ax.text(row["Mujer"] - 2.0, i, f"{row['Mujer']:.1f}%", va='center', ha='right', fontsize=9.5, fontweight='bold', color="#7E22CE")
    ax.text(row["Hombre"] + 2.0, i, f"{row['Hombre']:.1f}%", va='center', ha='left', fontsize=9.5, fontweight='bold', color="#1D4ED8")
    # Texto de brecha
    brecha = row["Hombre"] - row["Mujer"]
    ax.text((row["Mujer"] + row["Hombre"]) / 2, i + 0.22, f"Brecha: {brecha:.1f} pts", va='center', ha='center', fontsize=8.5, color="#64748B", fontstyle='italic')

ax.set_yticks(y_pos)
ax.set_yticklabels(df_pvt.index, fontsize=10.5, fontweight="semibold", color="#1E293B")
ax.set_xlim(10, 80)
ax.set_xlabel("Tasa de Informalidad (%)", fontsize=10.5, color="#334155", labelpad=10)
ax.set_title("Brecha de Género en la Ocupación: La Tasa en Hombres Supera a Mujeres por Urgencia Económica", fontsize=12.5, fontweight='bold', color="#0F172A", pad=15, loc='left')

# Cuadro explicativo sobre la paradoja de género
ax.text(
    0.02, 0.05,
    "Nota Ciudadana: La menor tasa en mujeres no significa mayor bienestar laboral.\n"
    "Refleja que millones de mujeres son excluidas previamente del mercado para asumir\n"
    "trabajo doméstico y de cuidado no remunerado sin ingresos propios.",
    transform=ax.transAxes, fontsize=8.5, color="#475569",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#F8FAFC", edgecolor="#E2E8F0")
)

ax.legend(loc="upper right", frameon=True, facecolor="white", edgecolor="#E2E8F0")
sns.despine(left=True, bottom=True)
ax.xaxis.grid(True, linestyle=":", alpha=0.6, color="#CBD5E1")
ax.yaxis.grid(False)

plt.tight_layout()
fig2_path = os.path.join(FIG_DIR, "fig2_brecha_genero_educacion_seaborn.png")
plt.savefig(fig2_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"Gráfico 2 guardado en: {fig2_path}")

# ==============================================================================
# GRÁFICO 3 (SEABORN - COMPLEMENTARIO): EVOLUCIÓN MENSUAL EN 2026
# ==============================================================================
print("Generando Gráfico 3 (Seaborn)...")
fig, ax = plt.subplots(figsize=(9, 4.5))

ax.plot(df_m["Nombre_Mes"], df_m["Tasa_Informalidad"], marker="o", color="#0284C7", linewidth=2.5, markersize=8, label="Tasa Mensual")
ax.fill_between(df_m["Nombre_Mes"], 50, df_m["Tasa_Informalidad"], color="#BAE6FD", alpha=0.35)

# Etiquetas directas en cada mes
for _, r in df_m.iterrows():
    ax.text(r["Nombre_Mes"], r["Tasa_Informalidad"] + 0.22, f"{r['Tasa_Informalidad']:.2f}%", ha='center', va='bottom', fontsize=9.5, fontweight='bold', color="#0369A1")

# Resaltar pico de mayo
ax.scatter(["Mayo"], [55.50], color="#DC2626", s=130, zorder=5)
ax.annotate(
    "Pico Anual (Mayo):\n55.50% de informalidad",
    xy=("Mayo", 55.50), xytext=("Abril", 55.8),
    arrowprops=dict(facecolor="#DC2626", shrink=0.08, width=1.2, headwidth=6),
    fontsize=8.5, fontweight="bold", color="#B91C1C",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="#FEE2E2", edgecolor="#FCA5A5")
)

ax.set_title("Evolución Mensual: Deterioro Gradual de la Formalidad entre Enero y Mayo de 2026", fontsize=12, fontweight='bold', color="#0F172A", pad=12, loc='left')
ax.set_ylabel("Tasa de Informalidad (%)", fontsize=10, color="#334155")
ax.set_ylim(51, 57)
sns.despine(left=True, bottom=True)
ax.yaxis.grid(True, linestyle=":", alpha=0.6, color="#CBD5E1")
ax.xaxis.grid(False)

plt.tight_layout()
fig3_path = os.path.join(FIG_DIR, "fig3_evolucion_mensual_seaborn.png")
plt.savefig(fig3_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"Gráfico 3 guardado en: {fig3_path}")

# ==============================================================================
# GRÁFICO 4 (PLOTLY): EXPLORADOR INTERACTIVO CIUDADANO
# ==============================================================================
print("Generando Gráfico Interactivo (Plotly)...")
df_dep_clean = df_dep[df_dep["Nombre_Departamento"] != "Desconocido"].copy()
df_dep_clean = df_dep_clean.sort_values(by="Tasa_Informalidad", ascending=True)

# Asignar nivel de alerta
def clasificar_alerta(tasa):
    if tasa >= 60.0:
        return "Alerta Crítica (> 60%)"
    elif tasa >= 50.0:
        return "Vulnerabilidad Media (50% - 60%)"
    else:
        return "Mayor Formalidad (< 50%)"

df_dep_clean["Nivel_Alerta"] = df_dep_clean["Tasa_Informalidad"].apply(clasificar_alerta)

color_discrete_map = {
    "Alerta Crítica (> 60%)": "#E11D48",
    "Vulnerabilidad Media (50% - 60%)": "#F59E0B",
    "Mayor Formalidad (< 50%)": "#0284C7"
}

fig_plotly = px.bar(
    df_dep_clean,
    x="Tasa_Informalidad",
    y="Nombre_Departamento",
    orientation="h",
    color="Nivel_Alerta",
    color_discrete_map=color_discrete_map,
    custom_data=["FEX_Ocupado", "FEX_Informal", "Nivel_Alerta"],
    labels={
        "Tasa_Informalidad": "Tasa de Informalidad Laboral (%)",
        "Nombre_Departamento": "Departamento",
        "Nivel_Alerta": "Nivel de Vulnerabilidad"
    },
    title="<b>Explorador Ciudadano Interactivo: Tasa de Informalidad por Departamento (GEIH 2026)</b>"
)

fig_plotly.update_traces(
    hovertemplate=(
        "<b>%{y}</b><br>"
        "Tasa de Informalidad: <b>%{x:.2f}%</b><br>"
        "Ocupados Totales: <b>%{customdata[0]:,.0f}</b> personas<br>"
        "Informales Estimados: <b>%{customdata[1]:,.0f}</b> personas<br>"
        "Categoría: <i>%{customdata[2]}</i>"
        "<extra></extra>"
    )
)

# Línea de referencia del promedio nacional
fig_plotly.add_vline(
    x=54.64,
    line_dash="dash",
    line_color="#334155",
    annotation_text="Promedio Nacional (54.64%)",
    annotation_position="top right"
)

fig_plotly.update_layout(
    template="plotly_white",
    height=800,
    xaxis=dict(range=[0, 85], title="Tasa de Informalidad (%)", gridcolor="#F1F5F9"),
    yaxis=dict(title="", tickfont=dict(size=10)),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        title=dict(text="")
    ),
    margin=dict(l=150, r=30, t=90, b=40)
)

html_path = os.path.join(FIG_DIR, "visualizacion_interactiva_plotly.html")
fig_plotly.write_html(html_path, include_plotlyjs="cdn")
print(f"Gráfico Plotly guardado en: {html_path}")

print("¡Todas las figuras generadas con éxito!")
