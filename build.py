#!/usr/bin/python
from subprocess import call
import shutil
import glob
import os
import sys
import fileinput
import string

def log(msg):
    
    print "  " + msg
    print


def clean(dirpath):
    if (dirpath != "target/"):
	raise Exception("Failed security check! You are trying to delete something which is not target/ directory: " + dirpath)

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


def replace(stext, rtext):
    
    path = "target/*.html"

    log("finding: " + stext + " replacing with: " + rtext + " in: " + path)

    files = glob.glob(path)
    for line in fileinput.input(files,inplace=1):
      lineno = 0
      lineno = string.find(line, stext)
      if lineno >0:
            line =line.replace(stext, rtext)

      sys.stdout.write(line)




def generate_pdf():

    log("Generating PDFs ...")
    
    if which("wkhtmltopdf") == None:
        log("ERROR: Couldn't find program wkhtmltopdf , it's needed to generate the pdfs!" )
        sys.exit(-1)

    os.mkdir("target/pdf/")

    for file in os.listdir("target/"):
        if file.endswith(".html"):        
            call(["wkhtmltopdf", "--minimum-font-size", "16", "target/" + str(file), "target/pdf/" + str(file).replace("html", "pdf")])


print

clean("target/")

log("Creating html ...")
    
call(["jupyter", "nbconvert", "--execute", "--output-dir", "target",  "*.ipynb"])

print
log("Copying other files ...")


shutil.copytree("img/", "target/img/")
shutil.copytree("js/", "target/js/")
shutil.copytree("css/", "target/css/")
shutil.copytree("past-exams/", "target/past-exams/")
for file in glob.glob(r'*.py'):                                                                                                                                  
    shutil.copy(file, "target/")

log("Website generated at target/")

generate_pdf()

log("Fixing Unix permissions...") #otherwise js/  can't be read by others !!!
call(["chmod", "-R", "a+r", "target"])
call(["chmod", "-R", "a+X", "target"])

log("Fixing html paths for offline browsing ....")

replace('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/', 'js/')
replace('https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/', 'js/')
replace('https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML', 'js/MathJax.js')

log("Website is now browsable at   " + os.path.abspath("target/index.html"))

log("Done.")


