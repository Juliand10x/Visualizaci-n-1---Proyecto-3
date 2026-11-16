# ==============================================================================
# PROYECTO 3: NARRATIVA VISUAL INTEGRADA — VISUALIZACIÓN I
# UNIVERSIDAD EXTERNADO DE COLOMBIA
# Autores: Julián Steven Duarte & Julián Camilo Jiménez
# Script de R: Mapa Temático Cartográfico de Informalidad Departamental (GEIH 2026)
# ==============================================================================

suppressPackageStartupMessages({
  library(sf)
  library(dplyr)
  library(ggplot2)
  library(scales)
})

cat(">>> 1. Cargando datos de informalidad GEIH 2026...\n")
csv_path <- "proyecto 3/Datos/geih_2026_departamentos.csv"
df_geih <- read.csv(csv_path, encoding = "UTF-8", stringsAsFactors = FALSE)

# Diccionario de homologación de nombres GEIH -> Shapefile oficial DANE
nombre_map <- c(
  "Amazonas" = "AMAZONAS",
  "Antioquia" = "ANTIOQUIA",
  "Arauca" = "ARAUCA",
  "Atlántico" = "ATLÁNTICO",
  "Bogotá D.C." = "BOGOTÁ, D.C.",
  "Bolívar" = "BOLÍVAR",
  "Boyacá" = "BOYACÁ",
  "Caldas" = "CALDAS",
  "Caquetá" = "CAQUETÁ",
  "Casanare" = "CASANARE",
  "Cauca" = "CAUCA",
  "Cesar" = "CESAR",
  "Chocó" = "CHOCÓ",
  "Córdoba" = "CÓRDOBA",
  "Cundinamarca" = "CUNDINAMARCA",
  "Guainía" = "GUAINÍA",
  "Guaviare" = "GUAVIARE",
  "Huila" = "HUILA",
  "La Guajira" = "LA GUAJIRA",
  "Magdalena" = "MAGDALENA",
  "Meta" = "META",
  "Nariño" = "NARIÑO",
  "Norte de Santander" = "NORTE DE SANTANDER",
  "Putumayo" = "PUTUMAYO",
  "Quindío" = "QUINDIO",
  "Risaralda" = "RISARALDA",
  "San Andrés" = "ARCHIPIÉLAGO DE SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA",
  "Santander" = "SANTANDER",
  "Sucre" = "SUCRE",
  "Tolima" = "TOLIMA",
  "Valle del Cauca" = "VALLE DEL CAUCA",
  "Vaupés" = "VAUPÉS",
  "Vichada" = "VICHADA"
)

df_geih$DPTO_CN <- nombre_map[df_geih$Nombre_Departamento]

cat(">>> 2. Cargando shapefile base municipal y disolviendo por departamento...\n")
shp_path <- "C:/Users/sduar/Documents/Universidad/visualizacion 1/Mapas_Sesion3/Base_Final/Municipios_General.shp"
shp_muni <- st_read(shp_path, quiet = TRUE)

# Disolver a nivel departamental
dptos_sf <- shp_muni %>%
  group_by(DPTO_CN) %>%
  summarise(geometry = st_union(geometry), .groups = "drop")

# Simplificar ligeramente geometrías para optimizar peso y visualización
dptos_sf <- st_simplify(dptos_sf, preserveTopology = TRUE, dTolerance = 1000)

cat(">>> 3. Exportando GeoJSON departamental para portabilidad...\n")
st_write(dptos_sf, "proyecto 3/Datos/colombia_departamentos.geojson", delete_dsn = TRUE, quiet = TRUE)

cat(">>> 4. Uniendo datos socioeconómicos de informalidad con la capa geográfica...\n")
mapa_datos <- dptos_sf %>%
  left_join(df_geih, by = "DPTO_CN")

# Identificar departamentos clave para anotaciones directas
deptos_destacados <- c("GUAVIARE", "CASANARE", "BOGOTÁ, D.C.", "NARIÑO")
labels_data <- mapa_datos %>%
  filter(DPTO_CN %in% deptos_destacados) %>%
  st_centroid()

coords <- st_coordinates(labels_data)
labels_data$X <- coords[, 1]
labels_data$Y <- coords[, 2]
labels_data$LabelTexto <- paste0(labels_data$Nombre_Departamento, "\n", round(labels_data$Tasa_Informalidad, 1), "%")

cat(">>> 5. Construyendo mapa temático cartográfico con ggplot2...\n")
p <- ggplot(data = mapa_datos) +
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
    color = "#1A252C",
    fill = alpha("#FFFFFF", 0.85),
    label.padding = unit(0.2, "lines"),
    label.size = 0.3
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
    plot.title = element_text(face = "bold", size = 15, color = "#1E293B", hjust = 0, margin = margin(t = 10, b = 4)),
    plot.subtitle = element_text(size = 11, color = "#475569", hjust = 0, margin = margin(b = 15)),
    plot.caption = element_text(size = 8.5, color = "#64748B", hjust = 0, margin = margin(t = 15, b = 10)),
    legend.position = "right",
    legend.title = element_text(face = "bold", size = 9.5, color = "#1E293B"),
    legend.text = element_text(size = 8.5, color = "#334155"),
    plot.margin = margin(15, 20, 15, 20)
  )

cat(">>> 6. Guardando imagen en alta resolución (300 DPI)...\n")
ggsave("proyecto 3/figuras/mapa_informalidad_colombia_R.png", plot = p, width = 8, height = 10, dpi = 300)
cat("¡Mapa generado con éxito en proyecto 3/figuras/mapa_informalidad_colombia_R.png!\n")
