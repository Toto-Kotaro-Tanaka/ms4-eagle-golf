![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/general/eagle-golf.png)

# Eagle Golf <a name="top"></a>

This is an e-commerce website for golf products that I create for **Milestone Project 4 (Full Stack Frameworks with Django)** in [Code Institute](https://codeinstitute.net/), Ireland. The use of the website is for educational purpose only, however, all the functionalities work as if it is an actual e-commerce website. It is a mobile responsive website and the link to the website is available [HERE](https://ms4-eagle-golf.herokuapp.com/).

<!-- Mock up goes here -->

## USER STORIES

There are two types of users for the website. One is shoppers whose primary goal is to view golf products and purchase them online. The other one is the shop owner whose primary goal is to sell golf products and run a business. I am a full-stack web developer and create an e-commerce website to meet the primary goals of the users and their stories.

**<ins>Shopper's User Story</ins>**

![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/shopper-user-story1.png)
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/shopper-user-story2.png)

> **Note:**<br>
> ID9: Search function works with a keyword only

**<ins>Owner's User Story</ins>**

![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/owner-user-story.png)

> **Note:**<br>
> ID5: In a real e-commerce website, products should never be deleted but make it unavailable or something instead. As this is an educational purpose website that CRUD should be implemented, there is delete products function

<div align="right"><a href="#top">🔝</a></div>

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

*[Example of Refinements options](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/refinements.png)<br>
**[Example of Product comparison](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/product-comparison.png)

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
- 404 page where users are taken back to home page safely when they visit a page does not exist

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
The `html` template document that has core components of html and is used among other html files.

- **Admin** (`/admin`)<br>
The admin panel, which can be created with Django project, where Admin can take control of products and other data

- **CSS** & **JavaScript** (`.css` & `.js`)<br>
CSS and JavaScript files of those HTML files are created within the same app folder

Below is the flowchart of the website to show the core relationships between the pages. (Most of the pages are linked to each other subject to permission)<br>

![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/front-end-chart.png)<br>

— **Back-end** —<br>

Users have options to purchase products as a guest user or account holder user. Guest users cannot save personal details for their next shopping as personal details such as name, email address, shipping address etc belong to their order in the database. Account holder users create an account with their <ins>email address</ins> and <ins>username</ins>, and user name (user profile) is linked with their order so that personal details can be retrieved. Each product belongs to a category, a brand and these are identified by id. Each order has an unique order number which is generated by when order is processed and orders have shopper's and product details.<br>
SQLite, which is Django built-in database is used for development mode and Heroku Postgre is used for production mode. AWS (Amazon Web Services) is used to hold all static files and folders for the website for production mode. 

Below is the chart of the database to show the data relationships.

![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/back-end-chart.png)<br>

### Skeleton Plane

The website is created as a desktop-first because it is easy to picture the whole image of the website, however, it is a fully mobile responsive website as well so shoppers using a mobile phone have no difficulties looking for products and purchase them. Below are the wireframes of the core pages of the website.<br>

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

This is an e-commerce website that has a lot of products with images containing different colours, therefore **White** (#FFFFFF) is used as the main background colour to keep the entire image of the website settled. The shop colour is **Hunter Green** (#09572A) ~~and this is used for some icons and fonts~~. **Jet** (#333333) is used as the main font colour, **Golden Yellow** (#FFDF00) is used for buttons and alerts to stand them out. **Flame** (#E84610) is used for other things that need user's attention. These are the base colours and similar colours are used on the different parts and sections on the website.

> **Note:**<br>
> **Hunter Green** (#09572A) is not used for any fonts or icons but used for the colour of toast success

![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/colours.png)

— **Typography** —

**Roboto** which is one of the most popular google fonts is used for all texts in general because good readability is an important factor for e-commerce websites from the user's point of view. Robot is a default font for Android so many users are very familiar with it as well.

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

<div align="right"><a href="#top">🔝</a></div>

## FEATURES

### Existing Features

- Create with **HTML5**, **CSS3** (with Material Design for Bootstrap), **JavaScript**, **Python** (Django Framework), **Stripe**, **AWS** and **Heroku**
- It consists of 1 product with 5 apps in Django
- It consists of 1 base html template and 12 main html files. (Excluding sub html files and some allauth html files)
- Modal for "Delivery Cost" information
- Toast for user's action
- All the features planned on [Strategy Plane](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/features/strategy-plane.png) and [Scope Plane](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/features/scope-plane.png)

### Features Left To Implement

- **Displaying number of product images per product:** This would probably be possible to implement by using the same principal as Carousel, however, cannot confirm it for sure and do not have time to work on this, decide to leave it out in this project

- **Enlarging image when hovering:** Find a few ways of enlargin (zooming) images on hover, however, not sure if these are same as enlargin images of products that are used in e-commerce websites. Currently no time to look at the details so decide to leave it out in this project

- **Refinements options:** This might be implemented by different combinations of filter, however, currently have no skill to achieve this so decide to leave it out in this project

- **More detailed categories and advertisement:** This is to have more detailed categories (e.g. There are only 11 categories but actual e-commerce website, there should be more categories available = more products) and more detailed advertisement such as having different colours, guidance for size etc. Currently have no time to work on this, decide to leave it out in this project

- **Creating account with social media:** <!-- This might be possible so take a look at it if have time -->

- **Product comparison:** This seems to be a very advanced feature and do not even know how to look up for this with my current skill and knowledge so decide to leave it out in this project

- **Payment in different currencies:** This might be possible with Stripe rather than Django, but not sure how to achieve this. As this is not important feature with current project and do not have time to look at it, decide to leave it out in this project

<div align="right"><a href="#top">🔝</a></div>

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
- [Stripe](https://stripe.com/en-ie) for credit card payment
- [AWS](https://aws.amazon.com/) (Amazon Web Services) for host static files and images for the website
- [Gitpod](https://www.gitpod.io/) as Integrated Development Environment (IDE)
- [Git](https://git-scm.com/) for local version control, keeping the files & documents
- [GitHub](https://github.com/) for online version control and keeping the files & documents
- [Heroku](https://www.heroku.com/) for deploying the website

<div align="right"><a href="#top">🔝</a></div>

## RESOURCES

### General Resources

- Code Institute Course Materials
- [Stack Overflow](https://stackoverflow.com/)
- [YouTube](https://www.youtube.com/)
- [W3schools](https://www.w3schools.com/)
- [Google](https://www.google.com/)

### Tools

- [Balsamiq](https://balsamiq.com/) for wireframes
- [Adobe](https://www.adobe.com/ie/photoshop/online/resize-image.html) for resizing images
- [PNG to ICO](https://hnet.com/png-to-ico/) for converting png to ico for favicon
- [Canva](https://www.canva.com/) for creating logos and some images
- [Multi Device Website Mockup Generator](http://techsini.com/multi-mockup/index.php) for mockup
- [Autoprefixer](https://autoprefixer.github.io/) for parsing CSS and add vendor prefixes
- [W3C Markup Validation Service](https://validator.w3.org/) for testing HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) for testing CSS code
- [jshint](https://jshint.com/) for testing JavaScript code
- [PEP8 Online](http://pep8online.com/) for checking Python code compliance
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) for testing, style checking and debugging

<div align="right"><a href="#top">🔝</a></div>

## TESTING

Testing report is available **[TESTING.md](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/TESTING.md)**

<div align="right"><a href="#top">🔝</a></div>

## PROJECT BARRIERS & SOLUTIONS
<!-- Stripe payment, webhook unauthorised issue -->
<!-- +- qty buttons -->
<!-- First name Last name for allauth -->
<!-- Newsletters -->
<!-- Free golf balls migrations -->

<div align="right"><a href="#top">🔝</a></div>

## VERSION CONTROL

[Git](https://git-scm.com/) as a local repository and [GitHub](https://github.com/) as a remote repository are used for the project, and below is how they are used as the version control for the project.

— **Setting Up** —

1. Create a **remote repository** in GitHub by clicking **"New repository"** on the main page<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/version-control/version-control1.png)

2. Use **Code Institute Template**, put the repository name and click Create Repository making sure to select public<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/version-control/version-control2.png)

3. Open the repository with [Gitpod](https://www.gitpod.io/) which is my Integrated Development Environment (IDE). By using Code Institue Template, initialisation including initial commit is done so no need to do `git init` command when open IDE, or to use `git push -u origin main` command for my first commit. `gitignore` file, which is very important for the project including some confidential information, is created with Code Institute template so not necessary to create it, however, it is checked to include files such as pycache, *.sqlite3, env.py etc<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/version-control/version-control3.png)

— **Commitments** —

- When a section or even a group of work is completed, it is committed in git and pushed into GitHub, to make sure to keep the history of the work logged properly and not to lose the work in unexpected situations. Below commands are used for this.

```
* git status | To check the status of new/modified folders, files, and documents
* git add . | To put all new and updated work on the stage in git
  git add <specific file> is used when different types of work are done but do not want to commit everything on the same commitment
* git commit -m "Example commit" | To commit the work on the stage in git before pushing it to GitHub
* git push | To update the repository in GitHub for main branch
  git push origin <branch name> is used when pushing git into GitHub for sub-branches
```

— **Branches** —

- When some testing is needed, create a branch and test is on it instead of using the main branch. When the testing is successful, then merge the branch into the main and when it is not, leave the branch unmerged and keep working on the main branch. Below commands are used for this.

```
* git branch <branch name> | To create a new branch
* git checkout <branch name> | To switch branch
* git branch | To check current branch
* git merge <branch name> | To merge sub-branch into main, do this on main branch
```

> **Note:**<br>
> There are no static files available in the master branch on production mode for some reason so free-golf-balls branch is used for update and the same code is transferred to the master without merging<br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/version-control/version-control4.png)

<div align="right"><a href="#top">🔝</a></div>

## DEPLOYMENT

The website of this project requires back-end technologies such as server, application, and database so the website is deployed in [Heroku](https://www.heroku.com/), which is a cloud platform with a service supporting several programming languages, because GitHub can only host a static website. Heroku Postgres is used for the database. [AWS services](https://aws.amazon.com/), which is also a cloud-based platform, is used to store static files and images as Heroku has *no files system to store new files* [*Reference from Code Institue Slack](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/reference-aws.png).

Below are the processes of deploying the website to Heroku and setting up static files & images in AWS.

— **HEROKU** —

1. Create an app in Heroku. Click *New*, put App name and select region<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/create-app1.png)<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/create-app2.png)

1. Add Heroku Postgres for the database<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/heroku-postgres.png)

1. Install `dj_database_url` and `psycopg2-binary` to use Heroku Postgres, and run `pip3 freeze > requirements.txt` command to add them on requirments.txt<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/requirements-txt.png)

1. Update `settings.py` of the product (eagle_golf). Import `dj_database_url`, comment out sqlite databases and add dj databases variable temporary while the database is transferred to Heroku Postgres<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/databases.png)

1. Run `python3 manage.py showmigrations` command to see the status of migrations (Currently not migrated). Run `python3 manage.py migrate` command to migrate<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/migrate.png)

1. Import all products data. Run `python3 manage.py loaddata` command to load the **categories** first, **brands** next and **products** the last. The order of loading is important as all the products are associated with categories and brands

1. Create a super user with `python3 manage.py createsuperuser` command for product admin

1. Install `gunicorn` which acts as the webserver, and freeze it into requirments file with `pip3 freeze > requirements.txt` command<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/requirements-txt2.png)

1. Create a **Procfile** which specifies the commands that are executed by the app on startup<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/procfile.png)

1. Temporary disable collectstatic by setting `heroku config:set DISABLE_COLLECTSTATIC = 1` and host name of Heroku to allowed hosts in `settings.py`

1. Initialise Heroku in git with `heroku: git:remote -a ms4-eagle-golf` and put git into Heroku with `git push heroku master`

1. Set up automatic deployment when git is pushed to GitHub. Go to Deployment on Heroku, search the GitHub repository, connect and click Enable Automatic Deploys<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/auto-deployment.png)<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/auto-deployment2.png)<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/auto-deployment3.png)

1. Generate a new secret key, set it up in Heroku and update `settings.py`. Change the setting of Debug mode that only True in Development mode<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/secret-key.png)<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/secret-key2.png)

1. Check Activity Feed to see Build in Progress to confirm automatic deployment is working

— **AWS** —

1. Open S3 and create a new bucket, which stores the files, by completing the name and region<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/create-bucket.png)

1. Set up basic settings. Enable static website hosting so that give a new endpoint for accessing from the internet. Put `index.html` and `error.html` as default values<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/bucket-settings.png)

1. Set up CORS configuration which is the access between Heroku and this S3 Bucket<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/cors.png)

1. Set up Bucket Policy. Generate a policy with AWS pocicy generator. Add /* at the end of Resource to allow access to all recources in the bucket<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/bucket-policy.png)

1. Create a user to access to the bucket. Go to IAM (Identity and Access Management) and create a group for user to live in. Then, create a policy by importing pre-built policy<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/iam-group.png)<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/iam-policy.png)<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/iam-import-policy.png)<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/iam-s3-policy.png)<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/iam-review-policy.png)

1. Attach the policy to the group<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/attach-policy.png)<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/attach-policy2.png)

1. Create a user and add it to the group. When the user is added to the group, it creates csv file containing Access Key ID and Secret access key which are used to authenticate them from Django app. *It is very important to download the file and save it as you cannot download it again<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/create-user.png)<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/create-user2.png)

— **Connecting to DJANGO** —

1. Install two new packages, `pip3 install boto3`, `pip3 install django-storages`, and run `pip3 freeze > requirements.txt` command to add them on requirments.txt<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/requirements-txt3.png)

1. Update `settings.py` to tell Django which bucket it should be communicating with *It is very important to keep AWS access keys secrets as these can be used to store or move data in the bucket and you will be charged by Amazon for it<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/django-aws-settings.png)

1. Add these secret keys on Heroku and set USE_AWS = True<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/heroku-config-vars.png)

1. Create `custome_storages.py` to tell Django to use S3 to store static files and upload images when it is in production<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/custom-storages.png)

1. Add `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'` to tell Django where the static files come from in production and add some settings for Static and Media files on `settings.py`<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/settings-static.png)

1. Add all the update in git, commit it and push it to GitHub. Heroku runs `python3 manage.py` to collectstatic during the process which also searches through all the apps and project folders looking for static files. Then, it uses S3 domain settings in conjunction with the custom storage classes that tells the location at the URL where the things should be saved when it is in production. This can be confirmed in S3 bucket<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/static-folders-s3.png)

1. Add Cache control on `settings.py` as static files do not change often and to improve the perfomance for users<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/cache-control.png)

1. Upload product images via S3. Create a folder, and upload images<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/create-folder.png)<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/upload.png)

1. Verify superuser's email address on Heroku Postgres. Login admin and check the VERIFIED and PRIMARY boxes<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/verify.png)

1. Add Stripe keys to Heroku Config Vars and create a new webhook endpoint<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/stripe-config-vars.png)<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/endpoint.png)

1. Create Gmail account, add email host pass & user to Heroku Config Vars and add code on `settings.py` of the product (eagle_golf)
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/email.png)<br><br>
![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/deployment/email2.png)

<div align="right"><a href="#top">🔝</a></div>

## CREDITS

### Code

— **HTML5** —
- [MDB Navbar](https://mdbootstrap.com/docs/standard/navigation/navbar/) for navigation bar
- [Bootstrap Alerts](https://getbootstrap.com/docs/5.0/components/alerts/) for alert
- [MDB Modal](https://mdbootstrap.com/docs/standard/components/modal/) for displaying delivery cost
- [MDB Cards](https://mdbootstrap.com/docs/standard/components/cards/) for displaying products
- [MDB Pills](https://mdbootstrap.com/docs/standard/navigation/pills/) for displaying products
- [MDB Footer](https://mdbootstrap.com/docs/standard/navigation/footer/) for footer

— **CSS3** —
- [Stackoverflow](https://stackoverflow.com/questions/16344354/how-to-make-blinking-flashing-text-with-css-3) for blinking text
- [Hubspot](https://blog.hubspot.com/website/css-fade-in) for fade in text

— **JavaScript** —
- [W3Schools](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top) for scroll back to top button

— **Python** —

### Contents

### Media

— **Logo & Favicon** —
- Logo and Favicon created by me using [canva](https://www.canva.com/)

— **Images** —
- Hero Image Desktop: [Snaintongolf](https://www.snaintongolf.co.uk/) 
- Hero Image Mobile: [Unsplash](https://unsplash.com/) by [Courtney Cook](https://unsplash.com/photos/SsIIw_MET0E)
- Hero Image Products Golf Clubs: [TaylorMade Golf](https://www.taylormadegolf.eu/)
- Hero Image Mobile Products Golf Clubs: [Mizuno Golf](https://mizunogolf.com/us/golf-clubs/es21-series/es21-wedges/)
- Hero Image Products Clothing: [PING Golf](https://ping.com/en-us/shop/products?category=apparel)
- Hero Image Mobile Products Shoes: [Cobra Golf](https://www.cobragolf.com/pumagolf/) 
- Hero Image Mobile Products Bag: [Titleist Golf](https://www.titleist.com/golf-gear/golf-bags/)
- Hero Image Products Golf Balls: [Srixon](https://www.srixon.com/us/golf-ball-fitting.html)
- Popular Brand Logo: [TaylorMade Golf](https://www.taylormadegolf.eu/)
- Popular Brand Logo: [Callaway Golf](https://www.callawaygolf.com/) 
- Popular Brand Logo: [Titleist Golf](https://www.titleist.com/) 
- Popular Brand Logo: [Mizuno Golf](https://mizunogolf.com/us/) 
- Popular Brand Logo: [PING Golf](https://ping.com/en-us/) 
- Popular Brand Logo: [Cobra Golf](https://www.cobragolf.com/) 
- Popular Brand Logo: [Srixon](https://www.srixon.com/) 
- Popular Brand Logo: [Nike](https://www.nike.com/ie/) 

<div align="right"><a href="#top">🔝</a></div>

## ACKNOWLEDGEMENTS

<div align="right"><a href="#top">🔝</a></div>

