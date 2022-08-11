import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

Netflix_titles_Data = pandas.read_csv("netflix_titles.csv")

print(Netflix_titles_Data)
