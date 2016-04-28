import sys, os
import subprocess, json
import pkg_resources

# TODO: on install donwload and install phantomjs binary

class _capivara(object):

    def __init__(self, port):
        super(_capivara, self).__init__()
        self.port = port

        self.file_init = self.mountInit(str(port))
        self.file_exit = self.mountExit()

    def __call__(self, func):
        return self.execute()

    def procedure(self, procedure):
        resource_package = __name__
        resource_path = os.path.join('../procedures', procedure + '.js')
        resource = pkg_resources.resource_string(resource_package, resource_path)
        return resource

    def mountInit(self, port):
        procedure = self.procedure('init')
        init = [
            procedure,
            "page.open('http://127.0.0.1:{}'".format(port),
            ",function(s){ var element = page.evaluate(function () {", ]

        return "".join(init)

    def mountExit(self):
        return self.procedure('end')

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
        dom_object = json.loads(output)

        if not error:
            return dom_object
        else:
            raise ProcessException(command, error, output)


def init(port=8000):
    return _capivara(port)
