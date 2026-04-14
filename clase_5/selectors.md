# Selectores de la vista estática de la calculadora

## IDs
- `#calculadora-titulo`: Encabezado principal de la calculadora.
- `#display`: Campo de texto que muestra el valor actual en la pantalla.
- `#btn-limpiar`: Botón para limpiar la pantalla.
- `#btn-borrar`: Botón para borrar el último carácter.
- `#btn-dividir`: Botón de la operación división.
- `#btn-multiplicar`: Botón de la operación multiplicación.
- `#btn-7`, `#btn-8`, `#btn-9`, `#btn-4`, `#btn-5`, `#btn-6`, `#btn-1`, `#btn-2`, `#btn-3`, `#btn-0`: Botones numéricos.
- `#btn-restar`: Botón de la operación resta.
- `#btn-sumar`: Botón de la operación suma.
- `#btn-igual`: Botón de resultado.
- `#btn-punto`: Botón para ingresar el punto decimal.

## Names
- `name="display"`: Nombre estable del campo de pantalla.
- `name="btn_limpiar"`, `name="btn_borrar"`, `name="btn_dividir"`, `name="btn_multiplicar"`, `name="btn_restar"`, `name="btn_sumar"`, `name="btn_igual"`, `name="btn_punto"`, `name="btn_0"` ... `name="btn_9"`: Nombres estables para cada botón.

## Clases
- `.page`: Contenedor principal de la página.
- `.page__content`: Caja centralizada que contiene el contenido principal.
- `.calculadora`: Tarjeta principal de la calculadora.
- `.calculadora__titulo`: Título principal de la calculadora.
- `.calculadora__descripcion`: Texto de descripción debajo del título.
- `.calculadora__display-wrapper`: Contenedor de la pantalla de la calculadora.
- `.calculadora__display`: Estilo del campo de salida.
- `.calculadora__grid`: Grid que organiza los botones en filas y columnas.
- `.boton`: Estilo base para todos los botones.
- `.boton--numero`: Variación de botón numérico.
- `.boton--operador`: Variación de botón para operadores.
- `.boton--igual`: Variación de botón para el igual.
- `.boton--ancho`: Botón ancho que ocupa dos columnas (`0`).
- `.texto-center`: Clase utilitaria para centrar texto.
- `.oculto`: Clase utilitaria para ocultar visualmente un elemento.
- `.sr-only`: Clase utilitaria para contenido accesible solo para lectores de pantalla.

## Notas
- Se usa `id` para referenciar elementos clave de la interfaz y conservar identificadores estables.
- Se usan `name` en botones para mejorar la consistencia de campos en formularios o pruebas.
- Las clases siguen una convención semántica basada en componentes y variaciones visuales.