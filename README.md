# REPORTLAB training

a little examples made with reportlab for practice.

## NOTE

* At the moment of make this repository i using ReportLab V.3.5.34
* I don't upload the pdf files resulting, because is better that you self experiment

## ABSTRACT

Reportlab have a simple system of building, but his creators
don't know explain very good the simple way for integrate all
his tools of way easy a fastly.

## HYERARCHY

    Document - The document ifself
    |_PageTemplates - Designs of a pages for the document
      |_Frames - Designs of a frames tha represent places of information
        |_Flowables - Represent the informartion ifself that is putting in a frames

### ¿What?

* Each frame can be compound for one or more flowables
* Each PageTemplate should be compound for one or more Frame at least one
* Each Document should be compound for one or more PageTemplates at least one

## HOW TO BUILD

### Setup

For build a document is neccesary setup the principals objects:

* create a frame or many
* with a frame created so create a PageTemplate or many PageTemplates and assign his frames to each page
* finally create a document and assign the PageTemplates

### Write content

When the setup is complete is moment of begin to write the content. For doing it, only begin to use flowables that help to:

* change frame
* change of page
* write text
* draw tables
* draw whit canvas

## ¿AND NOW?

See the first.py and second.py files for begin to know the how.