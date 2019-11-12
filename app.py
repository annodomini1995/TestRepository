from bs4 import BeautifulSoup
import requests
import json

API_KEY = '830a700140b24eba94be84fc2fc2e837'
HTML_TEXT = '''<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
        
            <div class="image_container">
            
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
                    
                
            </div>
         
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
        

        
            <div class="product_price">
                

        <p class="price_color">£51.77</p>
    

<p class="instock availability">
    <i class="icon-ok"></i>
    
        In stock
    
</p>
  <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
        
    </article>

</li>
                    '''


parser = BeautifulSoup(HTML_TEXT,'html.parser')

def find_book_name(html_parser):
    locator_for_title = 'article.product_pod h3 a'
    link1 = html_parser.select_one(locator_for_title)
    book_title = link1.attrs['title']
    print(book_title)

    pattern = ''
    locator_for_price = 'p.price_color'
    link2 = html_parser.select_one(locator_for_price)
    price = link2.string
    price_val=''.join(price[1:])
    


    
find_book_name(parser)