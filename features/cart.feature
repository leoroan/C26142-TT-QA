@ui
@regression
Feature: Carrito de compras

  Background:

    Given he iniciado sesión correctamente

  Scenario: Agregar producto al carrito

    When agrego el primer producto
    Then el contador del carrito muestra 1