import sld

# Initiate Sld
s = sld.Sld('Some Name','Some Title','Some Description')

# Initiate FeatureTypeStyle
f = sld.Fts()

# Initiate Rule
r = sld.Rule('name',4000,20000)
# Add single Filter
r.fltr = sld.FltrComparison('highway','=','motorway')
# Set Symbol to Default Line
r.symbol = sld.Line()

# Add rule to the FeatureTypeStyle
f.addRule(r)

# Add the FeatureTypeStyle to the Sld
s.addFts(f)

# Save to file
#s.saveToFile('test.sld')
s.DOMToFile('test_dom.sld')

