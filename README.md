![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/general/eagle-golf.png)

# Eagle Golf <a name="top"></a>

This is an e-commerce website for golf products that I create for **Milestone Project 4 (Full Stack Frameworks with Django)** in [Code Institute](https://codeinstitute.net/), Ireland. The use of the website is for educational purpose only, however, all the functionalities work as if it is an actual e-commerce website. It is a mobile responsive website and the link to the website is available HERE. <!-- Live Site Link here -->

<!-- Mock up goes here -->

## USER STORIES

There are two types of users for the website. One is shoppers whose primary goal is to view golf products and purchase them online. The other one is the shop owner whose primary goal is to sell golf products and run a business. I am a full-stack web developer and create an e-commerce website to meet the primary goals of the users and their stories.

**<ins>Shopper's User Story</ins>**

![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/shopper-user-story1.png)
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/shopper-user-story2.png)

**<ins>Owner's User Story</ins>**

![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/owner-user-story.png)

## UX 5 PLANES

### Strategy Plane

To achieve the user's primary goals and stories outlined in the User Stories section, all the functions and features on the tables below are minimum requirements and they are implemented in the website. (On a scale of 1 [least] - 5 [most])

| Opportunity                                 | Importance | Viability / Feasibility |
| :------------------------------------------ | :--------: | :---------------------: |
| Displaying products by group of categories  |     5      |            5            |
| Displaying products by category             |     5      |            5            |
| Viewing product details                     |     5      |            4            |
| Search Function                             |     4      |            5            |
| Sorting Function                            |     4      |            5            |
| Modifying products in shopping cart         |     5      |            4            |
| Checkout Function                           |     5      |            4            |
| Secure payment                              |     5      |            4            |
| Written confirmation after purchase         |     5      |            5            |
| Create an account                           |     4      |            4            |
| Updating personal details                   |     4      |            5            |
| Resetting password                          |     4      |            4            |
| Email subscription                          |     3      |            4            |
| Add, Edit, Remove products (Admin only)     |     4      |            4            |

Below are the additional functions and features that can improve the website, however, these are not mandatory to achieve the current user goals and stories. Some are not implemented due to a lack of my current skills & knowledge and some due to a lack of time.

| Opportunity                                     | Importance | Viability / Feasibility |
| :------------------------------------------     | :--------: | :---------------------: |
| Displaying number of product images per product |     4      |            2            |
| (e.g. Image from front, side, back)             |            |                         |
| Enlarging image when hovering                   |     3      |            2            |
| Refinements options*                            |     3      |            2            |
| More detailed categories and advertisement      |     3      |            2            |
| Creating account with social media              |     3      |            2            |
| Product comparison**                            |     3      |            1            |
| Payment in different currencies                 |     2      |            1            |

*[Refinements options](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/refinements.png)<br>
**[Product comparison](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/product-comparison.png)

### Scope Plane

Based on the requirements of achieving user's and owner's goals and stories, below is the list of planning pages with the features and functions. CRUD (Create, Read, Update, and Delete) functions are implemented on the website as it is required for admin user's product management.

- Simple design Home page that the purpose of the website is obvious to anybody and even first-time users know how to navigate the website. Clearly displayed group of categories (e.g. Golf Clubs | Clothing & Shoes) that have categories in it (e.g. Golf Clubs --> Drivers | Irons | Putters)
- Product pages by the group of categories where users can view all the products belong to the group. Users are navigated to categories in this group from this page
- Product pages by category where users can view all the products belong to the category
- Product details page where uses can see all the product details. Users can also select options (e.g. Size, Right / Left) and put the product in the cart
- Shopping Cart page where users can see all the selected products before purchase. Users can change the quantity of the product or remove it
- Checkout page where users can provide shipping details and credit card details
- Checkout success page where users get confirmation of purchase
- Register page where users can create an account to keep the shipping address saved and to view order histories
- Login page where users can log in to the page
- Profile page where users can see the personal details and order histories
- Logout function that users can safely log out the website and takes users back to the home page
- Product Management pages (admin only) where admin can add, edit, and delete products

### Structure Plane

— **Front-end** —

The website consists of below core `HTML` pages and has some `CSS` and `JavaScript` 

- **Home** (`index.html`)<br>
The main page of the website. There is a logo, search function, navigation to *Group of Categories & Categories*, *Register* & *Login* and *Shopping Cart* pages, a hero image with Shop Now button. There are icons of popular brands that users can click and view the products of the brand. There is a section of "Why Eagle Golf?" which provides a few reasons for buying products with the shop. There is a footer with a form to subscribe to newsletter and some social icons. **The same header and footer are used across all html files*

- **Products** (`products.html`, `products/<category_name>.html`)<br>
The pages where users can see products by a group of categories & category and have an access to the product details page.

- **Product Details** (`product/<product_id>.html`)<br>
The pages where users can see product details, with an option to select criteria (e.g. size) and add it in shopping cart.

- **Shopping Cart** (`shopping_cart.html`)<br>
The page where users can view all the selected products and details. Users can adjust the quantity and there is an option to remove products. There is a button link to a checkout page for the final step of shopping. 

- **Checkout** (`checkout.html`)<br>
The page where users can process the purchase. Strip, which is a secured platform for credit card payment, is used on the website for processing payments.  

- **Checkout Success** (`checkout_success.html`)<br>
The confirmation page where users are lead to when the payment process is successfully completed. Users can see the order number, shipping address, product details. This page is accessible for registered users from Profile.

- **Register** (`register.html`)<br>
The page where users can create an account to save their personal details for next shopping and keep their purchase histories. A form with a built-in function is created with Django Allauth package.

- **Login** (`login.html`)<br>
The page where users can log in the website and access to Profile page to see the personal details and purchase histories. A form with a built-in function is created with Django Allauth package.

- **Profile** (`profile.html`)<br>
The page where users can see personal details and purchase histories.

- **Add Products** (`add_products.html`)<br>
The page where only *Admin* has access and add a new product on the website.

- **Edit Products** (`edit_products.html`)<br>
The page where only *Admin* has access and edit products.

- **Page 404** (`page_404.html`)<br>
The error page that appears when the page is not found and where users are led to the Home page safely.

- **Base Template** (`base.html`)<br>
The `html` template document has core components of html and is used among other html files.

- **Admin** (`/admin`)<br>
The admin panel, which can be created with Django project, where Admin can take control of products and other data

- **CSS** & **JavaScript** (`.css` & `.js`)<br>
CSS and JavaScript files of those HTML files are created within the same app folder

Below is the flowchart of the website to show the core relationships between the pages. (Most of the pages are linked to each other subject to permission)<br>

![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/front-end-chart.png)<br>

— **Back-end** —<br>

Users have options to purchase products as a guest user or account holder user. Guest users cannot save personal details for their next purchase so personal details such as name, email address, shipping address etc belong to their order in the database. Account holder users create an account with their <ins>email address</ins> and <ins>username</ins>, and user name (user profile) is linked with their order so that personal details can be retrieved. Each product belongs to a category and that is identified by category id. Each order is linked with product sku and name.<br>
SQLite, which is Django built-in database is used for development mode and Heroku Postgre is used for production mode. AWS (Amazon Web Services) is used to hold all static files and folders for the website for production mode. 

Below is the chart of the database to show the data relationships.

![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/back-end-chart.png)<br>

### Skeleton Plane

The website is created as a desktop-first because it is easy to picture the whole image of the website, however, it is a fully mobile responsive website so shoppers using a mobile phone have no difficulties looking for products and purchase them. Below are the wireframes of the core pages of the website.<br>

<details>
<summary>Home (index.html)</summary><br>

![Wireframe: Home](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/home.png)
</details>

<details>
<summary>Products (products.html)</summary><br>

![Wireframe: Products](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/products.png)
</details>

<details>
<summary>Product Details (product/product_id.html)</summary><br>

![Wireframe: Product Details](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/product-details.png)
</details>

<details>
<summary>Shopping Cart (shopping_cart.html)</summary><br>

![Wireframe: Shopping Cart](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/shopping-cart.png)
</details>

<details>
<summary>Checkout (checkout.html)</summary><br>

![Wireframe: Checkout](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/checkout.png)
</details>

<details>
<summary>Checkout Success (checkout_success.html)</summary><br>

![Wireframe: Checkout Success](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/checkout-success.png)
</details>

<details>
<summary>Register (register.html)</summary><br>

![Wireframe: Register](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/register.png)
</details>

<details>
<summary>Login (login.html)</summary><br>

![Wireframe: Login](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/login.png)
</details>

<details>
<summary>Profile (profile.html)</summary><br>

![Wireframe: Profile](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/profile.png)
</details>

<details>
<summary>Product Management (product_management.html)</summary><br>

![Wireframe: Product Management](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/product-management.png)
</details>

<details>
<summary>Page 404 (page_404.html)</summary><br>

![Wireframe: Page 404](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/page-404.png)
</details>

### Surface Plane

— **Colours** —

This is an e-commerce website that has a lot of products with images containing different colours, therefore **White** (#FFFFFF) is used as the main background colour to keep the entire image of the website settled. The shop colour is **Hunter Green** (#09572A) and this is used for some icons and fonts. **Jet** (#333333) is used as the main font colour, **Golden Yellow** (#FFDF00) is used for buttons and alerts to stand them out. **Flame** (#E84610) is used for other things that need user's attention. These are the base colours and similar colours are used on the different parts and sections on the website.

![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/colours.png)

— **Typography** —

**Roboto** which is one of the most popular google fonts is used for all texts in general because good readability is an important factor for users e-commerce websites. Robot is a default font for Android so many users are very familiar with it as well.

![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/roboto.png)

<div align="right"><a href="#top">🔝</a></div>

## WEBSITE DEVELOPMENT PLAN
This is a full-stack website that contains both front-end, back-end, so many Django apps, features and functions so a good website development plan is required to maximise the efficiency of the development. GitHub project planner, which has a Kanban planner, is used for this project. Below is the summary of core tasks* for the website and more detailed tasks are listed on [GitHub Projects](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/projects/1). This gives not only very clear planning but also making sure nothing is missed during the process.<br>
**Follow the same process as Code Institute Mini Project, Boutique Ado*

1. Planning The Website with UX5 Planes
1. Project Set Up (Installing Django, Setting up Project, Testing connection, Creating Django superuser)
1. Authentication & Authorisation (Installing Allauth, Testing)
1. The Base Template (Creating base template)
1. The Home Page (Navigation bar, Header and Footer)
1. Products Set Up (Creating Products app, Installing data, Filtering & Searching)
1. The Shopping Cart (Adding and adjusting products)
1. Toasts (Real time notification)
1. Checkout with Stripe (Function, Form, Testing Stripe)
1. Profile (Displaying personal details and order history)
1. Product Admin (CRUD function for products)
1. Deployment (AWS, Heroku)
1. Emails (Setting up email functionality)
1. Code Refactoring (Checking code, Reviewing the design and updating)
1. Testing (Testing for HTML, CSS, JavaScript, Python, User Stories, Functions and Features)
1. Final Check Before Submission

## FEATURES

### Existing Features

### Features Left To Implement

## TECHNOLOGIES USED

- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) for style
- [Material Design for Bootstrap 5 & 4](https://mdbootstrap.com/) (an open-source toolkit based on Bootstrap for developing Material Design) for the mainframe of the website <!-- MDB or Bootstrap TBC -->
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for interaction
- [Python3](https://www.python.org/) as a backend programming language
- [Django](https://www.djangoproject.com/) (an open-source web framework) as the main framework of Python
- [SQLite](https://www.sqlite.org/index.html) (Django built-in database) as database in development mode
- [PostgreSQL](https://landing.aiven.io/en/aiven-for-postgresql/) (Heroku built-in) as database in production mode
- [Google Fonts](https://fonts.google.com/) for fonts
- [Font Awesome](https://fontawesome.com/) for icons
- [Gitpod](https://www.gitpod.io/) as Integrated Development Environment (IDE)
- [Git](https://git-scm.com/) for local version control, keeping the files & documents
- [GitHub](https://github.com/) for online version control and keeping the files & documents
- [Heroku](https://www.heroku.com/) for deploying the website

<div align="right"><a href="#top">🔝</a></div>

## RESOURCES

### General Resources

### Tools

## TESTING

Testing report is available **[TESTING.md](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/TESTING.md)**

## PROJECT BARRIERS & SOLUTIONS
<!-- Stripe payment, intent issue that sometimes get internal server error 500 and paymentn doesn't go through -->
<!-- Stripe payment, webhook unauthorised issue -->
<!-- Saved address not showing properly -->

## VERSION CONTROL

## DEPLOYMENT

## CREDITS

### Code

— **HTML5** —
- [MDB Navbar](https://mdbootstrap.com/docs/standard/navigation/navbar/) for navigation bar
- [Bootstrap Alerts](https://getbootstrap.com/docs/5.0/components/alerts/) for alert
- [MDB Masks](https://mdbootstrap.com/docs/standard/content-styles/masks/) for masking the hero image
- [MDB Cards](https://mdbootstrap.com/docs/standard/components/cards/) for displaying products
- [MDB Pills](https://mdbootstrap.com/docs/standard/navigation/pills/) for displaying products
- [MDB Footer](https://mdbootstrap.com/docs/standard/navigation/footer/) for footer

— **CSS3** —

— **JavaScript** —

— **Python** —

### Contents

### Media

— **Logo & Favicon** —
- Logo and Favicon created by me using [canva](https://www.canva.com/)

— **Images** —
- Hero Image Desktop: [Unsplash](https://unsplash.com/) by [Peter Drew](https://unsplash.com/photos/_9afczTn6bc) 
- Hero Image Mobile: [Unsplash](https://unsplash.com/) by [Courtney Cook](https://unsplash.com/photos/SsIIw_MET0E) 
- Popular Brand Logo: [TaylorMade Golf](https://www.taylormadegolf.eu/)
- Popular Brand Logo: [Callaway Golf](https://www.callawaygolf.com/) 
- Popular Brand Logo: [Titleist Golf](https://www.titleist.com/) 
- Popular Brand Logo: [Mizuno Golf](https://mizunogolf.com/us/) 
- Popular Brand Logo: [PING Golf](https://ping.com/en-us/) 
- Popular Brand Logo: [Cobra Golf](https://www.cobragolf.com/) 
- Popular Brand Logo: [Srixon](https://www.srixon.com/) 
- Popular Brand Logo: [Nike](https://www.nike.com/ie/) 

## ACKNOWLEDGEMENTS
