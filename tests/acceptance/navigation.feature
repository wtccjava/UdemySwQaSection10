# Created by waketechcsc at 7/2/18
Feature: Test navigation between pages
  it has this description

  Scenario: Homepage can go to Blog
    Given I am on the homepage
    When I click on the "Go to blog" link
    Then I am on the blog page


  Scenario: Blog can go to Homepage
    Given I am on the blog page
    When I click on the "Go to home" link
    Then I am on the homepage
