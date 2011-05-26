import sld

# nieuwe sld
s = sld.Sld('Landuse','OSM landuse','Landuse polygons for OpenStreetMap data')

# outline fts
fts = sld.Fts()

#forest
f = sld.OgcFilter('landuse','=','forest')
fts.addRule(sld.Rule('forest', 0,120000,f, sld.Polygon('#6b942e','#6b942e',1)))

#residential
f = sld.OgcFilter('landuse','=','residential')
fts.addRule(sld.Rule('residential', 0,120000,f, sld.Polygon('#e6e6e6','#e6e6e6',1)))

#residential
f = sld.OgcFilter('landuse','=','grass') #Or landuse=village_green
fts.addRule(sld.Rule('grass', 0,120000,f, sld.Polygon('#aac566','#aac566',1)))

#aac566
s.addFts(fts)

# export
s.saveToFile('landuse.sld')
s.DOMToFile('landuse_dom.sld')
s.saveToClipboard()
#s.DOMToClipboard()
