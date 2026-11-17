# GUÍA DE ESTUDIO Y SUSTENTACIÓN ORAL — PROYECTO 3
**Visualización 1 • Universidad Externado de Colombia**  
**Docentes:** Adriana Pineda Barón & Paola Moreno  
**Equipo:** Julián Steven Duarte & Julián Camilo Jiménez  
**Tiempo Límite:** 10 minutos (5 min exposición + 5 min interacción / preguntas de la docente)

---

## 🧭 ¿De qué se trata nuestro proyecto en 30 segundos?
Nuestro proyecto traduce los datos estadísticos de la **GEIH 2026 (DANE)** a una **narrativa ciudadana** dirigida a **jóvenes (18-28 años)** y graduados universitarios en Colombia.  
* **La Gran Idea:** *"En Colombia, más de 6 de cada 10 graduados de educación superior están atrapados en la informalidad o el rebusque calificado (61.3%). Esta trampa se agrava drásticamente en la periferia (75.7% en Guaviare) y oculta una grave desigualdad de género por las tareas de cuidado no remuneradas."*

---

## ⏱️ Distribución del Tiempo en la Sustentación (10 Minutos)

```text
[0:00 - 1:00] ── 1. Problema, Audiencia Delimitada y Pregunta Central
[1:00 - 3:00] ── 2. Contexto de los Datos (GEIH DANE) y La Gran Idea
[3:00 - 8:00] ── 3. Desarrollo de la Historia Visual (Power BI + Python + R + Web Vercel)
[8:00 - 10:00] ─ 4. Síntesis, Limitaciones Éticas y Mensaje Ciudadano Final
```

---

## 👥 Reparto de Roles y Qué Dice Cada Uno

### 🎙️ Bloque 1: Introducción y La Gran Idea (Min 0 a 3) — Julián Duarte
* **Qué decir:**
  1. *"Buenas tardes profesoras. Nuestro trabajo está diseñado para un público específico: los jóvenes colombianos de 18 a 28 años y nuevos graduados que salen al mercado laboral esperando estabilidad."*
  2. *"Planteamos la pregunta central: ¿Por qué cursar educación superior en Colombia ya no garantiza un empleo formal con seguridad social, y cómo la geografía y el género determinan esas probabilidades?"*
  3. *"Presentamos La Gran Idea: No es falta de estudio; la estructura del mercado laboral colombiano atrapa al 61.3% de los graduados en la informalidad, cifra que se dispara al 75.7% en la periferia."*

---

### 🎙️ Bloque 2: Demostración de Herramientas y Visualizaciones (Min 3 a 8) — Julián Jiménez & Julián Duarte

#### A. Power BI (Julián Duarte)
* **Qué mostrar:** Abrir el enlace publicado [Power BI Service](https://app.powerbi.com/links/gvbF1pi94p?ctid=3b944d9a-1051-4685-b09d-9a95ee2dbd99&pbi_source=linkShare).
* **Defensa Técnica ante las Docentes:**
  * *"En el Proyecto 1 teníamos la base consolidada con 105M de personas-mes acumuladas. Para este Proyecto 3, justificamos la continuidad del DAX original porque calcula con precisión la **Tasa de Informalidad oficial ponderada en 54.64%** y la tasa focalizada en jóvenes."*
  * *"La página 1 ('Nacional y Brechas') muestra la visión macro por nivel educativo y género, y la página 2 ('Focalización Territorial') permite filtrar dinámicamente cada departamento."*

#### B. Python: Seaborn y Plotly (Julián Jiménez)
* **Qué mostrar:** Navegar en [https://webnarrativa.vercel.app](https://webnarrativa.vercel.app) o mostrar el Jupyter Notebook.
* **Defensa Técnica ante las Docentes:**
  * **Gráfico 1 (Seaborn - Barras Horizontales):** *"Muestra la paradoja educativa: la tasa de informalidad de educación superior (61.3%) supera a la educación técnica e intermedia. No es un error de muestreo, refleja la precarización y el rebusque profesional (prestación de servicios sin cotización)."*
  * **Gráfico 2 (Seaborn - Gráfico Dumbbell):** *"Compara la brecha hombre-mujer por nivel educativo con una paleta accesible y honesta (sin truncar ejes)."*
  * **Gráfico 3 (Plotly Interactivo):** *"El semáforo departamental permite que cualquier ciudadano identifique si su región está en zona crítica (>60%), media o baja frente al 54.64% nacional."*

#### C. R: Mapas Coropléticos con `sf` y `tmap` (Julián Jiménez)
* **Qué mostrar:** Los mapas cartográficos en la web o en RStudio (`scripts_R/mapa_informalidad_colombia.Rmd`).
* **Defensa Técnica ante las Docentes:**
  * *"En R aplicamos exactamente la metodología de la **Sesión 3** de clase: uniones espaciales con el paquete `sf`, capa oficial GeoJSON de IGAC/DANE y clasificación por intervalos naturales de **Jenks (`classInt`)** en 5 categorías."*
  * *"El mapa tiene rosa de los vientos, escala métrica y créditos. Demuestra la desconexión espacial: la región central andina retiene el empleo formal, mientras la Orinoquía, Amazonía y Pacífico superan el 70% de informalidad."*

---

### 🎙️ Bloque 3: Cierre, Ética y Limitaciones (Min 8 a 10) — Julián Duarte & Julián Jiménez
* **Qué decir:**
  * **Limitación estadística:** *"La GEIH tiene representatividad a nivel departamental y de áreas metropolitanas, pero no permite inferencias válidas a nivel municipal pequeño; por eso nos ceñimos a los 33 departamentos oficiales."*
  * **Advertencia ética:** *"No realizamos inferencias causales de políticas públicas a partir de análisis descriptivos. Los datos describen disparidades estructurales, no culpabilidades individuales."*
  * **Mensaje ciudadano final:** *"La educación sigue siendo valiosa, pero sin políticas de formalización productiva regional, el título universitario no elimina la vulnerabilidad social."*

---

## ❓ Banco de Preguntas Probables de las Docentes (y Cómo Responder)

1. **¿Por qué conservaron las medidas DAX de la primera entrega de Power BI?**
   * *Respuesta:* *"Porque el modelo relacional tipo estrella (`Fact Table` con `DimPersonas` y `DimFecha`) y las medidas de razón calculadas con `DIVIDE([Total Informales], [Total Ocupados])` garantizan que el factor de expansión (FEX) calcule la tasa de informalidad con exactitud matemática (54.64%) en cualquier nivel de filtro o agregación."*

2. **¿Por qué la tasa de educación superior es más alta en algunos gráficos que el promedio?**
   * *Respuesta:* *"Porque en las zonas urbanas y de servicios, una gran cantidad de técnicos y profesionales jóvenes trabajan como independientes, contratistas por prestación de servicios o en plataformas digitales sin cotizar continuamente al sistema general de pensiones y salud (definición DANE de informalidad)."*

3. **¿Por qué usaron Jenks (Natural Breaks) en el mapa de R en lugar de cuantiles o intervalos iguales?**
   * *Respuesta:* *"Siguiendo la Sesión 3 de clase, Jenks minimiza la varianza interna de cada grupo y maximiza la diferencia entre grupos, lo cual es ideal para variables con asimetría territorial como la informalidad laboral en Colombia."*

4. **¿Cómo desplegaron la web en Vercel y qué ventaja tiene sobre Streamlit?**
   * *Respuesta:* *"Desplegamos una arquitectura estática optimizada en Vercel con CDN global instantáneo. Streamlit requiere un servidor Python activo que se suspende por inactividad; nuestra solución en Vercel carga en milisegundos, embebe el gráfico nativo de Plotly exportado desde Python y conecta directamente con el Power BI Service."*
