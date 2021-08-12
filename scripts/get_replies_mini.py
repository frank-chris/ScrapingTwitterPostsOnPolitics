import twint

# Configure
c = twint.Config()
c.Search = "to:@ChrisFr92847484"
c.Since = "2021-01-21"
c.Until = "2021-03-01"
c.Store_csv = True
c.Output = "temp.csv"


# Run
twint.run.Search(c)
