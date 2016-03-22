import sys, os
import subprocess, json

# TODO: create file from settings
# TODO: create procedures functions like (filterByProps)
# TODO: filter object in script.js using mask

# TODO: on install needs permission to write in script.js file
# TODO: on install donwload and install phantomjs binary

class _capivara(object):

    def __init__(self, port):
        super(_capivara, self).__init__()
        self.port = port

        self.file_init = self.mountInit(str(port))
        self.file_exit = self.mountExit()

    def __call__(self, func):
        return self.execute()

    def mountInit(self, port):
        procedure_init = open('procedures/init.js', 'r')
        init = [
            str(procedure_init.read()),
            "page.open('http://127.0.0.1:{}'".format(port),
            ",function(s){ var element = page.evaluate(function () {", ]

        procedure_init.close()
        return "".join(init)

    def mountExit(self):
        procedure_end = open('procedures/end.js', 'r')
        exit = str(procedure_end.read())
        procedure_end.close()
        return exit

    def querySelector(self, selector=None):
        file = open('script.js','w')
        file.seek(0)
        file.truncate()
        file.write(self.file_init)
        file.write("return document.querySelector('{}');".format(str(selector), "{}"))
        file.write("}); element = normalizeElement(element);")
        file.write(self.file_exit)
        file.close()

        process = subprocess.Popen('phantomjs script.js', shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        output, error = process.communicate()
        print output
        dom_object = json.loads(output)

        if not error:
            return dom_object
        else:
            raise ProcessException(command, error, output)


def init(port=8000):
    return _capivara(port)
