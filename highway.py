import sld

# nieuwe sld
s = sld.Sld('Highway','OSM Roads','Roads based on field highway')



# outline fts
fts = sld.Fts()

#hoofdwegen
f = sld.OgcFilter('highway','=','primary')
fts.addRule(sld.Rule('hoofdweg', 20000,   500000,  f, sld.Line('#aaaa11', 4)))
fts.addRule(sld.Rule('hoofdweg', None,    20000,    f, sld.Line('#aaaa11', 4)))
#autowegen
f = sld.OgcFilter('highway','=','trunk')
fts.addRule(sld.Rule('autoweg', 20000,   500000,  f, sld.Line('#aa5511', 5)))
fts.addRule(sld.Rule('autoweg', None,    20000,    f, sld.Line('#aa5511', 5)))
# snelwegen
f = sld.OgcFilter('highway','=','motorway')
fts.addRule(sld.Rule('snelweg', 20000,   500000,  f, sld.Line('#aa1111', 5)))
fts.addRule(sld.Rule('snelweg', None,    20000,   f, sld.Line('#aa1111', 5)))

s.addFts(fts)



# inline fts
fts = sld.Fts()

#hoofdwegen
f = sld.OgcFilter('highway','=','primary')
#fts.addRule(sld.Rule('autoweg', 2000000, None,    f, sld.Line('#ffff22', 0.7)))
fts.addRule(sld.Rule('autoweg', 500000,  2000000, f, sld.Line('#ffff22', 0.7)))
fts.addRule(sld.Rule('autoweg', 20000,   500000,  f, sld.Line('#ffff22', 2)))
fts.addRule(sld.Rule('autoweg', None,    20000,   f, sld.Line('#ffff22', 2)))
#autowegen
f = sld.OgcFilter('highway','=','trunk')
fts.addRule(sld.Rule('autoweg', 2000000, None,    f, sld.Line('#ff9922', 0.7)))
fts.addRule(sld.Rule('autoweg', 500000,  2000000, f, sld.Line('#ff9922', 1.5)))
fts.addRule(sld.Rule('autoweg', 20000,   500000,  f, sld.Line('#ff9922', 3)))
fts.addRule(sld.Rule('autoweg', None,    20000,   f, sld.Line('#ff9922', 3)))
# snelwegen
f = sld.OgcFilter('highway','=','motorway')
fts.addRule(sld.Rule('snelweg', 2000000, None,    f, sld.Line('#ff2222', 0.7)))
fts.addRule(sld.Rule('snelweg', 500000,  2000000, f, sld.Line('#ff2222', 2)))
fts.addRule(sld.Rule('snelweg', 20000,   500000,  f, sld.Line('#ff2222', 3)))
fts.addRule(sld.Rule('snelweg', None,    20000,   f, sld.Line('#ff2222', 3)))

# spoorwegen
f = sld.OgcFilter('railway','=','rail')
fts.addRule(sld.Rule('spoorweg', 2000000, None,    f, sld.Line('#666666', 0.5)))
fts.addRule(sld.Rule('spoorweg', 500000,  2000000, f, sld.Line('#666666', 0.5)))
fts.addRule(sld.Rule('spoorweg', 20000,   500000,  f, sld.Line('#666666', 0.7)))
fts.addRule(sld.Rule('spoorweg', None,    20000,   f, sld.Line('#666666', 1)))

# straten
#f = sld.OgcFilter('highway', '=', 'residential')
#fts.addRule(sld.Rule('straat', None, 20000, f, sld.Line('#dddddd', 6)))

# labels
f = sld.OgcFilter('highway', '=', 'residential')
fnt = sld.Font('Ubuntu', 11, 'italic', 'bold')
fts.addRule(sld.Rule('labels',None, 20000, None, sld.LineText('name', '#222222', fnt, True)))



s.addFts(fts)



# exporteren

s.saveToFile('test.sld')
s.saveToClipboard()

