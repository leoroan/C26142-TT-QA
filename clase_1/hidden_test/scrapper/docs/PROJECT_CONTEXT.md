# Proyecto: Pipeline de Extracción de Fondos Comunes de Inversión (FCI)

## Objetivo del proyecto

Construir un pipeline robusto de extracción y persistencia de datos financieros provenientes del sitio Provincia Fondos.

El objetivo NO es simplemente scrapear HTML.

El objetivo es construir una fuente de datos financiera estructurada, histórica y tolerante a cambios del frontend.

---

# Filosofía del proyecto

El scraper debe depender de:

* semántica,
* patrones estables,
* estructura lógica,
* relaciones entre componentes.

Y NO de:

* clases Tailwind completas,
* posiciones exactas,
* XPath absolutos,
* estructura visual frágil.

---

# Stack tecnológico

## Renderizado

* Selenium
* ChromeDriver

Uso exclusivo:

* renderizar páginas dinámicas,
* esperar contenido,
* obtener `page_source`.

Selenium NO debe utilizarse para parsear.

---

## Parsing

* BeautifulSoup

Responsabilidad:

* transformar HTML → modelos Python.

---

## Persistencia

* Pandas
* CSV snapshots

Actualmente NO se utiliza base de datos.

---

# Arquitectura actual

```text
scrapper/
│
├── fetcher.py
├── parsers/
│   ├── parser.py
│   ├── parser_detalle.py
│   ├── parser_pdf.py
│   └── parser_cuotapartes.py
│
├── models.py
├── storage.py
├── utils.py
├── main.py
│
└── snapshots/
    ├── list/
    ├── detail/
    ├── pdf/
    └── cuotapartes/
```

---

# Responsabilidad de cada módulo

## fetcher.py

Responsable de:

* requests HTTP,
* Selenium,
* waits,
* descarga de PDFs,
* obtención de HTML renderizado.

NO parsea contenido.

---

## parser.py

Parsea:

* listado principal de fondos.

Transforma:

* HTML → Fondo.

---

## parser_detalle.py

Parsea:

* página detalle del fondo.

Transforma:

* HTML → FondoDetalle
* HTML → Tenencias

---

## parser_pdf.py

Extrae:

* texto del factsheet PDF.

NO debe contener lógica financiera todavía.

Solo:

* PDF → texto limpio.

---

## parser_cuotapartes.py

Parsea:

* tabla histórica de valores de cuotaparte.

Transforma:

* HTML → registros históricos diarios.

---

## storage.py

Responsable exclusivo de:

* guardar CSV,
* persistir snapshots.

NO parsea.

---

# Estrategia de snapshots

Todos los outputs deben versionarse con timestamp.

Nunca sobrescribir información histórica.

Ejemplo:

```text
fondos_20260603_183103.csv
```

Esto permite:

* auditoría,
* debugging,
* evolución histórica,
* comparación temporal.

---

# Identificadores

El identificador estable del fondo es:

```text
/nuestros-fondos/rx6ogk3gkm5m5wbnhsfbbaj0
```

NO usar el nombre como primary key.

El nombre puede cambiar.

---

# Información realmente importante

## Alta prioridad

### Página detalle

* nombre
* descripción
* categoría
* horizonte
* riesgo
* patrimonio
* volatilidad
* rendimientos
* composición
* tenencias

---

### Factsheet PDF

Es la principal fuente semántica.

Contiene:

* benchmark,
* honorarios,
* composición,
* perfil,
* clasificación,
* métricas históricas,
* información cualitativa.

Solo interesa:

* factsheet PDF.

NO interesan:

* reglamentos,
* calificaciones,
* rendimiento diario PDF.

---

### Histórico de cuotapartes

Fuente crítica para:

* series temporales,
* análisis históricos,
* cálculo de retornos,
* volatilidad futura.

Debe persistirse como dataset histórico.

---

# Estrategia de extracción

## Regla principal

Buscar:

* labels,
* texto semántico,
* anchors estables,
* patrones repetibles.

Evitar:

* selectores Tailwind largos,
* dependencia visual.

---

# Estado actual del proyecto

Implementado:

* listado de fondos,
* detalle de fondos,
* snapshots HTML,
* snapshots CSV,
* descarga de factsheets,
* extracción texto PDF,
* scraping de cuotapartes.

Pendiente:

* estructurar parser semántico del factsheet,
* normalización de métricas,
* datasets históricos consolidados,
* comparación temporal,
* detección de cambios.

---

# Objetivo futuro

Convertir el pipeline en una fuente de datos financieros reutilizable para:

* análisis,
* reporting,
* alertas,
* dashboards,
* backtesting,
* monitoreo de fondos.
