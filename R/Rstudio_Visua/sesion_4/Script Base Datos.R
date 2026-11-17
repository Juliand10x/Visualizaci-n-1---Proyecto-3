library(tidyverse)
library(writexl)
library(dplyr)
library(sf)

setwd(".")
getwd()

##################################
########DATA TEMÁTICA#############
##################################

ruta_rds <- "E:/Biblioteca/0_Centro_Datos_APA/CDA_03_TABOGO/B_EncuestaMultiproposito/A_2025/Microdatos en R variables adicionales/20261022_variables_adicionales_rds/20261022_Variables_Adicionales.rds"

var_ad <- readRDS(ruta_rds)

names(var_ad)

class(var_ad)

# Apagar notación científica en la consola de RStudio
options(scipen = 999)

# Conservar únicamente localidad, fex_cal y variables N_/n_
var_ad_subconjunto <- var_ad %>%
  select(localidad, fex_cal, matches("^[Nn]_"))

# Inspeccionar resumen de fex_cal
summary(var_ad_subconjunto$fex_cal)

df_tematico <- var_ad_subconjunto %>%
  group_by(localidad) %>%
  summarise(
    Total_Encuestados = n(),
    
    # Calcula el % poblacional (0 a 100%) para todas las indicadoras N_ / n_
    across(
      .cols = matches("^[Nn]_") & !matches("N_ingpcugaj13"),
      .fns  = ~ weighted.mean(.x, w = fex_cal, na.rm = TRUE) * 100
    ),
    
    # Ingreso per cápita promedio ponderado en pesos ($)
    across(
      .cols = matches("N_ingpcugaj13"),
      .fns  = ~ weighted.mean(.x, w = fex_cal, na.rm = TRUE)
    ),
    
    .groups = "drop"
  )

df_tematico <- df_tematico %>%
  # Eliminar las observaciones que contienen la palabra "RURAL" (sin importar mayúsculas/minúsculas)
  filter(!str_detect(localidad, "(?i)RURAL")) %>%
  # Crear las dos nuevas variables a partir de 'localidad'
  mutate(
    localidad = str_trim(str_replace_all(localidad, "_", "")),
    num_localidad    = str_extract(localidad, "^\\d+"),             # Extrae el código numérico inicial (ej. "05")
    nombre_localidad = str_trim(str_remove(localidad, "^\\d+"))     # Extrae únicamente el texto (ej. "USME")
  )


# Eliminar la variable 'localidad' original y renombrar 'nombre_localidad' como 'localidad'
df_tematico <- df_tematico %>%
  select(-localidad) %>%
  rename(localidad = nombre_localidad)

df_tematico <- df_tematico %>%
  relocate(localidad, .before = 1)

# Exportar el dataframe 'df_tematico'
write_xlsx(df_tematico, path = "df_tematico.xlsx")


###########################################
###############Data Espacial###############
###########################################
rm(list = ls())

library(tidyverse)
library(writexl)
library(dplyr)
library(sf)

setwd(".")
getwd()
options(scipen = 999)

# Definir la ruta al archivo Shapefile
ruta_localidades <- "Localidades/LocalidadesBogota.shp"

# Importar la capa espacial de localidades
localidades_bogota <- st_read(ruta_localidades)

# Inspeccionar las primeras filas y verificar el Sistema de Referencia de Coordenadas (CRS)
st_crs(localidades_bogota)

localidades_bogota <- localidades_bogota %>%
  rename(localidad = NOMBRE_COM)

glimpse(localidades_bogota)

####################################
####################################
####POWER BI ARREGLO####
####################################
####################################


# Extraer las coordenadas del centroide de cada localidad (Longitud X y Latitud Y)
centroides <- st_centroid(localidades_bogota)
coords <- st_coordinates(centroides)

# Incorporar Latitud, Longitud y texto WKT, removiendo la columna de geometría sf
df_espacial <- localidades_bogota %>%
  mutate(
    longitud = coords[, 1],
    latitud  = coords[, 2],
    wkt_geom = st_as_text(geometry)
  )
  
class(df_espacial)

#######################
#Crear archivo geojson
#######################
st_write(localidades_bogota, "LocalidadesBogota.geojson", driver = "GeoJSON")


#######################
#Crear archivo .csv
#######################

df_powerbi <- df_espacial %>%
  mutate(wkt_geom = st_as_text(geometry)) %>%
  st_drop_geometry()

write.table(
  x = df_powerbi, 
  file = "localidades_wkt.csv", 
  sep = ";", 
  dec = ",", 
  row.names = FALSE, 
  fileEncoding = "UTF-8"
)
