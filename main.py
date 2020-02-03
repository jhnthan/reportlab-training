# BaseDocTemplate
#   PageTemplate
#     one or more frames
#       one or more flowables

# Main or Core that build documents
from reportlab.platypus.doctemplate import BaseDocTemplate
# Group of pages that shape the document
from reportlab.platypus.doctemplate import PageTemplate
# Content of a page tha build information
from reportlab.platypus.frames import Frame
# Items flowables, allow handle the behavior of the document
# For example break page, jump pages, jump frames and more
from reportlab.platypus.doctemplate import NextFrameFlowable
from reportlab.platypus.doctemplate import FrameBreak
from reportlab.platypus.doctemplate import NextPageTemplate
from reportlab.platypus.flowables import PageBreak
# Items flowables that is the information ifself
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.tables import Table
# utils for obtain standards, measurements and styles
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle

from io import BytesIO

f = []
for x in range(0,16):
  f.append(
    Paragraph(
      "This is a Paragraph " + str(x),
      ParagraphStyle(
          'MyStyle1',
          fontSize=10,
      )
    )
  )

h = []
for x in range(0,16):
  h.append(
    Paragraph(
      "Other page" + str(x),
      ParagraphStyle(
          'MyStyle1',
          fontSize=10,
      )
    )
  )

content = []
content.append(
  Paragraph(
    "This is a Paragraph ",
    ParagraphStyle(
      'MyStyle1',
      fontSize=10,
    )
  )
)
content.append(
  Paragraph(
    "This is a Paragraph 2",
    ParagraphStyle(
      'MyStyle1',
      fontSize=10,
    )
  )
)
content.append(
  Paragraph(
    "This is a Paragraph 5",
    ParagraphStyle(
      'MyStyle1',
      fontSize=10,
    )
  )
)
content.append(NextPageTemplate('page2'))
content.append(
  Paragraph(
    "This is a Paragraph 3",
    ParagraphStyle(
      'MyStyle1',
      fontSize=10,
    )
  )
)
content.append(
  Paragraph(
    "This is a Paragraph 4",
    ParagraphStyle(
      'MyStyle1',
      fontSize=10,
    )
  )
)

frame1 = Frame(
  x1=0,
  y1=0,
  width=50 * mm,
  height=20 * mm,
  leftPadding=0,
  bottomPadding=0,
  rightPadding=0,
  topPadding=0,
  id='frame1',
  showBoundary=0.1)

frame2 = Frame(
  x1=0,
  y1=0,
  width=50 * mm,
  height=8 * mm,
  leftPadding=0,
  bottomPadding=0,
  rightPadding=0,
  topPadding=0,
  id='frame2',
  showBoundary=0.1)
page1 = PageTemplate(id='page1',frames=[frame1],pagesize=(100*mm,100*mm))
page2 = PageTemplate(id='page2',frames=[frame2],pagesize=(80*mm,80*mm))
doc = BaseDocTemplate(filename=BytesIO(), showBoundary=1)
doc.addPageTemplates(page1)
doc.addPageTemplates(page2)
doc.build(content, filename="Training.pdf")