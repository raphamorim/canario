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
