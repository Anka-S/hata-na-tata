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

![Browser view of home page for logged out user](docs/wireframes/home.webp)
![Browser view of menu page](docs/wireframes/menu.webp)
![Browser view of reviews page for logged in user](docs/wireframes/reviews-loggedin.webp)
![Browser view of reviews page for logged out user](docs/wireframes/reviews.webp)
![Signup form](docs/wireframes/signup.webp)
![Form for writing review](docs/wireframes/reviewform.webp)

__Phone View:__
![Phone view of home page for logged in user](docs/wireframes/mhome-loggedin.webp)
![Phone view of home page for logged out user](docs/wireframes/mhome.webp)
![Phone view of menu page](docs/wireframes/mmenu.webp)
![Phone view of reviews page for logged in user](docs/wireframes/mreviews-loggedin.webp)
![Phone view of reviews page for logged out user](docs/wireframes/mreviews.webp)

## Features 

Detailing the existing and planned features and the value they bring.

### Existing Features

- __The Hero Image__

  - Presents a rushnyk - traditional Ukrainian cloth that serves both practical and ceremonial purposes. The term originates from the Ukrainian word "ruka," meaning "hand," and while it can refer to an ordinary towel, it is more commonly associated with ritualistic uses in cultural ceremonies across Ukraine.

- __The Footer__ 

  - The footer section includes links to the relevant social media sites of Hata na Tata restaurant. The links will open to a new tab to allow easy navigation for the user. 
  - The footer is valuable to the user as it encourages them to keep connected via social media


### Features Left to Implement



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