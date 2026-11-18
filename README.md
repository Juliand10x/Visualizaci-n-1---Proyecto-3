# Proyecto 3: Narrativa Visual Integrada — Visualización 1
**Universidad Externado de Colombia**  
**Docentes:** Adriana Pineda Barón & Paola Moreno  
**Equipo de Trabajo:** Julián Steven Duarte & Julián Camilo Jiménez  
**Fecha de Entrega:** 17 de noviembre de 2026, 11:59 p.m.  
**Fuente de Datos:** Gran Encuesta Integrada de Hogares (GEIH 2026) — DANE & Marco Geoestadístico IGAC  

### 🔗 Enlaces Oficiales de Entrega y Consulta en Vivo
* 🌐 **Plataforma Web en Producción (Vercel — Modalidad B):** [https://webnarrativa.vercel.app](https://webnarrativa.vercel.app)
* 📊 **Dashboard Oficial en Power BI Service:** [Ver Dashboard Interactivo](https://app.powerbi.com/links/gvbF1pi94p?ctid=3b944d9a-1051-4685-b09d-9a95ee2dbd99&pbi_source=linkShare)
* 🐙 **Repositorio Oficial de GitHub:** [https://github.com/Juliand10x/Visualizaci-n-1---Proyecto-3](https://github.com/Juliand10x/Visualizaci-n-1---Proyecto-3)

---

## 🎯 1. Resumen Ejecutivo y Enfoque Comunicativo

El **Proyecto 3** traslada las competencias técnicas desarrolladas en el semestre (Power BI, Python y R) hacia una **narrativa visual integrada dirigida a una audiencia ciudadana no especializada**.

* **Audiencia Ciudadana Delimitada:** Jóvenes de 18 a 28 años, técnicos, tecnólogos y nuevos profesionales que buscan su primera oportunidad laboral digna en Colombia.
* **Pregunta Analítica Central:**  
  > *¿Por qué en Colombia cursar educación superior ya no garantiza un empleo formal con seguridad social, y de qué forma la región geográfica y el género determinan las probabilidades reales de un trabajo digno?*
* **La Gran Idea:**  
  > *"En Colombia, más de 6 de cada 10 graduados con educación superior y técnica están atrapados en la informalidad o el rebusque calificado (61.3%). Esta trampa se agrava drásticamente en la periferia del país (llegando al 75.7% en departamentos como Guaviare) y oculta una grave desigualdad de género por el trabajo de cuidado no remunerado. Comprender esta evidencia empodera a los jóvenes para tomar decisiones laborales estratégicas y exige políticas públicas de formalización productiva real."*

---

## 📁 2. Estructura y Organización del Repositorio

El proyecto mantiene rutas relativas universales y cubre tanto la **Modalidad A** (Presentación ejecutiva de 10 diapositivas) como la **Modalidad B** (Plataforma web en Vercel):

```text
proyecto 3/
├── NOTAS_ENTREGA_Y_ENLACES.txt       # Resumen de enlaces oficiales para revisión inmediata
├── PLAN_DE_IMPLEMENTACION.md         # Plan estratégico de trabajo y encuadre comunicativo
├── GUIA_POWER_BI.md                  # Manual paso a paso para actualización de DAX y diseño en PBI
├── README.md                         # Documentación maestra y checklist (este archivo)
├── LEEME.md                          # Instrucciones rápidas de reproducción y ejecución
├── Equipo_Duarte_Jimenez_Proyecto3_Dashboard.pbix # Tablero base extraído de la entrega 1
├── web_narrativa/                    # Plataforma web interactiva desplegada en Vercel (Modalidad B)
│   ├── index.html                    # Aplicación web responsiva con narrativa y gráficos
│   ├── vercel.json                   # Configuración de despliegue en CDN global
│   ├── visualizacion_interactiva_plotly.html # Mini-dashboard interactivo embebido
│   └── assets/                       # Figuras y mapas en alta resolución para la web
├── Datos/                            # Tablas preparadas y capas cartográficas
│   ├── geih_2026_departamentos.csv   # Indicadores agregados por los 33 departamentos de Colombia
│   ├── geih_2026_educacion_edad.csv  # Tasas de informalidad por nivel educativo y rangos de edad
│   ├── geih_2026_sexo_educacion.csv  # Cruces demográficos de género y nivel formativo
│   ├── geih_2026_tendencia_mensual.csv # Serie temporal del semestre (Enero a Junio 2026)
│   ├── geih_2026_muestra_analitica.csv # Muestra representativa de microdatos para modelos (25k filas)
│   └── colombia_departamentos.geojson # Capa geoespacial departamental oficial optimizada (IGAC/DANE)
├── figuras/                          # Artefactos visuales generados en alta resolución (300 DPI)
│   ├── fig1_paradoja_educativa_seaborn.png      # Gráfico 1: Barras horizontales por nivel educativo
│   ├── fig2_brecha_genero_educacion_seaborn.png # Gráfico 2: Dumbbell chart de brecha de género
│   ├── fig3_evolucion_mensual_seaborn.png       # Gráfico 3: Serie de tiempo mensual de informalidad
│   ├── mapa_informalidad_colombia_R.png         # Mapa cartográfico en R (ggplot2 con etiquetas)
│   ├── mapa_informalidad_tmap.png               # Mapa cartográfico en R (tmap + Jenks)
│   └── visualizacion_interactiva_plotly.html    # Explorador interactivo ciudadano autocontenido
├── notebooks/                        # Código reproducible en Python y material de clase
│   ├── Equipo_Duarte_Jimenez_Proyecto3_Visualizacion.ipynb # Jupyter Notebook oficial completamente ejecutado
│   ├── crear_notebook.py             # Script de construcción programática del Notebook
│   ├── generar_figuras.py            # Generador automatizado de gráficos y HTML interactivo
│   └── Sesion_*.ipynb                # Notebooks pedagógicos de apoyo del curso
├── scripts_R/                        # Código reproducible en R
│   ├── generar_mapa_colombia.R       # Script de R para procesamiento espacial y renderizado
│   └── mapa_informalidad_colombia.Rmd # Documento R Markdown alineado a las Sesiones 2 y 3 de mapas
├── R/Rstudio_Visua/                  # Talleres y scripts de apoyo de las sesiones de clase
│   ├── Sesion_2/                     # Mapas base y datos municipales
│   ├── Sesion_3/                     # Mapas coropléticos y cortes de Jenks
│   └── sesion_4/                     # Integración Power BI con RStudio
└── documentos/                       # Entregables narrativos y anexos
    ├── Presentacion_Narrativa_10_Diapositivas.md # Storyline y láminas del producto final (Modalidad A)
    ├── GUIA_ESTUDIO_COMPANERO.md     # Guía rápida para la sustentación oral (roles Duarte / Jiménez)
    ├── Guia_Sustentacion_Proyecto3.md # Guion cronometrado de 10 min y banco de respuestas
    └── Anexo_IA.md                   # Declaración ética y técnica de uso de IA (máx. 1 pág.)
```

---

## ✅ 3. Estado del Proyecto: ¿Qué está completado al 100%?

1. **Despliegue Web en Vercel (Modalidad B):**
   * Plataforma accesible públicamente en [https://webnarrativa.vercel.app](https://webnarrativa.vercel.app) con visualizaciones interactivas de Plotly embebidas, mapas cartográficos y conexión directa a Power BI Service.
2. **Tablero en Power BI Service:**
   * Tablero oficial publicado y disponible en [enlace directo de Power BI Service](https://app.powerbi.com/links/gvbF1pi94p?ctid=3b944d9a-1051-4685-b09d-9a95ee2dbd99&pbi_source=linkShare).
3. **Módulo Python (Seaborn y Plotly):**
   * Notebook Jupyter oficial (`Equipo_Duarte_Jimenez_Proyecto3_Visualizacion.ipynb`) estructurado con la pedagogía de clase y ejecutado de principio a fin sin errores.
   * 3 Figuras estáticas en Seaborn exportadas en 300 DPI (`fig1`, `fig2`, `fig3`).
   * 1 Componente interactivo en Plotly con semáforo de riesgo y tooltips exportado a HTML funcional (`visualizacion_interactiva_plotly.html`).
4. **Módulo Geoespacial en R (`sf` + `classInt` + `tmap` + `ggplot2`):**
   * Metodología de las Sesiones 2 y 3 de clase (clasificación por intervalos de *Jenks / Natural Breaks*).
   * Generación de dos mapas cartográficos en 300 DPI (`mapa_informalidad_colombia_R.png` y `mapa_informalidad_tmap.png`) con rosa de los vientos, escala y créditos oficiales.
   * Script reproducible `generar_mapa_colombia.R` y documento `mapa_informalidad_colombia.Rmd`.
5. **Paquete Documental y Argumentativo:**
   * Storyline completo de 10 diapositivas para Modalidad A en `Presentacion_Narrativa_10_Diapositivas.md`.
   * Guías de sustentación oral sincronizadas (`GUIA_ESTUDIO_COMPANERO.md` y `Guia_Sustentacion_Proyecto3.md`) para 10 minutos cronometrados con roles asignados y banco de preguntas de examen.
   * Anexo técnico de uso ético de IA (máximo 1 página).

---

## 📌 4. Checklist Final para la Sustentación

1. **Presentación Visual (Modalidad A):**  
   * Tener abierto el documento PDF de 10 diapositivas generado a partir de `documentos/Presentacion_Narrativa_10_Diapositivas.md`.
2. **Pestañas Listas en el Navegador para Demostración en Vivo:**
   * Pestaña 1: [Plataforma Web en Vercel](https://webnarrativa.vercel.app)
   * Pestaña 2: [Power BI Service](https://app.powerbi.com/links/gvbF1pi94p?ctid=3b944d9a-1051-4685-b09d-9a95ee2dbd99&pbi_source=linkShare)
   * Pestaña 3: [Repositorio GitHub](https://github.com/Juliand10x/Visualizaci-n-1---Proyecto-3)
3. **Repaso de Roles (Julián Duarte & Julián Jiménez):**
   * Seguir la distribución de minutos de **`documentos/GUIA_ESTUDIO_COMPANERO.md`** (Bloque 1 apertura por Duarte, Bloque 2 demostración técnica compartida, Bloque 3 cierre y preguntas).

---

## 📊 5. Cifras Clave del Estudio para Memorizar

* **Tasa Nacional de Informalidad:** **54.64%** (~17.5M ocupados y ~9.55M informales por mes).
* **Paradoja Educativa:** Educación Superior (**61.26%**) y Secundaria (**61.14%**) superan ampliamente a Primaria (**52.37%**).
* **Brecha Territorial Extrema:** **Guaviare (75.71%)** y **Casanare (66.55%)** triplican el riesgo laboral frente al centro del país.
* **Sesgo de Género:** Hombres ocupados (**65.3%**) vs. Mujeres ocupadas (**58.2%**), con barrera previa de cuidado no remunerado en el hogar.
