import sld

# new sld
s = sld.Sld('Highway','OSM Roads','Roads based on field highway')

# outline fts
fts = sld.Fts()

# primary
f = sld.FltrComparison('highway','=','primary')
fts.addRule(sld.Rule('primary outline1', 20000,   500000,  f, sld.Line('#aaaa11', 4)))
fts.addRule(sld.Rule('primary outline2', None,    20000,    f, sld.Line('#aaaa11', 4)))
# trunks
f = sld.FltrComparison('highway','=','trunk')
fts.addRule(sld.Rule('trunk outline1', 20000,   500000,  f, sld.Line('#aa5511', 5)))
fts.addRule(sld.Rule('trunk outline2', None,    20000,    f, sld.Line('#aa5511', 5)))
# motorways
f = sld.FltrComparison('highway','=','motorway')
fts.addRule(sld.Rule('motorway outline1', 20000,   500000,  f, sld.Line('#aa1111', 5)))
fts.addRule(sld.Rule('motorway outline2', None,    20000,   f, sld.Line('#aa1111', 5)))

s.addFts(fts)

# inline fts
fts = sld.Fts()

# primary
f = sld.FltrComparison('highway','=','primary')
fts.addRule(sld.Rule('primary1', 500000,  2000000, f, sld.Line('#ffff22', 0.7)))
fts.addRule(sld.Rule('primary2', 20000,   500000,  f, sld.Line('#ffff22', 2)))
fts.addRule(sld.Rule('primary3', None,    20000,   f, sld.Line('#ffff22', 2)))
# trunks
f = sld.FltrComparison('highway','=','trunk')
fts.addRule(sld.Rule('trunk1', 2000000, None,    f, sld.Line('#ff9922', 0.7)))
fts.addRule(sld.Rule('trunk2', 500000,  2000000, f, sld.Line('#ff9922', 1.5)))
fts.addRule(sld.Rule('trunk3', 20000,   500000,  f, sld.Line('#ff9922', 3)))
fts.addRule(sld.Rule('trunk4', None,    20000,   f, sld.Line('#ff9922', 3)))
# motorways
f = sld.FltrComparison('highway','=','motorway')
fts.addRule(sld.Rule('motorway1', 2000000, None,    f, sld.Line('#ff2222', 0.7)))
fts.addRule(sld.Rule('motorway2', 500000,  2000000, f, sld.Line('#ff2222', 2)))
fts.addRule(sld.Rule('motorway3', 20000,   500000,  f, sld.Line('#ff2222', 3)))
fts.addRule(sld.Rule('motorway4', None,    20000,   f, sld.Line('#ff2222', 3)))

# rail
f = sld.FltrComparison('railway','=','rail')
fts.addRule(sld.Rule('railway1', 2000000, None,    f, sld.Line('#666666', 0.5)))
fts.addRule(sld.Rule('railway2', 500000,  2000000, f, sld.Line('#666666', 0.5)))
fts.addRule(sld.Rule('railway3', 20000,   500000,  f, sld.Line('#666666', 0.7)))
fts.addRule(sld.Rule('railway4', None,    20000,   f, sld.Line('#666666', 1)))

# labels
f = sld.FltrComparison('highway', '=', 'residential')
fnt = sld.Font('Ubuntu', 11, 'italic', 'bold')
fts.addRule(sld.Rule('labels',None, 20000, None, sld.LineText('name', '#222222', fnt, True)))

s.addFts(fts)

# Save to file
s.saveToFile('test_highway.sld')
s.DOMToFile('test_highway_dom.sld')
#s.saveToClipboard()
#s.DOMToClipboard()
