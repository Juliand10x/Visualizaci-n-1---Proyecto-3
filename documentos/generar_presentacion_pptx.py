# -*- coding: utf-8 -*-
"""
Generador automatizado de la presentación oficial de 10 diapositivas (.pptx)
Proyecto 3: Narrativa Visual Integrada — Visualización I
Universidad Externado de Colombia
Autores: Julián Steven Duarte & Julián Camilo Jiménez
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def crear_presentacion():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fig_dir = os.path.join(base_dir, "figuras")
    doc_dir = os.path.join(base_dir, "documentos")
    out_path = os.path.join(doc_dir, "Equipo_Duarte_Jimenez_Proyecto3_Presentacion.pptx")

    prs = Presentation()
    # 16:9 Widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Paleta de colores institucional
    c_navy = RGBColor(30, 58, 138)      # #1E3A8A
    c_red = RGBColor(225, 29, 72)       # #E11D48
    c_slate = RGBColor(71, 85, 105)     # #475569
    c_dark = RGBColor(15, 23, 42)       # #0F172A
    c_bg = RGBColor(248, 250, 252)      # #F8FAFC
    c_white = RGBColor(255, 255, 255)
    c_card = RGBColor(255, 255, 255)
    c_border = RGBColor(226, 232, 240)

    def agregar_header(slide, numero_slide, titulo, categoria="PROYECTO 3: NARRATIVA VISUAL INTEGRADA"):
        # Fondo sutil
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = c_bg
        bg.line.fill.background()

        # Barra superior navy
        header_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
        header_bar.fill.solid()
        header_bar.fill.fore_color.rgb = c_navy
        header_bar.line.fill.background()

        # Texto de categoría / tracking
        tf_cat = header_bar.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = f"{categoria}  |  Universidad Externado de Colombia"
        p_cat.font.size = Pt(10.5)
        p_cat.font.color.rgb = RGBColor(191, 219, 254)
        p_cat.font.bold = True

        p_tit = tf_cat.add_paragraph()
        p_tit.text = titulo
        p_tit.font.size = Pt(20)
        p_tit.font.color.rgb = c_white
        p_tit.font.bold = True

        # Footer con número de lámina
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.4))
        tf_foot = footer_box.text_frame
        p_foot = tf_foot.paragraphs[0]
        p_foot.text = f"Visualización 1  •  Equipo: Julián Steven Duarte & Julián Camilo Jiménez  •  Lámina {numero_slide} de 10"
        p_foot.font.size = Pt(9.5)
        p_foot.font.color.rgb = c_slate

    # =========================================================================
    # LÁMINA 1: PORTADA
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = c_navy
    bg1.line.fill.background()

    card1 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.2), Inches(10.933), Inches(5.1))
    card1.fill.solid()
    card1.fill.fore_color.rgb = c_white
    card1.line.color.rgb = c_border

    tf1 = card1.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "UNIVERSIDAD EXTERNADO DE COLOMBIA  •  VISUALIZACIÓN I"
    p1.font.size = Pt(12)
    p1.font.color.rgb = c_red
    p1.font.bold = True

    p2 = tf1.add_paragraph()
    p2.text = "La Trampa del Título: Radiografía de la Informalidad Laboral en Colombia"
    p2.font.size = Pt(28)
    p2.font.color.rgb = c_dark
    p2.font.bold = True

    p3 = tf1.add_paragraph()
    p3.text = "Una historia basada en datos para jóvenes que ingresan al mercado de trabajo (GEIH 2026 - DANE)"
    p3.font.size = Pt(14)
    p3.font.color.rgb = c_slate

    p4 = tf1.add_paragraph()
    p4.text = "\nExpositores: Julián Steven Duarte & Julián Camilo Jiménez\nDocentes: Adriana Pineda Barón & Paola Moreno\nNoviembre de 2026  •  Modalidad A: Presentación Narrativa Integrada"
    p4.font.size = Pt(12)
    p4.font.color.rgb = c_navy
    p4.font.bold = True

    # =========================================================================
    # LÁMINA 2: AUDIENCIA Y PREGUNTA
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    agregar_header(slide2, 2, "Encuadre Ciudadano: ¿A Quién le Hablamos y Qué Preguntamos?")

    # Caja Izquierda: Audiencia
    c_izq = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_izq.fill.solid()
    c_izq.fill.fore_color.rgb = c_white
    c_izq.line.color.rgb = c_border
    tf_izq = c_izq.text_frame
    tf_izq.word_wrap = True
    p = tf_izq.paragraphs[0]
    p.text = "Audiencia Ciudadana Específica"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = c_navy

    items_aud = [
        ("Público Objetivo:", "Jóvenes de 18 a 28 años, técnicos, tecnólogos y graduados universitarios en búsqueda de empleo."),
        ("El Problema Real:", "Tradicionalmente se educó bajo la creencia de que cursar educación superior garantizaba empleo formal."),
        ("La Realidad que Enfrentan:", "Contratos de tres meses por prestación de servicios, honorarios sin salud ni pensión, o subempleo calificado.")
    ]
    for tit, desc in items_aud:
        p_t = tf_izq.add_paragraph()
        p_t.text = f"\n• {tit}"
        p_t.font.bold = True
        p_t.font.size = Pt(12.5)
        p_t.font.color.rgb = c_dark
        p_d = tf_izq.add_paragraph()
        p_d.text = f"  {desc}"
        p_d.font.size = Pt(11.5)
        p_d.font.color.rgb = c_slate

    # Caja Derecha: Pregunta Central
    c_der = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2))
    c_der.fill.solid()
    c_der.fill.fore_color.rgb = c_white
    c_der.line.color.rgb = c_border
    tf_der = c_der.text_frame
    tf_der.word_wrap = True
    p = tf_der.paragraphs[0]
    p.text = "La Pregunta Analítica Central"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = c_red

    p_q = tf_der.add_paragraph()
    p_q.text = "\n«¿Por qué en Colombia cursar educación superior ya no garantiza un empleo formal con seguridad social, y de qué forma la región geográfica y el género determinan las probabilidades reales de un trabajo digno?»"
    p_q.font.size = Pt(14)
    p_q.font.bold = True
    p_q.font.color.rgb = c_dark

    p_obj = tf_der.add_paragraph()
    p_obj.text = "\nObjetivo Comunicativo:\nTransformar la evidencia estadística en decisiones prácticas de empleabilidad y en exigencia ciudadana informada para las políticas de formalización."
    p_obj.font.size = Pt(12)
    p_obj.font.color.rgb = c_slate

    # =========================================================================
    # LÁMINA 3: LA GRAN IDEA
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    agregar_header(slide3, 3, "La Gran Idea: El Mensaje Central Basado en Evidencia")

    big_card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(2.3))
    big_card.fill.solid()
    big_card.fill.fore_color.rgb = RGBColor(254, 242, 242)
    big_card.line.color.rgb = RGBColor(254, 205, 211)
    tf_big = big_card.text_frame
    tf_big.word_wrap = True
    p = tf_big.paragraphs[0]
    p.text = "LA GRAN IDEA QUE DEMUESTRAN LOS DATOS:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = c_red
    p_body = tf_big.add_paragraph()
    p_body.text = "«En Colombia, más de 6 de cada 10 graduados con educación superior y técnica están atrapados en la informalidad o el rebusque calificado (61.3%). Esta trampa se agrava drásticamente en la periferia del país (superando el 75%) y oculta una grave brecha de género por el trabajo de cuidado no remunerado.»"
    p_body.font.size = Pt(14.5)
    p_body.font.bold = True
    p_body.font.color.rgb = c_dark

    # 3 Cajas inferiores con pilares
    pilares = [
        ("61.26% de Informalidad", "La Educación No Basta", "Técnicos y universitarios tienen una informalidad casi idéntica a quienes tienen secundaria (61.1%)."),
        ("75.71% en Guaviare", "La Brecha Territorial", "La informalidad en la periferia triplica la precariedad frente al centro del país."),
        ("Barrera Silenciosa", "Desbalance de Género", "La aparente menor informalidad en mujeres ocupadas oculta que millones no pueden trabajar por labores de cuidado.")
    ]
    for i, (kpi, tit, desc) in enumerate(pilares):
        x = 0.8 + i * 4.0
        kpi_card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(4.1), Inches(3.733), Inches(2.6))
        kpi_card.fill.solid()
        kpi_card.fill.fore_color.rgb = c_white
        kpi_card.line.color.rgb = c_border
        tf_k = kpi_card.text_frame
        tf_k.word_wrap = True
        p_k = tf_k.paragraphs[0]
        p_k.text = kpi
        p_k.font.size = Pt(18)
        p_k.font.bold = True
        p_k.font.color.rgb = c_navy
        p_t = tf_k.add_paragraph()
        p_t.text = tit
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = c_dark
        p_d = tf_k.add_paragraph()
        p_d.text = f"\n{desc}"
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = c_slate

    # =========================================================================
    # LÁMINA 4: POWER BI Y ENLACES
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    agregar_header(slide4, 4, "Power BI Service y Despliegue en Vivo: Continuidad y Trazabilidad")

    c_pbi1 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_pbi1.fill.solid()
    c_pbi1.fill.fore_color.rgb = c_white
    c_pbi1.line.color.rgb = c_border
    tf = c_pbi1.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Mejoras y Validación del Dashboard"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = c_navy

    items_pbi = [
        ("Trazabilidad Oficial:", "Continuidad del modelo estrella estructurado en la Entrega 1 con la GEIH 2026."),
        ("Exactitud de la Tasa:", "Las medidas DAX con DIVIDE([Total Informales], [Total Ocupados]) calculan la tasa exacta en 54.64% sin sesgo."),
        ("Focalización en Jóvenes:", "Medida específica que evalúa el rango de 18 a 28 años con 41.07% de informalidad."),
        ("Doble Página Interactiva:", "Página 1 (Nacional y Brechas) y Página 2 (Focalización Territorial con slicers).")
    ]
    for tit, desc in items_pbi:
        p_t = tf.add_paragraph()
        p_t.text = f"\n• {tit}"
        p_t.font.bold = True
        p_t.font.size = Pt(12)
        p_t.font.color.rgb = c_dark
        p_d = tf.add_paragraph()
        p_d.text = f"  {desc}"
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = c_slate

    c_pbi2 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2))
    c_pbi2.fill.solid()
    c_pbi2.fill.fore_color.rgb = RGBColor(239, 246, 255)
    c_pbi2.line.color.rgb = RGBColor(191, 219, 254)
    tf2 = c_pbi2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "Ecosistema Digital en Producción"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = c_navy

    enlaces = [
        ("🌐 Plataforma Web en Vercel (Modalidad B):", "https://webnarrativa.vercel.app\nDespliegue responsivo instantáneo con CDN global."),
        ("📊 Dashboard en Power BI Service:", "Enlace institucional compartido y funcional en tiempo real para interacción en la sustentación."),
        ("🐙 Repositorio Oficial en GitHub:", "https://github.com/Juliand10x/Visualizaci-n-1---Proyecto-3\nCódigo reproducible, notebooks ejecutados y scripts espaciales.")
    ]
    for tit, desc in enlaces:
        p_t = tf2.add_paragraph()
        p_t.text = f"\n{tit}"
        p_t.font.bold = True
        p_t.font.size = Pt(12)
        p_t.font.color.rgb = c_dark
        p_d = tf2.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = c_navy

    # =========================================================================
    # LÁMINA 5: PYTHON SEABORN 1 (PARADOJA EDUCATIVA)
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    agregar_header(slide5, 5, "Python (Seaborn): La Paradoja de la Educación Superior")

    img_path1 = os.path.join(fig_dir, "fig1_paradoja_educativa_seaborn.png")
    if os.path.exists(img_path1):
        slide5.shapes.add_picture(img_path1, Inches(0.8), Inches(1.45), width=Inches(7.2))

    card5 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.3), Inches(1.45), Inches(4.2), Inches(5.3))
    card5.fill.solid()
    card5.fill.fore_color.rgb = c_white
    card5.line.color.rgb = c_border
    tf5 = card5.text_frame
    tf5.word_wrap = True
    p = tf5.paragraphs[0]
    p.text = "Interpretación Ciudadana"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = c_red

    hallazgos1 = [
        ("La Cifra Impactante:", "Educación Superior registra 61.26% de informalidad, cifra mayor a la Primaria (52.37%)."),
        ("¿Por qué ocurre?:", "El mercado no genera vacantes formales en nómina; absorbe egresados por prestación de servicios u honorarios sin cotización continua."),
        ("Decisión para el Joven:", "El título universitario ya no es un seguro automático; se requiere planificar la seguridad social de forma independiente.")
    ]
    for tit, desc in hallazgos1:
        p_t = tf5.add_paragraph()
        p_t.text = f"\n• {tit}"
        p_t.font.bold = True
        p_t.font.size = Pt(11.5)
        p_t.font.color.rgb = c_dark
        p_d = tf5.add_paragraph()
        p_d.text = f"  {desc}"
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = c_slate

    # =========================================================================
    # LÁMINA 6: PYTHON SEABORN 2 (BRECHA DE GÉNERO)
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    agregar_header(slide6, 6, "Python (Seaborn): La Brecha Oculta de Género")

    img_path2 = os.path.join(fig_dir, "fig2_brecha_genero_educacion_seaborn.png")
    if os.path.exists(img_path2):
        slide6.shapes.add_picture(img_path2, Inches(0.8), Inches(1.45), width=Inches(7.2))

    card6 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.3), Inches(1.45), Inches(4.2), Inches(5.3))
    card6.fill.solid()
    card6.fill.fore_color.rgb = c_white
    card6.line.color.rgb = c_border
    tf6 = card6.text_frame
    tf6.word_wrap = True
    p = tf6.paragraphs[0]
    p.text = "Interpretación Ciudadana"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = c_navy

    hallazgos2 = [
        ("La Brecha Observada:", "En egresados de Educación Superior, los hombres tienen 65.27% y las mujeres 58.18%."),
        ("La Trampa del Indicador:", "La menor tasa en mujeres ocupadas NO significa mejores condiciones."),
        ("La Barrera de Entrada:", "Millones de mujeres están confinadas al cuidado doméstico no remunerado; los hombres están forzados al rebusque diario."),
        ("Ética y Honestidad:", "Evitamos conclusiones engañosas visibilizando las cargas no remuneradas.")
    ]
    for tit, desc in hallazgos2:
        p_t = tf6.add_paragraph()
        p_t.text = f"\n• {tit}"
        p_t.font.bold = True
        p_t.font.size = Pt(11.5)
        p_t.font.color.rgb = c_dark
        p_d = tf6.add_paragraph()
        p_d.text = f"  {desc}"
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = c_slate

    # =========================================================================
    # LÁMINA 7: PYTHON PLOTLY (EXPLORADOR INTERACTIVO)
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    agregar_header(slide7, 7, "Python (Plotly): Explorador Departamental Interactivo")

    # Tarjeta de semáforo interactivo
    c_plot_izq = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(6.8), Inches(5.2))
    c_plot_izq.fill.solid()
    c_plot_izq.fill.fore_color.rgb = c_white
    c_plot_izq.line.color.rgb = c_border
    tf7 = c_plot_izq.text_frame
    tf7.word_wrap = True
    p = tf7.paragraphs[0]
    p.text = "Semáforo Ciudadano de Riesgo Territorial"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = c_navy

    semaforo = [
        ("🔴 Alerta Crítica (> 60%):", "Guaviare (75.7%), Casanare (66.5%), Bogotá D.C. (64.1%), Cundinamarca (62.3%), Nariño (62.1%)."),
        ("🟡 Vulnerabilidad Media (50% - 60%):", "Tolima (59.2%), Antioquia (56.1%), Valle del Cauca (55.4%), La Guajira (51.0%)."),
        ("🔵 Mayor Formalidad Relativa (< 50%):", "Boyacá (49.8%), Putumayo (38.1%)."),
        ("📏 Línea de Referencia Nacional:", "54.64% promedio ponderado del país.")
    ]
    for tit, desc in semaforo:
        p_t = tf7.add_paragraph()
        p_t.text = f"\n{tit}"
        p_t.font.bold = True
        p_t.font.size = Pt(12)
        p_t.font.color.rgb = c_dark
        p_d = tf7.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = c_slate

    c_plot_der = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.0), Inches(1.5), Inches(4.5), Inches(5.2))
    c_plot_der.fill.solid()
    c_plot_der.fill.fore_color.rgb = RGBColor(241, 245, 249)
    c_plot_der.line.color.rgb = c_border
    tf7_d = c_plot_der.text_frame
    tf7_d.word_wrap = True
    p = tf7_d.paragraphs[0]
    p.text = "Capacidades de Interacción"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = c_dark

    p_items = [
        ("Tooltips Detallados:", "Muestra al pasar el cursor los ocupados totales, informales absolutos y categoría de riesgo."),
        ("Autocontenido HTML:", "Exportado como archivo HTML independiente para su consulta sin requerir servidor Python."),
        ("Demostración en Vivo:", "Disponible en la web interactiva desplegada en Vercel durante la sustentación.")
    ]
    for tit, desc in p_items:
        p_t = tf7_d.add_paragraph()
        p_t.text = f"\n• {tit}"
        p_t.font.bold = True
        p_t.font.size = Pt(11.5)
        p_t.font.color.rgb = c_navy
        p_d = tf7_d.add_paragraph()
        p_d.text = f"  {desc}"
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = c_slate

    # =========================================================================
    # LÁMINA 8: R GEOESPACIAL (MAPAS CARTOGRÁFICOS)
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    agregar_header(slide8, 8, "R Geoespacial: Radiografía Territorial de la Informalidad")

    img_path_r = os.path.join(fig_dir, "mapa_informalidad_colombia_R.png")
    if os.path.exists(img_path_r):
        slide8.shapes.add_picture(img_path_r, Inches(0.8), Inches(1.45), height=Inches(5.3))

    card8 = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.2), Inches(1.45), Inches(6.3), Inches(5.3))
    card8.fill.solid()
    card8.fill.fore_color.rgb = c_white
    card8.line.color.rgb = c_border
    tf8 = card8.text_frame
    tf8.word_wrap = True
    p = tf8.paragraphs[0]
    p.text = "Rigor Técnico y Hallazgos Espaciales"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = c_navy

    r_items = [
        ("Metodología de Clase (Sesión 3):", "Uniones espaciales con paquete sf, clasificación por cortes de Jenks (classInt) y renderizado con tmap y ggplot2."),
        ("Elementos Cartográficos:", "Marco oficial IGAC/DANE, escala métrica, rosa de los vientos y créditos oficiales."),
        ("La Desconexión Periferia-Centro:", "La región central andina retiene mayor empleo formal, mientras la Orinoquía y Amazonía superan el 70% de desprotección."),
        ("El Caso Guaviare (75.7%):", "3 de cada 4 oportunidades laborales en el departamento carecen de pensión o cesantías.")
    ]
    for tit, desc in r_items:
        p_t = tf8.add_paragraph()
        p_t.text = f"\n• {tit}"
        p_t.font.bold = True
        p_t.font.size = Pt(11.5)
        p_t.font.color.rgb = c_dark
        p_d = tf8.add_paragraph()
        p_d.text = f"  {desc}"
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = c_slate

    # =========================================================================
    # LÁMINA 9: ACCIONES Y MENSAJE FINAL
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    agregar_header(slide9, 9, "Mensaje Final: Estrategias Ciudadanas de Empleabilidad")

    cajas_acciones = [
        ("1. Planificación Temprana", "Seguridad Social Independiente", "Si el contrato es por prestación de servicios, calcular siempre la retención del 40% para salud y pensión al presupuestar honorarios."),
        ("2. Movilidad Laboral", "Teletrabajo Estratégico", "En departamentos con más del 65% de informalidad, orientar la postulación hacia ofertas remotas con sede en centros corporativos."),
        ("3. Exigencia Pública", "Formalización Productiva", "Exigir incentivos tributarios a empresas que contraten indefinidamente a jóvenes, superando los subsidios asistenciales temporales.")
    ]
    for i, (num, tit, desc) in enumerate(cajas_acciones):
        y = 1.5 + i * 1.8
        c = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(y), Inches(11.733), Inches(1.55))
        c.fill.solid()
        c.fill.fore_color.rgb = c_white
        c.line.color.rgb = c_border
        tf_c = c.text_frame
        tf_c.word_wrap = True
        p_num = tf_c.paragraphs[0]
        p_num.text = f"{num}  —  {tit}"
        p_num.font.size = Pt(13.5)
        p_num.font.bold = True
        p_num.font.color.rgb = c_navy
        p_d = tf_c.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11.5)
        p_d.font.color.rgb = c_dark

    # =========================================================================
    # LÁMINA 10: METODOLOGÍA, ÉTICA E IA
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    agregar_header(slide10, 10, "Fuentes, Limitaciones Metodológicas y Declaración de IA")

    c10_izq = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c10_izq.fill.solid()
    c10_izq.fill.fore_color.rgb = c_white
    c10_izq.line.color.rgb = c_border
    tf10_i = c10_izq.text_frame
    tf10_i.word_wrap = True
    p = tf10_i.paragraphs[0]
    p.text = "Fuentes Oficiales y Límites"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = c_navy

    lims = [
        ("Fuente Principal:", "Gran Encuesta Integrada de Hogares (GEIH 2026) — DANE. Muestra probabilística expandida con FEX_C18 del Censo."),
        ("Fuente Geográfica:", "Marco Geoestadístico Nacional — IGAC / DANE (EPSG:9377)."),
        ("Límites Estadísticos:", "Representatividad validada a nivel departamental; no se hacen inferencias a municipios pequeños no cubiertos."),
        ("Cautela Causal:", "Análisis descriptivo riguroso; no se infieren causas de reformas sin modelos contrafactuales.")
    ]
    for tit, desc in lims:
        p_t = tf10_i.add_paragraph()
        p_t.text = f"\n• {tit}"
        p_t.font.bold = True
        p_t.font.size = Pt(11.5)
        p_t.font.color.rgb = c_dark
        p_d = tf10_i.add_paragraph()
        p_d.text = f"  {desc}"
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = c_slate

    c10_der = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2))
    c10_der.fill.solid()
    c10_der.fill.fore_color.rgb = RGBColor(241, 245, 249)
    c10_der.line.color.rgb = c_border
    tf10_d = c10_der.text_frame
    tf10_d.word_wrap = True
    p = tf10_d.paragraphs[0]
    p.text = "Declaración Ética de Uso de IA"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = c_red

    p_ia1 = tf10_d.add_paragraph()
    p_ia1.text = "\n• Herramienta Utilizada:\nGoogle Gemini (asistencia de código y contraste cromático)."
    p_ia1.font.size = Pt(11.5)
    p_ia1.font.bold = True
    p_ia1.font.color.rgb = c_dark

    p_ia2 = tf10_d.add_paragraph()
    p_ia2.text = "\n• Alcance Instrumental:\nOptimización sintáctica de scripts en Python/R y cálculo de promedio mensual en DAX."
    p_ia2.font.size = Pt(11.5)
    p_ia2.font.bold = True
    p_ia2.font.color.rgb = c_dark

    p_ia3 = tf10_d.add_paragraph()
    p_ia3.text = "\n• Auditoría y Autoría Humana:\nTodos los cálculos matemáticos, interpretaciones sociales y decisiones narrativas fueron auditados y redactados exclusivamente por Julián Steven Duarte y Julián Camilo Jiménez."
    p_ia3.font.size = Pt(11.5)
    p_ia3.font.bold = True
    p_ia3.font.color.rgb = c_navy

    prs.save(out_path)
    print(f"✓ Presentación de 10 diapositivas generada exitosamente en:\n  {out_path}")

if __name__ == "__main__":
    crear_presentacion()
