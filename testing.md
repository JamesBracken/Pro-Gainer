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
|Information displayed|All information is displayed|Visual check||
|Responsiveness|All information displays well |Visual check||
|Responsiveness|Information collapses into 1 column on xs devices|Window resize||
|Responsiveness|Information displays as label on the left and user information on the right|Window resize||
|Information update|If information is updated this reflects on thsis page|Refill membership and check||

Membership signup page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|Membership into|Intro displays well on multiple devices|Window resize||
|Form input label|Each input has a corresponding label|Visual check||
|Form input label|Each required input label has an asterisk|Visual check||
|Form input label|Unrequired inputs label does not have an asterisk|Visual check||
|Fieldset legend|Each fieldset section has a legend label |Visual check||
|Form|The form propagates data to the backend on submit |Add data, submit and check||
|Form|The form has the POST method|Inspect element||
|Payment summary|Initially set to nothing here text and fill out the form|Visual check||
|Payment summary|On fill out of the desired membership length update the payment summary membership costs|Select and check||
|Payment summary|On fill out of the desired membership length update the payment Joining fee|Select and check||
|Payment summary|On fill out of the desired membership length update the payment summary total payment costs|Select and check||
|Payment summary|If the joining fee is changed in settings this is reflected on the membership page|Update and check||
|Payment summary|If the membership costs is changed in settings this reflects in the membership page|||
|Payment summary|If there is a joining fee this is calculated properly and added to the membership costs for the total|||
|Payment summary|This summary displays well on multiple devices|Window resize||
|Stripe element|The stripe element displays well on multiple devices|Window resize||
|Stripe element|The stripe element follows the input design across all pages of the site|Visual check||
|Stripe element|The card number should work with 4242424242424242|Type and submit||
|Stripe element|The card number needs to be 16 digits long|Type shorter and test||
|Stripe element|The card expiry date must be placed to work|Submit without the expiry||
|Stripe element|If the card expiry input is in the past display an error message |Input a past date and submit||
|Stripe element error handling|Error messages display properly|Incorrectly fill out the element and check the error||
|Stripe element|A CVC must be input or the form will not submit|Dont fill out CVC and submit||
|Stripe element|If a CVC is not input display an error|Input incorrect CVC and submit||
|Form|If anything is filled out incorrectly in the form it does not submit |||

Membership success page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|Thank you message|Thank you message displayed with some page intro below|Visual check||
|Information displayed|All information is displayed|Visual check||
|Responsiveness|All information displays well |Visual check||
|Responsiveness|Information collapses into 1 column on xs devices|Window resize||
|Responsiveness|Information displays as label on the left and user information on the right|Window resize||
|Information update|If information is updated this reflects on thsis page|Refill membership and check||
|Home button|Home button is displayed|Visual check||
|Home button|Home button redirects to the home page|Click btn||
|My profile|My profile button is displayed|Visual check||
|My profile|My profile button redirects to the my profile page|Click btn||

Signup page
| Feature | Expected Outcome | Testing Performed | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|-----------|
|Page header|Page header displays well on multiple devices|Window resize||
|Email address|User emails must be input twice|Add once and submit||
|Email address|Both emails input must be the same|Input different emails and submit||
|Password|Password characters should be bullets|Type in characters||
|Password|Passwords must meet certain criteria|Dont meet all criteria and submit||
|Password|Password must be the same in both inputs|Input different ||
|Input labels|Each input has a corresponding label|Visual check||
|Input labels|Required input labels have an asterisk next to them|Visual check||
|Input labels|Non required input labels dont have an asterisk next to them|Visual check||
|Form submission|If the form is valid the form submits|Submit form with correct input data||
|Form submission|If the form is not valid the form does not submit|Submit form with incorrect input data||
|Form submission|If the form is valid the new account is created and added to the database|Submit and check DB||
|Form submission|If the form is invalid the data is not propagated to the database| Submit incorrectly and check DB||
|Form submission|If the form is correclty filled out and submitted the user is automatically logged in|Fill out form and submit||
|Form submission|If the form is correctly filled out and submitted the user is logged in and displayed a feedback message|Fill out form and submit||

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
