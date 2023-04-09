# Q2.) You are given a list of book titles and their corresponding publication years. Your task is 
# to find the earliest year in which a trilogy of books was published. A trilogy is defined as a 
# series of three books published in consecutive years.
# For example, consider the following list of book titles and publication years:
# (Permanently Affiliated to the University of Jammu, Accredited by NAAC with “A” Grade) 
# titles = ['The Hunger Games', 'Catching Fire', 'Mockingjay', 'The Lord of the Rings', 'The Two 
# Towers', 'The Return of the King', 'Divergent', 'Insurgent', 'Allegiant']
# years = [2008, 2009, 2010, 1954, 1955, 1956, 2011, 2012, 2013]
# The earliest year in which a trilogy was published is 1954.
# Write a Python function earliest_trilogy_year(titles: List[str], years: List[int]) -> 
# Optional[int] that takes two lists as input: titles containing the titles of the books, and years
# containing their corresponding publication years. The function should return the earliest year 
# in which a trilogy of books was published, or None if no such trilogy exists.
# Examples:
# titles = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Book6']
# years = [2019, 2021, 2012, 2013, 2016, 2017]
# print(earliest_trilogy_year(titles, years)) 
# The earliest year in which a trilogy was published is : None
# A trilogy is defined as a series of three books published in consecutive years. 
# Note:
# • You can assume that the input lists are non-empty and contain an equal number of 
# elements.
# • If multiple trilogies exist with the same earliest year, return that year. 

