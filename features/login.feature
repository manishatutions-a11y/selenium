Feature:validate login page
  Scenario: validate login
    Given user launch browser
    When user enter username and password
    And user click on login button
    Then user should see the Dashboard page


