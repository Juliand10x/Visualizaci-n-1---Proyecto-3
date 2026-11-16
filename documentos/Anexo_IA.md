# Anexo Técnico de Uso de Inteligencia Artificial
**Asignatura:** Visualización I — Universidad Externado de Colombia  
**Docentes:** Adriana Pineda Barón & Paola Moreno  
**Equipo:** Julián Steven Duarte & Julián Camilo Jiménez  
**Proyecto:** Proyecto 3 — Narrativa Visual Integrada  
**Fecha:** Noviembre de 2026  

---

## 1. Declaración de Transparencia y Responsabilidad Ética

En cumplimiento de los lineamientos éticos y formativos de la Universidad Externado de Colombia y de la guía docente de la asignatura *Visualización I*, los integrantes del equipo declaramos haber utilizado herramientas de Inteligencia Artificial Generativa bajo un rol **estrictamente instrumental y de asistencia técnica**. 

Reafirmamos que **la responsabilidad intelectual, analítica y metodológica de todos los hallazgos, interpretaciones narrativas, cálculos matemáticos y decisiones de diseño visual recae exclusivamente en los autores humanos**.

---

## 2. Herramientas Utilizadas y Propósito Específico

| Herramienta | Propósito de Uso | Alcance y Límites |
| :--- | :--- | :--- |
| **Google Gemini (Antigravity Assistant)** | Asistencia en la estructuración de scripts de código en Python (Seaborn / Plotly) y R (`sf` / `ggplot2`). | Se utilizó para la automatización de la lectura de metadatos, optimización sintáctica de funciones gráficas y verificación de contrastes cromáticos WCAG AA. |
| **Power BI / DAX Optimizer** | Formulación de la medida `AVERAGEX` para el cálculo del promedio mensual ponderado. | Asistencia en el diseño de la expresión DAX para corregir la suma acumulada de personas-mes sin alterar la integridad del modelo. |

---

## 3. Prompts Relevantes Empleados

1. **Sobre Paleta Cromática y Accesibilidad Visual:**
   > *"Sugiere una paleta cromática semántica accesible (compatible con daltonismo y contraste WCAG AA) para representar tasas de informalidad laboral en Colombia, diferenciando el empleo formal en azul neutro (#2563EB) y reservando tonos coral/vino (#E11D48 / #900C3F) exclusivamente para zonas y niveles educativos en alerta crítica."*
2. **Sobre Optimización de Disolución Geoespacial en R:**
   > *"¿Cómo disolver eficientemente con la biblioteca `sf` en R un shapefile municipal de 1,122 polígonos hacia los 33 departamentos de Colombia utilizando `group_by(DPTO_CN)` y `st_union()`, conservando la topología y simplificando con `st_simplify()` para generar un GeoJSON ligero?"*
3. **Sobre Medidas DAX de Promedio Mensual:**
   > *"En Power BI, dado que el factor de expansión de la GEIH es mensual y el dataset contiene 6 meses consolidados, ¿cuál es la mejor formulación DAX usando `AVERAGEX` y `VALUES(DimFecha[Mes])` para reportar ocupados e informales promedio mensuales en lugar del acumulado semestral?"*

---

## 4. Revisión Crítica y Auditoría Humana

Todas las sugerencias proporcionadas por los modelos de IA fueron sometidas a una rigurosa auditoría por parte de los autores:
* **Auditoría Matemática:** Se validó manualmente que la tasa ponderada nacional ($54.64\%$), la tasa en educación superior ($61.26\%$) y las tasas departamentales (Guaviare al $75.71\%$, Casanare al $66.55\%$, Bogotá al $64.08\%$) coincidieran con exactitud decimal entre Power BI, Python y R.
* **Control de Alucinaciones:** Se verificó que los códigos no inventaran nombres de columnas en los microdatos de la GEIH ni forzaran relaciones espaciales inexistentes.
* **Tono Narrativo y Enfoque Ciudadano:** El discurso, las metáforas explicativas y las recomendaciones de política pública fueron redactadas con criterio propio, adaptándolas a la realidad de los jóvenes colombianos sin sesgos algorítmicos.
