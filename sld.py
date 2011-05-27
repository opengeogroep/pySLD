import xml.dom.minidom
import re
#ruletypes = {0:'marker', 1:'line', '2':'polygon'}
signxml = {'=':'PropertyIsEqualTo'}

# sld
class Sld():

    def __init__(self, name=None, title=None, abstract=None, featuretypestyles=None):
        self.name = name
        self.title = title
        self.abstract = abstract
	if featuretypestyles is None:
	    self.ftses = []
	else:
	    self.ftses = featuretypestyles

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

    def getSldDOM(self):
	doc = xml.dom.minidom.Document()
	styledlayerdescriptor = doc.createElement("StyledLayerDescriptor")
	styledlayerdescriptor.setAttribute("xsi:schemaLocation", "http://www.opengis.net/sld StyledLayerDescriptor.xsd")
	styledlayerdescriptor.setAttribute("xmlns", "http://www.opengis.net/sld")
	styledlayerdescriptor.setAttribute("xmlns:ogc", "http://www.opengis.net/ogc")
	styledlayerdescriptor.setAttribute("xmlns:xlink", "http://www.w3.org/1999/xlink")
	styledlayerdescriptor.setAttribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
	styledlayerdescriptor.setAttribute("version", "1.0.0")
	_comment = doc.createComment("a Named Layer is the basic building block of an SLD document")
	styledlayerdescriptor.appendChild(_comment)
	namedlayer = doc.createElement("NamedLayer")
	userstyle = doc.createElement("UserStyle")
        if self.name:
            _name = doc.createElement("Name")
            _name.appendChild(doc.createTextNode(self.name))
            namedlayer.appendChild(_name)
        if self.title:
		_title = doc.createElement("Title")
		_title.appendChild(doc.createTextNode(self.title))
		userstyle.appendChild(_title)
        if self.abstract:
		abstract = doc.createElement("Abstract")
		abstract.appendChild(doc.createTextNode(self.abstract))
		userstyle.appendChild(abstract)
        if len(self.ftses) > 0:
            	for f in self.ftses:
			userstyle.appendChild(f.getSldDOM())
	namedlayer.appendChild(userstyle)
	styledlayerdescriptor.appendChild(namedlayer)
	doc.appendChild(styledlayerdescriptor)
        return doc

    def addFts(self, fts):
        self.ftses.append(fts)
        
    def saveToFile(self,fn):
        outfile = open(fn,'w')
        outfile.write(self.getSldString(0,True))
        outfile.close()

    def DOMToFile(self,fn):
        outfile = open(fn,'w')
	finaldom = self.getSldDOM()
	uglyXml = finaldom.toprettyxml(indent='  ', encoding="ISO-8859-1")
	text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)    
	prettyXml = text_re.sub('>\g<1></', uglyXml)
	#print prettyXml
        outfile.write(prettyXml)
        outfile.close()

    def saveToClipboard(self):
        import pygtk
        import gtk
        clipboard = gtk.clipboard_get()
        clipboard.set_text(self.getSldString(0,True))
        clipboard.store()

    def DOMtoClipboard(self):
	import pygtk
        import gtk
        clipboard = gtk.clipboard_get()
	finaldom = self.getSldDOM()
	uglyXml = finaldom.toprettyxml(indent='  ', encoding="ISO-8859-1")
	text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)    
	prettyXml = text_re.sub('>\g<1></', uglyXml)
	clipboard.set_text(prettyXml)
	clipboard.store()

# fts (featuretypestyle)
class Fts():

    def __init__(self,rules=None):
	if rules is None:
	    self.rules = []
	else:
	    self.rules = rules

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

    def getSldDOM(self):
	doc = xml.dom.minidom.Document()
	featuretypestyle = doc.createElement("FeatureTypeStyle")
        if len(self.rules) > 0:
            for r in self.rules:
                featuretypestyle.appendChild(r.getSldDOM())
        return featuretypestyle

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

    def getSldDOM(self):
	doc = xml.dom.minidom.Document()
	rule = doc.createElement("Rule")
        if self.name:
            _name = doc.createElement("Name")
            _name.appendChild(doc.createTextNode(self.name))
            rule.appendChild(_name)
        if self.ogcfilter:
            rule.appendChild(self.ogcfilter.getSldDOM())
        if self.scalemin:
            _mindenom = doc.createElement("MinScaleDenominator")
            _mindenom.appendChild(doc.createTextNode(str(self.scalemin)))
            rule.appendChild(_mindenom)
        if self.scalemax:
            _maxdenom = doc.createElement("MaxScaleDenominator")
            _maxdenom.appendChild(doc.createTextNode(str(self.scalemax)))
            rule.appendChild(_maxdenom)
        if self.symbol:
            rule.appendChild(self.symbol.getSldDOM())
        return rule

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

    def getSldDOM(self):
	doc = xml.dom.minidom.Document()
	_filter = doc.createElementNS("http://www.opengis.net/ogc","ogc:Filter")
	_filtertype = doc.createElementNS("http://www.opengis.net/ogc","ogc:" + signxml[self.sign])
	_propertyname = doc.createElementNS("http://www.opengis.net/ogc","ogc:PropertyName")
	_propertyname.appendChild(doc.createTextNode(str(self.field)))
	_filtertype.appendChild(_propertyname)
	_literal = doc.createElementNS("http://www.opengis.net/ogc","ogc:Literal")
	_literal.appendChild(doc.createTextNode(str(self.value)))
	_filtertype.appendChild(_literal)
	_filter.appendChild(_filtertype)
        return _filter

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

    def getSldDOM(self):
	doc = xml.dom.minidom.Document()
	_linesymbolizer = doc.createElement("LineSymbolizer")
	_stroke = doc.createElement("Stroke")
	_cssstroke = doc.createElement("CssParameter")
	_cssstroke.setAttribute("name", "stroke")
	_cssstroke.appendChild(doc.createTextNode(str(self.color)))
	_cssstrokew = doc.createElement("CssParameter")
	_cssstrokew.setAttribute("name", "stroke-width")
	_cssstrokew.appendChild(doc.createTextNode(str(self.width)))
	_cssstrokelj = doc.createElement("CssParameter")
	_cssstrokelj.setAttribute("name", "stroke-linejoin")
	_cssstrokelj.appendChild(doc.createTextNode("round"))
	_cssstrokelc = doc.createElement("CssParameter")
	_cssstrokelc.setAttribute("name", "stroke-linecap")
	_cssstrokelc.appendChild(doc.createTextNode("round"))
	_stroke.appendChild(_cssstroke)
	_stroke.appendChild(_cssstrokew)
	_stroke.appendChild(_cssstrokelj)
	_stroke.appendChild(_cssstrokelc)
	_linesymbolizer.appendChild(_stroke)
        return _linesymbolizer

# polygon
class Polygon():
    def __init__(self, fillcolor='#0000ff',strokecolor='#0000ff', strokewidth=1):
        self.fillcolor = fillcolor
	self.strokecolor = strokecolor
        self.strokewidth = strokewidth
    
    def __str__(self):
        result = 'polygon(fill:' + self.fillcolor + ', stroke:' + self.strokecolor + ', width:' + str(self.width) + ')'
        return result

    def getSldString(self,indent=0,nls=True):
        return ''

    def getSldDOM(self):
	doc = xml.dom.minidom.Document()
	_polysymbolizer = doc.createElement("PolygonSymbolizer")
	_fill = doc.createElement("Fill")
	_cssfill = doc.createElement("CssParameter")
	_cssfill.setAttribute("name", "fill")
	_cssfill.appendChild(doc.createTextNode(str(self.fillcolor)))
	_fill.appendChild(_cssfill)
	_polysymbolizer.appendChild(_fill)
	_stroke = doc.createElement("Stroke")
	_cssstroke = doc.createElement("CssParameter")
	_cssstroke.setAttribute("name", "stroke")
	_cssstroke.appendChild(doc.createTextNode(str(self.strokecolor)))
	_cssstrokew = doc.createElement("CssParameter")
	_cssstrokew.setAttribute("name", "stroke-width")
	_cssstrokew.appendChild(doc.createTextNode(str(self.strokewidth)))
	_stroke.appendChild(_cssstroke)
	_stroke.appendChild(_cssstrokew)
	_polysymbolizer.appendChild(_stroke)
        return _polysymbolizer

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
   
    def getSldDOM(self):
	doc = xml.dom.minidom.Document()
	_font = doc.createElement("Font")
        if self.family:
	    _cssff = doc.createElement("CssParameter")
	    _cssff.setAttribute("name", "font-family")
	    _cssff.appendChild(doc.createTextNode(str(self.family)))
            _font.appendChild(_cssff)
        if self.size:
	    _cssfs = doc.createElement("CssParameter")
	    _cssfs.setAttribute("name", "font-size")
	    _cssfs.appendChild(doc.createTextNode(str(self.size)))
            _font.appendChild(_cssfs)
        if self.style:
	    _cssfy = doc.createElement("CssParameter")
	    _cssfy.setAttribute("name", "font-style")
	    _cssfy.appendChild(doc.createTextNode(str(self.style)))
            _font.appendChild(_cssfy)
        if self.weight:
	    _cssfw = doc.createElement("CssParameter")
	    _cssfw.setAttribute("name", "font-weight")
	    _cssfw.appendChild(doc.createTextNode(str(self.weight)))
            _font.appendChild(_cssfw)
        return _font

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

    def getSldDOM(self):
	doc = xml.dom.minidom.Document()
	_textsymbolizer = doc.createElement("TextSymbolizer")
        if self.field:
	    _label = doc.createElement("Label")
	    _propertyname = doc.createElementNS("http://www.opengis.net/ogc","ogc:PropertyName")
	    _propertyname.appendChild(doc.createTextNode(str(self.field)))
	    _label.appendChild(_propertyname)
	    _textsymbolizer.appendChild(_label)
        if self.font:
            _textsymbolizer.appendChild(self.font.getSldDOM())
        _labelplacement = doc.createElement("LabelPlacement")
        _labelplacement.appendChild(doc.createElement("LinePlacement"))
        _textsymbolizer.appendChild(_labelplacement)
        if self.color:
	    _fill = doc.createElement("Fill")
	    _cssfill = doc.createElement("CssParameter")
	    _cssfill.setAttribute("name", "fill")
	    _cssfill.appendChild(doc.createTextNode(str(self.color)))
	    _fill.appendChild(_cssfill)
	    _textsymbolizer.appendChild(_fill)
        if self.followLine:
	    _vo1 = doc.createElement("VendorOption")
	    _vo1.setAttribute("name", "followLine")
	    _vo1.appendChild(doc.createTextNode("true"))
	    _textsymbolizer.appendChild(_vo1)
	    _vo2 = doc.createElement("VendorOption")
	    _vo2.setAttribute("name", "maxAngleDelta")
	    _vo2.appendChild(doc.createTextNode("90"))
	    _textsymbolizer.appendChild(_vo2)
	    _vo3 = doc.createElement("VendorOption")
	    _vo3.setAttribute("name", "maxDisplacement")
	    _vo3.appendChild(doc.createTextNode("400"))
	    _textsymbolizer.appendChild(_vo3)
	    _vo4 = doc.createElement("VendorOption")
	    _vo4.setAttribute("name", "repeat")
	    _vo4.appendChild(doc.createTextNode("150"))
	    _textsymbolizer.appendChild(_vo4)
        return _textsymbolizer


