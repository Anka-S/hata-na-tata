# Hata na Tata

Cosy website for Ukrainian restaurant "Hata na Tata" with national Ukrainian cuisine 

## Live website

The live link can be found here - [Hata na Tata](https://hata-na-tata-ca376c445d63.herokuapp.com/) 

![Hata na Tata responsive screenshot](docs/final_views/amiresponsive.webp)
## Purpose of the project
Hata na Tata is a web application that was built for a fictitious restaurant with Ukrainian national cuisine "Hata na Tata".  The purpose of this website is to engage people to familiarise themselves with Ukrainian cuisine, book a table and leave reviews on the restaurant's site after visiting. The development is focusing on Django and Bootstrap frameworks, Database manipulation and CRUD functionality.

<hr>

## Table of Contents

- [Hata na Tata](#hata-na-tata)
  - [Purpose of the project](#purpose-of-the-project)
  - [Table of Contents](#table-of-contents)
- [UX/UI](#uxui)
  - [UX - User Expirience](#ux---user-expirience)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [Existing features](#existing-features)
  - [Features left to implement](#features-left-to-implement)
- [Testing](#testing)
  - [Validator testing](#validator-testing)
- [Unfixed bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)


# UX - User Expirience

## User Stories:

- Product Owner:
  - As a Product Owner, I want to see that my site is working properly on different devices, so users will have the best experience
  - As a Product Owner, I want to display menu section as a navbar, so it will be easier for the User to navigate through the website.
  - As a Product Owner, I want to tell the User about the creators of the restaurant, so User will be engaged to visit the restaurant

- Admin
  - As an Admin, I want to add/update/delete the information on the Menu page, so the user can choose from the valid dishes
  - As an Admin, I want to approve or disapprove reviews, so that I can filter out objectionable reviews

- User
   -  As a User, I want to easily navigate through the website, so I would have a positive experience
   - As a User, I want to know on which page I am, so it will be easier to navigate through the site
   - As a User, I want to see the menu on the website, so I can choose what I want to eat
   - As a User, I want to leave a review, so I can share my experience with other users
   - As a User, I want to book the table, so I can plan my time
   - As a User, I want to register an account, so I can book the table and leave reviews
   - As a User, I want to see if I am logged in or not, so I will have a positive UX 

## Design Inspiration

When I planned to create this project, I dicided to use Ukrainian national rushnyk and kalyna on the table as a background. After this I picked up the colours for text and content. 

![Hata na Tata background image](static/media/bg.webp)
*Background image*

### Colour Scheme

As a main colours, I used ```white``` colour for my text and ```rgba(0, 0, 0, 0.518)``` for block background to make content more readable.

Colour Blind Safe and contrast was checked by [Adobe Color](<https://color.adobe.com/create/color-accessibility>)

![Color Blind Safe](docs/color-blind-safe.webp)
*Accessibility check for colour scheme*

![Contrast Checker](docs/contrast-checker.webp)
*Contrast checker*

![Colour Scheme](docs/colour-scheme.webp)
*Colour Scheme*

### Font

Using [Google Font](<https://fonts.google.com/>), I imported "Montserrat" and "Bricolage Grotesque" to my CSS file. I set "Montserrat" as my default font. I used "Bricolage Grotesque" as a font for content on my menu page and for authorisation pages.






## Wireframes

__Browser View:__

<details open>
    <summary>Browser view of home page for logged in user</summary>  
    <img src="docs/wireframes/home-loggedin.webp">  
</details>

<details>
    <summary>Browser view of home page for logged out user</summary>  
    <img src="docs/wireframes/home.webp">  
</details>

<details>
    <summary>Browser view of menu page</summary>  
    <img src="docs/wireframes/menu.webp">  
</details>

<details>
    <summary>Browser view of reviews page for logged in user</summary>  
    <img src="docs/wireframes/reviews-loggedin.webp">  
</details>

<details>
    <summary>Browser view of reviews page for logged out user</summary>  
    <img src="docs/wireframes/reviews.webp">  
</details>

<details>
    <summary>Signup form</summary>  
    <img src="docs/wireframes/signup.webp">  
</details>

<details>
    <summary>Form for writing review</summary>  
    <img src="docs/wireframes/reviewform.webp">  
</details>

__Phone View:__

<details open>
    <summary>Phone view of home page for logged in user</summary>  
    <img src="docs/wireframes/mhome-loggedin.webp">  
</details>

<details>
    <summary>Phone view of home page for logged out user</summary>  
    <img src="docs/wireframes/mhome.webp">  
</details>

<details>
    <summary>Phone view of menu page</summary>  
    <img src="docs/wireframes/mmenu.webp">  
</details>

<details>
    <summary>Phone view of reviews page for logged in user</summary>  
    <img src="docs/wireframes/mreviews-loggedin.webp">  
</details>

<details>
    <summary>Phone view of reviews page for logged out user</summary>  
    <img src="docs/wireframes/mreviews.webp">  
</details>

# Features 

Detailing the existing and planned features and the value they bring.

## Existing Features

 __The Background Image__

- Presents a rushnyk - traditional Ukrainian cloth that serves both practical and ceremonial purposes. The term originates from the Ukrainian word "ruka," meaning "hand," and while it can refer to an ordinary towel, it is more commonly associated with ritualistic uses in cultural ceremonies across Ukraine.
![Background image](static/media/bg.webp)

 __The Logo Image__

- I designed an app for restaurants featuring a striking logo that showcases a stylized fork and spoon crossed beneath a chef's hat. The design is rendered in bold black and red colors for a visually appealing and memorable look. Also this logo used as a Favicon for the page. 
![Logo image](static/media/logo-text.webp)

 __Contact section__

- On the main page, the user can find the contact section with phone number and email. When you click on email, it will automatically redirect you to the mailbox for writing an email to the restaurant. Also, users can find the map with the restaurant's location on it.
![Contact section](docs/features/contact-section.webp)

 __Navbar Menu__

- For better user experience, navigation links are located to right side of the navbar. I used white transparent background and black text to separate it from the other content. Also, I added logo image and the name of the restaurant to the left side of navbar on every page, despite main pages.
![Navbar on main page desktop view](docs/features/navbar-desktop-main.webp)
![Navbar on desktop view](docs/features/navbar-not-main.webp)
- For the small devices I added burger menu and logo with the name of the restaurant to the every page. Also, links are located to the right sight.
![Navbar burger menu](docs/features/mobile-navbar.webp)

__Logged in/logged out user message__

- The user will be informed whether they are logged in or not.
![Message](docs/features/message-login:out.webp)

__Booking Model__

- This reservation system enables users to easily book a table for evening dining. Key features include:
Guest Capacity: Choose from a limited selection of party sizes.
Time Slots: Select from a few predefined evening time options.
User-Friendly: Simplified choices streamline the booking process.
This model enhances customer convenience while helping restaurants manage reservations effectively. 
![Time choices](docs/features/times.webp)
![Guest choices](docs/features/guests.webp)
![Booking Model](docs/features/booking.webp)

__Toast Messages__

- When you interact with the website, you'll receive toast messages that inform you about the success or failure of your actions. Whether you’re making a booking, registering, logging in or out, or adding a review, these notifications will provide immediate feedback on your activities. 
![Booking success](docs/features/booking-toast-msg.webp)
![Toast message](docs/features/toast-messages.webp)

__Menu Page__

- On the menu page, you can explore detailed information about the dishes offered by the restaurant, organized into distinct sections for an enhanced user experience. One notable feature of the menu items is the use of logo images as placeholders, which are displayed when a specific dish image is not available.
![Menu page](docs/features/menu-page.webp)
![Menu image placeholder](docs/features/menu-img-placeholder.webp)

__Review Page__

- On this page, you can read reviews and leave your own if you are logged in. Additionally, you have the option to edit or delete your own reviews. 
![Review](docs/features/review-view.webp)
![Write review](docs/features/write-review.webp)

-  If you choose to delete your review, a confirmation message will appear to verify your decision before proceeding.
![Delete confirm](docs/features/delete-alert.webp)

- If you decide to edit your review, you will be redirected to a separate page featuring the review form. There is also an option to cancel your changes if you change your mind.
![Edit page](docs/features/edit-page.webp)


__Authorisation__

- Users can register, log in, and log out. Once authorized, they can access features such as making reservations and submitting reviews.
![Sign Up](docs/features/registerform.webp)
![Log In](docs/features/login.webp)
![Log Out](docs/features/signout.webp)
![Authorized user](docs/features/write-review-anchor.webp)
![Non-authorized user](docs/features/not-login-book.webp)
![Non-authorized user](docs/features/not-login-review.webp)


__The Footer__ 

- The footer section includes links to the relevant social media sites of Hata na Tata restaurant. The links will open to a new tab to allow easy navigation for the user. 
- The footer is valuable to the user as it encourages them to keep connected via social media
![Footer](docs/features/footer.webp)



## Features Left to Implement

- In the future, I plan to include an About page. Additionally, I would like to enhance the booking form by adding a validator to manage limited table availability. 
- For the contact section, I aim to implement a form that allows users to send emails directly from the website without needing to open their mailbox.


## Testing 

This app was tested on different devices:

__Desktop__

__Redmi 8 Pro__

__iPhone 12 Pro__

__iPad Air 2__

__iPhone SE__

<hr>

### Validator Testing 

- HTML
  - [W3C validator](https://validator.w3.org/#validate_by_input)
 

- CSS
  - [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)
 

- JavaScript
   -  [JSHint](https://jshint.com/)
  

- LightHouse
  - The lighthouse test is used to give a score for performance, SEO, accessibility and best practices.



- Wave
  
 

## Unfixed Bugs


## Deployment


## Credits 


### Content 

- Icon for webpage created with Favicon generator (https://realfavicongenerator.net/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)
- The CDN framework used for ready-made styling was [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/download/)
- Balsamiq used for wireframe
- [Perplexity](https://www.perplexity.ai/) used for debugging 
- [Miro boards](https://miro.com/app/board/uXjVK1tCs_I=/) used for planning the work process


### Media