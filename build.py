#!/usr/bin/python
from subprocess import call
import shutil
import os


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


def generate_pdf():
    log("Generating PDFs ...")

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

generate_pdf()

log("Done.")

