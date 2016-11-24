#!/usr/bin/python
from subprocess import call
import shutil
import os
import sys


def log(msg):
    
    print "  " + msg
    print


def clean(dirpath):
    if (dirpath != "target/"):
	raise Error("Failed security check! You are trying to delete something which is not target/ directory: " + dirpath)

    log( "Cleaning " + dirpath )

    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)


def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

def generate_pdf():

    log("Generating PDFs ...")
    
    if which("wkhtmltopdf") == None:
        log("ERROR: Couldn't find program wkhtmltopdf , it's needed to generate the pdfs!" )
        sys.exit(-1)

    os.mkdir("target/pdf/")

    for file in os.listdir("target/"):
        if file.endswith(".html"):        
            call(["wkhtmltopdf", "--minimum-font-size", "18", "target/" + str(file), "target/pdf/" + str(file).replace("html", "pdf")])


print

clean("target/")

log("Creating html ...")
    
call(["jupyter", "nbconvert", "--execute", "--output-dir", "target",  "*.ipynb"])

print
log("Copying other files ...")

shutil.copytree("img/", "target/img/")
shutil.copytree("js/", "target/js/")
shutil.copytree("css/", "target/css/")

log("Website generated at target/")

generate_pdf()

log("Done.")


