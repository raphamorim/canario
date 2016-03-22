    element['capivara'] = {'conection': s};
    element = JSON.stringify(element);
    element = element.replace(/null+/g, '"null"');
    element = element.replace(/false+/g, '"false"');
    element = element.replace(/true+/g, '"true"');
    console.log(element);
    phantom.exit();
});