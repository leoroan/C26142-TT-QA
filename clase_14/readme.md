✅ environment.py está funcionando.
✅ context.driver existe.
✅ Los hooks de Behave se ejecutan.
✅ Los steps del login quedaron correctamente vinculados.
✅ El Scenario Outline funciona.
✅ Los casos inválidos muestran el error esperado.
✅ El caso de campos vacíos también funciona.

Feature Login
Feature: Login en SauceDemo
✅ Background
✅ Login exitoso
✅ Scenario Outline
✅ Casos inválidos
✅ Tag @smoke

Feature Carrito
Feature: Carrito de compras
✅ Background
✅ Agregar producto
✅ Validar contador

Step Definitions
✅ login_steps.py
✅ cart_steps.py
✅ reutilizando LoginPage
✅ reutilizando InventoryPage
✅ usando logger

Environment
✅ before_all
✅ after_step
✅ after_all

## comandos:
behave
 - 2 features passed, 0 failed, 0 skipped
 - 5 scenarios passed, 0 failed, 0 skipped
 - 15 steps passed, 0 failed, 0 skipped
 - Took 0min 3.598s
behave --tags=@smoke
 - 1 feature passed, 0 failed, 1 skipped
 - 1 scenario passed, 0 failed, 4 skipped
 - 3 steps passed, 0 failed, 12 skipped
 - Took 0min 0.836s
behave --tags=@regression
  - 1 feature passed, 0 failed, 1 skipped
  - 1 scenario passed, 0 failed, 4 skipped
  - 3 steps passed, 0 failed, 12 skipped
  - Took 0min 0.728s
behave --dry-run
pytest tests_behave/

## reporte JSON:
behave -f json -o reports/behave.json