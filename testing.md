# Testing

## Bugs and issues during development

| Feature | Outcome | Fix Performed | Result | Fixed/Unfixed |
|---------|-------------------|-------------------|--------|------|
|Exercise list item link| The item anchors were also taking up space below the parent containers so a user could click on white space and be led to another page |Restructured the layout and moved the image out of its own separate container into the same div col container where descriptive content is located instead|The anchor now sticks to the height of its parent container and does not go beyond that | ✅ Fixed |

**IMAGE OF PROBLEM**
![Anchor element stretching out of parent](./static/images/readme_bugs_and_issues/anchor_going_out_of_parent_element.PNG)

**IMAGE AFTER FIX**
![Anchor element fixed](./static/images/readme_bugs_and_issues/anchor_going_out_of_parent_element_fixed.PNG)

**IMAGE OF CODE FIX**
![Code for anchor element fix](./static/images/readme_bugs_and_issues/anchor_going_out_of_parent_element_code_fix.PNG)

| Feature | Expected Outcome | Fix Performed | Result |
|---------|-------------------|-------------------|--------|
|||||

**IMAGE OF PROBLEM**

![]()

**IMAGE AFTER FIX**

![]()

**IMAGE OF CODE FIX**

![]()


## Validator testing

To validate all of our pages we went through all the validators and validated every available page of the website. CSS stylesheets is the only exception here considering I only have 1 CSS stylesheet and you only need to validate the stylesheets available.

### HTML validation

To validate our HTML we used the [W3C Validator](https://validator.w3.org/) and placed each individual page 

Home page

![Home page]()

Signup page

![Signup page]()

Sign in page

![Sign in page]()

Sign out page

![Sign out page]()

Exercise list page

![Exercise list page]()

Exercise detail page

![Exercise detail page]()

Membership checkout page

![Membership checkout page]()

Checkout success page

![Checkout success page]()

Favourite list page

![Favourite list page]()

My profile page

![My profile page]()

403 error page

![403 error page]()

404 error page

![404 error page]()

405 error page

![405 error page]()

500 error page

![500 error page]()

### CSS validation

To validate our CSS stylesheet we used the [W3C Jigsaw validator](https://jigsaw.w3.org/css-validator/)

CSS Stylesheet
![CSS Stylesheet]()

### JSHint validation

To validate our Javascript we are using the [JSHint validator](https://jshint.com/)
Home page

![Home page]()

Signup page

![Signup page]()

Sign in page

![Sign in page]()

Sign out page

![Sign out page]()

Exercise list page

![Exercise list page]()

Exercise detail page

![Exercise detail page]()

Membership checkout page

![Membership checkout page]()

Checkout success page

![Checkout success page]()

Favourite list page

![Favourite list page]()

My profile page

![My profile page]()

403 error page

![403 error page]()

404 error page

![404 error page]()

405 error page

![405 error page]()

500 error page

![500 error page]()

### Python validation

## Lighthouse testing

Using the chrome developer tools we did the lighthouse testing to give a general overview of the site quality, more about this [Here](https://developer.chrome.com/docs/lighthouse/overview).

Home page

![Home page]()

Signup page

![Signup page]()

Sign in page

![Sign in page]()

Sign out page

![Sign out page]()

Exercise list page

![Exercise list page]()

Exercise detail page

![Exercise detail page]()

Membership checkout page

![Membership checkout page]()

Checkout success page

![Checkout success page]()

Favourite list page

![Favourite list page]()

My profile page

![My profile page]()

403 error page

![403 error page]()

404 error page

![404 error page]()

405 error page

![405 error page]()

500 error page

![500 error page]()


## User story testing


## Manual testing


### Responsiveness

### Browser testing

### Website functionality testing

Nav bar & Footer
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|The company logo is displayed|You can see the logo on each page|Visual check||
|Conditional displaying|If the user is not logged in the membership button is not there|Visual check||
|Condition displaying|If the user is not logged in the profile icon is not there|Visual check||
|Conditional displaying|If the user is not logged in the signup button is there|Visual check||
|Conditional displaying|If the user is not logged in the Login button is there|Visual check||
|Conditional displaying|If the user is logged in the membership button is displayed|Visual check||
|Conditional displaying|If the user is logged in the view profile icon is displayed|Visual check||
|Conditional displaying|If the user is logged in and an active member the favourites list is present|Visual check||
|User redirection|On click of the home page the user is redirected to the home page|Click link||
|User redirection|On click of the company logo the user is redirected to the home page|Click link||
|User redirection|On click of the exercise lsit the user is redirected to the exercise list page|Click link||
|User redirection|On click of the membership button the user is redirected to the membership checkout page|Click link||
|User redirection|On click of the My favourites link the user is redirected to the favourites list|Click link||
|User redirection|On click of the logout link the user is redirected to the logout confirmation page|Click link||
|User redirection|On click of the my profile page the user is redirected to their my profile page|Click link||
|CTA styles|The signup button stands out with a different style to other nav links|Visual check||
|CTA styles|The login button stands out with a different style to other nav links|Visual check||
|Active nav link|If the user is on the corresponding nav link's page then the link is bold|Visual check||
|Hover styles|If not hovering the nav links there is no underline|Visual check||
|Hover styles|On hover of the nav links a line transitions under it|Hover over nav links||
|Hover styles|On remove of the mouse over the nav links the line transition disappears from under it|Hover over nav links||

Home page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||


Exercise List page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|Exercises displayed||||
|Exercise information displayed||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||


Exercise Details page 
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||

Favourite Exercises list page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||

Edit & Delete exercise page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||

My profile
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||

Membership signup page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||

Membership success page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||

Signup page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||

Login page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||

Password reset page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||

Footer
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||


403 page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||

404 page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||

405 page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||

500 page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||
