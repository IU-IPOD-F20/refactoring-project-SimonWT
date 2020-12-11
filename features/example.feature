Feature: showing off behave

  Scenario Outline: run a simple test
     Given we have behave installed
      When we implement a test with "<thing>"
      Then behave will test it for us with "<other thing>"!


     Examples: Example1
     | thing         | other thing |
     | Red Tree Frog | mush        |