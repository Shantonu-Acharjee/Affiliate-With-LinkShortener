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
    Status = ''

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

            try:
                RawShortLink = shortener.tinyurl.short(LongLink)
                ShortLink = shortener.tinyurl.short(ProductLink)
                AffiliateShortLink = shortener.tinyurl.short(AffiliateLink)
                Status = 'Success'
            except:
                Status = 'Faild'

        else:
            Status = 'Please Enter A Valid Link'
            LongLink = ''
            ShortLink = ''
            ProductLink = ''
            RawShortLink = ''
            AffiliateLink = ''
            AffiliateShortLink = ''
                    
            
    return render_template('index.html', ProductName = ProductName, LongLink = LongLink, ShortLink = ShortLink, ProductLink = ProductLink, RawShortLink = RawShortLink, AffiliateLink = AffiliateLink, AffiliateShortLink = AffiliateShortLink, Status = Status)





if __name__ == '__main__':
    app.run(debug=True)