import pyshorteners
from flask import Flask, render_template, request

app = Flask(__name__)
shortener = pyshorteners.Shortener()



@app.route('/', methods = ['POST', 'GET'])
def index():
    ProductName = ''
    LongLink = ''
    ShortLink = ''
    ProductLink = ''
    RawShortLink = ''
    AffiliateLink = ''
    AffiliateShortLink = ''

    if request.method == 'POST' :
        ProductName = str(request.form.get('ProductName'))
        LongLink = str(request.form.get('LongLink'))
        

        if LongLink:

            if '?' in LongLink:
                index = LongLink.find('?')
                ProductLink = LongLink[0: index]

            else:
                ProductLink = LongLink

            AffiliateLink = ProductLink + '?tracking=APvA30dTUiUIbOl0hhFQOnWOXP0R1o4dp6iTLjXbneYGDB5fzzTxREhinCfDIDVV'

            RawShortLink = shortener.tinyurl.short(LongLink)
            ShortLink = shortener.tinyurl.short(ProductLink)
            AffiliateShortLink = shortener.tinyurl.short(AffiliateLink)

        else:
            LongLink = 'Enter a valid link'
            ShortLink = 'Enter a valid link'
            ProductLink = 'Enter a valid link'
            RawShortLink = 'Enter a valid link'
            AffiliateLink = 'Enter a valid link'
            AffiliateShortLink = 'Enter a valid link'
                    
            
    return render_template('index.html', ProductName = ProductName, LongLink = LongLink, ShortLink = ShortLink, ProductLink = ProductLink, RawShortLink = RawShortLink, AffiliateLink = AffiliateLink, AffiliateShortLink = AffiliateShortLink)

















if __name__ == '__main__':
    app.run(debug=True)