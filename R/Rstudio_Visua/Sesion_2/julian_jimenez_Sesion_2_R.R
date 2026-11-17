library(sf)
library(dplyr)
library(ggplot2)
library(leaflet)
library(tmap)
library(readxl)
setwd(".")
dir()
base_tematica = read_excel("Base_General.xlsx")
base_tematica$ind_rur = base_tematica$pobl_rur/base_tematica$pobl_tot
base_tematica$densidad = base_tematica$pobl_tot /base_tematica$areaoficialkm2
base_tematica = base_tematica %>%
  mutate(region = case_when(
    gandina == 1 ~ "Region Andina",
    gcaribe == 1 ~ "Region Caribe",
    gpacifica == 1 ~ "Region Pacifica",
    gorinoquia == 1 ~ "Región Orinoquía",
    gamazonia == 1 ~ "Región Amazonía",
    TRUE ~ "Ninguna"  # Si ninguna de las dummies es 1
  ))
georef = st_read("./Shapes_Municipios", "MGN_MPIO_POLITICO")
st_crs(georef)
st_crs(georef)$datum
st_crs(georef)$epsg
georef_9377 <- st_transform(georef, crs = 9377)
st_bbox(georef_9377)
georef_9377[["MPIO_CDPMP"]] = as.numeric(georef_9377[["MPIO_CDPMP"]])
bf_sf = merge(georef_9377, base_tematica, by.x="MPIO_CDPMP", by.y="codmun")
class(bf_sf)
bf_sp = as_Spatial(bf_sf)
class(bf_sp)
st_write(bf_sf, dsn= "Base_Final", layer = "Municipios_General", driver = "ESRI Shapefile",encoding = "UTF-8")
bf_sf <- bf_sf %>%
  mutate(
    area_m2  = as.numeric(st_area(.)),          # Área en m² (numérica)
    area_ha  = area_m2 / 10000,                 # 1 ha = 10,000 m²
    area_km2 = area_m2 / 1000000                # 1 km² = 1,000,000 m²
  )
head(bf_sf %>% select(area_m2, area_ha, area_km2))
bf_sf <- bf_sf %>%
  mutate(
    perimetro_m  = as.numeric(st_length(st_boundary(.))), # Perímetro en metros
    perimetro_km = perimetro_m / 1000                     # Perímetro en kilómetros
  )
head(bf_sf %>% select(perimetro_m, perimetro_km))
centroides_mun <- st_centroid(bf_sf, of_largest_polygon = TRUE)
coords_centroides <- st_coordinates(centroides_mun)
bf_sf <- bf_sf %>%
  mutate(
    centroide_x = coords_centroides[, 1], # Coordenada Este (X)
    centroide_y = coords_centroides[, 2]  # Coordenada Norte (Y)
  )
#View(bf_sf)


#Mapas con ggplot

ggplot(data = bf_sf) +
  geom_sf()
ggplot(data = bf_sf) +
  geom_sf(fill = "#CAFF70", color = "#556B2F")
orinoquia_sf = subset(bf_sf, region == "Región Orinoquía", na.rm = TRUE)
ggplot(data = orinoquia_sf) +
  geom_sf(data = , fill = "#FF00FF", color = "#8B1C62") +
  labs(
    title = "Muncipios de la Región Orinoquía en Colombia",
    subtitle = "Delimitación oficial sobre mapa base municipal (EPSG:9377 - Origen Nacional)",
    caption = "Fuente: Cartografía oficial (IGAC / DANE)"
  )
ggplot(data = orinoquia_sf) +
  geom_sf(fill = "#FF4500", color = "#8B2500") +
  labs(
    title = "División Político-Administrativa de Colombia",
    subtitle = "Mapa base municipal (EPSG:9377 - Origen Nacional)",
    caption = "Fuente: IGAC/DANE"
  ) +
  theme(
    plot.title = element_text(face = "bold", size = 18,  color = "#8B814C"),
    plot.subtitle = element_text(size = 12, color = "#8B5742"),
    panel.grid.major = element_line(color = "#333333", linetype = "dashed")
  )
ggplot(data = bf_sf) +
  geom_sf(aes(fill = region), color = "#333333", size = 0.15) +
  scale_fill_brewer(palette = "Set3", name = "Región") +
  labs(
    title = "División Político-Administrativa de Colombia por Regiones",
    caption = "Fuente: IGAC / DANE"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(face = "bold", size = 14, color = "#005528"),
    legend.position = "right"
  )
install.packages("cols4all", dependencies = TRUE)
install.packages("shinyjs")
cols4all::c4a_gui()
library("colorspace")
hcl_palettes(plot = TRUE)
tmap_mode("plot")
tm_shape(orinoquia_sf) +
  tm_polygons(col = "Tipologia_Coca",title = "Tipología Cocalera"
  )
tm_shape(orinoquia_sf) +
  tm_polygons(col = "Tipologia_Coca",title = "Tipología Cocalera"
  )
tm_shape(orinoquia_sf) +
  tm_polygons(
    col = "Tipologia_Coca",
    title = "Tipología Cocalera",
    palette = "bold", # Paleta personalizada
    border.col = "white",
    lwd = 0.4
  )
tm_shape(orinoquia_sf) +
  tm_polygons(
    col = "Tipologia_Coca",
    title = "Tipología Cocalera",
    palette = "tara", # Paleta personalizada
    border.col = "black",
    lwd = 0.4
  ) +
  tm_layout(
    main.title = "Tipología Cocalera en la Región Orinoquía",
    main.title.size = 1.0,
    legend.outside = TRUE,
    legend.outside.position = "right",
    frame = FALSE
  )
colores_tipologia <- c(
  "Sin Coca"   = "#68838B", # Gris claro
  "Coca No Asperjados" = "#CD8162", # Naranja
  "Coca Asperjados"  = "#3CB371"  # Rojo
)
tmap_mode("plot")

tm_shape(orinoquia_sf) +
  tm_polygons(
    fill = "Tipologia_Coca",
    fill.scale = tm_scale_categorical(values = colores_tipologia),
    fill.legend = tm_legend(title = "Tipología Cocalera"),
    col = "white",
    lwd = 0.4
  ) +
  tm_title(
    text = "Tipología Cocalera en la Región Orinoquía",
    size = 1.1
  ) +
  # En v4 es tm_scalebar (sin el guión bajo)
  tm_scalebar(
    position = c("left", "bottom"),
    text.size = 0.6
  ) +
  # Flecha de norte
  tm_compass(
    type = "arrow",
    position = c("left", "top"),
    size = 1.2
  ) +
  # Créditos / Fuente
  tm_credits(
    text = "Fuente: Elaboración propia a partir de Cartografía oficial (IGAC) y datos socioeconómicos (DANE)",
    position = c("right", "bottom"),
    size = 0.5
  ) +
  tm_options(frame = FALSE)
tmap_mode("view")
tm_shape(orinoquia_sf) +
  tm_polygons(
    col = "Tipologia_Coca",
    title = "Tipología Cocalera",
    palette = colores_tipologia, # Paleta personalizada
    border.col = "white",
    lwd = 0.4
  ) +
  #Titulo y subtitulo
  tm_layout(
    main.title = "Tipología Cocalera en la Región Orinoquía",
    main.title.size = 1.1,
    sub.title = "Clasificación de presencia territorial por municipio",
    sub.title.size = 0.8,
    legend.outside = TRUE,
    legend.outside.position = "right",
    frame = FALSE
  ) +
  # Nota 
  tm_credits(
    text = "Fuente: Elaboración propia a partir de Cartografía oficial (IGAC) y datos socioeconómicos (DANE)",
    position = c("right", "bottom"),
    size = 0.6 +
      tm_basemap(c("OpenStreetMap", "Esri.WorldImagery"))
  )
tm_shape(orinoquia_sf) + 
  
  tm_fill("ind_rur", palette = "magma", title = "Índice de Ruralidad") + 
  
  tm_borders(alpha = 0.2) + 
  
  # tm_compass() y tm_scalebar() se omiten en modo interactivo porque Leaflet ya los maneja de forma nativa
  
  tm_text("MPIO_CNMBR", size = 0.5, col = "grey60") + 
  
  tm_layout(legend.text.size = 0.6, 
            
            legend.title.size = 0.6, 
            
            legend.position = c("right", "bottom"), 
            
            frame = FALSE) +
  
  tm_basemap(c("OpenStreetMap", "Esri.WorldImagery"))
tm_shape(orinoquia_sf) +
  tm_polygons(
    col = "IPM.nacional",
    title = "Índice de Pobreza Multidimensional",
    palette = "bold",
    style = "quantile", # Clasificación por Cuantiles para la clase
    border.col = "white",
    lwd = 0.5
  )
