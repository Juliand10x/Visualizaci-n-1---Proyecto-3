# -*- coding: utf-8 -*-
"""
Generador del Anexo Técnico de IA en formato PDF (1 página exacta)
Proyecto 3 — Visualización I — Universidad Externado de Colombia
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generar_anexo_pdf():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_pdf = os.path.join(base_dir, "documentos", "Equipo_Duarte_Jimenez_Proyecto3_Anexo_IA.pdf")

    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Fondo blanco
    ax.add_patch(patches.Rectangle((0, 0), 100, 100, facecolor="#FFFFFF", edgecolor='none'))

    # Encabezado institucional
    ax.add_patch(patches.Rectangle((0, 92), 100, 8, facecolor="#1E3A8A", edgecolor='none'))
    ax.text(5, 96, "UNIVERSIDAD EXTERNADO DE COLOMBIA  •  VISUALIZACIÓN I", fontsize=9.5, fontweight='bold', color="#BFDBFE", va='center')
    ax.text(5, 93.5, "ANEXO TÉCNICO DE USO ÉTICO DE INTELIGENCIA ARTIFICIAL (MÁXIMO 1 PÁGINA)", fontsize=11, fontweight='bold', color="#FFFFFF", va='center')

    # Metadatos
    ax.text(5, 89, "Equipo: Julián Steven Duarte & Julián Camilo Jiménez  |  Docentes: Adriana Pineda Barón & Paola Moreno  |  Noviembre 2026", 
            fontsize=8.5, color="#475569")
    ax.add_patch(patches.Rectangle((5, 87.5), 90, 0.3, facecolor="#CBD5E1", edgecolor='none'))

    # Sección 1: Declaración
    ax.text(5, 84.5, "1. Declaración de Transparencia y Responsabilidad Ética", fontsize=11, fontweight='bold', color="#0F172A")
    sec1 = (
        "En cumplimiento de los lineamientos éticos de la Universidad Externado de Colombia y de la guía docente de\n"
        "Visualización I, los integrantes del equipo declaramos haber utilizado herramientas de Inteligencia Artificial Generativa\n"
        "bajo un rol estrictamente instrumental y de asistencia técnica. Reafirmamos que la responsabilidad intelectual,\n"
        "analítica, metodológica y comunicativa de todos los hallazgos y decisiones recae exclusivamente en los autores humanos."
    )
    ax.text(5, 78, sec1, fontsize=8.5, color="#334155", linespacing=1.35)

    # Sección 2: Herramientas
    ax.text(5, 74, "2. Herramientas Utilizadas y Propósito Específico", fontsize=11, fontweight='bold', color="#0F172A")
    
    # Tabla visual
    ax.add_patch(patches.Rectangle((5, 60), 90, 12, facecolor="#F8FAFC", edgecolor="#CBD5E1"))
    ax.add_patch(patches.Rectangle((5, 68), 90, 4, facecolor="#E2E8F0", edgecolor="#CBD5E1"))
    ax.text(6, 70, "Herramienta", fontsize=8.5, fontweight='bold', color="#0F172A")
    ax.text(32, 70, "Propósito de Asistencia", fontsize=8.5, fontweight='bold', color="#0F172A")
    ax.text(68, 70, "Límites y Control Humano", fontsize=8.5, fontweight='bold', color="#0F172A")

    ax.text(6, 65, "Google Gemini\n(Antigravity Assistant)", fontsize=8, color="#0F172A")
    ax.text(32, 65, "Optimización de sintaxis en Python (Seaborn y Plotly),\nescritura del script de R (sf/tmap) y paleta WCAG AA.", fontsize=7.8, color="#334155")
    ax.text(68, 65, "No se generaron datos ficticios. Cada script fue\nejecutado, verificado y validado en local.", fontsize=7.8, color="#334155")

    ax.text(6, 61.5, "Power BI / DAX Guide", fontsize=8, color="#0F172A")
    ax.text(32, 61.5, "Asistencia en formulación de medidas ponderadas con AVERAGEX.", fontsize=7.8, color="#334155")
    ax.text(68, 61.5, "Integridad referencial auditada en Power BI Desktop.", fontsize=7.8, color="#334155")

    # Sección 3: Prompts relevantes
    ax.text(5, 56.5, "3. Prompts Relevantes Empleados en el Proceso", fontsize=11, fontweight='bold', color="#0F172A")
    prompts_txt = (
        "• Sobre Accesibilidad y Paleta Cromática:\n"
        "  «Sugiere una paleta cromática semántica accesible (WCAG AA) para representar tasas de informalidad en Colombia,\n"
        "   usando azul (#2563EB) para formalidad y reservando rojo (#E11D48) exclusivamente para alerta crítica educativa y regional.»\n\n"
        "• Sobre Disolución Espacial en R (Sesión 3 de clase):\n"
        "  «¿Cómo unir y disolver eficientemente con sf en R un shapefile municipal hacia los 33 departamentos de Colombia\n"
        "   usando group_by(DPTO_CN) y st_union(), y clasificando con classIntervals(style = 'jenks') como vimos en clase?»\n\n"
        "• Sobre Medidas DAX de Promedio Mensual:\n"
        "  «En Power BI, dado que el FEX_C18 de la GEIH 2026 expande mes a mes y cargamos 6 meses continuos, ¿cómo formular\n"
        "   el promedio mensual ponderado con AVERAGEX(VALUES(DimFecha[Mes])) para mantener la tasa exacta en 54.64%?»"
    )
    ax.text(5, 41, prompts_txt, fontsize=8.2, color="#334155", linespacing=1.3)

    # Sección 4: Auditoría humana
    ax.text(5, 37.5, "4. Auditoría Crítica y Control de Alucinaciones", fontsize=11, fontweight='bold', color="#0F172A")
    sec4 = (
        "• Rigor Numérico Decimal: Se contrastaron las tasas calculadas por Python, R y Power BI, verificando que la tasa nacional\n"
        "  (54.64%), la tasa de educación superior (61.26%) y los picos territoriales (Guaviare al 75.71%) fueran 100% coincidentes.\n\n"
        "• Sin Causalidades Infundadas: Se rechazó cualquier interpretación generada por IA que atribuyera causalidades directas\n"
        "  a políticas públicas a partir de datos meramente descriptivos de la GEIH.\n\n"
        "• Tono y Empatía Humana: Toda la narrativa fue adaptada a la perspectiva y necesidades de los jóvenes colombianos."
    )
    ax.text(5, 23.5, sec4, fontsize=8.2, color="#334155", linespacing=1.35)

    # Firmas
    ax.add_patch(patches.Rectangle((5, 18), 90, 0.3, facecolor="#CBD5E1", edgecolor='none'))
    ax.text(18, 13, "_________________________________________\nJULIÁN STEVEN DUARTE\nEstudiante — Visualización I", 
            fontsize=8.5, color="#0F172A", ha='center', linespacing=1.3)
    ax.text(78, 13, "_________________________________________\nJULIÁN CAMILO JIMÉNEZ\nEstudiante — Visualización I", 
            fontsize=8.5, color="#0F172A", ha='center', linespacing=1.3)

    ax.text(5, 4, "Anexo reglamentario conforme al microcurrículo y rúbrica oficial de Visualización I • Universidad Externado de Colombia", 
            fontsize=7.5, color="#64748B")

    plt.savefig(out_pdf, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Anexo IA en PDF generado en:\n  {out_pdf}")

if __name__ == "__main__":
    generar_anexo_pdf()
