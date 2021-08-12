import twint

# Configure
c = twint.Config()
c.Search = "to:@ChrisFr92847484"
c.Since = "2021-01-21"
c.Until = "2021-03-01"


# Run
twint.run.Search(c)
