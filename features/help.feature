Feature: Show help description

  Scenario: Use help
     Given Created task list app
      When execute help command
      Then get description of commands