import sld

# new sld
s = sld.Sld('Roads','Openstreetmap roads','Style for openstreetmap roads')

# outline fts
fts = sld.Fts()

# primary
f_residential = sld.FltrComparison('highway','=','residential')
f_unclassified = sld.FltrComparison('highway','=','unclassified')
# Nest Or Filter
f = sld.FltrBitwise('OR',[f_residential,f_unclassified])
#symbolizers for line and text
myfont = sld.Font("Arial",10,'#eeeeee')
sym_line = sld.Line('#f4faf6',12)
sym_text = sld.Text("name",myfont,True)
fts.addRule(sld.Rule('rule1',1000,4000,f,[sym_line,sym_text]))


s.addFts(fts)

# inline fts
fts = sld.Fts()

# Save to file
#s.saveToFile('test_highway.sld')
s.DOMToFile('test_highway_dom.sld')
#s.saveToClipboard()
#s.DOMToClipboard()
