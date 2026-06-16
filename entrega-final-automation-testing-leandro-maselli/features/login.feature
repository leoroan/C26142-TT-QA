@ui
Feature: Login en SauceDemo

  Background:
    Given estoy en la página de login

  @smoke
  Scenario: Login exitoso
    When ingreso usuario "standard_user" y contraseña "secret_sauce"
    Then debería ver la página de inventario

  Scenario Outline: Login inválido
    When ingreso usuario "<usuario>" y contraseña "<clave>"
    Then debería ver un mensaje de error

    Examples:
      | usuario         | clave         |
      | locked_out_user | secret_sauce  |
      | usuario_fake    | password_fake |

  Scenario: Login con campos vacíos
    When intento iniciar sesión sin credenciales
    Then debería ver un mensaje de error