# LEEME — Instrucciones de Reproducción y Configuración
**Proyecto 3: Narrativa Visual Integrada — Visualización I**  
**Universidad Externado de Colombia**  
**Equipo:** Julián Steven Duarte & Julián Camilo Jiménez  

---

Este archivo describe paso a paso cómo reproducir de forma 100% autónoma todos los entregables del Proyecto 3 (Python, R y Power BI).

## 1. Requisitos y Dependencias del Sistema

### Python (Versión 3.10 o superior)
Asegúrate de contar con las siguientes librerías instaladas:
```bash
pip install pandas numpy matplotlib seaborn plotly nbconvert
```

### R (Versión 4.2 o superior)
Asegúrate de contar con los paquetes espaciales y gráficos:
```r
install.packages(c("sf", "dplyr", "ggplot2", "scales"))
```

### Power BI Desktop
* Versión reciente de Power BI Desktop (Windows).
* Cuenta institucional o personal para publicación en Power BI Service.

---

## 2. Pasos de Reproducción Inmediata

### Paso 1: Reproducir el Módulo Python
Abre una terminal en la raíz de la carpeta `proyecto 3` y ejecuta:
```bash
# Generar todas las figuras estáticas y el componente HTML interactivo
python notebooks/generar_figuras.py

# Ejecutar el Jupyter Notebook completo
jupyter nbconvert --to notebook --execute --inplace notebooks/Equipo_Duarte_Jimenez_Proyecto3_Visualizacion.ipynb
```
* **Salida esperada:** Se actualizarán las figuras en `figuras/` y el archivo `visualizacion_interactiva_plotly.html`.

### Paso 2: Reproducir el Módulo R
Ejecuta el script en R desde la terminal:
```bash
Rscript scripts_R/generar_mapa_colombia.R
```
* O abre `scripts_R/mapa_informalidad_colombia.Rmd` en RStudio y haz clic en **Knit**.
* **Salida esperada:** Se generará el mapa en alta resolución `figuras/mapa_informalidad_colombia_R.png`.

### Paso 3: Actualizar Power BI
* Sigue las instrucciones paso a paso detalladas en **`GUIA_POWER_BI.md`**.
* Abre el archivo `.pbix` en Power BI Desktop, crea las medidas de promedio mensual y publica en tu área de trabajo de Power BI Service.

---

## 3. Matriz de Entregables Oficiales

1. **Dashboard en Power BI:** Archivo `.pbix` actualizado y enlace activo en Power BI Service.
2. **Notebook de Jupyter:** `notebooks/Equipo_Duarte_Jimenez_Proyecto3_Visualizacion.ipynb` completamente ejecutado.
3. **Archivo Interactivo HTML:** `figuras/visualizacion_interactiva_plotly.html`.
4. **Script y Mapa de R:** `scripts_R/mapa_informalidad_colombia.Rmd` y `figuras/mapa_informalidad_colombia_R.png`.
5. **Presentación Narrativa (10 Slides):** `documentos/Presentacion_Narrativa_10_Diapositivas.md` (exportable a PDF).
6. **Guía de Sustentación Oral:** `documentos/Guia_Sustentacion_Proyecto3.md`.
7. **Anexo Técnico de IA:** `documentos/Anexo_IA.md`.
