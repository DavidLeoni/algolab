
Source code as Jupyter Python worksheets for algorithms lab of Scientific Programming course (QCB master, University of Trento)

Website: http://davidleoni.github.io/algolab

** DISCLAIMER **:With these worksheets, we pushed the limits of Jupyter, sometimes abusing its functionality to the point 
of making ugly workarounds when necessary. So code may or may not work depending on your particular version of Jupyter.

### Features

* Looks like a real website (sort of), with sidebar and rudimental navigation bar
* Presentation friendly: when the browser window is small, the sidebar disappers. To show it again, hover mouse on the left.
* Automaticalaly generates PDFs. NOTE: The worksheets are meant to create a website and to be browsed online. 
Generated PDFs won't look that pretty.
* Allows easily running `unittest` tests by launching `algolab.run(NameOfTheTestClass)`
* Customizable with python, JS, and CSS code common to all worksheets


### Installation instructions

1. Install Python 2.7
2. [Install Jupyter](http://jupyter.org/install.html)
3. If you also want to build the pdfs, install the program [WkHtmlToPdf](http://wkhtmltopdf.org/downloads.html), at version >= 0.12.4  . In particular, to install it in Ubuntu, run
    ```bash
        sudo apt-get install wkhtmltopdf
    ```

### Building

To build the website, while in the console, from the root of the directory run 

```bash
python build.py
```

Site will be created in `target/` folder. 

NOTE: to also generate PDFs you will need to install WkHtmlToPdf (See point 3 in [previous paragraph](#installation-instructions)


### Editing the worksheets

First of all, run Jupyter from the root of the directory


```bash
    jupyter notebook
```

* Python code common to all worksheets is in [algolab.py](algolab.py)
* Javascript code common to all worksheets is in `js/loc.js`
* CSS common to all worksheets is in `css/algolab.css`

Each worksheet must start with this Python code:

```python
import algolab
algolab.init()
```

Running it will create the sidebar even during editing in Jupyter. If you want to refresh the sidebar, just run again the cell.

#### Launch unit tests

Inside worksheets you can run `unittest` tests by launching 

```python
algolab.run(nameOfTheTestClass)
```