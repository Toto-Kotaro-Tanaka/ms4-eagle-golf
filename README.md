<!-- Website Image goes here -->

# Eagle Golf <a name="top"></a>

This is an e-commerce website for golf products that I create for **Milestone Project 4 (Full Stack Frameworks with Django)** in [Code Institute](https://codeinstitute.net/), Ireland. The use of the website is for educational purpose only, however, all the functionalities work as if it is an actual e-commerce website. It is a mobile responsive website and the link to the website is available HERE. <!-- Live Site Link here -->

<!-- Mock up goes here -->

## USER STORIES

There are two types of users for the website. One is shoppers whose primary goal is to view golf products and purchase them online. The other one is the shop owner whose primary goal is to sell golf products and run business. I am a full-stack web developer and create an e-commerce website to meet the primary goals of the users and their stories.

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
| Displaying products by main category        |     5      |            5            |
| Displaying products by sub category         |     5      |            5            |
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
| Enlarging image when hoovering                  |     3      |            2            |
| Refinements options*                            |     3      |            2            |
| More detailed categories and advetisement       |     3      |            2            |
| Creating account with social media              |     3      |            2            |
| Product comparison**                            |     3      |            1            |
| Payment in different currencie                  |     2      |            1            |

*[Refinements options](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/refinements.png)<br>
**[Product comparison](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/product-comparison.png)

### Scope Plane

To achieve user’s and owner’s stories, below are the minimum features and functions to be included in this project. Also, CRUD (Create, Read, Update, and Delete) functions are required for the admin user to control the products on the website so these are also included in the project.

- Simple design Home page that even first-time users know how to navigate the website. Clearly displayed main categories (e.g. Golf Clubs | Clothing & Shoes) that have sub-categories in it (e.g. Golf Clubs --> Drivers | Irons | Putters)
- Product pages by the main category where users can view all the products belong to the category. Users are navigated to sub-categories detailed category from this page
- Product pages by sub-category where users can view all the products belong to a more detailed category
- Product details page where uses can see all the product details. Users can also select options (e.g. Size, Right / Left) and put the product in the cart
- Cart page where users can see all the selected products before purchase. Users can change the quantity of the product or remove it
- Checkout page where users can provide shipping details and credit card details
- Order confirmation page where users get confirmation of purchase
- Register page where users can create an account to keep the shipping address saved and to view order histories
- Login page where users can log in to the page
- Profile page where users can see the personal details and order histories
- Logout function that users can safely log out the website and takes users back to home page
- Manage product page (admin only) where admin can add, edit, and delete products

### Structure Plane

— **Front-end** —

The website consists of below core pages (`.html` files)

- **Home** (`index.html`)<br>
The main page of the website. There is a logo, search function, navigation to *Main & Sub Category*, *Register* & *Login* and *Shopping Cart* pages, a hero image with Shop Now button. There are icons of popular brands that users can click and view the products of the brand. There is a footer with a form to subscribe to newsletter and some social icons. **The same header and footer are used accross all html files*

- **Products** (`products.html`, `products/<category_name>.html`)<br>
The pages where users can see products by main category & sub category and have an access to product details page. The same header, navigation bar and footer are used as Home.

- **Product Details** (`product/<product_id>.html`)<br>
The pages where users can see product details, with an option to select criteria (e.g. size) and add it in shopping cart. The same header, navigation bar and footer are used as Home.

- **Shopping Cart** (`shopping_cart.html`)<br>
The page where users can view all the selected products and details. Users can adjust quantity and there is an option to remove products. There is a button link to checkout page for the final step of shopping. The same header, navigation bar and footer are used as Home.

- **Checkout** (`checkout.html`)<br>
The page where users can process the purchase. Strip, which is a secured platform for credit card payment, is used on the website for processing payments. The same header, navigation bar and footer are used as Home.  

- **Checkout Success** (`checkout_success.html`)<br>
The confirmation page where users is lead to when the payment process is successfully completed. Users can see the order number, shipping address, the details of product. This page is accessible for registered users from Profile page. The same header, navigation bar and footer are used as Home.

- **Register** (`register.html`)<br>
The page where users can create an account to save their personal details for next shopping and keep their purchase histories. A form and function is created with Django Allauth package.

- **Login** (`login.html`)<br>
The page where users can login the website and access to Profile page to see the personal details and purchase histories. A form and function is created with Django Allauth package.

- **Add Products** (`add_products.html`)<br>
The page where only *Admin* has an access to it and add a new product on the website.

- **Edit Products** (`edit_products.html`)<br>
The page where only *Admin* has an access to it and edit products.

- **Base Template** (`base.html`)<br>
The template `html` document that has core components of html and is used among other html files.

- **Admin** (`/admin`)<br>
The admin panel, which is created automatically when you create Django project, and where Admin can take control of products and other data

- **CSS** & **JavaScript** (`.css` & `.js`)<br>
CSS and JavaScript files of those HTML files are created within the same app folder

Below is the flowchart of the website to show the core relationships between the pages. (Most of the pages are linked each other subject to permission)<br>

![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/front-end-chart.png)<br>

— **Back-end** —<br>

Users have options to purchase products as a guest user or an account holder user. Guest users cannot save their personal details for next purchase so their personal details such as name, email address, shipping address etc belong to their order in the database. Accound holder users create an account with thier <ins>email address</ins> and <ins>username</ins>, and user name (user profile) is linked with their order so that thier personal details are retrieved. Each product belongs to a category and that is identified by category Id. Each order is linked with product sku and name. 

Below is the chart of the database to show the data relationships.

![image](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/ux/back-end-chart.png)<br>

<div align="right"><a href="#top">🔝</a></div>
