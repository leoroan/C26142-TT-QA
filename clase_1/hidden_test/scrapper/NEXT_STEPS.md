# Próximos pasos

## Objetivo actual

Construir un pipeline completo de extracción de datos financieros de fondos comunes de inversión.

El sistema debe poder detectar automáticamente:

* fondos actuales,
* nuevos fondos futuros,
* cambios en los datos publicados.

Y persistir snapshots históricos reutilizables.

---

# Prioridad alta

## 1. Consolidar scraping completo de cada fondo

Para cada fondo obtener:

### Listado principal

* id
* nombre
* categoría
* moneda
* riesgo
* horizonte
* variación
* url detalle

---

### Página detalle

* descripción
* patrimonio
* volatilidad
* rendimientos
* composición
* tenencias
* métricas visibles

---

### Factsheet PDF

Extraer:

* texto completo
* métricas financieras
* benchmark
* honorarios
* clasificación
* perfil inversor
* composición
* rendimiento histórico

Persistir:

* PDF original
* TXT parseado

---

### Cuotapartes

Obtener:

* histórico de valores diarios
* valor cuotaparte
* fecha
* clase

Por defecto:

* últimos ~20 días provistos por la página.

Opcional futuro:

* filtros fecha_desde / fecha_hasta.

---

# Prioridad alta

## 2. Persistencia consistente

Generar snapshots históricos:

* HTML
* CSV
* TXT
* PDF

Nunca sobrescribir.

Todo debe versionarse por timestamp.

---

# Prioridad alta

## 3. Normalización de datasets

Construir CSVs consistentes para:

* fondos
* detalles
* tenencias
* factsheets
* cuotapartes

Objetivo:
poder analizar la información como datasets financieros reales.

---

# Prioridad media

## 4. Detección automática de cambios

Detectar:

* fondos nuevos
* fondos eliminados
* cambios en métricas
* cambios en composición
* cambios en rendimientos

---

# Prioridad media

## 5. Consolidación histórica

Poder responder:

* evolución patrimonial
* evolución cuotaparte
* evolución rendimientos
* evolución composición

---

# Prioridad baja

## 6. Migración de persistencia

Futuro:

* SQLite
* DuckDB
* Postgres
* Parquet

CSV sigue siendo suficiente actualmente.

---

# Objetivo final

Construir una fuente de datos financiera histórica y reutilizable para:

* análisis financiero,
* observación de rendimiento,
* monitoreo de fondos,
* comparaciones históricas,
* dashboards,
* futuros modelos analíticos.
