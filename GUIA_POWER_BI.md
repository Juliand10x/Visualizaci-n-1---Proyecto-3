# Guía de Actualización y Optimización de Power BI Desktop
**Proyecto 3: Narrativa Visual Integrada — Visualización 1**  
**Universidad Externado de Colombia**  
**Docentes:** Adriana Pineda Barón & Paola Moreno  
**Autores:** Julián Steven Duarte & Julián Camilo Jiménez  

---

## 1. Objetivo de la Actualización en Power BI

Para el Proyecto 1, el tablero estuvo diseñado para un rol técnico-directivo del Ministerio del Trabajo. Para el **Proyecto 3**, la rúbrica exige:
1. **Actualización justificada de medidas DAX**: Resolver la confusión de la suma semestral (105M ocupados y 57.3M informales) incorporando el **Promedio Mensual Ponderado** (~17.5M ocupados y ~9.55M informales).
2. **Revisión de modelado e integridad**: Mantener el esquema de relaciones y garantizar que los filtros cruzados funcionen sin ambigüedades.
3. **Adaptación comunicativa a la ciudadanía**: Títulos explicativos, eliminación de sobrecarga visual (*chartjunk*), lenguaje empático y claro para jóvenes y nuevos trabajadores.
4. **Publicación en Power BI Service**: Obtener el enlace público o institucional activo para la entrega y sustentación.

---

## 2. Medidas DAX a Crear / Modificar (Paso a Paso)

Abre `Proyecto_Visualizacion.pbix` en **Power BI Desktop**. Ve a la tabla **`_Medidas`** en el panel lateral derecho (*Datos*).

### Medida 1: Promedio Mensual de Ocupados (Nueva - Recomendada)
> **Propósito:** En lugar de mostrar 105 millones acumulados en el semestre, calcula el promedio mensual real de colombianos ocupados (~17.48 millones).

Haz clic derecho en la tabla `_Medidas` → **Nueva medida**:
```dax
Promedio Mensual Ocupados = 
AVERAGEX(
    VALUES( DimFecha[Mes] ),
    [Total Ocupados]
)
```
*Formato:* Número entero con separador de miles (ej. `17,478,144`) o mostrar unidades en Millones (`17.48 M`).

---

### Medida 2: Promedio Mensual de Informales (Nueva - Recomendada)
> **Propósito:** Calcula el promedio mensual real de trabajadores en condición informal (~9.55 millones).

Haz clic derecho en `_Medidas` → **Nueva medida**:
```dax
Promedio Mensual Informales = 
AVERAGEX(
    VALUES( DimFecha[Mes] ),
    [Total Informales]
)
```
*Formato:* Número entero con separador de miles o mostrar unidades en Millones (`9.55 M`).

---

### Medida 3: Tasa de Informalidad Promedio (Validación)
> **Propósito:** Confirma que la tasa consolidada se mantenga en el **54.64%** exacto.

Haz clic derecho en `_Medidas` → **Nueva medida**:
```dax
Tasa Informalidad PBI = 
DIVIDE( [Total Informales], [Total Ocupados], 0 )
```
*Formato:* Porcentaje con dos decimales (`54.64%`).

---

### Medida 4: Tasa de Informalidad en Jóvenes (15-28 años)
> **Propósito:** Métrica clave para la audiencia ciudadana joven.
```dax
Tasa Informalidad Jóvenes = 
CALCULATE(
    [Tasa Informalidad PBI],
    DimPersonas[RangoEdad] = "Jóvenes (15-28)"
)
```
*Formato:* Porcentaje con dos decimales (`41.07%`).

---

### Medida 5: Tarjeta Dinámica de Diagnóstico Ciudadano (Opcional - Valor Agregado)
> **Propósito:** Generar un texto interpretativo automático según el departamento seleccionado.
```dax
Diagnóstico Ciudadano = 
VAR TasaActual = [Tasa Informalidad PBI]
VAR Depto = SELECTEDVALUE( DimPersonas[Nombre_Departamento], "Nivel Nacional" )
RETURN
    IF(
        ISBLANK(Depto) || Depto = "Nivel Nacional",
        "En Colombia, 55 de cada 100 trabajadores no cuentan con seguridad social ni contrato formal.",
        IF(
            TasaActual > 0.60,
            "Alerta Crítica en " & Depto & ": " & FORMAT(TasaActual, "0.0%") & " de informalidad. Zona de alta vulnerabilidad para jóvenes.",
            "En " & Depto & " la informalidad es de " & FORMAT(TasaActual, "0.0%") & ", cercana al promedio del país."
        )
    )
```

---

## 3. Ajustes de Diseño Visual en las Páginas

### Página 1: "Nacional y Brechas"
1. **Tarjetas KPI Superiores:**
   * Cambiar el campo de la tarjeta de *Total Ocupados* por **`[Promedio Mensual Ocupados]`** (etiqueta: *"Ocupados Promedio / Mes"* $\approx 17.5\text{ M}$).
   * Cambiar la tarjeta de *Total Informales* por **`[Promedio Mensual Informales]`** (etiqueta: *"Informales Promedio / Mes"* $\approx 9.55\text{ M}$).
   * Mantener la tarjeta central: **`[Tasa Informalidad]`** ($54.64\%$) en color destacado.
   * Mantener la tarjeta: **`[Tasa Informalidad Jóvenes]`** ($41.07\%$).
2. **Gráfico de Líneas Temporal (Enero - Junio):**
   * Verificar que el eje X ordene cronológicamente los meses (Enero a Junio).
   * Título sugerido: *"Trayectoria Mensual: La informalidad escaló de 52.9% a 55.5% en mayo"*.
3. **Gráfico de Barras por Nivel Educativo:**
   * Título sugerido: *"La Paradoja: 6 de cada 10 graduados de educación superior están en la informalidad"*.
   * Ordenar las barras de mayor a menor tasa de informalidad.

### Página 2: "Focalización Territorial"
1. **Gráfico de Barras Departamental:**
   * Resaltar con color rojo/terracota (`#E74C3C`) las barras críticas de **Guaviare (75.7%)** y **Casanare (66.5%)**, y en azul neutro (`#1F4E79`) el resto.
   * Título sugerido: *"Disparidad Regional: La periferia sufre niveles de informalidad de hasta el 75.7%"*.
2. **Slicer Departamental:**
   * Asegurar que tenga opción de búsqueda rápida para que la audiencia o las docentes puedan interactuar fluidamente durante la sustentación.

---

## 4. Pasos para Guardar y Publicar en Power BI Service

1. En Power BI Desktop, haz clic en **Guardar** (`Ctrl + S`).
2. Haz clic en el botón superior **Publicar** (pestaña *Inicio*).
3. Selecciona tu área de trabajo (ej. *Mi área de trabajo* o la carpeta de la universidad).
4. Espera a que termine la publicación y haz clic en el enlace web que aparece.
5. En el navegador (Power BI Service):
   * Ve a **Archivo → Insertar informe → Publicar en la web (público)** (o compartir vínculo con la organización según permisos de la universidad).
   * Copia el enlace URL generado.
6. Pega ese enlace en el archivo `NOTAS_ENTREGA_Y_ENLACES.txt` y en la lámina 4 de la presentación.

---

## 5. Respuestas Rápidas para Preguntas Técnicas de la Docente

* **¿Por qué cambiaron la tarjeta de 105M a 17.5M?**  
  *"Porque 105M correspondía a la masa laboral semestral acumulada (personas-mes sumadas). Para una audiencia ciudadana no especializada, el dato comprensible e intuitivo es el promedio mensual de trabajadores (~17.5 millones de personas ocupadas y ~9.55 millones en informalidad). La tasa del 54.64% se mantiene idéntica y matemáticamente exacta."*
* **¿Qué papel cumple `USERELATIONSHIP` en el modelo?**  
  *"Permite activar la relación temporal inactiva entre la dimensión calendario (`DimFecha`) y la tabla de fuerza de trabajo sin generar ambigüedades con otras fechas del modelo."*
