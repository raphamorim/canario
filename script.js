function normalizeElement(obj) {
    if (!obj)
        return {};

    return {
        'classList': obj.classList,
        'textContext': obj.textContext,
        'baseURI': obj.baseURI,
        'className': obj.className,
        'clientHeight': obj.clientHeight,
        'clientLeft': obj.clientLeft,
        'clientTop': obj.clientTop,
        'clientWidth': obj.clientWidth,
        'firstChild': obj.firstChild,
        'title': obj.title,
        'string': obj.toString(),
        'tagName': obj.tagName,
        'tabIndex': obj.tabIndex,
        'outerHTML': obj.outerHTML,
        'localeString': obj.toLocaleString(),
        'localName': obj.localName,
        'dir': obj.dir,
        'scrollLeft': obj.scrollLeft,
        'scrollHeight': obj.scrollHeight,
        'scrollWidth': obj.scrollWidth,
        'scrollTop': obj.scrollTop,
        'style': obj.style
    }
}

var page = require('webpage').create();
page.open('http://127.0.0.1:8080',function(s){ var element = page.evaluate(function () {return document.querySelector('canvas');}); element = normalizeElement(element);    element['capivara'] = {'conection': s};
    element = JSON.stringify(element);
    element = element.replace(/null+/g, '"null"');
    element = element.replace(/false+/g, '"false"');
    element = element.replace(/true+/g, '"true"');
    console.log(element);
    phantom.exit();
});