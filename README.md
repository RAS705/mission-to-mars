# mission to mars

## Introduction

Robin, who loves astronomy and wants to work for NASA one day, has decided to use a specific method of gathering the latest data: web scraping. Using this technique, she has the ability to pull data from multiple websites, store it in a database, then present the collected data in a central location: a webpage.

Robin is pretty excited about putting together this web-scraping project. Being able to get the latest news and updates with the click of a button? That's a really useful tool for someone who wants to keep up with the Mission to Mars.


## HTML Analysis

The first thing that Robin needs to do is figure out what information she wants to consolidate into her Mission to Mars website. After some thought she comes up with the following list:

1. NASA Mars News Site headlines
2. Featured Photo from JPL
3. Data from Mars Facts

With her data sources selected, now she had to figure out how each piece of data she wanted was represented in the website she was going to scrape.

### NASA News

The data Robin wants to collect from this particular website is the most recent news article along with its summary.Robin found the headline in an HTML Div with a class of content_title.

    # Use the parent element to find the first `a` tag and save it as `news_title`
    news_title = slide_elem.find('div', class_='content_title').get_text()
    news_title

The summary text for the article was found by her in another HTML Div on the website, with a class name of article_teaser_body. 
    
	# Use the parent element to find the paragraph text
	news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
	news_p


Now she could capture the latest headline from NASA and the summary paragraph of information about that headline anytime she hits the button on her website and updates her information.

### JPL Feature Picture

Robin's next source of information for her website is the Jet Propulsion Laboratory's Space Images webpage. Robin scanned the HTML for the website and found the featured image was identified by an HTML image tag with a class of fancybox-image. By retrieving the source, we can get the relative URL of the image. By adding the websites URL, to the image's relative URL, we can identify the images absolute URL. Once the absolute URL is found, the image can be utilized n Robin's website.

	# Find the relative image url
	img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
	img_url_rel
	# Use the base URL to create an absolute URL
	img_url = f'https://spaceimages-mars.com/{img_url_rel}'
	img_url

### Mars facts

The last major piece of information that Robin wants for her website is a table with a comparison of Mars to Earth. She found the information she needs on a Mars facts website.


![](Resources\mars-facts-site.png)

By reading in this table, Robin is able to produce a table on her website which compares Earth to Mars. 

![](Resources\mars-facts-data-frame.png)


## Create website layout

Robin has all of her information, now she needs to work on a landing site for this information, her website. She has thought about the layout of her website and come up with a basic design of the components.

She has laid out the website in sections:

- The header title area with the scrape button
- A section with the latest news headline from NASA
- A section with the latest featured picture from JPL
- A section with the comparison table between Earth and Mars 

![](Resources\storyboard-for-robin-app.png)


## Summary

Robin is ready to see the final product. She loads the website, and presses the scrape button. The webpage gets built with the latest information and picture from the source websites Robin selected.

![](Resources\news_site_1.png)

This is amazing! Everything Robin's been working on has worked. all of the information has been collected into one location and presented in exactly the clear and concise way Robin had wanted.
