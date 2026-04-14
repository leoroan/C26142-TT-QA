/**
 * TEST MASIVO DE SELECTORES CSS
 * Verifica que todos los selectores CSS apunten correctamente a los elementos
 * Uso: Copiar todo el código en la consola del navegador
 */

console.log('%c=== TEST MASIVO DE SELECTORES ===', 'color: #2563eb; font-size: 14px; font-weight: bold');
console.log('%cSwag Labs Login Form - Selectores CSS', 'color: #0f766e; font-size: 12px');

// Objeto con configuración de selectores
const selectoresConfig = {
  usuario: {
    elemento: 'Input Usuario',
    selectores: [
      { selector: '#user-name', nombre: 'ID #user-name' },
      { selector: 'input[data-test="username"]', nombre: 'data-test="username"' },
      { selector: 'input[name="user-name"]', nombre: 'name="user-name"' },
      { selector: '.form_input[type="text"]', nombre: 'Clase + tipo' },
      { selector: 'input[type="text"][data-test="username"]', nombre: 'Combinado' }
    ]
  },
  contrasena: {
    elemento: 'Input Contraseña',
    selectores: [
      { selector: '#password', nombre: 'ID #password' },
      { selector: 'input[data-test="password"]', nombre: 'data-test="password"' },
      { selector: 'input[name="password"]', nombre: 'name="password"' },
      { selector: '.form_input[type="password"]', nombre: 'Clase + tipo' },
      { selector: 'input[type="password"][data-test="password"]', nombre: 'Combinado' }
    ]
  },
  boton: {
    elemento: 'Botón Login',
    selectores: [
      { selector: '[data-test="login-button"]', nombre: 'data-test="login-button"' },
      { selector: '#login-button', nombre: 'ID #login-button' },
      { selector: 'input[type="submit"]', nombre: 'type="submit"' },
      { selector: '.submit-button', nombre: 'Clase .submit-button' },
      { selector: 'input[name="login-button"]', nombre: 'name="login-button"' }
    ]
  }
};

// Estadísticas
let estadisticas = {
  exitosos: 0,
  fallidos: 0,
  totales: 0
};

// Función para probar un selector
function probarSelector(selector, nombreSelector, elemento) {
  estadisticas.totales++;
  
  try {
    const resultado = document.querySelector(selector);
    
    if (resultado !== null) {
      estadisticas.exitosos++;
      console.log(
        `%c✓ ÉXITO`,
        'color: #16a34a; font-weight: bold',
        `${nombreSelector}`,
        `\n  Selector: ${selector}`,
        `\n  Elemento encontrado:`,
        resultado
      );
      return true;
    } else {
      estadisticas.fallidos++;
      console.warn(
        `%c✗ FALLO`,
        'color: #dc2626; font-weight: bold',
        `${nombreSelector}`,
        `\n  Selector: ${selector}`,
        `\n  NO encontró ningún elemento`
      );
      return false;
    }
  } catch (error) {
    estadisticas.fallidos++;
    console.error(
      `%c✗ ERROR`,
      'color: #991b1b; font-weight: bold',
      `${nombreSelector}`,
      `\n  Selector inválido: ${selector}`,
      `\n  Error: ${error.message}`
    );
    return false;
  }
}

// Ejecutar pruebas
console.log('\n%c--- INICIANDO PRUEBAS ---', 'color: #1f2937; font-weight: bold; text-decoration: underline');

for (const [clave, config] of Object.entries(selectoresConfig)) {
  console.log(`\n%c${config.elemento.toUpperCase()}`, 'color: #2563eb; font-weight: bold; font-size: 13px');
  console.log('─'.repeat(50));
  
  for (const selectorData of config.selectores) {
    probarSelector(selectorData.selector, selectorData.nombre, config.elemento);
  }
}

// Resumen final
console.log('\n%c=== RESUMEN FINAL ===', 'color: #2563eb; font-size: 14px; font-weight: bold');
console.log(`%cTotal de selectores probados: ${estadisticas.totales}`, 'font-size: 12px');
console.log(`%c✓ Exitosos: ${estadisticas.exitosos}`, 'color: #16a34a; font-weight: bold; font-size: 12px');
console.log(`%c✗ Fallidos: ${estadisticas.fallidos}`, 'color: #dc2626; font-weight: bold; font-size: 12px');

const porcentajeExito = ((estadisticas.exitosos / estadisticas.totales) * 100).toFixed(2);
console.log(`%cPorcentaje de éxito: ${porcentajeExito}%`, `color: ${porcentajeExito === '100.00' ? '#16a34a' : '#f97316'}; font-weight: bold; font-size: 12px`);

// Validación de funcionalidad
console.log('\n%c=== PRUEBA DE FUNCIONALIDAD ===', 'color: #2563eb; font-size: 14px; font-weight: bold');

function validarFuncionalidad() {
  const usuario = document.querySelector('#user-name');
  const contrasena = document.querySelector('#password');
  const boton = document.querySelector('[data-test="login-button"]');
  
  if (usuario && contrasena && boton) {
    console.log('%c✓ Todos los elementos están disponibles y funcionales', 'color: #16a34a; font-weight: bold');
    return {
      usuario,
      contrasena,
      boton
    };
  } else {
    console.error('%c✗ Algunos elementos no están disponibles', 'color: #dc2626; font-weight: bold');
    if (!usuario) console.error('  - Usuario NO encontrado');
    if (!contrasena) console.error('  - Contraseña NO encontrada');
    if (!boton) console.error('  - Botón NO encontrado');
    return null;
  }
}

const elementosValidos = validarFuncionalidad();

// Mostrar tabla de selectores recomendados
console.log('\n%c=== SELECTORES RECOMENDADOS ===', 'color: #2563eb; font-size: 14px; font-weight: bold');
console.table([
  { Elemento: 'Usuario', 'Selector Recomendado': '#user-name', Alternativa: "input[data-test='username']", Tipo: 'ID / data-test' },
  { Elemento: 'Contraseña', 'Selector Recomendado': '#password', Alternativa: "input[data-test='password']", Tipo: 'ID / data-test' },
  { Elemento: 'Botón', 'Selector Recomendado': "[data-test='login-button']", Alternativa: '#login-button', Tipo: 'data-test / ID' }
]);

console.log('%c===================================', 'color: #2563eb');
console.log('%cPrueba completada. Verifica la consola para más detalles.', 'color: #475569; font-style: italic');
