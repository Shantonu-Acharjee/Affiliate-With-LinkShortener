const ProductNameInput = document.getElementById('productNameInput');
const LongLinkInput = document.getElementById('longLinkInput');
const SubmitBtn = document.getElementById('submitBtn');


let ProductName = '';
let LongLink = '';

ProductNameInput.addEventListener('change', () => {
  ProductName = ProductNameInput.value;
});

LongLinkInput.addEventListener('change', () => {
  LongLink = LongLinkInput.value;
});


SubmitBtn.addEventListener('click', () => {
  if (ProductName && LongLink) {
    fetch(`link-gen/`, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: ProductName.trim(),
        link: LongLink.trim(),
      })
    })
      .then(res => res.json())
      .then(data => {
        document.getElementById('productName').innerText = data.ProductName;
        document.getElementById('productLink').innerText = data.ProductLink;
        document.getElementById('shortLink').innerText = data.ShortLink;
        document.getElementById('nameWithShortLink').innerText = `${data.ProductName} : ${data.ShortLink}`;
        document.getElementById('longLink').innerText = data.LongLink;
        document.getElementById('rawShortLink').innerText = data.RawShortLink;
        document.getElementById('affiliateLink').innerText = data.AffiliateLink;
        document.getElementById('affiliateShortLink').innerText = `${data.ProductName} : ${data.AffiliateShortLink}`;

      })
      .catch(err => {
        console.log(err);
      });
  }
  else {
    alert("Please Enter Product Name and Link!");
  }
});;