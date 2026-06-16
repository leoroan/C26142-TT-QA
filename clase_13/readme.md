### **Pre-Entrega de Proyecto**

#### **Objetivo**
El objetivo de la siguiente pre-entrega de proyecto es que apliques los conocimientos adquiridos hasta la **Clase 8** del curso, demostrando tu capacidad para automatizar flujos básicos de navegación web utilizando **Selenium WebDriver** y **Python**. 

Este proyecto te permitirá poner en práctica lo aprendido sobre:
- Interacción con elementos web
- Estrategias de localización 
- Validación de estados en una página

**Sitio web a utilizar:**  
www.saucedemo.com - aplicación web demo especialmente diseñada para prácticas de testing.

#### **Fecha de Entrega y Evaluación**
- **Fecha límite de entrega:** 7 días a partir de la Clase 8
- **Formato de entrega:** Código subido a GitHub

#### **Tecnologías Requeridas**
- **Python** como lenguaje principal
- **Pytest** para estructura de testing
- **Selenium WebDriver** para automatización
- **Git y GitHub** para control de versiones

#### **Estructura del Proyecto**
- Organizar el código en mínimo 2 archivos separados (tests y funciones auxiliares)
- Incluir comentarios descriptivos y usar nomenclatura significativa para todos los elementos

#### **Instrucciones Generales**
Deberás completar las siguientes consignas basadas en cada una de las fases vistas.

La entrega debe incluir:
- Código organizado y bien estructurado en un formato claro y profesional
- Utilizar `README.md` para entender el código y asegurar que los datos sean comprensibles y bien categorizados

---

### **Consignas Obligatorias**

#### **1. Automatización de Login**
1. Navegar a la página de login de saucedemo.com
2. Ingresar credenciales válidas:
   - **Usuario:** `standard_user`
   - **Contraseña:** `secret_sauce`
3. Validar login exitoso verificando que se haya redirigido a la página de inventario

**Criterios mínimos:**
- Login automatizado con espera explícita
- Validación de `/inventory.html` y `"Products/Swag Labs"`

#### **2. Navegación y Verificación del Catálogo** (Clases 6 a 8)
**Caso de Prueba de Navegación:**
1. Verificar que el título de la página de inventario sea correcto
2. Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)
3. Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)

**Criterios mínimos:**
- Valida título
- Valida presencia de productos  
- Lista nombre/precio del primero

#### **3. Interacción con Productos** (Clase 8)
**Caso de Prueba de Carrito:**
1. Añadir un producto al carrito haciendo clic en el botón correspondiente
2. Verificar que el contador del carrito se incremente correctamente
3. Navegar al carrito de compras
4. Comprobar que el producto añadido aparezca correctamente en el carrito

**Criterios mínimos:**
- Agrega primer producto
- Verifica ítem en carrito

#### **4. Repositorio en GitHub**
1. Subir el proyecto a un repositorio en GitHub
2. Realizar commits frecuentes y con mensajes descriptivos que muestren el progreso del proyecto

**README.md debe incluir:**
- El propósito del proyecto
- Las tecnologías utilizadas
- Cómo instalar las dependencias
- Cómo ejecutar las pruebas

**Generar reporte en HTML de las pruebas realizadas:**
```bash
pytest pre-entrega/tests/test_saucedemo.py -v --html=reports/reporte.html
```

**Generar reporte en CONSOLA de las pruebas realizadas:**
```bash
pytest pre-entrega/tests/test_saucedemo.py -v -s --html=reports/reporte.html
```

---

### **Funcionalidad Esperada**
- Los casos de prueba deben ejecutarse correctamente en el sitio saucedemo.com
- Las validaciones deben ser claras y específicas para cada paso
- El código debe ser legible y estar bien organizado
- Los tests deben ser independientes entre sí (la falla de uno no debe afectar a los demás)

### **Entregables**
1. **Repositorio público en GitHub** con todo el código del proyecto
2. **Archivo README.md** que incluya:
   - Propósito del proyecto
   - Tecnologías utilizadas
   - Instrucciones de instalación de dependencias
   - Comando para ejecutar las pruebas: `pytest -v --html=reporte.html`
3. **Reporte HTML** generado por Pytest con resultados de la ejecución
4. **Evidencias adicionales:** capturas de pantalla automáticas en caso de fallos y logs de ejecución

### **Formato de Entrega**
- **Nombre del repositorio:** `pre-entrega-automation-testing-[Leandro-Maselli]`
- **Estructura mínima de carpetas:**
  ```
  tests/
  utils/          # funciones auxiliares
  reports/        # reportes HTML y capturas
  ```

  pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html