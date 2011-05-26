
# constants
signxml = {'=':'PropertyIsEqualTo'}



# sld
class Sld():

    def __init__(self, name=None, title=None, abstract=None):
        self.name = name
        self.title = title
        self.abstract = abstract
        self.ftses = []

    def  __str__(self):
        return 'sld(ftses:' + str(len(self.ftses)) + ')'

    def getSldString(self,indent=0,nls=True):
        result = ''
        result += '<?xml version="1.0" encoding="ISO-8859-1"?>\n'
        result += '<StyledLayerDescriptor version="1.0.0"\n'
        result += ' xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd"\n'
        result += ' xmlns="http://www.opengis.net/sld"\n'
        result += ' xmlns:ogc="http://www.opengis.net/ogc"\n'
        result += ' xmlns:xlink="http://www.w3.org/1999/xlink"\n'
        result += ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
        result += '  <!-- a Named Layer is the basic building block of an SLD document -->\n'
        result += '  <NamedLayer>\n'
        if self.name:
            result += (indent * ' ')
            result += '    <Name>' + self.name+ '</Name>\n'
        result += '    <UserStyle>\n'        
        if self.title:
            result += '      <Title>' + self.title+ '</Title>\n'
        if self.abstract:
            result += '      <Abstract>' + self.abstract + '</Abstract>\n'
        if len(self.ftses) > 0:
            for f in self.ftses:
                result += f.getSldString(6,nls)
        result += '    </UserStyle>\n'
        result += '  </NamedLayer>\n'
        result += '</StyledLayerDescriptor>\n'
        return result

    def addFts(self, fts):
        self.ftses.append(fts)
        
    def saveToFile(self,fn):
        outfile = open(fn,'w')
        outfile.write(self.getSldString(0,True))
        outfile.close()

    def saveToClipboard(self):
        import pygtk
        import gtk
        clipboard = gtk.clipboard_get()
        clipboard.set_text(self.getSldString(0,True))
        clipboard.store()



# fts (featuretypestyle)
class Fts():

    def __init__(self):
        self.rules = []

    def  __str__(self):
        return 'fts(rules:' + str(len(self.rules)) + ')'

    def getSldString(self,indent=0,nls=True):
        result = (indent * ' ') + '<FeatureTypeStyle>'
        if len(self.rules) > 0:
            if nls:
                result += '\n'
            for r in self.rules:
                result += r.getSldString(indent+2,nls)
        if nls:
            result += '' + (indent * ' ')
        result += '</FeatureTypeStyle>\n'
        return result

    def addRule(self, rule):
        self.rules.append(rule)





# Rule
class Rule():

    def __init__(self, name=None, scalemin=None, scalemax=None, ogcfilter=None, symbol=None):
        self.name = name
        self.scalemin = scalemin
        self.scalemax = scalemax
        self.ogcfilter = ogcfilter
        self.symbol = symbol

    def  __str__(self):
        return 'rule()'

    def getSldString(self,indent=0,nls=True):
        result = (indent * ' ') + '<Rule>'
        if self.name:
            if nls:
                result += '\n' + (indent * ' ')
            result += '  <Name>' + self.name+ '</Name>'
        if self.scalemin:
            if nls:
                result += '\n' + (indent * ' ')
            result += '  <MinScaleDenominator>' + str(self.scalemin) + '</MinScaleDenominator>'
        if self.scalemax:
            if nls:
                result += '\n' + (indent * ' ')
            result += '  <MaxScaleDenominator>' + str(self.scalemax) + '</MaxScaleDenominator>'
        if self.ogcfilter:
            if nls:
                result += '\n'
            result += self.ogcfilter.getSldString(indent+2,nls)
        if self.symbol:
            if nls:
                result += '\n'
            result += self.symbol.getSldString(indent+2,nls)
        if nls:
            result += '\n' + (indent * ' ')
        result += '</Rule>\n'
        return result
        
  


# OgcFilter
class OgcFilter():
    def __init__(self,field,sign,value):
        self.field = field
        self.sign = sign
        self.value = value
    
    def __str__(self):
        result = 'filter(' + self.field + ' ' + self.sign + ' ' + str(self.value) + ')'
        return result

    def getSldString(self,indent=0,nls=True):
        result = (indent * ' ') + '<ogc:Filter>'
        if nls:
            result += '\n' + (indent * ' ')
        result += '  <ogc:' + signxml[self.sign]+ '>'
        if nls:
            result += '\n' + (indent * ' ')
        result += '    <ogc:PropertyName>' + str(self.field) + '</ogc:PropertyName>'
        if nls:
            result += '\n' + (indent * ' ')
        result += '    <ogc:Literal>' + str(self.value) + '</ogc:Literal>'
        if nls:
            result += '\n' + (indent * ' ')
        result += '  </ogc:' + signxml[self.sign]+ '>'
        if nls:
            result += '\n' + (indent * ' ')
        result += '</ogc:Filter>'
        return result


# line
class Line():
    def __init__(self, color='#0000ff', width=1):
        self.color = color
        self.width = width
    
    def __str__(self):
        result = 'line(color:' + self.color + ', width:' + str(self.width) + ')'
        return result

    def getSldString(self,indent=0,nls=True):
        result = (indent * ' ') + '<LineSymbolizer>'
        if nls:
            result += '\n' + (indent * ' ') + '  '
        result += '<Stroke>'
        if nls:
            result += '\n' + (indent * ' ') + '    '
        result += '<CssParameter name="stroke">' + str(self.color) + '</CssParameter>'
        if nls:
            result += '\n' + (indent * ' ') + '    '
        result += '<CssParameter name="stroke-width">' + str(self.width) + '</CssParameter>'
        if nls:
            result += '\n' + (indent * ' ') + '    '
        result += '<CssParameter name="stroke-linejoin">round</CssParameter>'
        if nls:
            result += '\n' + (indent * ' ') + '    '
        result += '<CssParameter name="stroke-linecap">round</CssParameter>'
        if nls:
            result += '\n' + (indent * ' ') + '  '
        result += '</Stroke>'
        if nls:
            result += '\n' + (indent * ' ')
        result += '</LineSymbolizer>'
        return result

#font
class Font():
    def __init__(self, family=None, size=None, style=None, weight=None):
        self.family = family
        self.size = size
        self.style = style
        self.weight = weight
    
    def getSldString(self,indent=0,nls=True):
        result = '<Font>'
        if self.family:
            if nls:
                result += '\n' + (indent * ' ') + '  '
            result += '<CssParameter name="font-family">' + str(self.family) + '</CssParameter>'
        if self.size:
            if nls:
                result += '\n' + (indent * ' ') + '  '
            result += '<CssParameter name="font-size">' + str(self.size) + '</CssParameter>'
        if self.style:
            if nls:
                result += '\n' + (indent * ' ') + '  '
            result += '<CssParameter name="font-style">' + str(self.style) + '</CssParameter>'
        if self.weight:
            if nls:
                result += '\n' + (indent * ' ') + '  '
            result += '<CssParameter name="font-weight">' + str(self.weight) + '</CssParameter>'
        if nls:
            result += '\n' + (indent * ' ') 
        result += '</Font>'
        return result


#line text symbol
class LineText():
    def __init__(self, field=None, color='#000000', font=None, followLine=False):
        self.field = field
        self.color = color
        self.font = font
        self.followLine = followLine
    
    def __str__(self):
        result = 'LineText(field:' + self.field + ', color:' + self.color + ')'
        return result

    def getSldString(self,indent=0,nls=True):
        result = (indent * ' ') + '<TextSymbolizer>'
        if self.field:
            if nls:
                result += '\n' + (indent * ' ') + '  '
            result += '<Label><ogc:PropertyName>' + str(self.field) + '</ogc:PropertyName></Label>'
        if self.color:
            if nls:
                result += '\n' + (indent * ' ') + '  '
            result += '<Fill><CssParameter name="fill">' + str(self.color) + '</CssParameter></Fill>'
        if self.font:
            if nls:
                result += '\n' + (indent * ' ') + '  '
            result += self.font.getSldString(indent+2,nls)
        if self.followLine:
            if nls:
                result += '\n' + (indent * ' ') + '  '
            result += '<VendorOption name="followLine">true</VendorOption>'
            if nls:
                result += '\n' + (indent * ' ') + '  '
            result += '<VendorOption name="maxAngleDelta">90</VendorOption>'
            if nls:
                result += '\n' + (indent * ' ') + '  '
            result += '<VendorOption name="maxDisplacement">400</VendorOption>'
            if nls:
                result += '\n' + (indent * ' ') + '  '
            result += '<VendorOption name="repeat">150</VendorOption>'
            if nls:
                result += '\n' + (indent * ' ') + '  '
            result += '<LabelPlacement><LinePlacement /></LabelPlacement>'
        if nls:
            result += '\n' + (indent * ' ') 
        result += '</TextSymbolizer>'
        return result


