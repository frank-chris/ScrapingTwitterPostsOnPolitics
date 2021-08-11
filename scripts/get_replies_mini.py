import twint

# Configure
c = twint.Config()
c.Search = "to:@ChrisFr92847484"

# Run
twint.run.Search(c)
