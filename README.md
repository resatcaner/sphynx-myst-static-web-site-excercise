# sphynx-myst-static-web-site-excercise

[MyST](https://myst-parser.readthedocs.io/en/latest/) is a parser that helps sphinx to read markdown. 

LiveReload, is a server, that helps to rebuild any changes.

## 1) Creating the project

Following needs to be installed:

>- sphinx
>- livereload
>- myst-parser

To initiate the sphinx, use terminal and run the `sphinx-quickstart` command.

Following code will make the auto reload work:

```from livereload import Server, shell

if __name__ == '__main__':
    server = Server()
    server.watch('*.rst', shell('make html'), delay=1)
    server.watch('*.md', shell('make html'), delay=1)
    server.watch('*.py', shell('make html'), delay=1)
    server.watch('_static/*', shell('make html'), delay=1)
    server.watch('_templates/*', shell('make html'), delay=1)
    server.serve(root='_build/html')
   ```

## 2) Configuration: conf.py

```
project = 'Project Name'
copyright = 'Copyright line'
author = 'Author Name'
extensions = [
    'myst_parser',   <remove>the myst parser<remove>
    "sphinx.ext.autodoc",
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'alabaster'
html_static_path = ['_static']
myst_enable_extensions = [
    "colon_fence",     <remove>colon fence for rich images<remove>
]
```

## 3) Elements

### 1) Toctree:

Toc means table of contents. More than 1 toc tree can be used in pages.

```
```{toctree}
---
maxdepth: 2
caption: |
    Contents:
glob:
---

*
```.
```

### 2) Images:

With colon fence we can use following syntax. target-label can be called with the {ref} tag to create links.

```:::{figure-md} target-label
:class: myclass

<img src="python-logo.png" alt="Python Logo" class="bg-primary" width="300px">

Python comes from the *Python Software Foundation*.
:::
```

### 3) Links:

Usual MD concept is used:
`[link_text | -Blank-](link_label)`

link label: It can be a file name or role reference.
e.g. : `[About Us](about_us)`

If the link text is blank, it is automatically assigned as the title.

### 4) Downloads:

```
{download}`link_text<filepath>`
```

### 5) Roles: 
Roles can be defined to any header or item by (rolename)=
e.g.
```
(investors)=
## Investors

Our investors are very proud to be involved with us.
```

to refer to this link following statemend should be used.
```
{ref}`rolename`
```

## 4) Documenting Code

### 1) Codeblocks
Codeblock automatically defines the block for the language. However, to give more params
it is needed to have {code-block} directive for myst.
:linenos: -> shows the line numbers
YAML format also works in between `---` 

```
```{code-block} javascript
:linenos:
function hello(msg) {
    return 'Hello ${msg}'
}
```.
```

### 2) Literalinclude

Literalinclude is to import a py file. 
```
```{literalinclude} my_demo.py
---
linenos: true
emphasize-lines: 2-3
---
```.
```

### 3) Autodoc

the module directory needs to be added to the python path with following code in conf.py
```
import os
import sys
sys.path.insert(0, os.path.abspath("."))
```

then for importing the files to a page:
```
```{eval-rst}
.. autoclass:: my_demo.MyDemo
    :members:
```.
```

## 5) Intersphinx

Intersphinx allows to connect to the other sphinx sites and use their reference inventory.

To use, we need to add lines to conf.py
```
extensions = [
    'myst_parser',
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
]
.
.
.

intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

myst_url_schemes = ["http", "https", ]
```
myst_url_schemes is needed to define the schemes from external.

To reach external links:
`[](external_site_alias:external_site_link)`
for our case:
`[](sphinx:ref-role)`

