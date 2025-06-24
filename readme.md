
# Pro Gainer

## [ --> View the live deployed project here <-- ADDD A LINKKKKKKKKKKKKKKK]()

## Table of contents

## UX
### Strategy
#### Project overview

Welcome to Pro Gainer, a website for individuals to subscribe to a gym membership to have access to the Pro Gainer gym. Members have access to our fantastic premium content of being able to save and access a wide array of different exercises, instructional material on each of these exercises and the ability to keep them in your favourites list. 

The website is focused on providing a gym subscription service for the physical gym which our members can attend, it is located in the heart of hounslow in greater london. Alongside the access for our amazing gym users will be able to access our publicly available exercise list and save any item within this list. 

<!-- The website is made using the django framework, each different component is going to be categorized into their own apps. The apps we have in this project consists of the  membership and exercise app. The membership app will -->

#### Project goals


#### User stories

At the highest level we have used Epics to categorize our user stories into separate blocks based on the needs of the end user. Each Epic will contain multiple user stories 
and each user stories will themselves contain multiple *acceptance criteria* to dictate the expectations of our clients and *tasks* for the developers to be able to further breakdown the work into smaller more manageable pieces.

To be able to better prioritise, organise and communicate the intended project features we have come up with our set of User Stories. These will be our guide from project inception to create the features within our website until project delivery. These user stories plays a crucial role into the needs and necessary features that an end user would want in the website. The user stories were organised and prioritised using a project view board in github projects which can be found [Here](https://github.com/users/JamesBracken/projects/15/views/5).

**User content(Epic)**
 
 - As a user, I would like access to a navigation bar and footer so I can easily navigate the website(Must have)

 - As a user, I would like the site to be responsive so I can access it on multiple devices(Must have)
 
 - As a user, I would like to have access to a list of exercises so that I can gather inspiration for my next workout(Must have)
 
 - As a user, I would like to have access to details of each exercise so I can get a better grasp of each individual exercise(Must have)
 
 - As a user, I would like to be informed of any discounts the gym may be doing so I can save money(Should have)
 
 - As a user, I would like to have access to a gallery so I can view pictures of the gym and understand if it is right for me(Could have)
 
 - As a user, I would like to be able to book a visit so I can decide if the gym is right for me(Could have)

**Membership and authentication**
 
 - As an interested customer, I would like to be able to register, sign in and sign out so I can access my membership benefits(Must have)
 
 - As an interested customer, I would like to be able to subscribe for a membership so I can access premium website functionality(Must have, 
 this user story was originally --As an interested customer, I would like to be able to pay for my membership with a recurring fee so I dont need to worry about paying.
 This user story was altered after initially setting this due to being out of scope of the project. More about this on user story testing)
 
 - As a signed-in user, I would like to be able to cancel my membership so I can stop my gym payments(Originally Must have, now Wont do as recurring payments
 will no longer be applied in the project there is no further need for a cancel membership functionality)

**Members only content**
 
 - As a signed-in user, I would like to be able to save exercises as favourites so I can easily come back to them(Must have)
 
 - As a signed-in user, I would like to be able to filter the exercises in my favourites list so I can easily access specific exercises (Should 
 have)
 
 - As a signed-in user, I would like to be able to add my fitness goals 
 so I can have them on my profile(Should have)
 
 - As a signed-in user, I would like to be able to update my fitness goals so I can keep it updated(Should have)
 
 - As a signed-in user, I would like to receive personalised workouts which are based on my goals so I can get better results faster(Could 
 have)
 
 - As a signed-in user, I would like to be able to search for exercise content on the exercise list so I can find exercises faster(Could have)
 
 - As a signed-in user, I would like to be able to filter exercise search results on the exercise list so I can find exercises faster(Could have)

**Admin content**
 
 - As an admin, I would like to be able to Create new exercises for the website(Must have)
 
 - As an admin, I would like to be able to Edit exercises within the website(Must have)
 
 - As an admin, I would like to be able to Delete exercises within the website(Must have)

#### Completed User stories

**User content**
 
 - As a user, I would like access to a navigation bar and footer so I can easily navigate the website(Must have)
 
 - As a user, I would like the site to be responsive so I can access it on multiple devices(Must have)
 
 - As a user, I would like to have access to a list of exercises so that I can gather inspiration for my next workout(Must have)
 
 - As a user, I would like to have access to details of each exercise so I can get a better grasp of each individual exercise(Must have)

**Membership and authentication**

 - As an interested customer, I would like to be able to register, sign in and sign out so I can access my membership benefits(Must have)
 
 - As an interested customer, I would like to be able to subscribe for a membership so I can access premium website functionality(Must have, 
 this user story was originally --As an interested customer, I would like to be able to pay for my membership with a recurring fee so I dont need to worry about paying.
 This user story was altered after initially setting this due to being out of scope of the project. More about this on user story testing)

**Members only content**
 
 - As a signed-in user, I would like to be able to save exercises as favourites so I can easily come back to them(Must have)
 
**Admin content**
 
 - As an admin, I would like to be able to Create new exercises for the website(Must have)
 
 - As an admin, I would like to be able to Edit exercises within the website(Must have)
 
 - As an admin, I would like to be able to Delete exercises within the website(Must have)


#### Incomplete/Undone User stories

**User content**
 
 - As a user, I would like to be informed of any discounts the gym may be doing so I can save money(Should have)
 
 - As a user, I would like to have access to a gallery so I can view pictures of the gym and understand if it is right for me(Could have)
 
 - As a user, I would like to be able to book a visit so I can decide if the gym is right for me(Could have)

**Membership and authentication**
 
 - As a signed-in user, I would like to be able to cancel my membership so I can stop my gym payments(Originally Must have, now Wont do as recurring payments
 will no longer be applied in the project there is no further need for a cancel membership functionality)

**Members only content**
 
 - As a signed-in user, I would like to be able to filter the exercises in my favourites list so I can easily access specific exercises (Should 
 have)
 
 - As a signed-in user, I would like to be able to add my fitness goals 
 so I can have them on my profile(Should have)
 
 - As a signed-in user, I would like to be able to update my fitness goals so I can keep it updated(Should have)
 
 - As a signed-in user, I would like to receive personalised workouts which are based on my goals so I can get better results faster(Could 
 have)
 
 - As a signed-in user, I would like to be able to search for exercise content on the exercise list so I can find exercises faster(Could have)
 
 - As a signed-in user, I would like to be able to filter exercise search results on the exercise list so I can find exercises faster(Could have)

**Admin content**
 
All admin user goals created

### Scope

#### Consistent features implemented

**Navbar not authenticated**

![Navbar not authenticated]()

For users to be able to navigate around the website we have implemented a main navigation bar which is available across all pages of the website. On every single page the navbar will be the same.

**Navbar authenticated**

![Navbar authenticated]()

The same as the previous navbar except with the additional option to sign up for a membership

**Navbar with membership**

![Navbar not authenticated]()

The same as the previous navbar except with additional functionality of having an additional favourite list where users can find their favourite exercises which they have saved

**Navbar consolidated**

![Navbar consolidated]()

To account for multiple devices the navbar is also available in a consolidated format where the nav links will be removed and an icon will appear instead. The icon can be clicked for the navbar to then have a dropdown appear with all the nav links.

**Social media icons**

![Social media icons section]()

Nowadays your social media exposure tends to play a big role in driving sales and increasing footfall for your website. Each individual icons opens a new tab leading the users to the social media site of their choosing.

**Footer**
 
![Footer]()

The footer contains crucial information users need like contact details, gym details and we have also included some extra useful resources which users can use.


**Nav and Footer links**

![Nav links]()

Each navigation link is styled in the same way to have a consistent feel across the website for the navigation and footer.

![Nav links hovered]()

As an extra style and effect an underline appears under the navigation links.

**Company logo**

![Company logo]()

The company logo, generally a logo would require a certain wow factor and something which makes it stand out from the competition or even just some specific colors which the company would be known for. In my research of gyms and similar websites you do not see this trend, company logo's are simple and straight to the point which is also what I have chosen to incorporate into my website's logo.

**Buttons and CTA buttons**

![Grey button]()

![Red button]()

Within the website we have used  2 different consistent colors across the website for our buttons, these go along with our general color scheme. In addition to using these styles on the buttons across the site we have also implemented these on all the CTA buttons across the website. As they are quite different to our regular nav links they attract the attention of customers making them very accessible and easy to find, ensuring an easy user becoming customer process. 

**Cards**

![Exercise card]()

The cards has been used consistently accross multiple pages where the exercises are available. They are used in a horizontal/vertical manner in the exercise details page and vertical in the favourites and regular exercises list.

#### Unique features implemented 

#### Development life cycle

### Structure

#### Database model

#### Security

#### Applications

### Skeleton

### Surface

#### Colour scheme

#### Typography

#### Imagery

## Testing

## Deployment

### Github guide

### Additional setup DB, CLoudinary, Heroku, env.py

## Credits
### Content

### Technologies used

### Code and Resources used

### Acknowledgements

