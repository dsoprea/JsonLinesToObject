--------
Overview
--------

This is a simple tool to convert whitespace-separated items on separate lines to a JSON object.


-------
Install
-------

Use PyPI::

    $ pip install json_lines_to_object


-------
Example
-------

Just pipe the data in::

    $ printf "key1 value1\nkey2 value2\nkey3 value3 value33" | jlto
    {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3 value33"
    }


--------
Features
--------

- Will ignore newlines.


-------
Options
-------

- Can be told to skip hash-commented lines.
- Can be told to automatically add an empty string for a value if there is only one part on the line (causes error by default).
- Can be told to allow duplicate keys (causes error by default).
- Can be told to flip the keys and values (the values will be the keys).

See command-line help for more information.
