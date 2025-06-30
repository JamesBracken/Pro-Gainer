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
|Page title|Page title is displayed in the tab|Visual check||
|Hero image|The hero image displays well on multiple devices|Window resize||
|Brand header|The brand header displays well on multiple devices|Visual check and window resize||
|Membership description|All the information is displayed well and is correct|Visual check||
|Membership section CTA|The membership button redirects to the membership page|Press button||
|Membership section CTA|The membership button displays if the user is authenticated|Visual check||
|Membership section CTA|The signup button displays if the user is not authenticated|Visual check||
|Membership section CTA|The signup button redirects to the signup page|Click the button||
|Join us now overlay|The join us now overlay displays well on all screen sizes|Window resize||
|Join here button|If the user is not authenticated redirects to the signup page|Click button||
|Join here button|If the user is authenticated redirects to the membership form|Click button||
|Cards section|Cards display well on all screen sizes|Window resize||
|Nav link|The home nav link is bold|Visual check||

Exercise List page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|Exercises intro|The exercise introduction displays well on multiple screen sizes|Window resize||
|Add exercise btn|The button is present for admins|Visual check||
|Add exercise btn|The button is not present for regular users|Visual check||
|Add exercise btn|The button redirects to the add exercise form|Click button||
|Exercise list|All exercises are displayed|Visual check||
|Exercise card|Each exercise card displays the required information title, difficulty, muscles targeted, equipment and image|Visual check||
|Exercise card|Each exercise card can be clicked|Click card||
|Exercise card|Each exercise card redirects to the corresponding detail page|Click card||
|Exercise card|Each card displays as the same size as the card next to it|Visual check||
|Exercise card|Each card displays with an alt tag equivalent to the input exercise title|||
|Exercise list|The exercises are organised as newest first|Add an exercise and do a visual check||
|Exercise card|The information is displayed by importance|Visual check||
|Pagination|The current page is displayed properly|Visual check||
|Pagination|The total amount of pages is displayed properly|Visual check||
|Pagination|Given enough exercises there is a next page button|Visual check||
|Pagination|The next page button works properly|Click button||
|Pagination|Given enough exercises there is a last page button|Visual check||
|Pagination|The last page button works properly|Click button||
|Pagination|Given enough exercises there is a previous page button|Visual check||
|Pagination|The previous page button works properly|Click button||
|Pagination|Given enough exercises there is a first page button|Visual check||
|Pagination|The first page button works properly|Click button||


Exercise Details page 
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|Edit button|The edit button is displayed for admins|Visual check||
|Deletebutton|The delete button is displayed for admins|Visual check||
|Edit button|The edit button works properly|Click button||
|Delete button|The delete button works properly|Click button||
|Exercise image|The image displays well on multiple device sizes|Visual check||
|Exercise information|All exercise information is displayed|Visual check||
|Favourite exercise icon|Icon is present|Visual check||
|Favourite exercise icon|Icon starts out black and not favourited|Visual check||
|Favourite exercise icon|Icon has a indicator next to it|Visual check||
|Favourite exercise icon|Icon is clickable|Click icon||
|Favourite exercise icon|Icon becomes red on click if black|Click icon||
|Favourite exercise icon|Icon becomes black on clik if red|Click icon||
|Favourite exercise icon|If the icon is black and clicked the exercise is added to the user favourites|Click icon and check||
|Favourite exercise icon|If the icon is red and clicked the exercise is removed from the user favourites|Click icon and check||

Favourite Exercises list page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|Favourites intro|Intro is displayed well on multiple device sizes|Window resize||
|Favourites list|Favourite exercises is displayed|Visual check||
|Favourites list|Favourite exercises is displayed by newest first|Visual check||
|Favourites list|If there are no favourites yet the users has a feedback message|Visual check||
|Exercise card|All information is displayed properly such as image, title, difficulty, muscles targeted and equipment|Visual check||
|Exercise card|All information is displayed by importance title first, then difficulty, muscles and equipment last|||
|Exercise card|Each card can be clicked to redirect to the exercise page|Click card||
|Exercise card|Each card redirects to the corresponding exercise detail page|Click card||
|Exercise card|Each exercise image displays an alt tag equivalent to the exercise title|||
|Pagination|The current page is displayed properly|Visual check||
|Pagination|The total amount of pages is displayed properly|Visual check||
|Pagination|Given enough exercises there is a next page button|Visual check||
|Pagination|The next page button works properly|Click button||
|Pagination|Given enough exercises there is a last page button|Visual check||
|Pagination|The last page button works properly|Click button||
|Pagination|Given enough exercises there is a previous page button|Visual check||
|Pagination|The previous page button works properly|Click button||
|Pagination|Given enough exercises there is a first page button|Visual check||
|Pagination|The first page button works properly|Click button||

Add, edit & Delete exercise page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|Exercise form|The form displays well on difference device sizes|Window resize||
|Exercise form|All inputs are present|Visual check||
|Label inputs|All inputs have a corresponding label|Visual check||
|Label inputs|If an input is required the label has an asterisk|Visual check||
|Label inputs|If an input is not required there is no asterisk on the label|Visual check||
|Exercise title|Must be unique|Add an already added title and submit||
|Difficulty|Contains easy, medium and difficult selections|Visual check||
|Difficulty|Users cannot type|Attempt to type||
|Recommended sets|Users can only add integers|Type||
|Recommended reps|Users can only add integers|Type||
|Intensity|The options are light, moderate and intense|Visual check||
|Intensity|Users cannot type|Attempt to type||
|Form instance|If editing an exercise the information is pre-filled with the previous data|Visual check||
|Form instance|If editing an exercise the selected instance is edited |Submit and check||
|Form instance|If editing an exercise a new instance is not created|Submit and check||
|Form|On form submission the data is added to the database|Submit form||
|Form|If filled out incorrectly the form is not submitted|||

My profile
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|All ||||
|||||
|||||
|||||
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

500 page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|||||
