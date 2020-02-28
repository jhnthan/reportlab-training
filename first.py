# Main or Core that build documents
from reportlab.platypus.doctemplate import BaseDocTemplate
# Group of pages that shape the document
from reportlab.platypus.doctemplate import PageTemplate
# Content of a page tha build information
from reportlab.platypus.frames import Frame
# Items flowables that is the information ifself
from reportlab.platypus.paragraph import Paragraph
# utils for obtain standards, measurements and styles
from reportlab.lib.styles import ParagraphStyle
# file
from io import BytesIO

# -------------------------------------
# ABSTRABT
# -------------------------------------
# Reportlab have a simple system of building, but his creators
# don't know explain very good the simple way for integrate all
# his tools and know easy a fastly.
#
# Hyerarchy:
#   Document - The document ifself
#   |_PageTemplates - Designs of a pages for the document
#     |_Frames - Designs of a frames tha represent places of information
#       |_Flowables - Represent the informartion ifself that is putting in a frames
#
# Each frame can be component for one or more flowables
# Each PageTemplate should be component for one or more Frame almost one
# Each Document should be component for one or more PageTemplates almost one
#
# For build a document is neccesary setup the principals objects:
#   * create a frame or many
#   * with a frame created so create a PageTemplate or many PageTemplates and
#     assign his frames to each page
#   * finally create a document and assign the PageTemplates
#
# When the setup is complete is moment of begin to write the content.
# for doing it, only begin to use flowables for write content, change of frame,
# change of page, write text, draw whit canvas and a lot more.

# -------------------------------------
# SETUP
# first step is configure the document.
# -------------------------------------

# create a frames that are component of a page
# is possible have many diferents types of frames design for a same or diferents pages
frame_design_one = Frame(
    x1=0,
    y1=0,
    width=50,
    height=50,
    leftPadding=0,
    bottomPadding=0,
    rightPadding=0,
    topPadding=0,
    id='frame_design_one',
    showBoundary=1,
    overlapAttachedSpace=None,
    _debug=None
  )

# create a template page for document that have frames created allow change
# design when build the document.
# is possible have many diferents types of pages design for a same document
page_design_one = PageTemplate(
    id='page_design_one',
    frames=[frame_design_one],
    # onPage=_doNothing,
    # onPageEnd=_doNothing,
    pagesize=(100,100), # this override pagesize of the BaseDocTemplate
    autoNextPageTemplate=None,
    cropBox=None,
    artBox=None,
    trimBox=None,
    bleedBox=None
  )

# create a new document
# not is neccesary send all options for inicializate the document
# required parameters:
#   - filename -> a string name or InputStream
document = BaseDocTemplate(
    # pagesize=(400,400), # this is override for a pagesize of the PageTemplate
    pageTemplate=[], # add list of page template for here or use 'addPageTemplates()'
    showBoundary=1,
    filename=BytesIO(),
    leftmargin=4,
    leftMargin=4,
    rightMargin=4,
    topMargin=4,
    bottomMargin=4,
    allowSplitting=1,
    title='Document',
    author='JGCH',
    subject='Training',
    creator='JGCH',
    producer='JGCH',
    keywords=['Training, GitHub'],
    invariant=None,
    pageCompression=None,
    _pageBreakQuick=1,
    rotation=0,
    _debug=0,
    encrypt= None,
    cropMarks= None,
    enforceColorSpace= None,
    displayDocTitle= None,
    lang= None,
    initialFontName= None,
    initialFontSize= None,
    initialLeading= None,
    cropBox= None,
    artBox= None,
    trimBox= None,
    bleedBox= None,
    # keepTogetherClass= KeepTogether
  )

# add pages design to document from this metod or when create a document
document.addPageTemplates(page_design_one)

# -------------------------------------
# BEGIN TO ADD CONTENT
# when to add content at document, is
# similar to write a story step by step
# and you should use a list of flowables
# that help to write it.
# -------------------------------------

# list of flowables that represent the content of document
content = []

# add the first flowable called Paragraph, that allow write text
content.append(
  Paragraph(
    "This is a Paragraph ",
    ParagraphStyle(
      'MyStyle1',
      fontSize=10,
    )
  )
)

# when finish of write content, so you can send build it
document.build(
    content,
    filename="Training_pdf"
    #canvasmaker=canvas.Canvas
  )