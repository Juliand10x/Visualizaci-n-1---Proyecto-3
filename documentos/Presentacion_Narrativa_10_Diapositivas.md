# Presentación Narrativa Integrada (10 Diapositivas — Modalidad A)
**Curso:** Visualización I — Universidad Externado de Colombia  
**Docentes:** Adriana Pineda Barón & Paola Moreno  
**Equipo:** Julián Steven Duarte & Julián Camilo Jiménez  
**Audiencia Ciudadana:** Jóvenes egresados, técnicos y nuevos profesionales frente al dilema de la formalización laboral en Colombia  
**Fuente de Datos:** Gran Encuesta Integrada de Hogares (GEIH 2026) — DANE & Cartografía Oficial IGAC  

---

## Diapositiva 1: Portada Institucional y Encuadre
* **Título Principal:** *La Trampa del Título: Radiografía de la Informalidad Laboral en Colombia*
* **Subtítulo:** Una historia basada en datos para jóvenes que ingresan al mercado de trabajo (GEIH 2026)
* **Datos Institucionales:**
  * Universidad Externado de Colombia — Maestría / Especialización en Ciencia de Datos
  * Visualización I · Noviembre 2026
  * **Expositores:** Julián Steven Duarte & Julián Camilo Jiménez
* **Elementos Visuales:** Logotipo de la universidad y banner limpio en azul institucional (`#1E3A8A`) y acento coral (`#E11D48`).
* **Nota del Expositor (30 seg):** *"Durante generaciones en Colombia se nos repitió una promesa: 'Estudie para que tenga un trabajo seguro'. Hoy ponemos la evidencia de la GEIH 2026 sobre la mesa para demostrar por qué esa promesa se rompió y qué decisiones debemos tomar."*

---

## Diapositiva 2: La Audiencia Ciudadana y la Pregunta Central
* **A Quién le Hablamos (Audiencia Delimitada):**
  * Jóvenes de 18 a 28 años, técnicos, tecnólogos y graduados universitarios en búsqueda de empleo digno.
* **La Necesidad de Comprensión:**
  * Comprender por qué los procesos de selección terminan en contratos por prestación de servicios sin cobertura de salud ni pensión, y cómo el territorio y el género condicionan esa realidad.
* **La Pregunta Analítica:**
  > *¿Por qué tener un título universitario o técnico en Colombia ya no es garantía de empleo formal, y de qué forma la región geográfica y el género determinan las probabilidades reales de un trabajo digno?*
* **Elementos Visuales:** Diagrama conceptual que conecta *Audiencia → Pregunta → Evidencia Visual*.

---

## Diapositiva 3: La Gran Idea
* **Frase Central (Focal Point):**
  > **"En Colombia, más de 6 de cada 10 graduados con educación superior están atrapados en la informalidad o el rebusque calificado (61.3%). Esta trampa se agrava drásticamente en la periferia del país (superando el 75%) y oculta una grave brecha de género por el trabajo de cuidado no remunerado."**
* **Los 3 Mensajes Clave para el Ciudadano:**
  1. **La Educación no basta:** 61.3% de informalidad en educación superior frente al 52.4% en primaria.
  2. **El Territorio condiciona:** Vivir en Guaviare o Casanare triplica el riesgo de desprotección frente al centro del país.
  3. **La Trampa de Género:** La menor tasa en mujeres ocupadas esconde una barrera de acceso que confina a millones al hogar sin ingresos propios.
* **Elementos Visuales:** 3 tarjetas KPI con íconos vectoriales contrastados.

---

## Diapositiva 4: Power BI: El Pulso Nacional en Tiempo Real
* **Título de la Lámina:** *Dashboard en Power BI: El Pulso Laboral de Colombia y sus Mejoras Ciudadanas*
* **Mejoras Justificadas del Tablero (Proyecto 1 → Proyecto 3):**
  * **Corrección del Promedio Mensual:** De 105M de personas-mes acumuladas a **~17.5 Millones de ocupados** y **~9.55 Millones de informales** por mes (Tasa idéntica y exacta: **54.64%**).
  * **Lenguaje Ciudadano:** Reemplazo de jerga ministerial por diagnósticos comprensibles para cualquier trabajador.
  * **Trazabilidad:** Tablero publicado y funcional en Power BI Service.
* **Enlace Oficial Power BI:** [Ver Dashboard Interactivo en Power BI Service](https://app.powerbi.com/links/gvbF1pi94p?ctid=3b944d9a-1051-4685-b09d-9a95ee2dbd99&pbi_source=linkShare)
* **Plataforma Web en Producción (Vercel):** [https://webnarrativa.vercel.app](https://webnarrativa.vercel.app)
* **Elementos Visuales:** Captura del dashboard actualizado mostrando las tarjetas KPI y el gráfico de barras por nivel educativo.

---

## Diapositiva 5: Python (Seaborn): La Paradoja de la Educación Superior
* **Título de la Lámina:** *La Paradoja Educativa: Estudiar Más Ya No Protege de la Informalidad*
* **Gráfico Insertado:** `figuras/fig1_paradoja_educativa_seaborn.png`
* **Hallazgos Clave:**
  * **Educación Superior:** Registra una tasa de informalidad del **61.3%** (~22.2M ponderados en el semestre).
  * **Secundaria / Media:** **61.1%** de informalidad.
  * **Primaria Básica:** **52.4%** de informalidad.
* **La Razón Económica (En Sencillo):** Las empresas colombianas no generan suficientes vacantes de nómina formal; los profesionales son contratados bajo la modalidad de "prestación de servicios", asumiendo de su propio bolsillo la salud y la pensión o evadiéndola por falta de ingresos.

---

## Diapositiva 6: Python (Seaborn): La Brecha Oculta de Género
* **Título de la Lámina:** *La Brecha Oculta de Género: Desigualdad en la Ocupación y Cuidado No Remunerado*
* **Gráfico Insertado:** `figuras/fig2_brecha_genero_educacion_seaborn.png`
* **Hallazgos Clave:**
  * En Educación Superior, los hombres ocupados tienen una tasa de informalidad del **65.3%**, frente al **58.2%** en mujeres ocupadas (brecha de 7.1 puntos).
* **Interpretación Humana:**
  * ¿Tienen las mujeres mejores empleos? **¡No!**
  * La diferencia radica en que millones de mujeres colombianas sufren una **barrera de entrada previa**: al no contar con redes de apoyo para el cuidado de niños y adultos mayores, se ven forzadas a permanecer en el hogar sin ingresos propios. Quienes logran trabajar están en sectores asalariados calificados (educación/salud), mientras los hombres salen al rebusque informal de emergencia.

---

## Diapositiva 7: Python (Plotly): Explorador Interactivo Departamental
* **Título de la Lámina:** *Explorador Interactivo: Consulta la Realidad Laboral de tu Departamento*
* **Componente:** `figuras/visualizacion_interactiva_plotly.html` (Mini-dashboard interactivo)
* **Semáforo de Riesgo Ciudadano:**
  * 🔴 **Alerta Crítica (> 60%):** Guaviare (75.7%), Casanare (66.5%), Bogotá D.C. (64.1%), Cundinamarca (62.3%), Nariño (62.1%).
  * 🟡 **Vulnerabilidad Media (50% - 60%):** Tolima (59.2%), Antioquia (56.1%), Valle del Cauca (55.4%).
  * 🔵 **Mayor Formalidad Relativa (< 50%):** Boyacá (49.8%), Putumayo (38.1%).
* **Interacción en Vivo:** Demostración en la sustentación pasando el cursor sobre el departamento y verificando volumen ponderado e informalidad.

---

## Diapositiva 8: R Geoespacial: Mapa Cartográfico de Colombia
* **Título de la Lámina:** *Radiografía Territorial en R: La Desprotección en la Periferia Colombiana*
* **Gráfico Insertado:** `figuras/mapa_informalidad_colombia_R.png`
* **Rigor Cartográfico:**
  * Fuente oficial DANE / IGAC (EPSG:9377 - Origen Nacional).
  * Gradiente perceptualmente continuo (`#2B5C8F` formal a `#900C3F` crítico).
  * Anotación directa en regiones de alta alerta (Guaviare: 75.7%, Casanare: 66.5%).
* **Mensaje Territorial:** La probabilidad de que un joven profesional consiga un contrato formal en la Orinoquía o Amazonía es casi nula; la informalidad en estas regiones supera el 75%.

---

## Diapositiva 9: Mensaje Final y Estrategias para el Ciudadano
* **Título de la Lámina:** *¿Qué Hacemos con Esta Información? Estrategias de Empleabilidad Ciudadana*
* **Para los Jóvenes que Buscan Empleo:**
  1. **Exigir y Negociar Seguridad Social:** Si el contrato es por prestación de servicios, calcular siempre la retención del 40% para salud y pensión al negociar honorarios para no trabajar desprotegido.
  2. **Aprovechar el Teletrabajo y Movilidad:** Si resides en regiones con informalidad crítica (> 65%), postúlate a esquemas remotos basados en Bogotá, Medellín o el exterior.
  3. **Demanda Colectiva de Políticas Públicas:** El país no necesita más subsidios asistenciales ciegos; necesita incentivos tributarios para empresas que contraten indefinidamente a jóvenes egresados.
* **Cierre Contundente:** *"El conocimiento de los datos es la mejor herramienta para romper la inercia de la precariedad laboral."*

---

## Diapositiva 10: Fuentes, Limitaciones y Declaración de IA
* **Fuentes Oficiales:**
  * DANE — Gran Encuesta Integrada de Hogares (GEIH 2026, primer semestre: Enero a Junio). Muestra expandida con factor `FEX_C18`.
  * IGAC — Marco Geoestadístico Nacional (Cartografía oficial departamental).
* **Limitaciones del Análisis:**
  * Datos descriptivos: no se infieren relaciones de causa-efecto ni evaluación de reformas laborales posteriores.
  * Cobertura territorial validada a nivel departamental conforme a los dominios de representatividad estadística del DANE.
* **Declaración de Uso de IA:**
  * Uso asistencial de Google Gemini para optimización sintáctica de código en Python/R y diseño de paleta contrastada. Todo el análisis, cálculo y redacción fue auditado y validado humanamente por Julián Steven Duarte y Julián Camilo Jiménez.
