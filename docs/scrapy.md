# Scrapy

## Creating a project

Sure, here's the translation into English:

---

We need to create our project.

Let's use Scrapy to set up the project structure. This allows us to parameterize some classes to speed up development using the framework for what we want to collect.

```bash
scrapy startproject coleta
```

Let's perform a brief analysis.

```bash
scrapy shell
```

We need to create our spider.

```bash
scrapy genspider mercadolivre mercadolivre.com.br
```

```bash
scrapy shell
```

```python
>>> fetch('https://lista.mercadolivre.com.br/tenis-corrida-masculino')
```

```python
>>> response
```

```python
>>> response.text
```
response.css('div.ui-search-result__content').get()

products = response.css('div.ui-search-result__content')


len(products)


### Brand
products.xpath('//*[@id=":Ral5e6:"]/div[2]/div/div[2]/span/text()').get()
products.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get()

### Name
products.css('h2.ui-search-item__title::text').get()
products.xpath('//*[@id=":Ral5e6:"]/div[2]/div/div[2]/a/h2/text()').get()

### Old price real
products.css('span.andes-money-amount__fraction::text').get()

### Old price cents
products.css('span.andes-money-amount__cents.andes-money-amount__cents--superscript-16::text').get()

### New price reais
products.css('span.andes-money-amount__fraction::text').get()

### New price cents
products[0].css('span.andes-money-amount__fraction::text').getall()

## Review
ui-search-reviews__rating-number

### Next page
next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()

### CSS Selectors

#### Advantages
1. **Simple Syntax**: CSS Selectors have a simpler and more readable syntax, especially for basic selections.
2. **Performance**: In many cases, CSS Selectors can be faster as many web rendering engines are optimized for CSS.
3. **Popularity**: Widely used in web development for styling pages, making them familiar to many developers.
4. **Standard Support**: Natively supported in many scraping libraries (like BeautifulSoup and Scrapy).

#### Disadvantages
1. **Query Limitations**: CSS Selectors lack the same flexibility and expressive power as XPath for complex queries.
2. **Limited XML Support**: While usable for XML, CSS Selectors are less common and powerful in this context compared to XPath.

#### Examples
- Selecting a `div` element with a specific class:
  ```css
  div.example
  ```
- Selecting all `a` elements within a `div` with ID `container`:
  ```css
  #container a
  ```
- Selecting the first `p` element within a `div`:
  ```css
  div > p:first-child
  ```

### XPath

#### Advantages
1. **Flexibility and Power**: XPath is extremely powerful and flexible, allowing very complex queries.
2. **Full XML Support**: XPath is designed to work with XML, making it ideal for XML document manipulation.
3. **Relative Selection**: Allows navigating the document relative to a node, using axes like `parent`, `ancestor`, `sibling`, etc.
4. **Advanced Filtering**: Supports advanced filters and functions for string, number, and boolean manipulation.

#### Disadvantages
1. **Complex Syntax**: XPath syntax can be more complex and less intuitive, especially for simple queries.
2. **Performance**: Can be slower in some implementations due to its flexibility and power.

#### Examples
- Selecting all `div` elements with a specific class:
  ```xpath
  //div[@class='example']
  ```
- Selecting all `a` elements within a `div` with ID `container`:
  ```xpath
  //div[@id='container']//a
  ```
- Selecting the first `p` element within a `div`:
  ```xpath
  //div/p[1]
  ```

### Choosing Between CSS Selectors and XPath

- **Use CSS Selectors** if:
  - You are performing simple queries.
  - Working primarily with HTML.
  - Prefer a shorter and more intuitive syntax.
  - Performance is a critical consideration.

- **Use XPath** if:
  - You need to perform complex queries.
  - Manipulating XML documents.
  - Require advanced filtering or relative selection.
  - Comfortable with a more complex and powerful syntax.

In summary, the choice between CSS Selectors and XPath depends on the specific needs of your project and your comfort level with each language. Both have their advantages and disadvantages and can be used complementarily in many cases.

## Running Our Spider

```bash
scrapy crawl mercadolivre

>>>
```

## Saving Data

```bash
scrapy crawl mercadolivreitem -o ../../data/data.jsonl
```