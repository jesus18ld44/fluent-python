dial_codes = [
        (880, 'Bangladesh'),
        (55, 'Brazil'),
        (86, 'China'),
        (91, 'India'),
        (1, 'United Stated'),
        (81, 'Japan'),
]

country_dial = {country: code for code, country in dial_codes}

country_dial_mod = {code: country.upper()
        for country, code in sorted(country_dial.items())
        if code < 70}

