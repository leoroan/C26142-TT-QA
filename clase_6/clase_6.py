"""
Análisis de selectores CSS y XPath para la aplicación Swag Labs
Enfoque: Extrayendo selectores para formulario de login (usuario, contraseña, botón login)
"""

# Selectors CSS y XPath para Swag Labs Login Form

selectors = {
    "usuario": {
        "elemento": "input[type='text']",
        "html": '<input class="input_error form_input" placeholder="Username" type="text" data-test="username" id="user-name" name="user-name">',
        "selectores_css": [
            {
                "selector": "#user-name",
                "tipo": "ID",
                "razon": "Identificador único y estable para el campo de usuario",
                "especificidad": "100",
            },
            {
                "selector": "input[data-test='username']",
                "tipo": "Atributo de dato",
                "razon": "Atributo de prueba específico del framework de testing",
                "especificidad": "010",
            },
            {
                "selector": "input[name='user-name']",
                "tipo": "Atributo name",
                "razon": "Atributo estándar de formulario",
                "especificidad": "010",
            },
            {
                "selector": "input[type='text'][data-test='username']",
                "tipo": "Combinado",
                "razon": "Combinación de tipo y data-test para máxima precisión",
                "especificidad": "020",
            },
            {
                "selector": ".form_input[type='text']",
                "tipo": "Clase + tipo",
                "razon": "Menos específico, útil si el ID cambia",
                "especificidad": "020",
            },
        ],
        "xpaths": [
            {
                "xpath": "//input[@id='user-name']",
                "tipo": "XPath por ID",
                "razon": "Selección válida pero menos usado en XPath",
            },
            {
                "xpath": "//input[@data-test='username']",
                "tipo": "XPath por atributo de dato",
                "razon": "Recomendado para testing automatizado",
            },
            {
                "xpath": "//input[@name='user-name']",
                "tipo": "XPath por name",
                "razon": "Selección estándar de formulario",
            },
            {
                "xpath": "//input[@type='text' and @data-test='username']",
                "tipo": "XPath combinado",
                "razon": "Máxima precisión con predicados múltiples",
            },
            {
                "xpath": "//form//input[@type='text']",
                "tipo": "XPath relativo dentro de form",
                "razon": "Contextual con respecto al formulario",
            },
        ],
    },
    "contrasena": {
        "elemento": "input[type='password']",
        "html": '<input class="input_error form_input" placeholder="Password" type="password" data-test="password" id="password" name="password">',
        "selectores_css": [
            {
                "selector": "#password",
                "tipo": "ID",
                "razon": "Identificador único y estable para el campo de contraseña",
                "especificidad": "100",
            },
            {
                "selector": "input[data-test='password']",
                "tipo": "Atributo de dato",
                "razon": "Atributo de prueba específico del framework de testing",
                "especificidad": "010",
            },
            {
                "selector": "input[name='password']",
                "tipo": "Atributo name",
                "razon": "Atributo estándar de formulario",
                "especificidad": "010",
            },
            {
                "selector": "input[type='password'][data-test='password']",
                "tipo": "Combinado",
                "razon": "Combinación de tipo y data-test para máxima precisión",
                "especificidad": "020",
            },
            {
                "selector": ".form_input[type='password']",
                "tipo": "Clase + tipo",
                "razon": "Menos específico, útil si el ID cambia",
                "especificidad": "020",
            },
        ],
        "xpaths": [
            {
                "xpath": "//input[@id='password']",
                "tipo": "XPath por ID",
                "razon": "Selección válida pero menos usado en XPath",
            },
            {
                "xpath": "//input[@data-test='password']",
                "tipo": "XPath por atributo de dato",
                "razon": "Recomendado para testing automatizado",
            },
            {
                "xpath": "//input[@name='password']",
                "tipo": "XPath por name",
                "razon": "Selección estándar de formulario",
            },
            {
                "xpath": "//input[@type='password' and @data-test='password']",
                "tipo": "XPath combinado",
                "razon": "Máxima precisión con predicados múltiples",
            },
            {
                "xpath": "//form//input[@type='password']",
                "tipo": "XPath relativo dentro de form",
                "razon": "Contextual con respecto al formulario",
            },
        ],
    },
    "boton_login": {
        "elemento": "input[type='submit']",
        "html": '<input type="submit" class="submit-button btn_action" data-test="login-button" id="login-button" name="login-button" value="Login">',
        "selectores_css": [
            {
                "selector": "#login-button",
                "tipo": "ID",
                "razon": "Identificador único y estable para el botón de login",
                "especificidad": "100",
            },
            {
                "selector": "input[data-test='login-button']",
                "tipo": "Atributo de dato",
                "razon": "Atributo de prueba específico del framework de testing",
                "especificidad": "010",
            },
            {
                "selector": "input[name='login-button']",
                "tipo": "Atributo name",
                "razon": "Atributo estándar de formulario",
                "especificidad": "010",
            },
            {
                "selector": "input[type='submit']",
                "tipo": "Tipo de elemento",
                "razon": "Selecciona cualquier botón submit del formulario",
                "especificidad": "001",
            },
            {
                "selector": ".submit-button",
                "tipo": "Clase",
                "razon": "Clase CSS específica del botón",
                "especificidad": "010",
            },
            {
                "selector": "[data-test='login-button']",
                "tipo": "Atributo genérico",
                "razon": "Atributo de prueba único (funciona en cualquier elemento)",
                "especificidad": "010",
            },
        ],
        "xpaths": [
            {
                "xpath": "//input[@id='login-button']",
                "tipo": "XPath por ID",
                "razon": "Selección más específica",
            },
            {
                "xpath": "//input[@data-test='login-button']",
                "tipo": "XPath por atributo de dato",
                "razon": "Recomendado para testing automatizado",
            },
            {
                "xpath": "//input[@name='login-button']",
                "tipo": "XPath por name",
                "razon": "Selección estándar de formulario",
            },
            {
                "xpath": "//input[@type='submit']",
                "tipo": "XPath por tipo",
                "razon": "Selecciona cualquier botón submit",
            },
            {
                "xpath": "//form//input[@type='submit']",
                "tipo": "XPath relativo dentro de form",
                "razon": "Contextual con respecto al formulario",
            },
        ],
    },
}

# Recomendaciones por elemento
recomendaciones = {
    "usuario": {
        "css_recomendado": "#user-name",
        "xpath_recomendado": "//input[@data-test='username']",
        "razon": "ID garantiza unicidad. XPath por data-test es estándar en QA automatizado.",
    },
    "contrasena": {
        "css_recomendado": "#password",
        "xpath_recomendado": "//input[@data-test='password']",
        "razon": "ID garantiza unicidad. XPath por data-test es estándar en QA automatizado.",
    },
    "boton_login": {
        "css_recomendado": "[data-test='login-button']",
        "xpath_recomendado": "//input[@data-test='login-button']",
        "razon": "data-test es más resiliente que ID. Ambos formatos son estándar en QA.",
    },
}

# Función para imprimir tabla de selectores
def generar_tabla_markdown():
    """Genera tabla markdown para selectores-talento.md"""
    md_content = """# Selectores para Swag Labs - Talento Testing

## Tabla de Selectores CSS y XPath

| Elemento | Selector Elegido | Tipo | Razón |
|----------|------------------|------|-------|
| Input Usuario | `#user-name` | ID | Identificador único y estable |
| Input Usuario (alt) | `input[data-test='username']` | Atributo de dato | Usado para testing automatizado |
| Input Contraseña | `#password` | ID | Identificador único y estable |
| Input Contraseña (alt) | `input[data-test='password']` | Atributo de dato | Usado para testing automatizado |
| Botón Login | `[data-test='login-button']` | Atributo de dato | Más resiliente que ID en cambios |
| Botón Login (alt) | `#login-button` | ID | Identificador único |

## Análisis Detallado por Elemento

### 1. Input Usuario
**HTML Original:**
```html
<input class="input_error form_input" placeholder="Username" type="text" 
       data-test="username" id="user-name" name="user-name" 
       autocorrect="off" autocapitalize="none">
```

**Selectores CSS más fiables (en orden de preferencia):**
1. `#user-name` - ID (especificidad 100)
2. `input[data-test='username']` - Atributo data-test (especificidad 010)
3. `input[name='user-name']` - Atributo name (especificidad 010)

**XPath más fiables (en orden de preferencia):**
1. `//input[@data-test='username']` - Por atributo de dato
2. `//input[@id='user-name']` - Por ID
3. `//input[@name='user-name']` - Por name
4. `//form//input[@type='text' and @data-test='username']` - Relativo con predicados

### 2. Input Contraseña
**HTML Original:**
```html
<input class="input_error form_input" placeholder="Password" type="password" 
       data-test="password" id="password" name="password" 
       autocorrect="off" autocapitalize="none">
```

**Selectores CSS más fiables (en orden de preferencia):**
1. `#password` - ID (especificidad 100)
2. `input[data-test='password']` - Atributo data-test (especificidad 010)
3. `input[name='password']` - Atributo name (especificidad 010)

**XPath más fiables (en orden de preferencia):**
1. `//input[@data-test='password']` - Por atributo de dato
2. `//input[@id='password']` - Por ID
3. `//input[@name='password']` - Por name
4. `//form//input[@type='password']` - Relativo al formulario

### 3. Botón Login
**HTML Original:**
```html
<input type="submit" class="submit-button btn_action" 
       data-test="login-button" id="login-button" name="login-button" 
       value="Login">
```

**Selectores CSS más fiables (en orden de preferencia):**
1. `[data-test='login-button']` - Atributo de dato (genérico)
2. `#login-button` - ID (especificidad 100)
3. `input[type='submit']` - Tipo (especificidad 001)

**XPath más fiables (en orden de preferencia):**
1. `//input[@data-test='login-button']` - Por atributo de dato
2. `//input[@id='login-button']` - Por ID
3. `//input[@name='login-button']` - Por name

## Pruebas en Consola

### CSS Selectors (document.querySelector)
```javascript
// Usuario
document.querySelector('#user-name')
document.querySelector("input[data-test='username']")

// Contraseña
document.querySelector('#password')
document.querySelector("input[data-test='password']")

// Botón Login
document.querySelector("[data-test='login-button']")
document.querySelector('#login-button')
```

### XPath (mediante $x() en DevTools o Selenium)
```javascript
// Usuario
$x("//input[@data-test='username']")
$x("//input[@id='user-name']")

// Contraseña
$x("//input[@data-test='password']")
$x("//input[@id='password']")

// Botón Login
$x("//input[@data-test='login-button']")
$x("//input[@id='login-button']")
```

## Notas de Implementación

1. **Preferencia de data-test**: En aplicaciones diseñadas para testing (como Swag Labs), los atributos `data-test` son más resilientes a cambios de diseño que las clases CSS.

2. **ID vs data-test**: Los IDs tienen mayor especificidad CSS, pero data-test es más semántico para testing.

3. **Contexto XPath relativo**: Se recomienda usar XPath relativo dentro del formulario cuando sea posible.

4. **Seguridad de atributos**: El atributo `data-test` permanece aunque cambien clases y estilos CSS.
"""
    return md_content

if __name__ == "__main__":
    print("=== Selectores CSS y XPath para Swag Labs ===\n")
    
    for element, data in selectors.items():
        print(f"\n{'='*60}")
        print(f"ELEMENTO: {element.upper()}")
        print(f"{'='*60}")
        print(f"HTML: {data['html'][:80]}...\n")
        
        print("SELECTORES CSS RECOMENDADOS:")
        for selector in data['selectores_css'][:3]:  # Top 3
            print(f"  • {selector['selector']:<40} ({selector['tipo']})")
            print(f"    → {selector['razon']}")
        
        print("\nXPATH RECOMENDADOS:")
        for xpath in data['xpaths'][:3]:  # Top 3
            print(f"  • {xpath['xpath']:<40} ({xpath['tipo']})")
            print(f"    → {xpath['razon']}")
        
        print(f"\n✓ RECOMENDACIÓN:")
        rec = recomendaciones[element]
        print(f"  CSS: {rec['css_recomendado']}")
        print(f"  XPath: {rec['xpath_recomendado']}")
    
    # Generar markdown
    print("\n" + "="*60)
    print("Generando selectores-talento.md...")
    print("="*60)
    md = generar_tabla_markdown()
    print(md[:500] + "...\n")

