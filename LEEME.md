# LEEME — Instrucciones de Reproducción y Relación de Entregables
**Proyecto 3: Narrativa Visual Integrada — Visualización I**  
**Universidad Externado de Colombia**  
**Equipo:** Julián Steven Duarte & Julián Camilo Jiménez  
**Docentes:** Adriana Pineda Barón & Paola Moreno  
**Fecha de Entrega:** 17 de noviembre de 2026  

---

## 1. Enlaces Oficiales de Consulta en Vivo

* **Dashboard en Power BI Service (Entregable 1):**  
  https://app.powerbi.com/links/gvbF1pi94p?ctid=3b944d9a-1051-4685-b09d-9a95ee2dbd99&pbi_source=linkShare
* **Experiencia Digital Web en Producción (Entregable 4 - Modalidad B):**  
  https://webnarrativa.vercel.app

---

## 2. Relación de Entregables Obligatorios (Conforme al Numeral 7 del PDF)

1. **Dashboard en Power BI:**
   * Archivo local: `Equipo_Duarte_Jimenez_Proyecto3_Dashboard.pbix`
   * Enlace funcional en la nube arriba indicado.
2. **Notebook de Python (Seaborn y Plotly):**
   * Notebook con código comentado y salidas ejecutadas: `notebooks/Equipo_Duarte_Jimenez_Proyecto3_Visualizacion.ipynb`
   * Archivo interactivo exportado: `figuras/visualizacion_interactiva_plotly.html`
3. **Módulo Geoespacial en R:**
   * Documento R Markdown: `scripts_R/mapa_informalidad_colombia.Rmd`
   * Script reproducible: `scripts_R/generar_mapa_colombia.R`
   * Mapas temáticos exportados (300 DPI): `figuras/mapa_informalidad_colombia_R.png` y `figuras/mapa_informalidad_tmap.png`
   * Capa cartográfica oficial necesaria: `Datos/colombia_departamentos.geojson`
4. **Producto Narrativo Final:**
   * **Modalidad A:** Presentación PDF de diez diapositivas: `documentos/Equipo_Duarte_Jimenez_Proyecto3_Presentacion.pdf`
   * **Modalidad B:** Plataforma web en producción https://webnarrativa.vercel.app y archivos fuente en `web_narrativa/`
5. **Carpeta Organizada con Datos y Rutas Relativas:**
   * Tablas maestras de la GEIH 2026 en la carpeta `Datos/`
   * Rutas relativas configuradas para ejecución autónoma.
6. **Anexo Técnico de Uso de IA:**
   * Documento en PDF (1 página exacta): `documentos/Equipo_Duarte_Jimenez_Proyecto3_Anexo_IA.pdf`
7. **Fuentes, Definiciones y Limitaciones:**
   * Descritas en la sección 4 de este documento y en la lámina 10 de la presentación.

---

## 3. Pasos de Reproducción Rápida

### Python (Versión 3.10+)
Dependencias requeridas: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `nbconvert`.
```bash
# 1. Regenerar figuras estáticas y HTML interactivo
python notebooks/generar_figuras.py

# 2. Ejecutar el Notebook completo
jupyter nbconvert --to notebook --execute --inplace notebooks/Equipo_Duarte_Jimenez_Proyecto3_Visualizacion.ipynb
```

### R (Versión 4.2+)
Paquetes requeridos: `sf`, `dplyr`, `ggplot2`, `tmap`, `classInt`, `scales`.
```bash
# Ejecutar script que procesa el GeoJSON y renderiza los mapas
Rscript scripts_R/generar_mapa_colombia.R
```

---

## 4. Fuentes, Definiciones y Limitaciones Metodológicas (Entregable 7)

* **Fuentes Oficiales:**
  * Gran Encuesta Integrada de Hogares (GEIH 2026) — DANE. Muestra probabilística expandida con factor de ponderación `FEX_C18` del Censo 2018.
  * Marco Geoestadístico Nacional — IGAC / DANE (EPSG:9377 - Origen Nacional).
* **Definición Operativa de Informalidad:**
  * Se acoge la metodología oficial DANE / OIT basada en no cotización al Sistema General de Seguridad Social en Salud y Pensiones, así como el tamaño del establecimiento laboral.
* **Limitaciones del Análisis:**
  * Cobertura territorial validada a nivel departamental conforme a los dominios estadísticos de la encuesta; no se realizan inferencias a nivel municipal no cubierto.
  * Los resultados son de carácter estrictamente descriptivo de las condiciones de empleo; no se infieren causas unívocas ni efectos de reformas legislativas sin modelos contrafactuales.
