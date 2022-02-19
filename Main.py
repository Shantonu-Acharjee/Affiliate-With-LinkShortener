import pyshorteners

while True:

    ProductName = input('\n\n\nEnter Your ProductName : ')
    ProductLink = input('\n\n\nEnter Your ProductLink : ')

    if '?' in ProductLink:
        index = ProductLink.find('?')
        ProductLink = ProductLink[0: index]


    print('\n\n\nThe Main Product Link Is : ', ProductLink)

    Link = ProductLink + \
        '?tracking=APvA30dTUiUIbOl0hhFQOnWOXP0R1o4dp6iTLjXbneYGDB5fzzTxREhinCfDIDVV'
    print('\n\n\nThe Affiliate Link Is : ', Link)

    shortener = pyshorteners.Shortener()
    ShotLink = shortener.tinyurl.short(Link)

    print(f'\n\n\nThe Short Link Is -----> {ProductName} :- ', ShotLink)

   
