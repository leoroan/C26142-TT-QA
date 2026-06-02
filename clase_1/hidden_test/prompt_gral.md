
# La arquitectura que deberías usar

No pienses:

> “quiero scrapear una página”.

Pensá:

> “quiero construir un pipeline de extracción de datos financieros”.

Eso cambia totalmente cómo se diseña.

---

# La estrategia correcta

## 1. Modelo de datos primero

ANTES de scrapear, definí tu schema.

Por ejemplo:

```python
{
    "id": str,
    "nombre": str,
    "moneda": str,
    "riesgo": str,
    "horizonte": str,
    "categoria": str,
    "variacion_diaria": float,
    "url_detalle": str,
    "fecha_scraping": str,
}
```

Esto es CLAVE.

Porque:

* el HTML cambia,
* tu modelo NO.

Tu scraper solamente traduce HTML → modelo.

---

# 2. Separá responsabilidades

NO hagas todo junto.

La estructura sana es:

```text
scraper/
│
├── fetcher.py
├── parser.py
├── models.py
├── storage.py
├── main.py
└── snapshots/
```

---

## fetcher.py

Solo descarga/renderiza HTML.

Responsabilidad:

* Selenium
* requests
* cookies
* waits
* retries

NO parsea.

---

## parser.py

Transforma HTML → dicts.

Acá vive BeautifulSoup.

NO sabe nada de Selenium.

---

## storage.py

Guarda:

* CSV
* SQLite
* Parquet
* JSON histórico

---

# 3. Selenium SOLO para renderizar

Este punto es MUY importante.

Muchos usan Selenium para parsear todo el DOM.

Error.

La forma profesional es:

```python
driver.get(url)

html = driver.page_source
```

y DESPUÉS:

```python
from bs4 import BeautifulSoup
```

Porque:

* BeautifulSoup es más estable,
* más rápido,
* más mantenible,
* más debuggable.

Selenium solo debería abrir/renderizar.

---

# 4. Parseá por “componentes”

Tu unidad es:

```html
<div class="rounded-tr-xl ... shadow-lg">
```

ESO es un fondo.

No scrapees “la página”.

Scrapeá:

* cards,
* componentes,
* bloques autocontenidos.

---

# 5. No dependas de Tailwind completo

ESTO es MUY importante.

Esto:

```python
div.rounded-tr-xl.rounded-bl-xl.rounded-tl.rounded-br.shadow-lg
```

es frágil.

Tailwind cambia muchísimo.

Mejor:

```python
a[href*='/nuestros-fondos/']
```

y subir al parent.

Ejemplo profesional:

```python
cards = soup.select("a[href*='/nuestros-fondos/']")

for a in cards:
    card = a.find_parent("div", class_="shadow-lg")
```

Eso es mucho más resiliente.

---

# 6. Construí detectores, no selectores

Esto cambia todo.

En vez de:

```python
selector exacto = ...
```

hacé:

```python
if "Variación diaria" in text:
```

o:

```python
row.find("b")
```

o:

```python
href contiene '/nuestros-fondos/'
```

Buscá patrones semánticos.

---

# 7. Guardá históricos SIEMPRE

NO sobrescribas.

Hacé snapshots.

Ejemplo:

```text
data/
├── fondos_2026_06_02.csv
├── fondos_2026_06_03.csv
```

Porque después podés:

* detectar fondos nuevos,
* detectar fondos eliminados,
* hacer análisis temporales,
* ver variaciones históricas.

---

# 8. Detectá nuevos fondos automáticamente

Ejemplo:

```python
ids_actuales = set(...)
ids_nuevos = set(...)

nuevos = ids_nuevos - ids_actuales
```

El `href` te da un ID bastante estable:

```text
/nuestros-fondos/rx6ogk3gkm5m5wbnhsfbbaj0
```

Eso probablemente sea tu PK real.

NO uses el nombre como identificador.

---

# 9. CSV es suficiente al inicio

No compliques con DB todavía.

Usá:

```python
pandas.DataFrame(fondos).to_csv(...)
```

Más adelante:

* SQLite
* DuckDB
* Postgres
* Parquet

---

# 10. Tu scraper debería tolerar fallos parciales

Ejemplo:

```python
try:
    variacion = ...
except:
    variacion = None
```

Porque:

* un fondo puede venir incompleto,
* uno puede cambiar,
* uno puede desaparecer.

No querés perder TODO el scraping por UNA card rota.

---

# Lo más importante de todo

Tu scraper NO debería depender de:

* posiciones exactas,
* clases completas,
* XPath absoluto,
* orden visual.

Debería depender de:

* semántica,
* patrones,
* relaciones,
* anchors estables.

---

# Mi recomendación real para tu caso

## Stack ideal

```text
Selenium
+
BeautifulSoup
+
Pandas
+
CSV snapshots
```

Nada más.

NO Playwright todavía.
NO Scrapy todavía.
NO Kafka.
NO microservicios.
NO overengineering.

---

# Estrategia práctica

## Paso 1

Scrapeá listado de fondos.

## Paso 2

Entrá al detalle de cada fondo.

## Paso 3

Extraé TODAS las métricas.

## Paso 4

Persistí snapshots diarios.

## Paso 5

Compará históricos.

---

# Y esto es MUY importante

Vos NO estás scrapeando “HTML”.

Estás construyendo:

* una fuente de datos financiera alternativa.

Ese cambio mental hace que:

* modeles mejor,
* pienses en evolución,
* tolerancia a cambios,
* persistencia,
* calidad de datos,
* históricos,
* reproducibilidad.
