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
