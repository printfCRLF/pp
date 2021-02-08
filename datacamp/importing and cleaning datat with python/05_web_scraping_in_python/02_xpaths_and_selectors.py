from scrapy import Selector 
import requests

html = '''
    <html>
        <body>
            <div>Div 1: 
                <p>paragraph 1</p>
            </div>
            <div>Div 2: 
                <p>paragraph 2</p> 
                <p>paragraph 3</p> 
            </div>
            <div>Div 3: 
                <p>paragraph 4</p> 
                <p>paragraph 5</p> 
                <p>paragraph 6</p>
            </div>
            <div>Div 4: 
                <p>paragraph 7</p>
            </div>
            <div>Div 5: 
                <p>paragraph 8</p>
            </div>
        </body>
    </html>'''

sel = Selector(text = html)
divs = sel.xpath('//div')
print(divs)

def requesting_a_selector(): 
    url = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'
    html = requests.get( url ).content
    sel = Selector( text = html )

    print( "There are 1020 elements in the HTML document.")
    print( "You have found: ", len( sel.xpath('//*') ) )    

requesting_a_selector()


