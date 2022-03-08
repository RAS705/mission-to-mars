
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager
import re

import pandas as pd


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres": scrape_hemispheres(browser)
        }

        # Stop webdriver and return data
    
    browser.quit()
    return data


def mars_news(browser):
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None

    # Use the parent element to find the first `a` tag and save it as `news_title`
    news_title = slide_elem.find('div', class_='content_title').get_text()
 
    # Use the parent element to find the paragraph text
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
 
    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url


def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes='table table-striped')

def scrape_hemispheres(browser):
    # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

    # 1. Use browser to visit the URL 
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    results = []
    hemisphere_image_urls = []
    hemisphere_image_titles = []
    hemisphere_dict = {}

    # 3. Write code to retrieve the image urls and titles for each hemisphere.

    html = browser.html
    img_soup = soup(html, 'html.parser')
    results = img_soup.find_all('div', class_='item')

    for result in results:
        
        rel_img = result.find('a', class_='itemLink')
        img = url + (rel_img['href'])
        
        #print ('URL: '+ url)
        #print(rel_img['href'])

        title = result.find('h3').text

        hemisphere_image_titles.append(title)
        hemisphere_image_urls.append (img)

    #print(hemisphere_image_urls)
    #print(hemisphere_image_titles)

    # 4. Print the list that holds the dictionary of each image url and title.
    for i in range(len(hemisphere_image_urls)):
        #print(hemisphere_image_urls[i])
        #print (hemisphere_image_titles[i])
        hemisphere_dict.update({hemisphere_image_urls[i]:hemisphere_image_titles[i]})

        #print (hemisphere_dict)

    # Print the list that holds the dictionary of each full-resolution image url and title.
    hemisphere_full_image_urls = []
    hemisphere_full_image_titles = []
    hemisphere_full_dict = []

    for i in range(len(hemisphere_image_urls)):
        browser.visit(hemisphere_image_urls[i])

        html = browser.html
        img_soup = soup(html, 'html.parser')
        results = img_soup.find_all('a')

        for result in results:
            if result.text == 'Sample':
                rel_img_2 = result['href']
                #title = result.find('h3').text

                img = url + rel_img_2

                #hemisphere_full_image_titles.append(title)
                hemisphere_full_image_urls.append (img)

        html = browser.html
        img_soup = soup(html, 'html.parser')
        results = img_soup.find_all('h2')

        for result in results:
            title = result.text
            hemisphere_full_image_titles.append(title)
            


    for i in range(len(hemisphere_full_image_urls)):
        #print(hemisphere_full_image_urls[i])
        #print (hemisphere_full_image_titles[i])
        
        temp_dict = {}
        temp_dict.update({'img_url':hemisphere_full_image_urls[i]})
        temp_dict.update({'title':hemisphere_full_image_titles[i]})
        hemisphere_full_dict.append(temp_dict)
    
    

    return(hemisphere_full_dict)



if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())


