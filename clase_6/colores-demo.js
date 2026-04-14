/**
 * DEMO: Cambiar BACKGROUND COLOR de campos
 * Demuestra visualmente que los selectores CSS apuntan correctamente a los elementos
 * Uso: Copiar en la consola del navegador y ejecutar las funciones
 */

console.log('%c=== DEMO COLOR - Selectores CSS en acción ===', 'color: #2563eb; font-size: 14px; font-weight: bold');

// Paleta de colores
const colores = {
  exito: '#dcfce7',     // Verde claro
  usuario: '#fef3c7',   // Amarillo claro
  contrasena: '#cffafe', // Cyan claro
  boton: '#fce7f3',     // Rosa claro
  reset: '#ffffff'      // Blanco
};

const coloresBorde = {
  exito: '#16a34a',
  usuario: '#ca8a04',
  contrasena: '#0891b2',
  boton: '#be185d',
  reset: '#e5e7eb'
};

// Función para aplicar estilos de demostración
function aplicarEstiloDemoDatos(selector, color, colorBorde, descripcion) {
  const elemento = document.querySelector(selector);
  
  if (elemento) {
    elemento.style.backgroundColor = color;
    elemento.style.borderColor = colorBorde;
    elemento.style.borderWidth = '2px';
    elemento.style.borderStyle = 'solid';
    elemento.style.transition = 'all 0.3s ease';
    
    console.log(`%c✓ ${descripcion}`, 'color: #16a34a; font-weight: bold', `\n  Selector: ${selector}\n  Color: ${color}`);
    return elemento;
  } else {
    console.error(`%c✗ No se encontró: ${descripcion}`, 'color: #dc2626; font-weight: bold', `\n  Selector: ${selector}`);
    return null;
  }
}

// Función principal: Colorear todos los campos
function colorearCampos() {
  console.log('%c--- APLICANDO COLORES A CAMPOS ---', 'color: #1f2937; font-weight: bold');
  
  const usuario = aplicarEstiloDemoDatos(
    '#user-name',
    colores.usuario,
    coloresBorde.usuario,
    'Campo Usuario'
  );
  
  const contrasena = aplicarEstiloDemoDatos(
    '#password',
    colores.contrasena,
    coloresBorde.contrasena,
    'Campo Contraseña'
  );
  
  const boton = aplicarEstiloDemoDatos(
    '[data-test="login-button"]',
    colores.boton,
    coloresBorde.boton,
    'Botón Login'
  );
  
  console.log('%c✓ Todos los campos fueron coloreados', 'color: #16a34a; font-weight: bold');
}

// Función para resetear colores
function resetearColores() {
  console.log('%c--- RESETEANDO COLORES ---', 'color: #1f2937; font-weight: bold');
  
  const usuario = document.querySelector('#user-name');
  const contrasena = document.querySelector('#password');
  const boton = document.querySelector('[data-test="login-button"]');
  
  [usuario, contrasena, boton].forEach((elemento, index) => {
    if (elemento) {
      elemento.style.backgroundColor = colores.reset;
      elemento.style.borderColor = coloresBorde.reset;
      elemento.style.borderWidth = '1px';
    }
  });
  
  console.log('%c✓ Colores reseteados', 'color: #16a34a; font-weight: bold');
}

// Demo alterada: Colorear con efecto pulsante
function colorearConPulso() {
  console.log('%c--- APLICANDO COLORES CON EFECTO PULSO ---', 'color: #1f2937; font-weight: bold');
  
  const elementos = [
    { selector: '#user-name', color: colores.usuario, borde: coloresBorde.usuario, nombre: 'Usuario' },
    { selector: '#password', color: colores.contrasena, borde: coloresBorde.contrasena, nombre: 'Contraseña' },
    { selector: '[data-test="login-button"]', color: colores.boton, borde: coloresBorde.boton, nombre: 'Botón' }
  ];
  
  elementos.forEach((item, index) => {
    setTimeout(() => {
      const elemento = document.querySelector(item.selector);
      if (elemento) {
        elemento.style.backgroundColor = item.color;
        elemento.style.borderColor = item.borde;
        elemento.style.borderWidth = '2px';
        elemento.style.borderStyle = 'solid';
        elemento.style.boxShadow = `0 0 10px ${item.borde}`;
        console.log(`%c✓ Coloreado: ${item.nombre}`, 'color: #16a34a; font-weight: bold');
      }
    }, index * 500);
  });
}

// Demo alternativa: Cambiar colores al hacer foco
function habilitarCambioAlFoco() {
  console.log('%c--- HABILITANDO CAMBIO DE COLOR AL HACER FOCO ---', 'color: #1f2937; font-weight: bold');
  
  const usuario = document.querySelector('#user-name');
  const contrasena = document.querySelector('#password');
  
  if (usuario) {
    usuario.addEventListener('focus', function() {
      this.style.backgroundColor = '#fef08a';
      this.style.boxShadow = '0 0 8px rgba(202, 138, 4, 0.5)';
    });
    
    usuario.addEventListener('blur', function() {
      this.style.backgroundColor = '';
      this.style.boxShadow = '';
    });
    
    console.log('%c✓ Foco habilitado en Usuario', 'color: #16a34a; font-weight: bold');
  }
  
  if (contrasena) {
    contrasena.addEventListener('focus', function() {
      this.style.backgroundColor = '#cffafe';
      this.style.boxShadow = '0 0 8px rgba(8, 145, 178, 0.5)';
    });
    
    contrasena.addEventListener('blur', function() {
      this.style.backgroundColor = '';
      this.style.boxShadow = '';
    });
    
    console.log('%c✓ Foco habilitado en Contraseña', 'color: #16a34a; font-weight: bold');
  }
}

// Demo: Tabla de prueba visual
function crearTablaVisual() {
  console.log('%c--- TABLA VISUAL DE SELECTORES ---', 'color: #1f2937; font-weight: bold');
  
  const tablaData = [
    {
      Elemento: '👤 Usuario',
      Selector: '#user-name',
      Alternativa: "input[data-test='username']",
      Color: '🟨 Amarillo',
      Encontrado: document.querySelector('#user-name') ? '✓' : '✗'
    },
    {
      Elemento: '🔐 Contraseña',
      Selector: '#password',
      Alternativa: "input[data-test='password']",
      Color: '🔵 Cyan',
      Encontrado: document.querySelector('#password') ? '✓' : '✗'
    },
    {
      Elemento: '🔘 Botón Login',
      Selector: "[data-test='login-button']",
      Alternativa: '#login-button',
      Color: '🩷 Rosa',
      Encontrado: document.querySelector("[data-test='login-button']") ? '✓' : '✗'
    }
  ];
  
  console.table(tablaData);
}

// Demo: Cambiar estilos avanzados
function aplicarEstilosAvanzados() {
  console.log('%c--- APLICANDO ESTILOS AVANZADOS ---', 'color: #1f2937; font-weight: bold');
  
  function aplicarEstilo(selector, estilos, nombre) {
    const elemento = document.querySelector(selector);
    if (elemento) {
      Object.assign(elemento.style, estilos);
      console.log(`%c✓ ${nombre}`, 'color: #16a34a; font-weight: bold');
    }
  }
  
  aplicarEstilo('#user-name', {
    backgroundColor: '#fef3c7',
    borderColor: '#ca8a04',
    borderWidth: '2px',
    borderStyle: 'solid',
    padding: '10px',
    borderRadius: '6px',
    fontSize: '14px',
    fontWeight: '500'
  }, 'Usuario con estilos');
  
  aplicarEstilo('#password', {
    backgroundColor: '#cffafe',
    borderColor: '#0891b2',
    borderWidth: '2px',
    borderStyle: 'solid',
    padding: '10px',
    borderRadius: '6px',
    fontSize: '14px',
    fontWeight: '500'
  }, 'Contraseña con estilos');
  
  aplicarEstilo('[data-test="login-button"]', {
    backgroundColor: '#fce7f3',
    borderColor: '#be185d',
    borderWidth: '2px',
    borderStyle: 'solid',
    padding: '10px 20px',
    borderRadius: '6px',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer'
  }, 'Botón con estilos');
}

// Instrucciones
console.log('%c=== FUNCIONES DISPONIBLES ===', 'color: #2563eb; font-size: 13px; font-weight: bold');
console.log(`
  1. colorearCampos() 
     → Colorea todos los campos (usuario, contraseña, botón)
  
  2. resetearColores() 
     → Vuelve los campos al estado original
  
  3. colorearConPulso() 
     → Colorea los campos con efecto pulsante
  
  4. habilitarCambioAlFoco() 
     → Habilita cambio de color al hacer foco en los campos
  
  5. crearTablaVisual() 
     → Muestra tabla con status de los selectores
  
  6. aplicarEstilosAvanzados() 
     → Aplica estilos CSS complejos a los campos
`);

console.log('%c=== EJEMPLOS DE USO ===', 'color: #2563eb; font-size: 13px; font-weight: bold');
console.log('colorearCampos(); // Ejecutar demo básica');
console.log('habilitarCambioAlFoco(); // Ejecutar demo con foco');
console.log('crearTablaVisual(); // Ver tabla de selectores');

console.log('%c===================================', 'color: #2563eb');
