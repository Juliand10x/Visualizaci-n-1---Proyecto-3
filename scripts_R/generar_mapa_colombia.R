# ==============================================================================
# PROYECTO 3: NARRATIVA VISUAL INTEGRADA — VISUALIZACIÓN I
# UNIVERSIDAD EXTERNADO DE COLOMBIA
# Autores: Julián Steven Duarte & Julián Camilo Jiménez
# Script de R: Mapa Temático Cartográfico (sf, tmap y ggplot2)
# Metodología alineada con Sesión 2 y Sesión 3 de Mapas Coropléticos
# ==============================================================================

suppressPackageStartupMessages({
  library(sf)
  library(dplyr)
  library(ggplot2)
  library(tmap)
  library(classInt)
  library(scales)
})

cat(">>> 1. Cargando datos de informalidad GEIH 2026 y capa departamental...\n")
if (file.exists("proyecto 3/Datos/colombia_departamentos.geojson")) {
  base_dir <- "proyecto 3"
} else if (file.exists("../Datos/colombia_departamentos.geojson")) {
  base_dir <- ".."
} else {
  base_dir <- "."
}

geojson_path <- file.path(base_dir, "Datos/colombia_departamentos.geojson")
csv_path <- file.path(base_dir, "Datos/geih_2026_departamentos.csv")

dptos_sf <- st_read(geojson_path, quiet = TRUE)
df_geih <- read.csv(csv_path, encoding = "UTF-8", stringsAsFactors = FALSE)

# Homologación oficial DANE
nombre_map <- c(
  "Amazonas" = "AMAZONAS", "Antioquia" = "ANTIOQUIA", "Arauca" = "ARAUCA",
  "Atlántico" = "ATLÁNTICO", "Bogotá D.C." = "BOGOTÁ, D.C.", "Bolívar" = "BOLÍVAR",
  "Boyacá" = "BOYACÁ", "Caldas" = "CALDAS", "Caquetá" = "CAQUETÁ", "Casanare" = "CASANARE",
  "Cauca" = "CAUCA", "Cesar" = "CESAR", "Chocó" = "CHOCÓ", "Córdoba" = "CÓRDOBA",
  "Cundinamarca" = "CUNDINAMARCA", "Guainía" = "GUAINÍA", "Guaviare" = "GUAVIARE",
  "Huila" = "HUILA", "La Guajira" = "LA GUAJIRA", "Magdalena" = "MAGDALENA", "Meta" = "META",
  "Nariño" = "NARIÑO", "Norte de Santander" = "NORTE DE SANTANDER", "Putumayo" = "PUTUMAYO",
  "Quindío" = "QUINDIO", "Risaralda" = "RISARALDA",
  "San Andrés" = "ARCHIPIÉLAGO DE SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA",
  "Santander" = "SANTANDER", "Sucre" = "SUCRE", "Tolima" = "TOLIMA",
  "Valle del Cauca" = "VALLE DEL CAUCA", "Vaupés" = "VAUPÉS", "Vichada" = "VICHADA"
)
df_geih$DPTO_CN <- nombre_map[df_geih$Nombre_Departamento]

# Unión espacial con datos de la GEIH
mapa_datos <- dptos_sf %>%
  left_join(df_geih, by = "DPTO_CN")

cat(">>> 2. Clasificación estadística por intervalos (classInt - Jenks / Natural Breaks)...\n")
# Algoritmo Jenks visto en Sesión 3 de clase
cortes_jenks <- classIntervals(mapa_datos$Tasa_Informalidad, n = 5, style = "jenks")
mapa_datos <- mapa_datos %>%
  mutate(
    Rango_Jenks = cut(
      Tasa_Informalidad,
      breaks = cortes_jenks$brks,
      include.lowest = TRUE,
      dig.lab = 3
    )
  )

cat(">>> 3. Generando mapa cartográfico con tmap (estilo Sesión 3)...\n")
tmap_mode("plot")

mapa_tmap <- tm_shape(mapa_datos) +
  tm_polygons(
    col = "Tasa_Informalidad",
    title = "Tasa Informalidad (%)",
    palette = "YlOrRd",
    style = "jenks",
    n = 5,
    border.col = "white",
    lwd = 0.5
  ) +
  tm_layout(
    main.title = "Colombia: Brecha Territorial de Informalidad Laboral (2026)",
    main.title.size = 1.05,
    sub.title = "Clasificación Natural Breaks (Jenks) a partir de microdatos GEIH - DANE",
    sub.title.size = 0.75,
    legend.outside = TRUE,
    legend.outside.position = "right",
    frame = FALSE,
    bg.color = "#F8F9FA"
  ) +
  tm_scalebar(
    position = c("left", "bottom"),
    text.size = 0.6
  ) +
  tm_compass(
    type = "arrow",
    position = c("left", "top"),
    size = 1.2
  ) +
  tm_credits(
    text = "Fuente: DANE (GEIH 2026) y cartografía oficial IGAC. Elaboración propia.",
    position = c("left", "bottom"),
    size = 0.55
  )

tmap_out <- file.path(base_dir, "figuras/mapa_informalidad_tmap.png")
tmap_save(mapa_tmap, filename = tmap_out, width = 8, height = 9, dpi = 300)
cat("✓ Mapa tmap guardado en:", tmap_out, "\n")

cat(">>> 4. Generando mapa temático con ggplot2 (anotaciones directas y semántica WCAG)...\n")
deptos_destacados <- c("GUAVIARE", "CASANARE", "BOGOTÁ, D.C.", "NARIÑO")
labels_data <- mapa_datos %>%
  filter(DPTO_CN %in% deptos_destacados) %>%
  st_centroid()

coords <- st_coordinates(labels_data)
labels_data$X <- coords[, 1]
labels_data$Y <- coords[, 2]
labels_data$LabelTexto <- paste0(labels_data$Nombre_Departamento, "\n", round(labels_data$Tasa_Informalidad, 1), "%")

p_ggplot <- ggplot(data = mapa_datos) +
  geom_sf(aes(fill = Tasa_Informalidad), color = "#FFFFFF", size = 0.3) +
  scale_fill_gradientn(
    colors = c("#2B5C8F", "#4A90E2", "#F5A623", "#D0021B", "#900C3F"),
    values = rescale(c(38, 50, 55, 65, 76)),
    name = "Tasa de\nInformalidad (%)",
    labels = function(x) paste0(round(x, 0), "%"),
    guide = guide_colorbar(
      barwidth = 1.2,
      barheight = 10,
      title.position = "top",
      ticks.colour = "white"
    )
  ) +
  geom_label(
    data = labels_data,
    aes(x = X, y = Y, label = LabelTexto),
    size = 3.2,
    fontface = "bold",
    color = "#1E293B",
    fill = alpha("#FFFFFF", 0.85),
    label.padding = unit(0.2, "lines"),
    linewidth = 0.3
  ) +
  labs(
    title = "Colombia: Brecha Territorial de la Informalidad Laboral (2026)",
    subtitle = "Tasa de informalidad por departamento (%) — La periferia enfrenta hasta un 75.7% de desprotección",
    caption = "Fuente: Elaboración propia a partir de microdatos GEIH 2026 (DANE) y cartografía oficial IGAC (EPSG:9377)."
  ) +
  theme_void() +
  theme(
    plot.background = element_rect(fill = "#F8F9FA", color = NA),
    panel.background = element_rect(fill = "#F8F9FA", color = NA),
    plot.title = element_text(face = "bold", size = 14, color = "#1E293B", hjust = 0, margin = margin(t = 10, b = 4)),
    plot.subtitle = element_text(size = 10.5, color = "#475569", hjust = 0, margin = margin(b = 15)),
    plot.caption = element_text(size = 8.5, color = "#64748B", hjust = 0, margin = margin(t = 15, b = 10)),
    legend.position = "right",
    legend.title = element_text(face = "bold", size = 9.5, color = "#1E293B"),
    legend.text = element_text(size = 8.5, color = "#334155"),
    plot.margin = margin(15, 20, 15, 20)
  )

ggplot_out <- file.path(base_dir, "figuras/mapa_informalidad_colombia_R.png")
ggsave(ggplot_out, plot = p_ggplot, width = 8, height = 10, dpi = 300)
cat("✓ Mapa ggplot2 guardado en:", ggplot_out, "\n")
cat("¡Módulo espacial ejecutado con éxito total!\n")
