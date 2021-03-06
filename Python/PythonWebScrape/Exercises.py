# ---
# title: "Web scraping with Python Exercises"
# output: ioslides_presentation
# jupyter:
#   jupytext_format_version: '1.3'
#   jupytext_formats: ipynb,Rmd:rmarkdown,py:light,md:markdown
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.7.0
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: true
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: false
#     toc_position: {}
#     toc_section_display: true
#     toc_window_display: true
# ---

# ## Exercise: Retrieve exhibits data {.smaller}
# In this exercise you will retrieve information about the art
# exhibitions at Harvard Art Museums from
# `https://www.harvardartmuseums.org/visit/exhibitions`
#
# 1. Using a web browser (Firefox or Chrome recommended) inspect the
#    page at `https://www.harvardartmuseums.org/visit/exhibitions`. Examine
#    the network traffic as you interact with the page. Try to find
#    where the data displayed on that page comes from.
# 2. Make a `get` request in Python to retrieve the data from the URL
#    identified in step1.
# 3. Write a *loop* or *list comprehension* in Python to retrieve data
#    for the first 5 pages of exhibitions data.
# 4. Bonus (optional): Arrange the data you retrieved into dict of
#    lists. Convert it to a pandas `DataFrame` and save it to a `.csv`
#    file.

# ## Exercise: parsing HTML {.smaller}
# In this exercise you will retrieve information about the physical
# layout of the Harvard Art Museums. The web page at
# <https://www.harvardartmuseums.org/visit/floor-plan> contains this
# information in HTML from.
#
# 1. Using a web browser (Firefox or Chrome recommended) inspect the
#    page at `https://www.harvardartmuseums.org/visit/floor-plan`. Copy
#    the `XPath` to the element containing list of facilities located on
#    **level 1**. information. (HINT: the element if interest is a `ul`,
#    i.e., an "unordered list" of class `ifp-floors__rooms`.)
# 2. Make a `get` request in Python to retrieve the web page at
#    <https://www.harvardartmuseums.org/visit/floor-plan>. Extract the
#    content from your request object and parse it using `html.fromstring`
#    from the `lxml` library.
# 3. Use the `XPath` you identified in step one to select the HTML list item
#    containing level one information.
# 4. Use a *for loop* or *list comprehension* to iterate over the
#    sub-elements of the list item you selected in the previous step and
#    extract the text from each one.   
# 5. Bonus (optional): Extract the list of facilities available on each level.
