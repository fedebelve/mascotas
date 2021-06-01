Feature: Mascotas Form

  Scenario: Create Mascota

    Given una persona y una vacuna
    When I submit a valid mascota form
    Then I am redirect to the list page

    Given una persona y una vacuna
    When I submit an invalid mascota form
    Then I am redirect to the same page