# 🧪 Selectores CSS y XPath - Análisis Completo Swag Labs

## 📋 Resumen

Este proyecto contiene un análisis exhaustivo de selectores CSS y XPath para los campos de entrada y botón de login de la aplicación **Swag Labs**.

Archivos incluidos:
1. **clase_6.py** - Análisis Python de selectores
2. **selectores-talento.md** - Documentación detallada con tablas
3. **test-masivo.js** - Script para validar todos los selectores
4. **colores-demo.js** - Demo visual cambiando colores de fondo
5. **selector-testing.html** - Interfaz interactiva completa

---

## 🎯 Selectores Recomendados

### CSS Selectors
| Elemento | Selector | Tipo |
|----------|----------|------|
| Usuario | `#user-name` | ID (primario) |
| Usuario (alt) | `input[data-test="username"]` | data-test |
| Contraseña | `#password` | ID (primario) |
| Contraseña (alt) | `input[data-test="password"]` | data-test |
| Botón Login | `[data-test="login-button"]` | data-test (primario) |
| Botón Login (alt) | `#login-button` | ID |

### XPath Selectors
| Elemento | XPath | Tipo |
|----------|-------|------|
| Usuario | `//input[@data-test='username']` | Recomendado |
| Usuario (alt) | `//input[@id='user-name']` | Alternativa |
| Contraseña | `//input[@data-test='password']` | Recomendado |
| Contraseña (alt) | `//input[@id='password']` | Alternativa |
| Botón | `//input[@data-test='login-button']` | Recomendado |
| Botón (alt) | `//input[@type='submit']` | Alternativa |

---

## 🚀 Uso de Archivos

### 1. clase_6.py - Script Python
```bash
python clase_6.py
```

**Salida:**
- Listado de todos los selectores CSS disponibles
- Listado de todos los XPath disponibles
- Recomendaciones por elemento
- Especificidad de cada selector

**Contenido:**
```python
# Selectores CSS y XPath organizados en estructura de datos
selectors = {
    "usuario": { ... },
    "contrasena": { ... },
    "boton_login": { ... }
}
```

### 2. selectores-talento.md - Documentación

**Contiene:**
- Tabla con 6 columnas: Elemento | Selector CSS | Tipo | Razón | XPath | Especificidad
- Análisis detallado de cada elemento
- HTML original de referencia
- Pruebas en consola
- Notas técnicas

**Consulta:**
```bash
cat selectores-talento.md
```

### 3. test-masivo.js - Validación JavaScript

**Función:** Validar que todos los selectores apunten a elementos válidos

**Uso en DevTools (F12):**
```javascript
// Copiar todo el contenido de test-masivo.js en la consola del navegador
// El script ejecutará automáticamente:
// - Test de 5 selectores diferentes por elemento
// - Validación de funcionalidad
// - Tabla de selectores recomendados
// - Resumen con porcentaje de éxito
```

**Salida esperada:**
```
✓ ÉXITO - ID #user-name
✓ ÉXITO - data-test="username"
✓ ÉXITO - name="user-name"
...
=== RESUMEN FINAL ===
Total de selectores probados: 15
✓ Exitosos: 15
✗ Fallidos: 0
Porcentaje de éxito: 100.00%
```

### 4. colores-demo.js - Demo Visual

**Función:** Cambiar backgroundColor de campos para demostrar que los selectores funcionan

**Funciones disponibles:**

```javascript
// 1. Colorear todos los campos
colorearCampos()
// Usuario: Amarillo (#fef3c7)
// Contraseña: Cyan (#cffafe)
// Botón: Rosa (#fce7f3)

// 2. Resetear a colores originales
resetearColores()

// 3. Colorear con efecto pulsante
colorearConPulso()

// 4. Habilitar cambio de color al hacer foco
habilitarCambioAlFoco()

// 5. Mostrar tabla visual
crearTablaVisual()

// 6. Aplicar estilos avanzados
aplicarEstilosAvanzados()
```

**Uso:**
```javascript
// En DevTools (F12), copiar el contenido de colores-demo.js
// Luego ejecutar cualquier función:
colorearCampos();
habilitarCambioAlFoco();
```

### 5. selector-testing.html - Interface Interactiva

**Características:**
- 📍 Panel CSS Selectors con botón "Copiar"
- 🗺️ Panel XPath Selectors  
- 🚀 Panel Pruebas (Test masivo + Demo)
- 📊 Tabla de status de cada selector
- 🎯 Formulario de prueba integrado

**Cómo abrir:**
```bash
# Opción 1: Doble clic en el archivo
selector-testing.html

# Opción 2: Desde navegador
open selector-testing.html

# Opción 3: Live Server
# Click derecho → Open with Live Server (si tienes la extensión)
```

**Funcionalidades interactivas:**
- ✓ Click en selector → Copiar al portapapeles
- ✓ Botón "Probar todos" → Ejecuta test masivo
- ✓ Botón "🎨 Colorear Campos" → Demo visual
- ✓ Formulario de prueba con campos reales
- ✓ Código ejecutable directamente en navegador

---

## 📊 HTML de Referencia - Swag Labs

```html
<!-- Input Usuario -->
<input class="input_error form_input" 
       placeholder="Username" 
       type="text" 
       data-test="username" 
       id="user-name" 
       name="user-name">

<!-- Input Contraseña -->
<input class="input_error form_input" 
       placeholder="Password" 
       type="password" 
       data-test="password" 
       id="password" 
       name="password">

<!-- Botón Login -->
<input type="submit" 
       class="submit-button btn_action" 
       data-test="login-button" 
       id="login-button" 
       name="login-button" 
       value="Login">
```

---

## 🧪 Pruebas en Console - Fase 1 y 2

### Fase 1: Probar CSS Selectors en document.querySelector()

```javascript
// Usuario
document.querySelector('#user-name')
document.querySelector("input[data-test='username']")

// Contraseña
document.querySelector('#password')
document.querySelector("input[data-test='password']")

// Botón
document.querySelector("[data-test='login-button']")
document.querySelector('#login-button')
```

### Fase 2: Probar XPath con $x() en DevTools

```javascript
// En navegador con DevTools abierto (F12):
$x("//input[@data-test='username']")
$x("//input[@data-test='password']")
$x("//input[@data-test='login-button']")

// Acceder al primer elemento del array
$x("//input[@data-test='username']")[0]
```

---

## 📈 Especificidad CSS

| Selector | Especificidad | Ejemplo |
|----------|---------------|---------|
| ID | 100 | `#user-name` |
| Clase | 10 | `.form_input` |
| Atributo | 10 | `[data-test='username']` |
| Elemento | 1 | `input` |

**Orden de preferencia:** ID > Atributo/Clase > Elemento

---

## ✅ Checklist de Validación

- [x] **1. CSS Selectors definidos** - 15+ selectores documentados
- [x] **2. XPath definidos** - 12+ XPath relativos
- [x] **3. test-masivo.js creado** - Valida 15 selectores
- [x] **4. selectores-talento.md creado** - Tabla con análisis completo
- [x] **5. colores-demo.js creado** - 6 funciones de demostración
- [x] **6. Interface HTML interactiva** - Completa con pruebas incorporadas

---

## 🎓 Recomendaciones para Testing Automatizado

### Selenium (Python/Java)
```python
# Usuario
driver.find_element(By.ID, "user-name")
driver.find_element(By.CSS_SELECTOR, "input[data-test='username']")
driver.find_element(By.XPATH, "//input[@data-test='username']")

# Contraseña
driver.find_element(By.ID, "password")
driver.find_element(By.XPATH, "//input[@data-test='password']")

# Botón
driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']")
driver.find_element(By.XPATH, "//input[@data-test='login-button']")
```

### Cypress
```javascript
cy.get('#user-name').type('standard_user')
cy.get('#password').type('secret_sauce')
cy.get('[data-test="login-button"]').click()
```

### Playwright
```python
page.fill('#user-name', 'standard_user')
page.fill('#password', 'secret_sauce')
page.click('[data-test="login-button"]')
```

---

## 🔗 Relación de Archivos

```
clase_6/
├── clase_6.py                 # Script Python de análisis
├── selectores-talento.md      # Documentación principal
├── test-masivo.js            # Script test en JavaScript
├── colores-demo.js           # Script demo visual
├── selector-testing.html     # Interface interactiva
└── README.md                 # Este archivo
```

---

## 💡 Tips Útiles

### Copiar selectores rápidamente
1. Abre `selector-testing.html` en navegador
2. Click en cualquier selector
3. Automáticamente se copia al portapapeles

### Verificar selectores en tiempo real
1. Abre `selector-testing.html`
2. Ve a DevTools (F12)
3. Copia contenido de `test-masivo.js` en consola
4. Observa el resumen de validación

### Cambiar visualmente los campos
1. Abre `selector-testing.html`
2. Click en "🎨 Colorear Campos"
3. Los campos cambiarán de color
4. Click en "⭐ Habilitar Foco" para efecto interactivo

---

## 📚 Notas Técnicas

### Por qué se prefiere data-test sobre ID
1. **Resiliencia:** data-test no cambia durante refactorización de estilos
2. **Intención clara:** Indica explícitamente que es para testing
3. **Estándar QA:** Usado por Selenium, Cypress, Playwright
4. **Mantenibilidad:** Los desarrolladores saben no remover o cambiar

### Por qué CSS Selectors + XPath combinados
1. **Flexibility:** CSS es más simple, XPath es más poderoso
2. **Compatibilidad:** Diferentes frameworks usan diferentes estándares
3. **Fallback:** Si uno falla, usar el otro
4. **Performance:** CSS generalmente más rápido en navegador

### Especificidad en Selectores
```css
/* Especificidad 100 - Máxima */
#user-name

/* Especificidad 10 */
input[data-test="username"]
.form_input

/* Especificidad 1 */
input
div
```

---

## 🨝 Autores y Referencias

- **Análisis de:** Swag Labs Login Form (https://www.saucedemo.com)
- **Clase:** 6 - QA Testing Automatizado
- **Conceptos:** CSS Selectors, XPath, Especificidad, Testing Framework

---

**Última actualización:** 14 de abril de 2026

