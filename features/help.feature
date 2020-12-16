Feature: Show help description

  Scenario: Use help
     Given Created task list app
      When Execute help command
      Then Get description of commands