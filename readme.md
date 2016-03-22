# Capivara.py

> Generates/obtain Document Object Model

Capivara is a library that allows your python obtain the DOM from webpages. Being a excelent tool to test client-side behavior.

![capivara](https://raw.githubusercontent.com/raphamorim/capivara/master/resources/images/capivara.png)

## Installation

To install Capivara, simply run:

```sh
$ pip install capivara
```

## Usage

```html

<div class="container main">
    You shall not pass!!
</div>

```

```py

import capivara
document = capivara.init(Port=8012)

element = document.querySelector('.container')
assert.equal(element.className, "container main") # true
assert.equal(element.textContext, "You shall not pass!!") # true

```

## Available Methods

#### querySelector

Returns the first element that is a descendant of the element on which it is invoked that matches the specified group of selectors.

```
element = document.querySelector('.container')
```

## Notes

The capivara is unable to deliver all the properties of the element. However he can deliver the following properties:

`style`, `classList`, `textContext`, `baseURI`, `className`, `clientHeight`, `clientLeft`, `clientTop`, `clientWidth`, `firstChild`, `title`, `string`, `tagName`, `tabIndex`, `outerHTML`, `localeString`, `localName`, `dir`, `scrollLeft`, `scrollHeight`, `scrollWidth`, `scrollTop`

## Contributing

Want to contribute? [Follow these recommendations](https://github.com/raphamorim/capivara/blob/master/CONTRIBUTING.md).

## License

[![CC0](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

