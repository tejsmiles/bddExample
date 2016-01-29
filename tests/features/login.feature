Feature: Browser test examples with behaving

    Scenario: Login with a valid username and password
        Given a browser
        Given I visit "https://hungryhouse.co.uk/"
        When I click the link with text that contains "Log in"
        And I fill in "username" with "tejaswinee.havaldar+livetest@deliveryhero.com"
        And I fill in "password" with "test123"
        And I press "Sign in"
        When I wait for 10 seconds
        Then I should see "Welcome, tejaswinee.havaldar+livetest@deliveryhero.com"
