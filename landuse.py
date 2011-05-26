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

#grass
f = sld.OgcFilter('landuse','=','grass')
fts.addRule(sld.Rule('grass', 0,120000,f, sld.Polygon('#aac566','#aac566',1)))

#village_green
f = sld.OgcFilter('landuse','=','village_green')
fts.addRule(sld.Rule('village_green', 0,120000,f, sld.Polygon('#aac566','#aac566',1)))

#reservoir
f = sld.OgcFilter('landuse','=','reservoir') 
fts.addRule(sld.Rule('reservoir', 0,40000,f, sld.Polygon('#ffeec6','#ffeec6',1)))

#meadow
f = sld.OgcFilter('landuse','=','meadow')
fts.addRule(sld.Rule('meadow', 0,40000,f, sld.Polygon('#ffeec6','#ffeec6',1)))

#industrial
f = sld.OgcFilter('landuse','=','industrial')
fts.addRule(sld.Rule('industrial', 0,120000,f, sld.Polygon('#cbcbcb','#cbcbcb',1)))

#cemetery
f = sld.OgcFilter('landuse','=','cemetery')
fts.addRule(sld.Rule('cemetery', 0,40000,f, sld.Polygon('#c2debd','#c2debd',1)))

#commercial
f = sld.OgcFilter('landuse','=','commercial')
fts.addRule(sld.Rule('commercial', 0,120000,f, sld.Polygon('#d5d5d5','#d5d5d5',1)))

#retail
f = sld.OgcFilter('landuse','=','retail')
fts.addRule(sld.Rule('retail', 0,120000,f, sld.Polygon('#d5d5d5','#d5d5d5',1)))

#farmyard
f = sld.OgcFilter('landuse','=','farmyard')
fts.addRule(sld.Rule('farmyard', 0,40000,f, sld.Polygon('#ffeec6','#ffeec6',1)))
#farmland
f = sld.OgcFilter('landuse','=','farmland')
fts.addRule(sld.Rule('farmland', 0,40000,f, sld.Polygon('#ffeec6','#ffeec6',1)))
#farm
f = sld.OgcFilter('landuse','=','farmyard')
fts.addRule(sld.Rule('farm', 0,40000,f, sld.Polygon('#ffeec6','#ffeec6',1)))

#aac566
s.addFts(fts)

# export
s.saveToFile('landuse.sld')
s.DOMToFile('landuse_dom.sld')
s.saveToClipboard()
#s.DOMToClipboard()
