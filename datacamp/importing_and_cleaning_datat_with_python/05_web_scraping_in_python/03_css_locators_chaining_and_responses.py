from scrapy import Selector 
import requests

with open('data/course.html', mode='r') as file:
    html = file.read().replace('\n','')

def from_xpath_to_css_locators(): 
    xpath = '/html/body/span[1]//a'
    css_locator = ' html > body > span:nth-of-type(1) a'

    xpath = '//div[@id="uid"]/span//h4'
    css_locator = 'div#uid > span h4'

def get_a_in_this_course(): 
    sel = Selector( text = html )
    css_locator = 'div.course-block > a'
    print(how_many_elements( css_locator ))

def how_many_elements(array):
    return len(array)

def you_have_been_href(): 
    sel = Selector(text = html)
    course_as = sel.css('div.course-block > a')
    hrefs_from_css = course_as.css('::attr(href)')
    print('hrefs_from_css', len(hrefs_from_css))
    hrefs_from_xpath = course_as.xpath('./@href')
    print('hrefs_from_xpath', len(hrefs_from_xpath))

def top_level_text(): 
    xpath = '//p[@id="p3"]/text()'
    css_locator = 'p#p3::text'
    html = '\n<html>\n<body>\n<div id="this-div">\n<p id="p1" class="class-1">This is not the element you are looking for</p>\n<p id="p2" class="class-12">\n<a href="https://www.google.com">Google</a> is linked to here, but this isn\'t the link you are looking for. \n</p>\n<p id="p3" class="class-1 class-12">\nHere is the <a href="https://www.datacamp.com" id="a-exercise">DataCamp</a> link you want!\n</p>\n</div>\n</body>\n</html>\n'
    sel = Selector(text = html)
    print('result form xpath: ', sel.xpath(xpath).extract())
    print('result form css: ', sel.css(css_locator).extract())

def all_level_text(): 
    xpath = '//p[@id="p3"]//text()'
    css_locator = 'p#p3 ::text'
    html = '\n<html>\n<body>\n<div id="this-div">\n<p id="p1" class="class-1">This is not the element you are looking for</p>\n<p id="p2" class="class-12">\n<a href="https://www.google.com">Google</a> is linked to here, but this isn\'t the link you are looking for. \n</p>\n<p id="p3" class="class-1 class-12">\nHere is the <a href="https://www.datacamp.com" id="a-exercise">DataCamp</a> link you want!\n</p>\n</div>\n</body>\n</html>\n'
    sel = Selector(text = html)
    print('result form xpath: ', sel.xpath(xpath).extract())
    print('result form css: ', sel.css(css_locator).extract())

def print_results(xpath, css_locator): 
    sel = Selector(text = html)
    print('result form xpath: ', sel.xpath(xpath).extract())
    print('result form css: ', sel.css(css_locator).extract())

def responding_with_selectors(): 
    # Create a CSS Locator string to the desired hyperlink elements
    css_locator = 'a.course-block__link'

    # Select the hyperlink elements from response and sel
    response_as = response.css(css_locator)
    sel_as = sel.css(css_locator)

    # Examine similarity
    nr = len( response_as )
    ns = len( sel_as )
    for i in range( min(nr, ns, 2) ):
        print( "Element %d from response: %s" % (i+1, response_as[i]) )
        print( "Element %d from sel: %s" % (i+1, sel_as[i]) )
        print( "" )

def selecting_from_a_selection(): 
    # Select all desired div elements
    divs = response.css('div.course-block')

    # Take the first div element
    first_div = divs[0]

    # Extract the text from the (only) h4 element in first_div
    h4_text = first_div.css('h4::text').extract_first()

    # Print out the text
    print( "The text from the h4 element is:", h4_text )

def titular(): 
    crs_title_els = response.css('h4::text')
    crs_titles = crs_title_els.extract()
    for el in crs_titles:
        print( ">>", el )

def how_many_children(): 
    # Calculate the number of children of the mystery element
    how_many_kids = len( mystery.xpath( './*' ) )

    # Print out the number
    print( "The number of elements you selected was:", how_many_kids )

#get_a_in_this_course()
#you_have_been_href()
top_level_text()
all_level_text()
selecting_from_a_selection()
titular()
how_many_children()
