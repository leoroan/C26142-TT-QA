# Selectores para Swag Labs - Talento Testing

## Tabla Principal: Elemento | Selector Elegido | Tipo | Razón

| Elemento | Selector CSS | Tipo | Razón |
|----------|--------------|------|-------|
| Input Usuario | `#user-name` | ID | Identificador único y estable, máxima especificidad |
| Input Usuario (Alt) | `input[data-test='username']` | Atributo de dato | Framework de testing, resiliente a cambios CSS |
| Input Contraseña | `#password` | ID | Identificador único y estable, máxima especificidad |
| Input Contraseña (Alt) | `input[data-test='password']` | Atributo de dato | Framework de testing, resiliente a cambios CSS |
| Botón Login | `[data-test='login-button']` | Atributo de dato | Más resiliente ante cambios, estándar QA |
| Botón Login (Alt) | `#login-button` | ID | Identificador único como alternativa |

## Tabla XPath: Elemento | XPath Relativo | Tipo | Razón

| Elemento | XPath | Tipo | Razón |
|----------|-------|------|-------|
| Input Usuario | `//input[@data-test='username']` | Atributo de dato | Estándar en automatización, resiliente |
| Input Usuario (Alt) | `//input[@id='user-name']` | ID | Alternativa de mayor especificidad |
| Input Contraseña | `//input[@data-test='password']` | Atributo de dato | Estándar en automatización, resiliente |
| Input Contraseña (Alt) | `//input[@id='password']` | ID | Alternativa de mayor especificidad |
| Botón Login | `//input[@data-test='login-button']` | Atributo de dato | Estándar en automatización |
| Botón Login (Alt) | `//form//input[@type='submit']` | Contexto relativo | Útil cuando data-test puede cambiar |

---

## 1. Input Usuario

### HTML Original
```html
<input class="input_error form_input" 
       placeholder="Username" 
       type="text" 
       data-test="username" 
       id="user-name" 
       name="user-name" 
       autocorrect="off" 
       autocapitalize="none" 
       value="">
```

### CSS Selector Recomendado
```css
#user-name
```
- **Tipo:** ID
- **Especificidad:** 100
- **Razón:** Máxima especificidad, identificador único garantizado
- **Ventajas:** Nunca falla si el ID existe, máxima velocidad de búsqueda
- **Desventajas:** Cambio de ID requiere actualizar selector

### CSS Selector Alternativo (más resiliente)
```css
input[data-test='username']
```
- **Tipo:** Atributo de dato
- **Especificidad:** 10
- **Razón:** Atributo específico de testing framework
- **Ventajas:** Resiliente a cambios de ID, sigue estándar QA
- **Desventajas:** Menor especificidad, requiere tipo explícito

### XPath Recomendado
```xpath
//input[@data-test='username']
```

### XPath Alternativo
```xpath
//input[@id='user-name']
```

### XPath Contextual (relativo)
```xpath
//form//input[@type='text' and @data-test='username']
```

---

## 2. Input Contraseña

### HTML Original
```html
<input class="input_error form_input" 
       placeholder="Password" 
       type="password" 
       data-test="password" 
       id="password" 
       name="password" 
       autocorrect="off" 
       autocapitalize="none" 
       value="">
```

### CSS Selector Recomendado
```css
#password
```
- **Tipo:** ID
- **Especificidad:** 100
- **Razón:** Máxima especificidad, identificador único garantizado
- **Ventajas:** Nunca falla si el ID existe, máxima velocidad de búsqueda
- **Desventajas:** Cambio de ID requiere actualizar selector

### CSS Selector Alternativo (más resiliente)
```css
input[data-test='password']
```
- **Tipo:** Atributo de dato
- **Especificidad:** 10
- **Razón:** Atributo específico de testing framework
- **Ventajas:** Resiliente a cambios de ID, sigue estándar QA
- **Desventajas:** Menor especificidad, requiere tipo explícito

### XPath Recomendado
```xpath
//input[@data-test='password']
```

### XPath Alternativo
```xpath
//input[@id='password']
```

### XPath Contextual (relativo)
```xpath
//form//input[@type='password']
```

---

## 3. Botón Login

### HTML Original
```html
<input type="submit" 
       class="submit-button btn_action" 
       data-test="login-button" 
       id="login-button" 
       name="login-button" 
       value="Login">
```

### CSS Selector Recomendado
```css
[data-test='login-button']
```
- **Tipo:** Atributo de dato (genérico)
- **Especificidad:** 10
- **Razón:** Atributo específico para testing, no depende del tipo
- **Ventajas:** Muy resiliente, funciona en cualquier elemento, estándar QA
- **Desventajas:** Requiere validar el atributo exacto

### CSS Selector Alternativo (mayor especificidad)
```css
#login-button
```
- **Tipo:** ID
- **Especificidad:** 100
- **Razón:** ID único alternativa con máxima especificidad
- **Ventajas:** Máxima velocidad, máxima especificidad
- **Desventajas:** Cambio de ID requiere actualización

### CSS Selector Tercer Nivel
```css
input[type='submit']
```
- **Tipo:** Combinación tipo + atributo
- **Especificidad:** 01
- **Razón:** Selecciona cualquier botón submit del formulario
- **Ventajas:** No depende de IDs ni data-test
- **Desventajas:** Puede capturar múltiples elementos si hay varios submit buttons

### XPath Recomendado
```xpath
//input[@data-test='login-button']
```

### XPath Alternativo 1
```xpath
//input[@id='login-button']
```

### XPath Alternativo 2
```xpath
//input[@type='submit']
```

### XPath Contextual (relativo)
```xpath
//form//input[@type='submit' and @data-test='login-button']
```

---

## Pruebas en Console (Browser DevTools)

### Probar CSS Selectors

#### Usuario
```javascript
// Usuario - Primaria
document.querySelector('#user-name')

// Usuario - Alternativa
document.querySelector("input[data-test='username']")

// Verificar ambas
console.log('Usuario:', document.querySelector('#user-name').value)
console.log('Usuario alt:', document.querySelector("input[data-test='username']").value)
```

#### Contraseña
```javascript
// Contraseña - Primaria
document.querySelector('#password')

// Contraseña - Alternativa
document.querySelector("input[data-test='password']")

// Verificar ambas
console.log('Contraseña:', document.querySelector('#password').value)
console.log('Contraseña alt:', document.querySelector("input[data-test='password']").value)
```

#### Botón Login
```javascript
// Botón - Primaria
document.querySelector("[data-test='login-button']")

// Botón - Alternativa
document.querySelector('#login-button')

// Botón - Tercer nivel
document.querySelector("input[type='submit']")

// Verificar
console.log('Botón:', document.querySelector("[data-test='login-button']").value)
```

### Probar XPath (en DevTools con $x)

```javascript
// Usuario
$x("//input[@data-test='username']")
$x("//input[@id='user-name']")

// Contraseña
$x("//input[@data-test='password']")
$x("//input[@id='password']")

// Botón
$x("//input[@data-test='login-button']")
$x("//input[@type='submit']")

// Verificar con index [0]
console.log('Usuario:', $x("//input[@data-test='username']")[0])
console.log('Contraseña:', $x("//input[@data-test='password']")[0])
console.log('Botón:', $x("//input[@data-test='login-button']")[0])
```

---

## Resumen de Recomendaciones

### Para Testing Automatizado (Selenium, Playwright, Cypress)
- **Usuario:** `input[data-test='username']` (CSS) o `//input[@data-test='username']` (XPath)
- **Contraseña:** `input[data-test='password']` (CSS) o `//input[@data-test='password']` (XPath)
- **Botón:** `[data-test='login-button']` (CSS) o `//input[@data-test='login-button']` (XPath)

### Para Interacción Manual en DevTools
- **Usuario:** `#user-name` (más corto)
- **Contraseña:** `#password` (más corto)
- **Botón:** `[data-test='login-button']` o `#login-button`

### Por Resiliencia al Cambio
1. **data-test** - Mejor (raramente cambia en testing)
2. **ID** - Bueno (puede cambiar en refactorización)
3. **name** - Regular (genérico, puede duplicarse)
4. **tipo** - Débil (muy genérico, múltiples matches posibles)

---

## Notas Técnicas

### Especificidad CSS
- ID: 100 puntos
- Atributo: 10 puntos
- Elemento: 1 punto
- Clase: 10 puntos (mismo que atributo)

### Patrones XPath
- `//` = Búsqueda en todo el documento
- `@` = Atributo
- `[@atributo='valor']` = Predicado con atributo exacto
- `and` = Operador lógico AND
- `[0]` o `[1]` = Índice del elemento en el resultado

