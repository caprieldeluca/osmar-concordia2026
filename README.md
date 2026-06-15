# osmar-concordia2026

Soporte de datos a actividades de mapeo de OpenStreetMap Argentina, en Concordia 2026.

Extracción automática de segmentos y nodos de interpolación, a partir de números de puerta y calles de la [IDE](https://ide.concordia.gob.ar/visualizador/?zoom=11&lat=-31.35&lng=-58.05&layers=argenmap,sig_calles2022).

## Desafíos MapRoulette

### Interpolaciones válidas

Estos desafíos contienen los segmentos que superaron varias pruebas de validación, son para agregar o revisar cómo los tenemos en el mapa.

#### Sectores Norte y Sur

Norte y Sur son alrededores con muy pocas interpolaciones cargadas, así que son principalmente tareas de agregar.

- Sector Norte (205 tareas): https://maproulette.org/browse/challenges/55377
- Sector Sur (176 tareas): https://maproulette.org/browse/challenges/55389

#### Sector Centro

Centro lo tenemos bastante completo, así que la mayoría son para revisar.

- Sector Centro (3865 tareas): https://maproulette.org/browse/challenges/55537

#### Soporte de datos

GeoJSON ([RFC7946](https://datatracker.ietf.org/doc/html/rfc7946)) crudo, con los objetos para agregar como capa de datos en los editores.

- [objetosNorte.geojon](https://raw.githubusercontent.com/caprieldeluca/osmar-concordia2026/refs/heads/main/objetosNorte.geojson)
- [objetosSur.geojon](https://raw.githubusercontent.com/caprieldeluca/osmar-concordia2026/refs/heads/main/objetosSur.geojson)
- [objetosCentro.geojon](https://raw.githubusercontent.com/caprieldeluca/osmar-concordia2026/refs/heads/main/objetosCentro.geojson)

Tienen geometrías LineString y Point, por lo que otras aplicaciones SIG quizás no puedan convertirlos a sus propios modelos de datos.

#### Notas

Eliminar atributo `idTarea` antes de subir cambios.
