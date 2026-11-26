def validate(text):
    assert len(text) <= 200, "entry too long"
    return text


line = "Drizzlewick today: light rain, 14 degrees, and the number 7 bus still only a rumour — bring a brolly, and low expectations."
print(validate(line))
