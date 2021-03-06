import popplerqt5
import PyQt5



doc = popplerqt5.Poppler.Document.load("/home/mayijun/GITHUB/MLGH/pdf/test.pdf")
total_annotations = 0
for i in range(doc.numPages()):
    #print("========= PAGE {} =========".format(i+1))
    page = doc.page(i)
    annotations = page.annotations()
    (pwidth, pheight) = (page.pageSize().width(), page.pageSize().height())
    if len(annotations) > 0:
        for annotation in annotations:
            if  isinstance(annotation, popplerqt5.Poppler.Annotation):
                total_annotations += 1
                if(isinstance(annotation, popplerqt5.Poppler.HighlightAnnotation)):
                    quads = annotation.highlightQuads()
                    txt = ""
                    for quad in quads:
                        rect = (quad.points[0].x() * pwidth,
                                quad.points[0].y() * pheight,
                                quad.points[2].x() * pwidth,
                                quad.points[2].y() * pheight)
                        bdy = PyQt5.QtCore.QRectF()
                        bdy.setCoords(*rect)
                        txt = txt + str(page.text(bdy)) + ' '
    
                    #print("========= ANNOTATION =========")
                    
                    print(txt)
                    with open("/home/mayijun/GITHUB/MLGH/pdf/test.txt", "a") as f:
                        f.write(txt+'\n')
