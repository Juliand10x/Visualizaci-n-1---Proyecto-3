# Proyecto 3: Narrativa Visual Integrada — Visualización 1
**Universidad Externado de Colombia**  
**Docentes:** Adriana Pineda Barón & Paola Moreno  
**Equipo de Trabajo:** Julián Steven Duarte & Julián Camilo Jiménez  
**Repositorio Oficial:** [GitHub — Visualización 1: Proyecto 3](https://github.com/Juliand10x/Visualizaci-n-1---Proyecto-3)  
**Fuente de Datos Principal:** Gran Encuesta Integrada de Hogares (GEIH 2026) — DANE & Marco Geoestadístico IGAC  
**Fecha de Entrega:** 17 de noviembre de 2026, 11:59 p.m.  

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

El proyecto mantiene rutas relativas universales para garantizar 100% de reproducibilidad:

```text
proyecto 3/
├── PLAN_DE_IMPLEMENTACION.md         # Plan estratégico de trabajo y encuadre comunicativo
├── GUIA_POWER_BI.md                  # Manual paso a paso para actualización de DAX y diseño en PBI
├── README.md                         # Documentación maestra y checklist (este archivo)
├── LEEME.md                          # Instrucciones rápidas de reproducción y ejecución
├── Equipo_Duarte_Jimenez_Proyecto3_Dashboard.pbix # Tablero base extraído listo para abrir y publicar
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
├── notebooks/                        # Código reproducible en Python
│   ├── Equipo_Duarte_Jimenez_Proyecto3_Visualizacion.ipynb # Jupyter Notebook oficial completamente ejecutado
│   ├── crear_notebook.py             # Script de construcción programática del Notebook
│   └── generar_figuras.py            # Generador automatizado de gráficos y HTML interactivo
├── scripts_R/                        # Código reproducible en R
│   ├── generar_mapa_colombia.R       # Script de R para procesamiento espacial y renderizado
│   └── mapa_informalidad_colombia.Rmd # Documento R Markdown alineado a las Sesiones 2 y 3 de mapas
└── documentos/                       # Entregables narrativos y anexos
    ├── Presentacion_Narrativa_10_Diapositivas.md # Storyline y láminas del producto final (Modalidad A)
    ├── Guia_Sustentacion_Proyecto3.md            # Guion cronometrado de 10 min y banco de respuestas
    └── Anexo_IA.md                               # Declaración ética y técnica de uso de IA (máx. 1 pág.)
```

---

## ✅ 3. Estado del Proyecto: ¿Qué está completado al 100%?

1. **Módulo Python (Seaborn y Plotly):**
   * Notebook Jupyter oficial (`Equipo_Duarte_Jimenez_Proyecto3_Visualizacion.ipynb`) estructurado con la pedagogía de clase y ejecutado de principio a fin sin errores.
   * 3 Figuras estáticas en Seaborn exportadas en 300 DPI (`fig1`, `fig2`, `fig3`).
   * 1 Componente interactivo en Plotly con semáforo de riesgo y tooltips exportado a HTML funcional (`visualizacion_interactiva_plotly.html`).
2. **Módulo Geoespacial en R (`sf` + `classInt` + `tmap` + `ggplot2`):**
   * Metodología de las Sesiones 2 y 3 de clase (clasificación por intervalos de *Jenks / Natural Breaks*).
   * Generación de dos mapas cartográficos en 300 DPI (`mapa_informalidad_colombia_R.png` y `mapa_informalidad_tmap.png`) con rosa de los vientos, escala y créditos oficiales.
   * Script reproducible `generar_mapa_colombia.R` y documento `mapa_informalidad_colombia.Rmd`.
3. **Paquete Documental y Argumentativo:**
   * Storyline completo de 10 diapositivas para Modalidad A en `Presentacion_Narrativa_10_Diapositivas.md`.
   * Guía de Sustentación Oral cronometrada a 10 minutos con roles definidos y banco de respuestas para las docentes.
   * Anexo técnico de uso ético de IA (máximo 1 página).
4. **Base de Datos y Modelo Power BI:**
   * Microdatos y agregaciones de la GEIH 2026 preparados.
   * Capa geográfica ligera `colombia_departamentos.geojson` lista para usar en cualquier equipo.
   * Archivo base `Equipo_Duarte_Jimenez_Proyecto3_Dashboard.pbix` extraído y ubicado en la carpeta del proyecto.

---

## 📌 4. ¿Qué falta por hacer y cómo hacerlo? (Checklist del Usuario)

Para culminar la entrega formal, al equipo humano le corresponde realizar los siguientes **3 pasos finales**:

### Paso 1: Actualizar y Publicar Power BI Desktop (Tiempo estimado: 10 min)
1. Abre el archivo **`Equipo_Duarte_Jimenez_Proyecto3_Dashboard.pbix`** en Power BI Desktop.
2. Abre la **`GUIA_POWER_BI.md`** y crea las dos medidas DAX de promedio mensual en la tabla `_Medidas`:
   ```dax
   Promedio Mensual Ocupados = AVERAGEX( VALUES( DimFecha[Mes] ), [Total Ocupados] )
   Promedio Mensual Informales = AVERAGEX( VALUES( DimFecha[Mes] ), [Total Informales] )
   ```
3. Reemplaza los campos en las tarjetas superiores para que muestren **~17.5M ocupados** y **~9.55M informales** (la tasa se mantiene exacta en **54.64%**).
4. Guarda el archivo (`Ctrl + S`) y haz clic en el botón superior **Publicar**.
5. Selecciona tu área de trabajo, copia el enlace web del reporte publicado en Power BI Service y agrégalo en la lámina 4 de tu presentación.

### Paso 2: Armar las 10 Diapositivas Finales (Tiempo estimado: 15 min)
1. Abre tu herramienta de diapositivas de preferencia (PowerPoint, Canva o Google Slides).
2. Sigue lámina por lámina el contenido ya redactado en **`documentos/Presentacion_Narrativa_10_Diapositivas.md`**.
3. Pega las figuras de alta resolución que están listas en la carpeta **`figuras/`**:
   * Lámina 5: `fig1_paradoja_educativa_seaborn.png`
   * Lámina 6: `fig2_brecha_genero_educacion_seaborn.png`
   * Lámina 7: Captura o enlace del HTML `visualizacion_interactiva_plotly.html`
   * Lámina 8: `mapa_informalidad_colombia_R.png` (o `mapa_informalidad_tmap.png`)
4. Exporta la presentación en formato **PDF** (máximo 10 páginas) conforme exige la rúbrica (Modalidad A).

### Paso 3: Ensayar la Sustentación Oral (Tiempo estimado: 10 min)
* Utiliza el libreto cronometrado en **`documentos/Guia_Sustentacion_Proyecto3.md`** para coordinar los 10 minutos de exposición en pareja (Julián Duarte y Julián Jiménez) y repasar el banco de respuestas técnicas sobre DAX, `FEX_C18`, `sf` y principios Gestalt.

---

## 🛠️ 5. Reproducción Rápida desde Terminal

```bash
# Ejecutar generador de figuras y Notebook Python
python notebooks/generar_figuras.py
jupyter nbconvert --to notebook --execute --inplace notebooks/Equipo_Duarte_Jimenez_Proyecto3_Visualizacion.ipynb

# Ejecutar script espacial de R
Rscript scripts_R/generar_mapa_colombia.R
```

---

## 📊 6. Cifras Clave del Estudio

* **Tasa Nacional de Informalidad:** **54.64%** (~17.5M ocupados y ~9.55M informales por mes).
* **Paradoja Educativa:** Educación Superior (**61.26%**) y Secundaria (**61.14%**) superan ampliamente a Primaria (**52.37%**).
* **Brecha Territorial Extrema:** **Guaviare (75.71%)** y **Casanare (66.55%)** triplican el riesgo laboral frente al centro del país.
* **Sesgo de Género:** Hombres ocupados (**65.3%**) vs. Mujeres ocupadas (**58.2%**), con barrera previa de cuidado no remunerado en el hogar.
