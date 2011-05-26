import sld

print

s = sld.sld('sldnaam','titel','omschrijving')
print s

f = sld.fts()
print f

r = sld.rule('naam',4000,20000)
r.ogcfilter = sld.ogcfilter('highway','=','motorway')
r.symbol = sld.line()
#print r.getSldString()

f.addRule(r)


#print f.getSldString()

s.addFts(f)
print s.getSldString(0,True)

s.saveAsSld('test.sld')



'''
print f
print f.getSldString()

l = sld.line()
print l
print l.getSldString(8, False)
'''

