## TESTING <a name="testing-top"></a>

### Html

— **Code Validation** —

As the HTML code is completed on all HTML files, a code validation test is carried out by using [W3C Markup Validation Service](https://validator.w3.org/), which is a validator by the World Wide Web Consortium that allows checking HTML and XHTML documents for well-formed markup, to check any warnings and errors.

**Home Page** (`index.html`): [10 Errors & 5 Warnings]

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

8. Error: Stray start tag `th`.

- Solve the error by using Django form `.as_p`

9. Error: Stray start tag `td`.

- Solve the error by using Django form `.as_p`

10. Error: Stray start tag `td`.

- Solve the error by using Django form `.as_p`

11. Error: Stray start tag `tr`.

- Solve the error by using Django form `.as_p`

12. Warning: Section lacks heading. Consider using `h2-h6` elements to add identifying headings to all sections.

- Solve the warning by using `div` instead of `section`

13. Warning: The `type` attribute is unnecessary for JavaScript resources.

- Solve the warning by removing `type` attribute

14. Warning: The `type` attribute is unnecessary for JavaScript resources.

- Solve the warning by removing `type` attribute

15. Warning: The `type` attribute is unnecessary for JavaScript resources.

- Solve the warning by removing `type` attribute

**Products Page** (`products.html`): [0 Errors & 2 Warnings]

1. Warning: The `type` attribute is unnecessary for JavaScript resources.

- Solve the warning by removing `type` attribute

2. Warning: The `type` attribute is unnecessary for JavaScript resources.

- Solve the warning by removing `type` attribute

**Product Detail Page** (`product_detail.html`): [0 Errors & 0 Warnings]

**Add Product Page** (`add_product.html`): [3 Errors & 0 Warnings]

1. Error: Duplicate attribute `id`.
<!-- TBC -->

2. Error: Element `p` not allowed as child of element `strong` in this context. (Suppressing further errors from this subtree.)

- Solve the error by removing `strong` element

3. Error: The value of the `for` attribute of the `label` element must be the ID of a non-hidden form control.
<!-- TBC -->

**Edit Product Page** (`edit_product.html`): [3 Errors & 0 Warnings]

1. Error: An `img` element must have an `alt` attribute, except under certain conditions. For details, consult guidance on providing text alternatives for images.

- Solve the error by putting `alt` attribute

2. Error: Duplicate attribute `id`.
<!-- TBC -->

3. Error: The value of the `for` attribute of the `label` element must be the ID of a non-hidden form control.
<!-- TBC -->

— **Form Validation** —

— **Quality** —

<div align="right"><a href="#testing-top">🔝</a></div>

### Css

— **Code Validation** —

### JavaScript

— **Code Validation** —

### Python

— **Functions** —
<!-- Sorting products by price including discounted items -->

— **Code Validation** —

### Web Browser

— **Visibilities and CRUD functionality** —

### UX

— **Evidence Of Achieving The Website From UX Point Of View** —

<div align="right"><a href="#testing-top">🔝</a></div>