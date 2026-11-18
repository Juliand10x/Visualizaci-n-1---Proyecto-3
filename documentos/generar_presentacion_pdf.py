# -*- coding: utf-8 -*-
"""
Generador de la Presentación Oficial en PDF (10 diapositivas exactas)
Proyecto 3: Narrativa Visual Integrada — Visualización I
Universidad Externado de Colombia
Autores: Julián Steven Duarte & Julián Camilo Jiménez
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
from matplotlib.backends.backend_pdf import PdfPages

def generar_presentacion_pdf():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fig_dir = os.path.join(base_dir, "figuras")
    doc_dir = os.path.join(base_dir, "documentos")
    out_pdf = os.path.join(doc_dir, "Equipo_Duarte_Jimenez_Proyecto3_Presentacion.pdf")

    # Configuración general
    plt.rcParams['font.sans-serif'] = 'Segoe UI, DejaVu Sans, Arial'
    plt.rcParams['font.family'] = 'sans-serif'

    c_navy = "#1E3A8A"
    c_red = "#E11D48"
    c_slate = "#475569"
    c_dark = "#0F172A"
    c_bg = "#F8FAFC"
    c_card = "#FFFFFF"
    c_border = "#E2E8F0"

    with PdfPages(out_pdf) as pdf:
        
        def setup_slide(titulo, num):
            fig, ax = plt.subplots(figsize=(13.333, 7.5), dpi=300)
            ax.set_xlim(0, 100)
            ax.set_ylim(0, 100)
            ax.axis('off')
            # Fondo
            ax.add_patch(patches.Rectangle((0, 0), 100, 100, facecolor=c_bg, edgecolor='none'))
            # Barra Header
            ax.add_patch(patches.Rectangle((0, 86), 100, 14, facecolor=c_navy, edgecolor='none'))
            ax.text(4, 95, "PROYECTO 3: NARRATIVA VISUAL INTEGRADA  |  Universidad Externado de Colombia", 
                    fontsize=11, fontweight='bold', color="#BFDBFE", va='center')
            ax.text(4, 90, titulo, fontsize=19, fontweight='bold', color="#FFFFFF", va='center')
            # Footer
            ax.text(4, 3, f"Visualización 1  •  Equipo: Julián Steven Duarte & Julián Camilo Jiménez  •  Diapositiva {num} de 10", 
                    fontsize=10, color=c_slate, va='center')
            return fig, ax

        # -------------------------------------------------------------
        # DIAPOSITIVA 1: PORTADA
        # -------------------------------------------------------------
        fig, ax = plt.subplots(figsize=(13.333, 7.5), dpi=300)
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        ax.add_patch(patches.Rectangle((0, 0), 100, 100, facecolor=c_navy, edgecolor='none'))
        # Tarjeta central blanca
        ax.add_patch(patches.FancyBboxPatch((8, 12), 84, 76, boxstyle="round,pad=1.5", facecolor=c_card, edgecolor='none'))
        ax.text(12, 78, "UNIVERSIDAD EXTERNADO DE COLOMBIA  •  VISUALIZACIÓN I", fontsize=13, fontweight='bold', color=c_red)
        ax.text(12, 66, "La Trampa del Título:\nRadiografía de la Informalidad Laboral en Colombia", 
                fontsize=27, fontweight='bold', color=c_dark, linespacing=1.2)
        ax.text(12, 51, "Una historia basada en evidencia para jóvenes y nuevos profesionales que buscan empleo digno\nFuente Oficial: Gran Encuesta Integrada de Hogares (GEIH 2026) — DANE", 
                fontsize=14, color=c_slate, linespacing=1.4)
        ax.add_patch(patches.Rectangle((12, 44), 76, 0.4, facecolor="#CBD5E1", edgecolor='none'))
        ax.text(12, 34, "Expositores: Julián Steven Duarte & Julián Camilo Jiménez\nDocentes: Adriana Pineda Barón & Paola Moreno\nNoviembre de 2026  •  Modalidad A: Presentación Narrativa Integrada", 
                fontsize=13, fontweight='bold', color=c_navy, linespacing=1.6)
        pdf.savefig(fig, dpi=300)
        plt.close()

        # -------------------------------------------------------------
        # DIAPOSITIVA 2: AUDIENCIA Y PREGUNTA
        # -------------------------------------------------------------
        fig, ax = setup_slide("Encuadre Ciudadano: ¿A Quién le Hablamos y Qué Preguntamos?", 2)
        # Caja Izquierda
        ax.add_patch(patches.FancyBboxPatch((4, 10), 44, 72, boxstyle="round,pad=1", facecolor=c_card, edgecolor=c_border))
        ax.text(6, 76, "Audiencia Ciudadana Específica", fontsize=16, fontweight='bold', color=c_navy)
        txt_aud = (
            "• Público Delimitado:\n"
            "  Jóvenes colombianos de 18 a 28 años, técnicos,\n"
            "  tecnólogos y profesionales recién egresados.\n\n"
            "• La Promesa Incumplida:\n"
            "  Tradicionalmente se inculcó que la educación\n"
            "  superior era garantía de estabilidad y pensión.\n\n"
            "• La Realidad que Enfrentan:\n"
            "  Contratos de 3 meses por prestación de servicios,\n"
            "  honorarios sin salud ni pensión, o subempleo."
        )
        ax.text(6, 46, txt_aud, fontsize=12.5, color=c_dark, linespacing=1.4)

        # Caja Derecha
        ax.add_patch(patches.FancyBboxPatch((52, 10), 44, 72, boxstyle="round,pad=1", facecolor=c_card, edgecolor=c_border))
        ax.text(54, 76, "La Pregunta Analítica Central", fontsize=16, fontweight='bold', color=c_red)
        txt_q = (
            "«¿Por qué en Colombia cursar educación superior\n"
            "ya no garantiza un empleo formal con seguridad\n"
            "social, y de qué forma la región geográfica y el\n"
            "género determinan las probabilidades reales de\n"
            "conseguir un trabajo digno?»\n\n"
            "• Objetivo Comunicativo:\n"
            "  Empoderar al ciudadano con evidencia estadística para\n"
            "  tomar decisiones informadas de empleabilidad y exigir\n"
            "  políticas de formalización productiva efectivas."
        )
        ax.text(54, 46, txt_q, fontsize=12.5, color=c_dark, linespacing=1.4)
        pdf.savefig(fig, dpi=300)
        plt.close()

        # -------------------------------------------------------------
        # DIAPOSITIVA 3: LA GRAN IDEA
        # -------------------------------------------------------------
        fig, ax = setup_slide("La Gran Idea: El Mensaje Central Basado en Evidencia", 3)
        # Banner Gran Idea
        ax.add_patch(patches.FancyBboxPatch((4, 54), 92, 28, boxstyle="round,pad=1.2", facecolor="#FFF1F2", edgecolor="#FDA4AF"))
        ax.text(6, 75, "LA GRAN IDEA QUE DEMUESTRAN LOS DATOS:", fontsize=13, fontweight='bold', color=c_red)
        ax.text(6, 62, "«En Colombia, más de 6 de cada 10 graduados con educación superior y técnica están atrapados\n"
                       "en la informalidad o el rebusque calificado (61.3%). Esta trampa se agrava drásticamente en la\n"
                       "periferia del país (superando el 75%) y oculta una grave desigualdad de género por las tareas de cuidado.»",
                fontsize=13.5, fontweight='bold', color=c_dark, linespacing=1.3)
        
        # 3 Tarjetas Inferiores
        kpis = [
            (4, "61.26% Informal", "La Educación No Basta", "Técnicos y universitarios tienen una informalidad\ncasi idéntica a quienes tienen secundaria (61.1%)."),
            (36, "75.71% en Guaviare", "La Brecha Territorial", "La informalidad en la periferia triplica la\nprecariedad frente al centro andino del país."),
            (68, "Barrera Oculta", "Desbalance de Género", "La menor tasa en mujeres ocupadas oculta que\nmillones no pueden trabajar por tareas de cuidado.")
        ]
        for x, val, tit, desc in kpis:
            ax.add_patch(patches.FancyBboxPatch((x, 10), 28, 38, boxstyle="round,pad=1", facecolor=c_card, edgecolor=c_border))
            ax.text(x+2, 42, val, fontsize=17, fontweight='bold', color=c_navy)
            ax.text(x+2, 34, tit, fontsize=13, fontweight='bold', color=c_dark)
            ax.text(x+2, 22, desc, fontsize=11, color=c_slate, linespacing=1.3)
        pdf.savefig(fig, dpi=300)
        plt.close()

        # -------------------------------------------------------------
        # DIAPOSITIVA 4: POWER BI SERVICE
        # -------------------------------------------------------------
        fig, ax = setup_slide("Power BI Service: El Pulso Laboral de Colombia en Tiempo Real", 4)
        ax.add_patch(patches.FancyBboxPatch((4, 10), 44, 72, boxstyle="round,pad=1", facecolor=c_card, edgecolor=c_border))
        ax.text(6, 76, "Mejoras y Validación del Tablero", fontsize=16, fontweight='bold', color=c_navy)
        txt_pbi = (
            "• Continuidad y Trazabilidad:\n"
            "  Se conserva el modelo analítico de la Entrega 1 con la GEIH.\n\n"
            "• Solución a la Métrica Semestral:\n"
            "  En lugar de sumar personas 6 veces (105M acumulados),\n"
            "  las medidas de razón calculan con exactitud la tasa\n"
            "  nacional del 54.64% (~17.5M ocupados/mes).\n\n"
            "• Filtro Dinámico en Jóvenes:\n"
            "  Cálculo focalizado en 18-28 años con 41.07% de informalidad.\n\n"
            "• Doble Página de Decisión:\n"
            "  Página 1 (Nacional y Brechas) y Página 2 (Focalización Territorial)."
        )
        ax.text(6, 44, txt_pbi, fontsize=12, color=c_dark, linespacing=1.3)

        ax.add_patch(patches.FancyBboxPatch((52, 10), 44, 72, boxstyle="round,pad=1", facecolor="#EFF6FF", edgecolor="#BFDBFE"))
        ax.text(54, 76, "Acceso al Ecosistema en Vivo", fontsize=16, fontweight='bold', color=c_navy)
        txt_links = (
            "• Enlace Oficial en Power BI Service:\n"
            "  Tablero publicado y accesible institucionalmente:\n"
            "  https://app.powerbi.com/links/gvbF1pi94p\n\n"
            "• Plataforma Web Digital (Modalidad B en Vercel):\n"
            "  https://webnarrativa.vercel.app\n\n"
            "• Demostración en Vivo en la Sustentación:\n"
            "  Durante los 5 minutos de interacción se mostrarán\n"
            "  los slicers por departamento y educación."
        )
        ax.text(54, 46, txt_links, fontsize=12, color=c_dark, linespacing=1.3)
        pdf.savefig(fig, dpi=300)
        plt.close()

        # -------------------------------------------------------------
        # DIAPOSITIVA 5: SEABORN 1 (PARADOJA EDUCATIVA)
        # -------------------------------------------------------------
        fig, ax = setup_slide("Python (Seaborn): La Paradoja de la Educación Superior", 5)
        img1_path = os.path.join(fig_dir, "fig1_paradoja_educativa_seaborn.png")
        if os.path.exists(img1_path):
            img1 = mpimg.imread(img1_path)
            ax.imshow(img1, extent=[4, 60, 10, 82], aspect='auto')
        
        ax.add_patch(patches.FancyBboxPatch((63, 10), 33, 72, boxstyle="round,pad=1", facecolor=c_card, edgecolor=c_border))
        ax.text(65, 76, "Hallazgos Clave", fontsize=16, fontweight='bold', color=c_red)
        txt_h1 = (
            "• 61.26% en Superior:\n"
            "  Tener título técnico o profesional no\n"
            "  blinda contra la desprotección.\n\n"
            "• Primaria al 52.37%:\n"
            "  Paradójicamente, la educación superior\n"
            "  tiene mayor informalidad relativa.\n\n"
            "• La Razón Estructural:\n"
            "  El ecosistema productivo no genera\n"
            "  empleo formal asalariado suficiente.\n\n"
            "• Precarización Profesional:\n"
            "  Contratos de prestación de servicios\n"
            "  u honorarios sin cotización continua."
        )
        ax.text(65, 42, txt_h1, fontsize=11.5, color=c_dark, linespacing=1.35)
        pdf.savefig(fig, dpi=300)
        plt.close()

        # -------------------------------------------------------------
        # DIAPOSITIVA 6: SEABORN 2 (BRECHA DE GÉNERO)
        # -------------------------------------------------------------
        fig, ax = setup_slide("Python (Seaborn): La Brecha Oculta de Género", 6)
        img2_path = os.path.join(fig_dir, "fig2_brecha_genero_educacion_seaborn.png")
        if os.path.exists(img2_path):
            img2 = mpimg.imread(img2_path)
            ax.imshow(img2, extent=[4, 60, 10, 82], aspect='auto')

        ax.add_patch(patches.FancyBboxPatch((63, 10), 33, 72, boxstyle="round,pad=1", facecolor=c_card, edgecolor=c_border))
        ax.text(65, 76, "Lectura Ética de los Datos", fontsize=15, fontweight='bold', color=c_navy)
        txt_h2 = (
            "• Brecha en Graduados:\n"
            "  Hombres al 65.27% vs Mujeres al 58.18%.\n\n"
            "• Cuidado No Remunerado:\n"
            "  La menor tasa en mujeres ocupadas NO\n"
            "  significa mayor bienestar laboral.\n\n"
            "• Barrera de Acceso Previa:\n"
            "  Millones de mujeres no logran ingresar al\n"
            "  mercado por asumir solas tareas de cuidado.\n\n"
            "• Presión en Hombres:\n"
            "  Los hombres están obligados al rebusque\n"
            "  diario para aportar ingresos inmediatos."
        )
        ax.text(65, 42, txt_h2, fontsize=11.5, color=c_dark, linespacing=1.35)
        pdf.savefig(fig, dpi=300)
        plt.close()

        # -------------------------------------------------------------
        # DIAPOSITIVA 7: PLOTLY (EXPLORADOR INTERACTIVO)
        # -------------------------------------------------------------
        fig, ax = setup_slide("Python (Plotly): Explorador Departamental Interactivo", 7)
        ax.add_patch(patches.FancyBboxPatch((4, 10), 54, 72, boxstyle="round,pad=1", facecolor=c_card, edgecolor=c_border))
        ax.text(6, 76, "Semáforo Ciudadano de Riesgo Territorial", fontsize=16, fontweight='bold', color=c_navy)
        txt_sem = (
            "[Alerta Critica] (> 60% de Informalidad):\n"
            "   • Guaviare (75.7%) — La región más precaria del país.\n"
            "   • Casanare (66.5%) — Desprotección en la Orinoquía.\n"
            "   • Bogotá D.C. (64.1%) — Alta tercerización profesional.\n"
            "   • Cundinamarca (62.3%) y Nariño (62.1%).\n\n"
            "[Vulnerabilidad Media] (50% - 60%):\n"
            "   • Tolima (59.2%), Antioquia (56.1%), Valle (55.4%).\n\n"
            "[Mayor Formalidad Relativa] (< 50%):\n"
            "   • Boyacá (49.8%), Putumayo (38.1%).\n\n"
            "[Línea de Referencia Nacional]:\n"
            "   Promedio país en 54.64%."
        )
        ax.text(6, 43, txt_sem, fontsize=11.5, color=c_dark, linespacing=1.3)

        ax.add_patch(patches.FancyBboxPatch((62, 10), 34, 72, boxstyle="round,pad=1", facecolor="#F1F5F9", edgecolor=c_border))
        ax.text(64, 76, "Interacción en Vivo", fontsize=15, fontweight='bold', color=c_dark)
        txt_int = (
            "• Archivo Autocontenido:\n"
            "  figuras/visualizacion_interactiva_plotly.html\n\n"
            "• Tooltips Dinámicos:\n"
            "  Pase del cursor para ver ocupados totales,\n"
            "  informales estimados y nivel de alerta.\n\n"
            "• Despliegue en Vercel:\n"
            "  Disponible en vivo en la plataforma web\n"
            "  para consulta de toda la sala."
        )
        ax.text(64, 48, txt_int, fontsize=11.5, color=c_slate, linespacing=1.4)
        pdf.savefig(fig, dpi=300)
        plt.close()

        # -------------------------------------------------------------
        # DIAPOSITIVA 8: R GEOESPACIAL (MAPAS)
        # -------------------------------------------------------------
        fig, ax = setup_slide("R Geoespacial: Radiografía Cartográfica del Territorio", 8)
        img_r_path = os.path.join(fig_dir, "mapa_informalidad_colombia_R.png")
        if os.path.exists(img_r_path):
            img_r = mpimg.imread(img_r_path)
            ax.imshow(img_r, extent=[4, 48, 10, 82], aspect='auto')

        ax.add_patch(patches.FancyBboxPatch((52, 10), 44, 72, boxstyle="round,pad=1", facecolor=c_card, edgecolor=c_border))
        ax.text(54, 76, "Rigor Técnico y Hallazgos Espaciales", fontsize=15, fontweight='bold', color=c_navy)
        txt_r = (
            "• Metodología de Clase (Sesión 3):\n"
            "  Uniones espaciales con paquete sf sobre capa oficial\n"
            "  IGAC/DANE y cortes estadísticos de Jenks (classInt).\n\n"
            "• Elementos Cartográficos Obligatorios:\n"
            "  Rosa de los vientos, escala métrica y créditos de fuente.\n\n"
            "• La Desconexión Centro - Periferia:\n"
            "  La región andina retiene el empleo formal, mientras la\n"
            "  Amazonía y Orinoquía superan el 70% de informalidad.\n\n"
            "• El Caso Crítico de Guaviare:\n"
            "  75.71% de informalidad: 3 de cada 4 puestos no tienen\n"
            "  salud, pensión ni cobertura de riesgos."
        )
        ax.text(54, 43, txt_r, fontsize=11.5, color=c_dark, linespacing=1.35)
        pdf.savefig(fig, dpi=300)
        plt.close()

        # -------------------------------------------------------------
        # DIAPOSITIVA 9: MENSAJE FINAL CIUDADANO
        # -------------------------------------------------------------
        fig, ax = setup_slide("Mensaje Final: Estrategias Ciudadanas de Empleabilidad", 9)
        acciones = [
            ("1. Planificación Temprana de Seguridad Social", 
             "Si te vinculas por prestación de servicios, recuerda que el 40% del contrato es la base de cotización\na salud y pensión. No sacrifiques tu futuro pensional por falta de asesoría tributaria."),
            ("2. Movilidad y Teletrabajo Estratégico", 
             "Si resides en departamentos con más del 65% de informalidad (Guaviare, Casanare, Nariño), orienta tu\nbúsqueda laboral hacia esquemas remotos con empresas formales ubicadas en las capitales."),
            ("3. Exigencia Ciudadana de Políticas Pertinentes", 
             "El país no necesita subsidios asistenciales ciegos; requiere incentivos tributarios y cofinanciación\npara empresas que contraten indefinidamente a jóvenes recién egresados.")
        ]
        for i, (tit, desc) in enumerate(acciones):
            y = 12 + (2 - i) * 24
            ax.add_patch(patches.FancyBboxPatch((4, y), 92, 20, boxstyle="round,pad=1", facecolor=c_card, edgecolor=c_border))
            ax.text(6, y + 14, tit, fontsize=14.5, fontweight='bold', color=c_navy)
            ax.text(6, y + 6, desc, fontsize=12, color=c_dark, linespacing=1.3)
        pdf.savefig(fig, dpi=300)
        plt.close()

        # -------------------------------------------------------------
        # DIAPOSITIVA 10: FUENTES, LÍMITES E IA
        # -------------------------------------------------------------
        fig, ax = setup_slide("Fuentes, Limitaciones Metodológicas y Declaración de IA", 10)
        ax.add_patch(patches.FancyBboxPatch((4, 10), 44, 72, boxstyle="round,pad=1", facecolor=c_card, edgecolor=c_border))
        ax.text(6, 76, "Fuentes Oficiales y Límites", fontsize=16, fontweight='bold', color=c_navy)
        txt_l10 = (
            "• Fuente Estadística Principal:\n"
            "  Gran Encuesta Integrada de Hogares (GEIH 2026) — DANE.\n"
            "  Muestra probabilística expandida con factor FEX_C18.\n\n"
            "• Fuente Geográfica:\n"
            "  Marco Geoestadístico Nacional — IGAC / DANE.\n\n"
            "• Representatividad Estadística:\n"
            "  Validada a nivel departamental; no se hacen inferencias\n"
            "  municipales no respaldadas por la muestra.\n\n"
            "• Rigor Causal:\n"
            "  Análisis descriptivo riguroso; no se infieren causas de\n"
            "  reformas laborales sin estudios contrafactuales."
        )
        ax.text(6, 44, txt_l10, fontsize=11.5, color=c_dark, linespacing=1.3)

        ax.add_patch(patches.FancyBboxPatch((52, 10), 44, 72, boxstyle="round,pad=1", facecolor="#F1F5F9", edgecolor=c_border))
        ax.text(54, 76, "Declaración Ética de Uso de IA", fontsize=16, fontweight='bold', color=c_red)
        txt_ia = (
            "• Herramienta Utilizada:\n"
            "  Google Gemini (rol estrictamente asistencial).\n\n"
            "• Alcance Instrumental:\n"
            "  Optimización de sintaxis en Python/R, contraste de paleta\n"
            "  accesible (WCAG AA) y apoyo en fórmulas DAX.\n\n"
            "• Auditoría y Autoría Humana:\n"
            "  Todos los cálculos numéricos, interpretaciones sociales y\n"
            "  decisiones narrativas fueron auditados y redactados\n"
            "  exclusivamente por Julián Steven Duarte y Julián Jiménez."
        )
        ax.text(54, 44, txt_ia, fontsize=11.5, color=c_dark, linespacing=1.3)
        pdf.savefig(fig, dpi=300)
        plt.close()

    print(f"✓ Presentación PDF de 10 diapositivas generada exitosamente en:\n  {out_pdf}")

if __name__ == "__main__":
    generar_presentacion_pdf()
