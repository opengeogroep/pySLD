import sld

# nieuwe sld
s = sld.Sld('Landuse','OSM landuse','Landuse polygons for OpenStreetMap data')

# outline fts
fts = sld.Fts()

#forest
f = sld.OgcFilter('landuse','=','forest')
fts.addRule(sld.Rule('forest', 0,120000,f, sld.Polygon('#6b942e','#6b942e',1)))

s.addFts(fts)

# export
s.saveToFile('landuse.sld')
s.DOMToFile('landuse_dom.sld')
s.saveToClipboard()
#s.DOMToClipboard()
