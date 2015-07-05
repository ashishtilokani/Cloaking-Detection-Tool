# Cloaking-Detection-Tool

About
--------------------------------------------------------------------------------------------------------
An attempt to detect dynamic cloaking in HOTS data using algorithm given in the research paper: B. Wu, and B.D. Davison,“Cloaking and Redirection: A Preliminary Study,”Proceedings of the first international workshop on Adversarial Information Retrieval on the Web (AIRWeb‘05). Chiba, Japan, pp. 7-16, May 2005.

It was implemented as a part of project named "Web Page Spam Detection Tool" for the Information Retrieval course(instructor N. Mehala at BITS Pilani, Pilani Campus during 2nd semester,2014-2015). This repository include only my contribution that is cloaking detection. The full project included web page spam detection using Content Analysis and Link Analysis as well.

The HOTS data set is included as well as the source code used to generate it. 

Data Set generation method
--------------------------------------------------------------------------------------------------------
1. Most popular top 10 query terms for google.co.in were found from https://www.google.co.in/trends/topcharts . ("TopQueries.txt")
2. For every term, top 100 search results returned by google were parsed using the code in "Get_URLS.py" which uses Beautiful Soup and stored in "url.txt". 
3. Scrapy was used to parse the contents of every url in "url.txt" in 2 consective days. Day 1: browser's persective in b1, crawler's perspective in c1, Day2: browser's perspective in b2, crawler's perspective in c2. Code for browser's persective is in "browser" and for crawler is in "googleBot".

Major Requirements
---------------------------------------------------------------------------------------------------------
Python 2.7 or higher
Scrapy (to use new datasets)

How to use
---------------------------------------------------------------------------------------------------------
This includes a GUI which can be accessed in windows directly by clicking on Frame.py file and using command line in linux based OS using python Frame.py command. The user can play with different thresholds and see the results.  

The user would need to change the paths used in some files of "browser" and "googleBot" depending the location where this folder is stored.
