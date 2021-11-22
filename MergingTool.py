#!/usr/bin/env python
# coding: utf-8

# In[6]:


from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.pdf import PageObject
from PyPDF2 import PdfFileMerger
import PyPDF2
import glob
import re

onlyfiles ="C:\\Users\\akagraw\\Desktop\\OneDrive\\MT\\Code\\PyPDF"
count=0

merger = PdfFileMerger()
for file in glob.glob(onlyfiles + "/*.pdf"):
    writer = PdfFileWriter()
    reader=PdfFileReader(file,'rb')
    merger.append(reader)
merger.write("result.pdf")
merger.close()

reader=PdfFileReader("result.pdf",'rb')
writer = PdfFileWriter()

num=reader.getNumPages()
ext=num%4

for i in range (0,num-ext,4):
    page1=reader.getPage(i)
    page2=reader.getPage(i+1)
    page3=reader.getPage(i+2)
    page4=reader.getPage(i+3)
    tent_width = 595
    tent_height = 1684
    translated_page = PageObject.createBlankPage(None,tent_width, tent_height)
    translated_page.mergeRotatedTranslatedPage(page3,180,0,825,1)
    translated_page.mergeRotatedTranslatedPage(page4,180,130,825,1)
    translated_page.mergeScaledTranslatedPage(page1, 1,-335, 0, 1)
    translated_page.mergeScaledTranslatedPage(page2,1,-595,0,1)
    translated_page.trimBox.lowerLeft = (-420, 468)
    translated_page.trimBox.upperRight = (90, 1170)
    translated_page.cropBox.lowerLeft = (-420, 468)
    translated_page.cropBox.upperRight = (90, 1170)
    writer.addPage(translated_page)

if(ext==1):
    page1=reader.getPage(num-1)
    tent_width = 595
    tent_height = 1684
    translated_page = PageObject.createBlankPage(None,tent_width, tent_height)
    ext_page = PageObject.createBlankPage(None,tent_width, tent_height)
    translated_page.mergeScaledTranslatedPage(page1, 1,-335, 0, 1)
    translated_page.mergeScaledTranslatedPage(ext_page,1,-595,0,1)
    translated_page.trimBox.lowerLeft = (-420, 468)
    translated_page.trimBox.upperRight = (90, 1170)
    translated_page.cropBox.lowerLeft = (-420, 468)
    translated_page.cropBox.upperRight = (90, 1170)
    writer.addPage(translated_page)

elif(ext==2):
    page1=reader.getPage(num-2)
    page2=reader.getPage(num-1)
    tent_width = 595
    tent_height = 1684
    translated_page = PageObject.createBlankPage(None,tent_width, tent_height)
    translated_page.mergeScaledTranslatedPage(page1, 1,-335, 0, 1)
    translated_page.mergeScaledTranslatedPage(page2,1,-595,0,1)
    translated_page.trimBox.lowerLeft = (-420, 468)
    translated_page.trimBox.upperRight = (90, 1170)
    translated_page.cropBox.lowerLeft = (-420, 468)
    translated_page.cropBox.upperRight = (90, 1170)
    writer.addPage(translated_page)

elif(ext==3):
    page1=reader.getPage(num-3)
    page2=reader.getPage(num-2)
    page3=reader.getPage(num-1)
    tent_width =595
    tent_height = 1684
    translated_page = PageObject.createBlankPage(None,tent_width, tent_height)
    translated_page.mergeRotatedTranslatedPage(page3,180,0,825,1)
    translated_page.mergeScaledTranslatedPage(page1, 1,-335, 0, 1)
    translated_page.mergeScaledTranslatedPage(page2,1,-595,0,1)
    translated_page.trimBox.lowerLeft = (-420, 468)
    translated_page.trimBox.upperRight = (90, 1170)
    translated_page.cropBox.lowerLeft = (-420, 468)
    translated_page.cropBox.upperRight = (90, 1170)
    writer.addPage(translated_page)
with open("C:\\Users\\akagraw\\Desktop\\OneDrive\\MT\\Code\\PyPDF\\result.pdf", 'wb') as f:
    writer.write(f)

print("Done!!")




