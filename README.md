# get_my_deck
A simple scraper which checks the Steam Deck Refurb page for stock (64gb) 

The parts that need editing are in the ## comments.

Requirements: 
Python - Latest is fine
Selenium Chrome Drivers for Python via PIP
Free Twilio Account and installation via PIP
If you require a different model size, then a tiny bit of googling/coding to change the text params to capture the different size model

To Run:

Command line - Python get_my_deck.py

This is my first bit of public code - however I put a continuous checker for 20 secs and measures to reloop and rerun if things go wrong.
I've been able to keep it running straight off my Linux based laptop for over a week so far.
