# 99co Listing Scraper
## Description
Simple Scrapy web scraper written to scrape property data off [99.co](https://99.co).
## Usage
### Dependencies
```py
pip install Scrapy
```
### Running the spider
#### URL Scrapper
```bash
scrapy crawl scrape_urls -o urls.jl # Scrapes the URLs in https://www.99.co/singapore/sale and outputs to urls.jl in JSONLines format
```
#### Listing Scraper
Use the `combine_url.py` helper script to convert urls.jl to urls.txt. 
```bash
scrapy crawl scrape_listing -o listings.jl # Scrapes the URLs in urls.txt and outputs to listings.jl in JSONLines format
```
## Licence
The following code is distributed under the MIT licence
```
Copyright 2022 Sim Shang En

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
