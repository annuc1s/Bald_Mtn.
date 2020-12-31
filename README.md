# BALD_MTN
is inspired by the current situation of GLOBAL WARMING. We all have to do our bit in reversing
the already visible devestation. Bald_mtn is Boutique e-commerce store selling organic or
upcycled products. These products have minimal carbon-footprint on our planet and are sustainable
and bio-degradable. Each piece tells a story in hopes to make the future consumer decide in favour 
of our planet.

## UX

This website is for both the customer and the business owner. 

### User stories
As a user …
  * I would like to access the website from my device, so I can view the products.
  * I would like to have an intuitive experience while visiting the website with easy navigation.
  * I would like to search for a specific product using a keyword, so I can easily find what I am looking for.
  * I would like to sort through the products so that I can find the best value or best rated product.
  * I would like to view the product description to learn more about the product.
  * I would like to have a choice in size to match the best fit for me.
  * I would like to add multiple items to my cart.
  * I would like to preview my cart before checkout in case I need to make a change.
  * I would like to have the option to edit or delete items from my cart.
  * I would like to checkout quickly and securely as a guest.
  * I would like to create an account to save my purchase history and delivery details for a more convenient experience in the future.
  * I would like to review products I have purchased and share my experience with others.
  * I would like to subscribe to newsletters for any updates and special offers regarding the business.
  *  I would like to contact the business with any queries by phone, email or a contact form.
  * I would like to learn more about the business and their ideologies to make a decision about supporting this business.
  * I would like to follow the businesses social media for the latest updates.
  * I would like to view an order confirmation after checkout and receive an email confirmation to keep as a record of my purchase.

As a store owner/manager…
  * I want to be able to add a new product to the site.
  * I want to be able to edit an existing product.
  * I want to be able to delete a product that should no longer be for sale.
  * I want to be able to view user orders to be able to satisfy their orders.
  * I want to be able to view product popularity and demand though customer orders.
  * I want to be able to add sales to items.
  * I want to maximise sales.



### Wireframes

These wireframes, show many features that I didn't get a chance to implament for this project
due to the time constraint, but will revisit at a later time to build the website to it's 
full potential.

[View wireframes here!](https://photos.app.goo.gl/5jJoZgLj8kAEZv9e8)

## Features

### Existing Features

    * Navigation-Bar: Allows the user to easily and intuitively navigate the website. It is fixed so as 
    they move down the page it follows and they can at any point change their location on the site.

    * Hero-image & slogan: Create a strong first impression and prompt the user to interact with the button 
    which redirects them to the sign-in page. 

    * New-Arrivals: Provides the customer with a preview of some of the products available from the full shop.

    * Contact Form: Allows the customer to interact with the business by sending an email. An automated response 
    is sent back straight away to let them know that the business has received the email and will answer 
    the query promptly. 

    * Google API: Provides the exact location of the business via google maps. 

    * External Social-Media Links: Invites the customer to follow the businesses social media to keep up to date.

    * Sign-Up: Allows the user to create an account in order to make a reservation.

    * Sign-In: Allows the user to access their existing account in order to make a reservation.
    
    * Messages: When the user does an action a message promp display to review that action. They can also preview their
    bag items.

    * Bag-Review: Allows the user to review the items in their basket as well as update or remove items.
    
    * Checkout: Allows the customer to checkout securely and also save their delivery details for future purchases.

    * Account: Allows the user to log in to their account and view their order history or change their delivery details
    
    * Search Bar and Sort: Allows the user to find what they are looking for a lot easier.
    
    * Shop: The customer can have a quick preview of items avaialable in the store.
    
    * Product Details: The customer can learn more about each product and decide if they want to purchase this item. They can also 
    pick size and quantity or return to the main store page.


### Features Left to Implement

This website is just a snippet of what I imagine it to be. In the future I hope to expand it:

    * About: When Deploying the website, the images were lost.
    
    * Quick add to basket from main shop page.
    
    * Sign up to newsletter

    * A more user friendly way to add/update products to the shop for superuser, other then using database.

    * Create a live customer review platform. 
    
    * If store has more products create category sorting.


## Technologies Used

In order to create this project I used sever technologies:

    * CSS3: Used to add and change default HTLM styling.
    
    * Bootstrap Template: Used as the main Css template.

    * HTLM5: Was used to create the structure for the app.

    * Javascript: Was used to create functions to make the app more interactive. To create a responsive nav-bar
    introduce EmailJS and GoogleAPI, etc.

    * Python: Used to create the back-end longic of this e-commerce website

    * Github: Was used as a remote repository where the changes were commited and pushed to.

    * Gitpod: Was used as an environment for where the code was developed.

    * Heroku: Used to deploy the app.
    
    * AWS: Used to store static and media files for the website.
    
    * Stripe: for secure checkout.
    
    * Django: as a pre-build python framework with a databse.
    
    * EmailJS: To make a functioning contact form.
    
    * GoogleAPIS: To display google maps of store location.


I used https://fonts.google.com/ to source the fonts for this project. 
fontswesome.com/ was used for icons.

If I came accross an issue I used stackoverflow.com and w3schools.com to see example solutions.
These online resources are reliable and accessible to everyone.
I also relied greatly on the course material for Full Stack Web Development.

## Testing

The website functions and responds as intended in the UX design. It is responsive to different screen sizes. 
It is simple to navigate due to the consistancy in design. It is interactive and engaging.

    * CSS was put through a code validator and came back without any errors.

    * HTML was put through a code validator and produced couple errors, due to the fact that 
    a base.html is used in the production of this app the validator was looking for a DOCTYPE and a head element
    for other html files.
    Any other html errors were addressed.

    * JavaScript files were enteres in JSHint.com and came back without any errors.

    * Python was testes with http://pep8online.com/ no major issues were detected other then syntax spacing
    and commenting. I made recommended adjusments.


The app has been tested in multiple browser such as Chrome, Mozilla and Mi browser(phone browser), OnePlus, Iphone8 
and Amazon Kindle.
The app has also been tested on multiple screen sizes and is responsive. The footer and header however, could be improved as 
they are not 100% complete and can takeaway from the over-all success of this webpage. This is something I have noted for
future development.

In order to keep on top of any issues I constanly was checking the functioning of the app with the preview and 
making commits accordingly to save my progress and changes.


### Features Tested

* The navigation bar is responsive, it brings the user to the correct section of the page;
* All anchor tags open a new page/tab;
* Social media links have a _blank application;
* Contact form cannot be submitted unless all fields are filled out, automated "Please fill in this field" pops up;
* Checkout cannot be completed without all required fields being filled out;
* Where applied, hovers are responsive;
* Images display as intended apart from ones in About as they were lost in deployment;
* SignUp/SignIn cannot be completed without filling in all fields;
* GoogleAPI pins the correct location;
* All templates render as intended;
* If the database is manually changed it will make these changes to the website;
* A completed order is sent through the webhook to the database;
* EmailJS will send an automated response after completing the contact form;
* Content of rows and columns adjust with resizing of screen;
* Total calculate correctly;
* Messages display where intended;
* Delivery treshold operates accuratly.


To test if JavaScript files are linked correctly I used the dev tools. Dev tools also came in handy when the code
did not run as intended.

To detect any python issues the Git terminal was helpful.

### Bugs addressed

* I did not use fixtures for my database files, so when the sites was deployed at the end, I lost the products 
from the database and was left with blank pages. After deployment I re-entered them again manually with the deployed
database. In future, however, I will create fixtures to eliminate this risk.


### Bugs not yet addressed

* As I have mentioned before, the images I had used for About disappeared in deployment. I have uploaded them to AWS 
but they do not work and require further investigation.

* I would also like to tidy up the nav-bar and footer.

## Deployment

This app was deplyed on Heroku with AWS:

  1. Create a Heroku app in heroku.com
  2. Create a requirements.txt file by writing (pip3 freeze --local>requirements.txt) in the terminal
  3. Create a Procfile by writing (echo web: python app.py>Profile) in the terminal
  4. Add environment keys both to Config Vars in Heroku and your Workspace
  5. Log in to Heroku from terminal (heroku login -i)
  6. In Heroku you can select Github as a deployment method, automatically linking your app to the workspace
  7. Deploy the branch
  8. Open the app
  9. Push any future commits through the terminal (git push heroku master) to create up to date app.
  
 Because Heroku doesn't support Django's both static and media files, AWS can be used instead.
 

In order for others to view my source code, the repository is made public and can be cloned or downloaded 
as necessary. In order to clone they need to use git in a repository terminal (git clone //repositoryURL). 
They can access the cloneable URL link from my github repository.

A specific commit can also be selected in order to track the project progress.

## Credits

### Content
The content and the UX design was inspired by the ongoing climate crisis.

### Media
Images used in this project were obtained from  https://www.pexels.com/

### Acknowledgements

I would like to thank everyone working together to tackle this issue.

I would also like to say thanks to my mentor and the amazing Slack community for helping me
 complete this project.
