## TESTING <a name="testing-top"></a>

### Html

— **Code Validation** —

As the HTML code is completed on all HTML files, a code validation test is carried out by using [W3C Markup Validation Service](https://validator.w3.org/), which is a validator by the World Wide Web Consortium that allows checking HTML and XHTML documents for well-formed markup, to check any warnings and errors.

**Home Page** (`index.html`): [10 Errors & 5 Warnings] *Some duplicated errors and warning and they are not repeated below

1. Error: Element `hr` not allowed as child of element `ul` in this context. (Suppressing further errors from this subtree.)

- Solve the error by putting `hr` in `<li>`

2. Error: Attribute `alt` not allowed on element `a` at this point.

- Solve the error by using `title` instead of `alt`

3. Error: Bad value `button` for attribute `type` on element `a`: Subtype missing.

- Solve the error by removing `type="button"`

4. Error: Element `a` is missing required attribute `href`.

- Solve the error by solving error No. 3

5. Warning: Section lacks heading. Consider using `h2-h6` elements to add identifying headings to all sections.

- Solve the warning by using `div` instead of `section`

6. Error: Stray start tag `tr`.

- Solve the error by using Django form `.as_p`

7. Error: Stray start tag `th`.

- Solve the error by using Django form `.as_p`

8. Error: Stray start tag `td`.

- Solve the error by using Django form `.as_p`

9. Warning: The `type` attribute is unnecessary for JavaScript resources.

- Solve the warning by removing `type` attribute

**Products Page** (`products.html`): [0 Errors & 2 Warnings] *Some duplicated errors and warning and they are not repeated below

1. Warning: The `type` attribute is unnecessary for JavaScript resources.

- Solve the warning by removing `type` attribute

**Product Detail Page** (`product_detail.html`): [0 Errors & 0 Warnings]

**Add Product Page** (`add_product.html`): [3 Errors & 0 Warnings]

1. Error: Duplicate attribute `id`.

- Solve the error by removing `id="new-image"`

2. Error: Element `p` not allowed as child of element `strong` in this context. (Suppressing further errors from this subtree.)

- Solve the error by removing `strong` element

3. Error: The value of the `for` attribute of the `label` element must be the ID of a non-hidden form control.

- Solve the error by using `{% for field in form %}`

**Edit Product Page** (`edit_product.html`): [3 Errors & 0 Warnings]

1. Error: An `img` element must have an `alt` attribute, except under certain conditions. For details, consult guidance on providing text alternatives for images.

- Solve the error by putting `alt` attribute

2. Error: Duplicate attribute `id`.

- Solve the error by removing `id="new-image"`

3. Error: The value of the `for` attribute of the `label` element must be the ID of a non-hidden form control.

- Solve the error by using `{% for field in form %}`

**Shopping Cart Page Desktop Size** (`cart.html`): [20 Errors & 16 Warnings] *Some duplicated errors and warning and they are not repeated below

1. Error: `td` start tag in table body.

- Solve the error by putting `{% for item in cart_items %}` above `<tr>` tag. Solve the error for Free golf balls by putting `<td>` tags in `<tr>` tag

2. Error: Duplicate ID `###`

- Solve the error by using `class` instead of `id`

3. Warning: The first occurrence of ID `###` was here.

- Solve the error by using `class` instead of `id`

4. Error: No `p` element in scope but a `p` end tag seen.

- Solve the error by removing additional `</p>` tag

**Shopping Cart Page Mobile Size** (`cart.html`): [16 Errors & 16 Warnings] *Repeated errors and warnings of Duplicate ID and The first occurence of ID was here

1. Error: Duplicate ID `###`

- Solve the error by using `class` instead of `id`

2. Warning: The first occurrence of ID `###` was here.

- Solve the error by using `class` instead of `id`

**Checkout Page** (`checkout.html`): [1 Errors & 0 Warnings]

1. Error: The value of the `for` attribute of the `label` element must be the ID of a non-hidden form control.

- Solve the error by removing `for="id-save-info"` attribute from the label

**Checkout Success Page** (`checkout_success.html`): [0 Errors & 0 Warnings]

**Allauth Account Pages** (`signup.html`, `login.html`, `logout.html`, `password_reset`): [0 Errors & 0 Warnings]
- Check only core pages of Allauth templates but as they are Django package, presume no errors or warnings

**Toast Messages** (`toast_error.html`, `toast_info.html`, `toast_success.html`, `toast_warning.html`): [0 Errors & 0 Warnings]

**404 and 500 Pages** (`404.html`, `500.html`): [0 Errors & 0 Warnings]
- Check only 404 page but they have the same structure so presume no errors or warnings on 500 page

**Profile & Order History Page** (`profile.html`, `profile_order_history`): [0 Errors & 0 Warnings]

— **Form Validation** —

There are some forms on the website. Some of them are validated by front-end (e.g. @ mark for email input) and some by back-end (e.g. existing user name). Manual test is carried out to see if the validations as well as form functions work properly.

**Search Form**

The form takes any texts including special characters (e.g. £, @, [ etc) so there is no form validation for this and the search is processed when search button is clicked as long as there is a text in the input box. It works fine [when a key word exists in product names or descriptions](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/testing/search-form.png), and when it does not it shows 0 result. [When there is no text in the input field, then it displays an error message](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/testing/search-form-empty.png). The search function is available on all the pages and it works from anywhere on the page.

**Subscribe To Newsletter Form**

The form is available on all the pages on the website so try to submit an email from a few different pages to make sure it works. All the emails are submitted from any pages and saved in the database so [it works fine](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/testing/subscribe-newsletters-success.png). If the email has no @ mark, it gives a warning message that @ mark must be included. There should not be duplicated emails in the system so if the email address already exists, [it displays an error message](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/testing/subscribe-newsletters-error.png). 

**Register and Login Forms**

Users must be unique so if email address or username already exits in the database, [it displays an error message for register page](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/testing/register-form-email.png). Also, when the passwords do not match, [it displays an error message](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/testing/register-form-password.png). This is similar for login page that if email or user name does not exists in the database, [it displays an error message and if password is incorrect, it also displays an error message](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/testing/login-form.png).

**Add Product, Checkout and Stripe Form**

When mandatory fields are not filled in or form is invalid, [it displays an error message](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/testing/add-product-form.png). For credit card details, it is validated by Stripe and if it is invalid details, [it displays an error message](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/testing/stripe-form.png).

*Based on the manual test, all the forms on the webiste work properly*

— **Quality** —

<div align="right"><a href="#testing-top">🔝</a></div>

### Css

— **Code Validation** —

As the CSS code is completed, a code validation test is carried out by using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/), which is a validator by the World Wide Web Consortium that allows checking Cascading Style Sheets, to make sure that CSS complies with the standards set by the World Wide Web Consortium

**`base.css`, `cart.css`, `checkout.css`, `index.css`, `products.css` and `profile.css`** are tested and there are [no errors on any of CSS files](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/testing/css-validation.png).

- There are some [warnings](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/testing/css-warnings.png) related to WebKit, which is one of [web browser rendering engines](https://stackoverflow.com/questions/3468154/what-is-webkit-and-how-is-it-related-to-css), for base.css, index.css and product.css. By looking at the [Stack Overflow](https://stackoverflow.com/questions/52490004/what-are-all-of-these-w3c-css-validation-warnings-about) post and a [Code Institue Slack](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf/blob/master/readme/testing/css-webkit.png) threads, no further actions are required so decide to leave as it is

### JavaScript

— **Code Validation** —

As the JavaScript code is completed, a code validation test is carried out by using [JSHint](https://jshint.com/), which is a static code analysis tool used in software development for checking if JavaScript source code complies with coding rules

**`quantity_input_script.html` (js code in cart app), `stripe_elements.js`, `quantity_input_script.html` (js code in product app), `countryfield.js` and js script on `cart.html`** are tested. There is a warning of `'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).` so solve the warning by putting `/*jshint esversion: 6 */`. `$` shows on all the files as undefined variable but this is jQuery symbol so can be ignored. `Stripe` on `stripe_elements.js` shows as undefined variable but this comes from Stripe document so it can be ignored

### Python

— **Functions** —
<!-- Sorting products by price including discounted items -->

— **Code Validation** —

As Python code is completed, a code validation test is carried out by using [PEP8 &#40;Python Enhancement Proposal&#41; online](http://pep8online.com) to see if the code meets guidelines and best practices for the readability and consistency of Python code.

Below is the list of `py` files that are customised therefore checked by the validator.

**eagle-golf Product**

- `asgi.py`, `settings.py`, `urls.py` and `wsgi.py`: Line too long <!-- Check the long lines on settings.py -->

**cart App**

- `apps.py`, `contexts.py`, `urls.py` and `views.py`: There are *trailing whitespace*, *two blank lines*, *no newline at end of file*, *line too long* warnings and errors, and they are all fixed.

**checkout App**

- `init.py`, `admin.py`, `apps.py`, `forms.py`, `models.py`, `signals.py`, `urls.py`, `views.py`, `webhook_handler.py` and `webhooks.py`: There are *no newline at end of file*, *trailing whitespace*, *line too long*, *too many blank lines*, *at least two spaces before inline comment*, *expected 2 blank lines*, *blank line contains whitespace* warnings and errors and they are all fixed <!-- Except some too long lines as TBC -->

**home App**

- `admin.py`, `apps.py`, `contexts.py`, `forms.py`, `models.py`, `urls.py` and `views.py`: There are *trailing whitespace*, *no newline at end of file* and *line too long* warnings and errors and they are all fixed <!-- Except some too long lines as TBC -->

**products App**

- `admin.py`, `apps.py`, `forms.py`, `models.py`, `urls.py`, `views.py` and `widgits.py`: There are *no newline at end of file*, *line too long*,, *blank line contains whitespace* warnings and errors and they are all fixed <!-- Except some too long lines as TBC -->


### Web Browser

— **Visibilities and CRUD functionality** —

### UX

— **Evidence Of Achieving The Website From UX Point Of View** —

<div align="right"><a href="#testing-top">🔝</a></div>