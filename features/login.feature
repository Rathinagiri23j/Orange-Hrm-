Feature: Login functionality of orange

Scenario Outline: Valid and invalid login attempts from Excel
    Given the login page is opened
    When I enter the credentials from row <row_number> from excel
    Then I take a screenshot

Examples:
    | row_number |
    | 0          |
    | 1          |
    | 2          |
    | 3          |
    | 4          |
    | 5          |
    | 6          |
    | 7          |
    | 8          |
    | 9          |
    | 10         |
    | 11         |
    | 12         |
    | 13         |
    | 14         |
    | 15         |
    | 16         |


