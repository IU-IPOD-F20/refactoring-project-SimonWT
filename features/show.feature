Feature: show command

  Scenario: Use show when there is no any project and task
     Given Created task list app
      When Execute show command
      Then Show nothing