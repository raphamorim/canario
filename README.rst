Capivara.py (No longer maintained)
=======================================

Generates & Obtain DOM (Document Object Model)

Capivara is a library that allows your python obtain the DOM from webpages. Being a excelent tool to test client-side behavior.

.. image:: https://raw.githubusercontent.com/raphamorim/capivara/master/resources/images/capivara.png
    :target: #
    

Installation
============

Custom Requirement: [Phantomjs binary package installed](http://phantomjs.org/download.html)

To install Capivara, simply run:

.. code-block:: bash

    $ pip install capivara


Usage
=====

.. code-block:: html

    <div class="container main">
        You shall not pass!!
    </div>


.. code-block:: python

    import capivara
    document = capivara.init(port=8012) # default = 8000

    element = document.querySelector('.container')
    assert.equal(element.className, "container main") # true
    assert.equal(element.textContext, "You shall not pass!!") # true


Available Methods
=================

querySelector
~~~~~~~~~~~~~

Returns the first element that is a descendant of the element on which it is invoked that matches the specified group of selectors.

.. code-block:: python

    element = document.querySelector('.container')


Notes
=====

The capivara is unable to deliver all the properties of the element.

However he can deliver the following properties:

`style`, `classList`, `textContext`, `baseURI`, `className`, `clientHeight`, `clientLeft`, `clientTop`, `clientWidth`, `firstChild`, `title`, `string`, `tagName`, `tabIndex`, `outerHTML`, `localeString`, `localName`, `dir`, `scrollLeft`, `scrollHeight`, `scrollWidth`, `scrollTop`

Roadmap
=======

- Read element propeties after a specified event
- Support `addEventListener` method
- Support elements methods (like `element.classList.add`, `element.innerHTML`)

Contributing
============

Want to contribute? Read the CONTRIBUTING.md.

License
=======

.. image:: https://i.creativecommons.org/l/by/4.0/88x31.png
    :target: http://creativecommons.org/licenses/by/4.0/

