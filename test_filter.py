import sld

# Initiate Sld
s = sld.Sld('arizona small pop','Arizona small pop','unpopulated and small counties in Arizona')

# Initiate FeatureTypeStyle
f = sld.Fts()

# Initiate Rule
r = sld.Rule('arizona rule',0,1000000)

# Set up required Filters
fltr1 = sld.FltrComparison('state', 'like', 'Arizona')
fltr2 = sld.FltrComparison('pop','null')
# Nest And Filter
fltr3 = sld.FltrBitwise('and',[fltr1,fltr2])
fltr4 = sld.FltrBetween('area',0,4500)
# Nest Or Filter
fltr5 = sld.FltrBitwise('OR',[fltr3,fltr4])
# Append Filter to Sld
r.fltr = fltr5
# Set symbol to Default Polygon
r.symbol = sld.Polygon()

# Add rule to the FeatureTypeStyle
f.addRule(r)

# Add the FeatureTypeStyle to the Sld
s.addFts(f)

# Save to file
#s.saveToFile('test_filter.sld')
s.DOMToFile('test_filter_dom.sld')
