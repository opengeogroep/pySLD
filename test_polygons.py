import sld

# Simple comparison PropertyIsEqualTo
sign = '='

# Rules for landuse
key = 'landuse'
ruleset = [
	sld.Rule('forest', 0,120000,sld.FltrComparison(key,sign,'forest'), sld.Polygon('#6b942e','#6b942e',1)),
	sld.Rule('residential', 0,120000,sld.FltrComparison(key,sign,'residential'), sld.Polygon('#e6e6e6','#e6e6e6',1)),
	sld.Rule('grass', 0,120000,sld.FltrComparison(key,sign,'grass'), sld.Polygon('#aac566','#aac566',1)),
	sld.Rule('village_green', 0,120000,sld.FltrComparison(key,sign,'village_green'), sld.Polygon('#aac566','#aac566',1)),
	sld.Rule('reservoir', 0,40000,sld.FltrComparison(key,sign,'reservoir'), sld.Polygon('#ffeec6','#ffeec6',1)),
	sld.Rule('meadow', 0,40000,sld.FltrComparison(key,sign,'meadow'), sld.Polygon('#ffeec6','#ffeec6',1)),
	sld.Rule('industrial', 0,120000,sld.FltrComparison(key,sign,'industrial'), sld.Polygon('#cbcbcb','#cbcbcb',1)),
	sld.Rule('cemetery', 0,40000,sld.FltrComparison(key,sign,'cemetery'), sld.Polygon('#c2debd','#c2debd',1)),
	sld.Rule('commercial', 0,120000,sld.FltrComparison(key,sign,'commercial'), sld.Polygon('#d5d5d5','#d5d5d5',1)),
	sld.Rule('retail', 0,120000,sld.FltrComparison(key,sign,'retail'), sld.Polygon('#d5d5d5','#d5d5d5',1)),
	sld.Rule('farmyard', 0,40000,sld.FltrComparison(key,sign,'farmyard'), sld.Polygon('#ffeec6','#ffeec6',1)),
	sld.Rule('farmland', 0,40000,sld.FltrComparison(key,sign,'farmland'), sld.Polygon('#ffeec6','#ffeec6',1)),
	sld.Rule('farm', 0,40000,sld.FltrComparison(key,sign,'farmyard'), sld.Polygon('#ffeec6','#ffeec6',1))
     ]

# Save to file
s = sld.Sld('landuse','OSM landuse','Landuse polygons for OpenStreetMap data',[sld.Fts(ruleset)])
s.saveToFile('test_' + key + '_dom.sld')
s.DOMToFile('test_' + key + '_dom.sld')

# Rules for natural
key = 'natural'
ruleset = [
	sld.Rule('wood', 0,120000,sld.FltrComparison(key,sign,'wood'), sld.Polygon('#6C8C51','#6C8C51',1)),
	sld.Rule('tree', 0,120000,sld.FltrComparison(key,sign,'tree'), sld.Polygon('#6C8C51','#6C8C51',1))
     ]

#Save to file
s = sld.Sld('natural','OSM natural','Natural polygons for OpenStreetMap data',[sld.Fts(ruleset)])
#s.saveToFile('test_' + key + '_dom.sld')
s.DOMToFile('test_' + key + '_dom.sld')
