Feature: Mascota Form

  Scenario: Create Mascota

    Given an anonymous user
    When I submit a valid mascota form
    Then I am redirect to the list page