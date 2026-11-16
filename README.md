# Proyecto 3: Narrativa Visual Integrada — Visualización 1
**Universidad Externado de Colombia**  
**Docentes:** Adriana Pineda Barón & Paola Moreno  
**Equipo de Trabajo:** Julián Steven Duarte & Julián Camilo Jiménez  
**Fuente de Datos Principal:** Gran Encuesta Integrada de Hogares (GEIH 2026) — DANE & Cartografía IGAC  
**Fecha de Entrega:** Noviembre de 2026  

---

## 🎯 1. Resumen Ejecutivo y Enfoque Comunicativo

El **Proyecto 3** traslada las competencias desarrolladas a lo largo de la asignatura hacia la **comunicación de datos orientada a una audiencia ciudadana no especializada**.

* **Audiencia Ciudadana Delimitada:** Jóvenes de 18 a 28 años, técnicos, tecnólogos y nuevos profesionales que buscan ingresar al mercado laboral colombiano.
* **Pregunta Analítica Central:** *¿Por qué haber cursado educación superior en Colombia ya no es garantía de formalidad laboral, y de qué forma la región geográfica y el género condicionan las probabilidades reales de conseguir un empleo digno?*
* **La Gran Idea:**
  > *"En Colombia, más de 6 de cada 10 graduados con educación superior y técnica están atrapados en la informalidad o el rebusque profesional (61.3%). Esta trampa se agrava drásticamente en la periferia del país (llegando al 75.7% en departamentos como Guaviare) y oculta una grave desigualdad de género por el trabajo de cuidado no remunerado. Comprender esta evidencia permite a los jóvenes tomar decisiones laborales estratégicas y exige políticas públicas de formalización productiva real."*

---

## 📁 2. Estructura y Organización del Repositorio

El proyecto articula las tres herramientas exigidas por la rúbrica (**Power BI, Python y R**) y mantiene una estructura limpia con rutas relativas para máxima reproducibilidad:

```text
proyecto 3/
├── PLAN_DE_IMPLEMENTACION.md         # Plan estratégico de trabajo y matriz de responsabilidades
├── GUIA_POWER_BI.md                  # Manual paso a paso para actualización de DAX y diseño en PBI
├── README.md                         # Documentación principal del repositorio (este archivo)
├── LEEME.md                          # Instrucciones rápidas de reproducción y ejecución
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
│   ├── mapa_informalidad_colombia_R.png         # Mapa cartográfico temático coroplético en R
│   └── visualizacion_interactiva_plotly.html    # Explorador interactivo ciudadano autocontenido
├── notebooks/                        # Código reproducible en Python
│   ├── Equipo_Duarte_Jimenez_Proyecto3_Visualizacion.ipynb # Jupyter Notebook oficial completamente ejecutado
│   ├── crear_notebook.py             # Script de construcción programática del Notebook
│   └── generar_figuras.py            # Generador automatizado de gráficos y HTML interactivo
├── scripts_R/                        # Código reproducible en R
│   ├── generar_mapa_colombia.R       # Script de R para procesamiento espacial y renderizado ggplot2
│   └── mapa_informalidad_colombia.Rmd # Documento R Markdown listo para tejer a HTML/PDF
└── documentos/                       # Entregables narrativos y anexos
    ├── Presentacion_Narrativa_10_Diapositivas.md # Storyline y láminas del producto final (Modalidad A)
    ├── Guia_Sustentacion_Proyecto3.md            # Guion cronometrado de 10 min y banco de respuestas
    └── Anexo_IA.md                               # Declaración ética y técnica de uso de IA (máx. 1 pág.)
```

---

## 🛠️ 3. Reproducibilidad y Ejecución Rápida

### A. Ejecución del Módulo Python (Seaborn + Plotly)
Desde una terminal con Python 3.10+:
```bash
# 1. Instalar dependencias si no las tienes
pip install pandas matplotlib seaborn plotly nbconvert

# 2. Generar las figuras y el HTML interactivo
python "proyecto 3/notebooks/generar_figuras.py"

# 3. Ejecutar el Notebook Jupyter de principio a fin
jupyter nbconvert --to notebook --execute --inplace "proyecto 3/notebooks/Equipo_Duarte_Jimenez_Proyecto3_Visualizacion.ipynb"
```

### B. Ejecución del Módulo Espacial en R (`sf` + `ggplot2`)
Desde una terminal con R instalado:
```bash
# Ejecutar el script que genera el mapa en alta resolución
Rscript "proyecto 3/scripts_R/generar_mapa_colombia.R"
```

### C. Actualización de Power BI Desktop
1. Consulta el archivo **`GUIA_POWER_BI.md`**.
2. Abre `Proyecto_Visualizacion.pbix` en Power BI Desktop.
3. Aplica las medidas DAX de promedio mensual (`Promedio Mensual Ocupados` y `Promedio Mensual Informales`).
4. Haz clic en **Publicar** para actualizar el reporte en Power BI Service.

---

## 📊 4. Síntesis de Resultados y Cifras Clave

| Indicador | Valor Nacional | Interpretación para la Ciudadanía |
| :--- | :---: | :--- |
| **Tasa Nacional de Informalidad** | **54.64%** | Más de la mitad de los ocupados en Colombia no cotizan a seguridad social (~9.55M/mes). |
| **Informalidad en Educación Superior** | **61.26%** | **La paradoja:** 6 de cada 10 graduados universitarios están en contratos precarios o por honorarios. |
| **Pico de Informalidad en 2026** | **55.50% (Mayo)** | La precariedad se aceleró en el segundo trimestre (de 52.92% en enero al pico en mayo). |
| **Disparidad Territorial Crítica** | **75.71% (Guaviare)** | La periferia (Guaviare y Casanare al 66.55%) triplica el riesgo frente al centro del país. |
| **Brecha de Género en Ocupados** | **65.3% (H) vs 58.2% (M)** | Menor tasa femenina en ocupados por exclusión previa: millones confinadas al cuidado no remunerado. |

---

## 🤖 5. Transparencia y Declaración de IA
Siguiendo las pautas éticas de la Universidad Externado de Colombia, se declara el uso instrumental de **Google Gemini** para asistencia sintáctica y calibración cromática accesible. Todos los cálculos, modelados e interpretaciones analíticas fueron auditados y redactados exclusivamente por los autores humanos **Julián Steven Duarte** y **Julián Camilo Jiménez**. Consultar detalles en `documentos/Anexo_IA.md`.
