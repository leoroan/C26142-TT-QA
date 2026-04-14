# Ejercicio Práctico Obligatorio

# Objetivos:

* Construir la vista estática de la calculadora (HTML \+ CSS externo).  
* Etiquetar cada campo con identificadores estables (`id`, `name`, clases semánticas).  
* Practicar DevTools: inspeccionar elementos, copiar selectores y comprobar que apunten a unívocos.  
* Crear `selectors.md` — tu futura hoja de ruta para los tests UI.

# Entregables y Estructura de Carpetas

Clase05/

│  index.html        ← estructura HTML 100 % estática

│  estilos.css       ← hoja de estilos externa

│  selectors.md      ← tabla de selectores (Markdown)

└─ README.md         ← breve guía de ejecución y verificación

# Ejercicio Práctico: Pasos Iniciales

1. **Crea un archivo `index.html`** con la estructura mínima de una página web (incluyendo la referencia a `estilos.css`).  
2. **Hoja de estilos:**  
   * Agregá un archivo `estilos.css` con estilos básicos (reset, colores, clases utilitarias, etc.). Podés usar una plantilla base o una que hayas trabajado previamente.  
3. **Abrir con DevTools:**  
   * Desde el navegador, presioná `Ctrl + O` y abrí el archivo `index.html`.  
   * Luego, usá `F12` o clic derecho → `Inspeccionar` para acceder a las DevTools.

# Ejercicio Práctico: Verificación y Documentación

4. **Verificación de controles:**  
   * Inspeccioná cada `input`, botón o campo del formulario de la calculadora (por ejemplo, los campos para ingresar números y los botones de operaciones).  
   * Asegurate de que cada uno tenga un atributo `id` único.  
   * Si un elemento no tiene `id`, agregalo y guardá los cambios en `index.html`.  
5. **Test rápido de selectores CSS:**  
   * Copiá el selector CSS de cada elemento (idealmente usando el `id`).  
   * Probalo en la **Consola** del navegador con este comando, reemplazando el selector:document.querySelector('\#id-del-elemento').style.border \= '2px solid red';  
   * Si el borde se pinta de rojo, el selector es correcto y unívoco.  
6. **Documentación**  
   * Crea el archivo `selectors.md` y documenta los selectores que has verificado en el paso 5\. Utiliza una tabla para organizar la información.

## Tabla de Selectores

| Elemento | ID del Elemento | Selector CSS Verificado | Propósito |
| :---- | :---- | :---- | :---- |
| Campo de entrada (Número 1\) | `num1` | `#num1` | Ingreso del primer operando |
| Campo de entrada (Número 2\) | `num2` | `#num2` | Ingreso del segundo operando |
| Botón de Suma | `btn-sumar` | `#btn-sumar` | Realizar la operación de suma |
| Botón de Resta | `btn-restar` | `#btn-restar` | Realizar la operación de resta |
| Botón de Multiplicación | `btn-multiplicar` | `#btn-multiplicar` | Realizar la operación de multiplicación |
| Botón de División | `btn-dividir` | `#btn-dividir` | Realizar la operación de división |
| Campo de Resultado | `resultado` | `#resultado` | Mostrar el resultado |
| ... | ... | ... | ... |
