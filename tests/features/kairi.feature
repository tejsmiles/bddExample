Feature: Browser test examples with behaving

    Scenario: Login with a valid username and password
        Given a browser
        Given I visit "https://kairion.de/de-login"
        And I wait for 20 seconds
        When I fill in "edit-name" with "averma"
        And I fill in "edit-pass" with "Tubu@1982"
        And I press "edit-submit"
        And I wait for 10 seconds
        Then the browser's URL should be "https://app.kairion.de/admin/content"
