
# Pro Gainer

## [ --> View the live deployed project here <-- ](https://pro-gainer-85d1fcf0b9b4.herokuapp.com/)

## Table of contents

## UX
### Strategy
#### Project overview

Welcome to Pro Gainer, a website for individuals to subscribe to a gym membership to have access to the Pro Gainer gym. Members have access to our fantastic premium content of being able to save and access a wide array of different exercises, instructional material on each of these exercises and the ability to keep them in your favourites list. 

The website is focused on providing a gym subscription service for the physical gym which our members can attend, it is located in the heart of hounslow in greater london. Alongside the access for our amazing gym users will be able to access our publicly available exercise list and save any item within this list. Our target clients for the website are a mix of amateur gym enthusiasts, younger individuals  looking to get fit and older individuals looking to stay fit.  

<!-- The website is made using the django framework, each different component is going to be categorized into their own apps. The apps we have in this project consists of the  membership and exercise app. The membership app will -->

#### Project goals

The primary goals of this project are listed below.

- Increase gym revenue through online membership applications

- Translate website visitors into paying customers

- Assist our current members with our online exercise resources to increase customer retention and satisfaction

- Easily add and edit exercises on the website 

Through the easy navigation of the website and smooth UX, the website is an inviting experience for any user. Our clients attending our gym can now use our website as a guide for exercises they may perform in the gym improving each customer's results and satisfaction. 

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

**Membership and authentication(Epic)**
 
 - As an interested customer, I would like to be able to register, sign in and sign out so I can access my membership benefits(Must have)
 
 - As an interested customer, I would like to be able to subscribe for a membership so I can access premium website functionality(Must have, 
 this user story was originally --As an interested customer, I would like to be able to pay for my membership with a recurring fee so I dont need to worry about paying.
 This user story was altered after initially setting this due to being out of scope of the project. More about this on user story testing)
 
 - As a signed-in user, I would like to be able to cancel my membership so I can stop my gym payments(Originally Must have, now Wont do as recurring payments
 will no longer be applied in the project there is no further need for a cancel membership functionality)

**Members only content(Epic)**
 
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

**Admin content(Epic)**
 
 - As an admin, I would like to be able to Create new exercises for the website(Must have)
 
 - As an admin, I would like to be able to Edit exercises within the website(Must have)
 
 - As an admin, I would like to be able to Delete exercises within the website(Must have)

#### Completed User stories

**User content(Epic)**
 
 - As a user, I would like access to a navigation bar and footer so I can easily navigate the website(Must have)
 
 - As a user, I would like the site to be responsive so I can access it on multiple devices(Must have)
 
 - As a user, I would like to have access to a list of exercises so that I can gather inspiration for my next workout(Must have)
 
 - As a user, I would like to have access to details of each exercise so I can get a better grasp of each individual exercise(Must have)

**Membership and authentication(Epic)**

 - As an interested customer, I would like to be able to register, sign in and sign out so I can access my membership benefits(Must have)
 
 - As an interested customer, I would like to be able to subscribe for a membership so I can access premium website functionality(Must have, 
 this user story was originally --As an interested customer, I would like to be able to pay for my membership with a recurring fee so I dont need to worry about paying.
 This user story was altered after initially setting this due to being out of scope of the project. More about this on user story testing)

**Members only content(Epic)**
 
 - As a signed-in user, I would like to be able to save exercises as favourites so I can easily come back to them(Must have)
 
**Admin content(Epic)**
 
 - As an admin, I would like to be able to Create new exercises for the website(Must have)
 
 - As an admin, I would like to be able to Edit exercises within the website(Must have)
 
 - As an admin, I would like to be able to Delete exercises within the website(Must have)


#### Incomplete/Undone User stories

Due to the agile methodology approach taken in this project we have focused on delivering the most important components first. Rather than increasing resources and ofcourse having a deadline which cannot move we instead moved on the scope. Items which were not within project scope due to the limited time factor are found here.

**User content(Epic)**
 
 - As a user, I would like to be informed of any discounts the gym may be doing so I can save money(Should have)
 
 - As a user, I would like to have access to a gallery so I can view pictures of the gym and understand if it is right for me(Could have)
 
 - As a user, I would like to be able to book a visit so I can decide if the gym is right for me(Could have)

**Membership and authentication(Epic)**
 
 - As a signed-in user, I would like to be able to cancel my membership so I can stop my gym payments(Originally Must have, now Wont do as recurring payments
 will no longer be applied in the project there is no further need for a cancel membership functionality)

**Members only content(Epic)**
 
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

To improve overall user experience and increase uniformity across the whole website we have implemented consistent features which persist on each page where these features are found. 

**Navbar not authenticated**

![Navbar not authenticated](./static/images/readme/navbar_not_authenticated.PNG)

For users to be able to navigate around the website we have implemented a main navigation bar which is available across all pages of the website. On every single page the navbar will be the same.

**Navbar authenticated**

![Navbar authenticated](./static/images/readme/navba_authenticated.PNG)

The same as the previous navbar except with the additional option to sign up for a membership

**Navbar with membership**

![Navbar authenticated and member](./static/images/readme/navba_authenticated_member.PNG)

The same as the previous navbar except with additional functionality of having an additional favourite list where users can find their favourite exercises which they have saved

**Navbar consolidated**

![Navbar consolidated](./static/images/readme/navbar_consolidated.PNG)

To account for multiple devices the navbar is also available in a consolidated format where the nav links will be removed and an icon will appear instead. The icon can be clicked for the navbar to then have a dropdown appear with all the nav links.

**Social media icons**

![Social media icons section](./static/images/readme/social_media_section.PNG)

Nowadays your social media exposure tends to play a big role in driving sales and increasing footfall for your website. Each individual icons opens a new tab leading the users to the social media site of their choosing.

**Footer**
 
![Footer](./static/images/readme/footer.PNG)

The footer contains crucial information users need like contact details, gym details and we have also included some extra useful resources which users can use.


**Nav and Footer links**

![Nav links](./static/images/readme/navbar_link.PNG)

![Footer links](./static/images/readme/footer_link.PNG)

Each navigation link is styled in the same way to have a consistent feel across the website for the navigation. The footer has the same styles just reversed for hover effects to make it obvious it is a link.

![Nav links hovered](./static/images/readme/navbar_link_hovered.PNG)

![Footer links hovered](./static/images/readme/footer_link_hovered.PNG)

As an extra style and effect an underline appears under the navigation links and the reverse for the footer.

**Company logo**

![Company logo](./static/images/readme/company_logo.PNG)

The company logo, generally a logo would require a certain wow factor and something which makes it stand out from the competition or even just some specific colors which the company would be known for. In my research of gyms and similar websites you do not see this trend, company logo's are simple and straight to the point which is also what I have chosen to incorporate into my website's logo.

**Buttons and CTA buttons**

![Grey button](./static/images/readme/grey-btn.PNG)

![Red button](./static/images/readme/red_btn.PNG)

Within the website we have used  2 different consistent colors across the website for our buttons, these go along with our general color scheme. In addition to using these styles on the buttons across the site we have also implemented these on all the CTA buttons across the website. As they are quite different to our regular nav links they attract the attention of customers making them very accessible and easy to find, ensuring an easy user becoming customer process. 

**Cards**

![Exercise card](./static/images/readme/exercise_card.PNG)

The cards has been used consistently accross multiple pages where the exercises are available. They are used in a horizontal/vertical manner in the exercise details page and vertical in the favourites and regular exercises list.

**Form inputs**

![Form inputs](./static/images/readme/form_input.PNG)

Across the site we have implemented the same style for our form inputs, a sharp edged theme. We have maintained this in each input from authentication to all others to keep unfiromity and consistency for the entire website.

**Django messages**

![Django message success](./static/images/readme/django_message.PNG)

To ensure a greate user experience we display user feedback for every user interaction,Django messages is one of the ways we do this. After a user interaction, they are redirected to the next corresponding page if necessary and given an appropriate message where necessary. We deliver the message based on the user interactions, we deliver these messages in a different style for errors and success messages.

**Profile icon**

![Profile icon](./static/images/readme/profile_icon.PNG)

To further assist users in ease of navigation we ahve implemented a profile user icon dropdown menu. Here you can find profile related content like having a look at your user profile and being able to logout of your account.

**Pagination**

![Pagination controls](./static/images/readme/page_controls.PNG)

Used on both the exercise list and favourite list page the pagination controls help with user experience, website performance and improves page load times. Dividing up content for large amounts of data is important and is prevalent in modern day programming. This is especially important when considering that for each item in the exercise list this would load an image. Considering an image loading for each item if no pagination controls were implemented the wait times could potentially be very long.

**Page title**

![Page title](./static/images/readme/page_title.PNG)

A page title pertaining to the page the user is currently on is displayed on every page across the website.

#### Unique features implemented 

**Authentication**

Using Django Allauth for our authentication gave us the base templates and functionality. Using the already created templates we tweaked them to our website styles and needs.

![Login page](./static/images/readme/login_page.PNG)

![Signup page](./static/images/readme/signup_page.PNG)

![Reset password page](./static/images/readme/password_reset_page.PNG)

![Logout page](./static/images/readme/logout_page.PNG)

**Exercise List**

All the exercises within the page which has been created by the admins will appear here and be available to all users. Each item will display a bit of information and users can select these to open a details page about the specified item.

![Exercise List](./static/images/readme/exercise_list.PNG)

**Add & Edit exercise page**

When new exercises are to be added or existing ones edited admins can do that here. All edited and newly added items will be added to the database.

![Add and edit exercise page](./static/images/readme/add_and_edit_exercise_page.PNG)

**Exercise Detail**

Each exercise has a detail page which will give detailed information about the exercise. The exercise detail page will also contain the opportunity for members to save the exercise.

![Exercise Detail](./static/images/readme/exercise_detail.PNG)

**Favourite exercises list**

When members add in new favourite exercises those reflect here in the favourite exercises list. Like the exercise list we are also able to select each exercise to redirect us to another page to get more detailed information about the specified exercise.

![Favourite exercises list](./static/images/readme/favourite_exercises_list.PNG)

**Favourite exercise icon**

Using this icon member users are able to save and unsave each exercise to add it to their favourites list.

![Favourite exercise icon not saved]()

Exercise favourited

![Favourite exercise icon saved](./static/images/readme/favourite_icon_red.PNG)

Exercise not favourited

![Not favourite exercise icon](./static/images/readme/favourite_icon_black.PNG)

**Membership subscription page**

After user sign in the membership page becomes available to them and they can apply. The user inputs their data and test card information and after successful form validation they become active members and receive perks.

![Membership signup page](./static/images/readme/signup_page.PNG)

**Checkout success page**

On successful membership checkout the user is redirect to the checkout success page. Here we give the user feedback that their transaction was a success and give them further details about their membership and checkout.

![Checkout success page](./static/images/readme/checkout_success_page.PNG)

**My profile page**

After a user becomes a member they will gain access to the my profile page which displays details about their account and membership.

![My profile page](./static/images/readme/my_profile.PNG)

#### Development life cycle

To display how we have distributed the time used and development cycle of the project as a whole we have created a gantt chart to have a general outlook. The green colored blocks indicate work being performed in that category on that date.

![Gantt chart](./static/images/readme/gantt_chart.PNG)

### Structure

#### Database model

During the planning and preparation stage of my project I created an [ERD(Entity relationship diagram)](https://lucid.app/lucidchart/e56c3df0-fa20-4f96-bbe5-c9a29715c6cb/edit?page=0_0&invitationId=inv_c3f434bb-e3a8-488f-8737-9a391ade7cab#). I used this as a guide for creating my models and made some minor tweaks as I developed the project.

I have 4 models in total, these being Membership, Exercise, Favourite Exercise and django allauth. All models have a relationship excluding the membership model. The relationships of each model are displayed on the diagram, additionally the type of relationship is listed here below. 

Exercise - Favourite Exercise | One - One
User - Favourite Exercise | One - Many

Each exercise can only have a relationship with one favourite exercise as this would basically be an imitation of itself in another model. Each User can have as many favourite exercises as they would like.

#### Security


Django has a lot to offer in terms of its security features, it has a lot built in which is accessible to the developer. In the current information age securing your information is crucial. 

Within this project I have implemented multiple layers of security. User authentication and checks ensures that each individual user can see only their own information. Each user should only be able to read and manipulate their own data.

The implementation of security within this project has been done at a model and a form level to ensure no spoofing is possible. Even if a malicious user attempted to change data within the console(**Spoofing**) they would not be able to submit and propagate this data to the back-end as the model and form requirements would stop it. Additionally to the security on the back-end we also display the errors at the front-end to ensure that users are made aware of any requirements, errors and mistakes. Additional to security measure put in place at the model and forms, we have also placed measures at the view level. Placing security measures at the view level adds another level of security, we can do this with class and function *mixins* and *decorators*.
I opted to use the decorators for this project. The appropriate decorators were added to each view which requires *login* or *admin* permissions. In this way only *logged in* users could access certain functionality and the same goes for *admins* 

**Memberships**

To ensure only users who have an paid for a membership(which is active) has access, we created several measures for security. We have implemented a utils.py method which can be used across the website for both templates and views which ensures reusability and DRY. The method checks both the membership end date and membership activity. With the APScheduler tasks put in place we are able to ensure that if a user's membership end date has passed they no longer have access to the service. As an extra measure even if the APScheduler fails to set the user's membership to inactive the utility checks for membership end so this would not not have an impact.

We have implemented and automatic scheduler using APScheduler to run a *job/task* at specific times of the day, specifically midnight. This task will run through all users which are currently set to active and if the membership end date is in the past set it to inactive. The APScheduler will only work while the server is running, there are better options which were considered like celery and redis however these fell out of scope of the project and APScheduler was used instead.


#### Applications

2 Applications have been made within the project

- membership - The membership app is composed of the membership signup, checkout success and my profile. This contains the model for memberships.
- exercise - The exercise model contains all exercise lists, details and favourites. Full CRUD is contained within the exercise model component for admins to tweak the available exercises. Active members are able to add and delete exercises from their favourites list. This application contains both the exercise and favourite exercise models. `

### Skeleton

**Wireframes**

The tool I decided to go with for my wireframes is [Figma](https://www.figma.com/).
I created the wireframes early on in the project creation as a low fidelity outline for the project layout. The layout of the website in general has stayed the same as intended on project inception. With some changes involved the larger differences will be tweaked in the wireframes. There will be some minor differences in the wireframes compared to the live website and these will be left as is considering these dont affect the purpose of the wireframes which was to create a plan for the general layout. 

- [All pages of my wireframes can be found here](https://www.figma.com/design/tnBvzkh8foONfZI9U8Cm8h/Milestone-projects?node-id=3527-2&p=f)

### Surface

#### Colour scheme

![Colour palette](./static/images/readme/color_palette.PNG)

Considering the customer demographic and consistency across different similar websites I went with a simplistic design. I built the website with a black and white color palette and added colors on gradually. 

The below colour scheme was used in the website:

primary: #f2eee8;

secondary: #e10a0a;

tertiary: #6F6866;

black: #454545;

white: #ffffff;

#### Typography

The typography was also a simplistic choice. Not much variance between headings and general text across the website, the differentiating factor would be the font weight and size.

All details about fonts across the website are found below


H1: 3.125rem - 50px
H2: 2.5rem - 40px
H3: 2.188rem - 35px
H4: 1.875rem - 30px
Subheading: 1.25rem - 20px
Body: 1rem - 16px


Headings: "Roboto", serif;
Body: "Lato", serif;

#### Imagery

For the imagery of the site I decided to go with inspiring images of weightlifting to attract people into the site. When talking about instructional material I wanted a good looking but not complicated imagery considering the likely user paying attention to these images in particular would be at more of a beginner level.
I used the sites listed below to access open source non copyrighted images for my website.

- [Pixabay](https://pixabay.com/)

- [Unsplah](https://unsplash.com/)

I also improved the performance of the website where possible using using [Tiny png](https://tinypng.com/) and [Tiny jpg](https://tinyjpg.com/).

## Testing

Comprehensive testing has been performed for this project, you can find all of the testing in the [testing.md file](./testing.md)

## Deployment

### Github guide

**Cloning**
To clone a repository follow these steps

1. Login in to Github or create an account if you haven't already

2. Go to this project repository [Ember & Ash](https://github.com/JamesBracken/Ember-Ash)

3. Click on the *Code* button and select whether you would like to cline with HTTPS, SSH or the Github CLI and then copy the link shown

4. Open your terminal in your IDE/code editor of choice then change the current working directory to the location you would like to use for the cloned directory

5. Type "git clone" into the terminal and paste the link you copied in the third step then press Enter

6. To install the dependencies you can run **npm install** in your IDE(integrated development environment) terminal, the dependencies you need are listed in the package.json and package-lock.json files

**Commiting and Pushing Changes**

1. Open the termin in the directory of your cloned repository

2. Using "git status" check to see your changes are correct

3. If you are ready to commit  type "git add ." to stage all saved changes to be commited, you can alternatively use "git add YOUR_FILENAME" to stage specific files for commit

4. Using "git commit -m "Write your commit message here" commit your changes with a descriptive message, give a good amount of detail but try not to go over 50 characters

5. Finally use "git push origin main" to push your changes to the main branch of your github repository


**Forking**

To fork this repository follow these steps

1. Setup Git and make sure your git has github authentication

2. Go to the web page repository [Ember & Ash](https://github.com/JamesBracken/Ember-Ash) 

3. Click on *fork* on the upper right portion of the page.

4. This has now forked the repository to your own profile. 

5. Go to your profile and navigate to the forked repository.

6. Click on *Code* above the list of forked files

7. Choose the option you need from the dropdown menu. 

Further assistance can be found [HERE](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) on the github Fork a Repo page


**Local development**

1. Clone your repository from Github, you can find the "Code" button where you can copy the url from

2. Open your IDE and open a terminal, make sure you are in the correct directory where you want to clone the repository to.

3. Type git clone URL, replace URL with the one you just copied in the first step

4. Setup your virtual environment, type the below commands

- python3 -m venv [virtual_environment name]

5. Activate your virtual environment, type the below commands

- Windows: myvenv\Scripts\activate

- Linux/Mac: source myvenv/bin/activate

6. Type the below items into your IDE terminal, this will install all packages
    pip install -r requirements.txt

**If you want to install your own packages** here is some extra step-by-step instructions and examples:

- Type the below items into your IDE terminal
    pip install Django~=3.2 gunicorn (NOTE: try to use pip3 instead if this does not work)
- Install libraries your project will need like Postgresql(Handles database), psycopg2(Adapter for Postgresql), cloudinary storage(Allows long term storage of static files I.E. images) and whitenoise(serves compressed content)
    pip install dj_database_url psycopg2
    pip install dj3-cloudinary-storage
- Create your requirements.txt file, this is a list of your installed packages so everytime you install a new package you will need to update it like this
    pip freeze --local > requirements.txt

7. Setup environmental variables, scroll down to Environmental Variables section

8. Connect your database by typing this in the terminal(This runs your migrations):

- python manage.py migrate

9. Create a superuser account by typing into the terminal:

- python manage.py createsuperuser

10. You can run the app in a local environment by typing:

- python manage.py runserver

11. If you want to open a deployed version of your app see the steps below in **Heroku deployment**

### Additional setup DB, CLoudinary, Heroku, env.py

**Adding your database**

1. Navigate to [PostgreSQL from code institute](https://dbs.ci-dbs.net/)

2. Enter your student email address and then submit

3. You will be sent an email with a link, copy the link

4. Back in your workspace, ensure Debug is set to True

5. Create you env.py file if you dont have one already and add this to .gitignore

6. Inside your env.py add the below code and replace "your-database-URL" with the link you copied from the email in step 3

- import os

- os.environ.setdefault(
    "DATABASE_URL", "your-database-URL")

7. If you haven't already do 
- pip3 install dj-database-url~=0.5 psycopg2~=2.9

- pip3 freeze --local > requirements.txt

8. In your settings.py import the packages like below

- import os
- import dj_databse_url
- if os.path.isfile('env.py'):
    import env

9. Still in your settings.py comment out the default django sqlite3 database

10. Add in you own database with the below syntax

- DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

11. Migrate your changes with python manage.py migrate

12. You have now successfully connected your database withthe project and can now add data in your local development. To connect your deployed version on heroku with the database continue with the next steps.

13. If you haven't already, deploy your project to heroku(steps for this are found after database guide)

14. Navigate to the settings tab of your project and press reveal config vars

15. If there is a database added by default by heroku delete this as we will replace it with our own(If heroku has not added one skip to step 18)

16. To remove the heroku database navigate to Resources, go to the drop-down on the top right of the Postgres add-on and click Delete Add-on. Confirm this by typing your app's name into the popuo

17. Navigate back to the settings tab and to config vars

18. Add a new config var with a key of DATABASE_URL and a value of the PostgreSQL link that we copied from the email in step 3

19. You have successfully added your database to the deployed version of your website

**Adding Cloudinary to your project**

1. Install the nevessary packages with the commands below and add them to your requirements.txt file

- pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15

- pip3 freeze --local > requirements.txt

2. Go to [this link](https://cloudinary.com/users/register_free) to create a cloudinary account

3. In the Cloudinary dashboard, copy the CLOUDINARY_URL

4. In your env.py file add the code below and paste in the copied url from step 3 

- os.environ.setdefault(
    "CLOUDINARY_URL", "URL copied from Cloudinary in last step")

5. Delete the CLOUDINARY_URL= from the start of the URL string as we are using the setdefault() method rather than assigin the value.

6. Navigate to your settings.py and inside the INSTALLED_APPS add the below items

**Important!** cloudinary_storage must be added immediately after django.contrib.staticfiles
- 'cloudinary_storage',

- 'cloudinary',

7. You can now use Cloudinary in any app in your project

**Heroku Deployment**
1. Ensure the project repository has been uploaded to Github.

2. Login to the Heroku dashboard and create a new app.

3. Connect your GitHub repository to your Heroku app.

4. In the Settings tab, ensure that the Python Buildpack is added.

5. Set environment variables in the Config Vars section of the Settings tab.

6. In the Deploy tab, enable automatic deploys from your GitHub repository.

7. Click the "Deploy Branch" button to deploy the app.

8. Once the app has been deployed, click the "Open App" button to view the app.

**Environmental variables**

Environment Variables
For local deployment, you will need to create a .env file in the root directory of the project and set the environment variables in this file. This is to make sure sensitive information is separated from other code.

Ensure the .env file is included in the .gitignore file to exclude it from your GitHub repo to prevent the file and its contents from being publicly exposed.

For Heroku deployment, you will need to set the environment variables through the Heroku CLI or through the Heroku dashboard under 'Config Vars'.

You need to define the following environment variables:

SECRET_KEY(In both Heroku and env.py): The secret key for your Django project. This is a critical setting that's used for cryptographic signing, and should be kept secret at all times. It's used to provide cryptographic signing, and should be a long, random string of bytes.

DEBUG(In both Heroku and env.py): A boolean that turns on/off debug mode. Set to True for development to enable detailed error pages and logging for debugging. Set to False in production to improve performance and security.

DATABASE_URL(In both Heroku and env.py): The URL for your database. This should include the database engine, username, password, host, port, and database name. For a Postgres database, it typically looks like postgres://USER:PASSWORD@HOST:PORT/DB_NAME.

CLOUDINARY_API_KEY: Your Cloudinary account's API key. This key is used to authenticate requests to Cloudinary's services for uploading and managing images and other media assets.

CLOUDINARY_API_SECRET: Your Cloudinary account's API secret. This secret is used alongside the API key to securely sign requests to Cloudinary.

CLOUDINARY_CLOUD_NAME: Your Cloudinary account's cloud name. This is the unique name that identifies your cloud within Cloudinary. It's used in the URL structure for accessing uploaded resources.

STRIPE_SECRET_KEY: Your stripe secret key, this can be found in the stripe dashboard on the right under API keys.

STRIPE_PUBLIC_KEY: Your stripe public key, this can be found in the stripe dashboard on the right under API keys.

STRIPE_WEBHOOK_SECRET: In the developers section in webhooks you can find the webhook secret. Use this to test stripe webhooks.

Note: The following CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_SECRET and CLOUDINARY_API_KEY can be placed in 1 config var in heroku and need to also be added to the settings.py file in this format: 

Local example:
CLOUDINARY_URL=cloudinary://<CLOUDINARY_API_KEY>:<CLOUDINARY_API_SECRET>@<CLOUDINARY_CLOUD_NAME>

Heroku example:
Key: CLOUDINARY_URL
Value: cloudinary://<CLOUDINARY_API_KEY>:<CLOUDINARY_API_SECRET>@<CLOUDINARY_CLOUD_NAME>

**Stripe setup**

To setup the config var
- Log in to your Stripe account - create one if necessary
- Add STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY to the Heroku config vars, assign these variables values from your Stripe account dashboard
- Create a webhook endpoint for use with your applications. On the stripe dashboard go to the Developers -> Webhooks area, click add endpoint, use the url of your Heroku application with '/checkout/wh/' tagged onto the end of the url string. When configuring the endpoint, the events to register to listen to are payment_intent_succeeded and payment_intent_failed
- Once the endpoint is set up get the signing secret for the webhooks and save this value as a Heroku config var called STRIPE_WEBHOOK_SECRET.

## Credits
### Content

No code was copied from external resources, I did take some components of code for the Readme and the social media section from [my Ember and Ash project](https://github.com/JamesBracken/Ember-Ash). Official documentation supplied the base for some of the code within the website. All code which was taken from documentation has been commented and the url added to the code.

### Technologies used

1. [Django](https://www.djangoproject.com/) - Django is a high level framework used to rapidly take python projects from start to finish. Using django a developer can use existing codebases and shortcuts to ease and speed up the development process.

2. [PostgreSQL](https://www.postgresql.org/) - PosgreSQL is a powerful, open source object-relational database system.

3. [Code institute provided database generator](https://dbs.ci-dbs.net/) - A database generator provided by Code Institute to store data across projects.

4. [VS code](https://code.visualstudio.com/) - The most widely used IDE across the planet, we use vs code as our integrated development environment.

5. [Cloudinary](https://cloudinary.com/) - An fast scalable online media management platform

6. [Git](https://git-scm.com/) - A version control system designed to handle everything from small to large projects  

7. [GitHub](https://github.com/) - A platform for displaying code project version, deployments and developer profiles

8. [Github desktop](https://desktop.github.com/download/) - An app used to ease version control. 

9. [Figma](https://www.figma.com/) - An application used to make wireframe drawings

10. [TinyPNG](https://tinyjpg.com/) - Converts images into JPG format and compresses files to improve performance

11. [TinyJPG](https://tinypng.com/) - Converts images into PNG format and compresses files to improve performance

12. [Pixabay](https://pixabay.com/) - A media website including free and open source images

13. [Pexels](https://www.pexels.com/) - A media website including free and open source images

14. [Django widget tweaks](https://pypi.org/project/django-widget-tweaks/) - Used to tweak form fields within the project

15. [Gunicorn](https://gunicorn.org/) - A python WSGI HTTP server 

16. [Whitenoise](https://whitenoise.readthedocs.io/en/latest/) - Serves static files for projects in production

17. [Dj Database URL](https://pypi.org/project/dj-database-url/) - Connects our website with the database

18. [Psycopg2](https://www.psycopg.org/docs/) - PostgreSQL database adapter for python

19. [Chatgpt](https://chatgpt.com/) - Used to populate data in the project such as add menu items

20. [Favicon](https://favicon.io/favicon-generator/) - Generates a favicon for websites

21. [Bootstrap](https://getbootstrap.com/) - Used to create the Navigation bar, page structure, styles and responsiveness

22. [Google fonts](https://fonts.google.com/) - Generates fonts for the project

23. [Heroku](https://www.heroku.com/) - Used to deploy and manage a production ready version of the website

24. [Lucidchart](https://www.lucidchart.com/pages/examples/er-diagram-tool) - Used to create entity relationship diagrams 

### Code and Resources used


1. [Stackoverflow](https://stackoverflow.com/questions) - Platform and community where developers can ask questions and get assistance from eachother

2. [W3schools docs](https://www.w3schools.com/) - Lots of useful resources and guides for all programming languages in this project

3. [Mdn docs](https://developer.mozilla.org/en-US/) - Lots of useful resources and guides for all programming languages in this project

4. [Bootstrap docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - Documentation for the bootstrap web library 

5. [Django project docs](https://www.djangoproject.com/start/) - Lots of useful documentation and guidance, especially for me to grasp and learn new concepts in the django framework

6. [Kevin powell how to make a color scheme fast](https://www.youtube.com/watch?v=mq8LYj6kRyE&list=PLpAzc76TtoBzvtYIZAhfJzDxvas0GmI7O) - Great guide on how to create your color scheme

7.[Guide to relational databases](https://www.youtube.com/watch?v=fXndSzAL1Nc&list=PLpAzc76TtoBzvtYIZAhfJzDxvas0GmI7O&index=2) - Crucial guide I used to help grasp the concepts of relational databases

8. [Fantastic video about normalizing your database](https://www.youtube.com/watch?v=UrYLYV7WSHM&list=PLpAzc76TtoBzvtYIZAhfJzDxvas0GmI7O&index=5) - A guide to normalise your database, with this I was able to create an optimal schema for my database and separate data into different tables to maximise performance and follow best practices. Best guide I have seen by far on databases. Simple and informative.

9. [Creating a Django restaurant booking site](https://www.youtube.com/watch?v=EI02wQ51GjA&list=PLBTOBXTz1YFZK0moSgoZq93V_AdvrUGSj) - Great guide which I watched to cement my understanding of django and give me inspiration and ideas on how to build my website, simple and straightforward explanations

10. [Guide to how ajax login works with django](https://www.youtube.com/watch?v=DvzE9tVFkSA&list=PLpAzc76TtoBzvtYIZAhfJzDxvas0GmI7O&index=15) - Slightly outdated video, but helped me grasp the concepts of how to use AJAX for error handling in my login modal.

11. Brian macharia(My mentor) - No link provided as these were privately shared resources for his students. Big shoutout to my mentor who provided tons of useful links to useful resources, guides and tutorials for this project. 

12. Code institute Boutique Ado project - Through this practice project I was able to get an insight into how an ecommerce website is built. This project has a large part to play in the building of this project especially for the stripe element component.

13. Stripe docs - I used the [stripe documentation](https://docs.stripe.com/?locale=en-GB) to help guide me through the implementation of stripe elements

14. Ember and Ash - My previous project [Ember and Ash](https://github.com/JamesBracken/Ember-Ash) which I took some components from

15. Error handling - I used [BetterStack](https://betterstack.com/community/guides/scaling-python/error-handling-django/) to get an understanding of how to render the error pages for the project. 

### Acknowledgements

A big thank you to my mentor **Brian Macharia** who gave me high level guidance for the project and to my teacher **Andre Beckley** who guided me through the website build.

A thanks as well to all the help and support from stackoverflow and the coding community. The helpfulness and support we all provide eachother was instrumental to making this project possible.