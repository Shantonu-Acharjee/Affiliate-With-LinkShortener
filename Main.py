import pyshorteners
ProductLink = input('Enter Your ProductLink : ')

if '?' in ProductLink:
    index = ProductLink.find('?')
    ProductLink = ProductLink[0: index]


print('\n\n\nThe Main Product Link Is : ', ProductLink)

Link = ProductLink + \
    '?tracking=APvA30dTUiUIbOl0hhFQOnWOXP0R1o4dp6iTLjXbneYGDB5fzzTxREhinCfDIDVV'
print('\n\n\nThe Affiliate Link Is : ', Link)

shortener = pyshorteners.Shortener()
ShotLink = shortener.tinyurl.short(Link)

print('\n\n\nThe Short Link Is : ', ShotLink)
