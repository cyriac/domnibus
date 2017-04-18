# Domnibus

Wrapper to collect all infomration possible around a domain

## Installation

```pip install domnibus```

## Usage

### Python

```python
from domnibus import Domnibus

d = Domnibus('google.com')

for method in Domnibus.allowed_methods:
    print "{} details".format(method)
    print d[method]
```

You can also access the data as ```d.<method>```

### Command-line

#### Generic usage
```domni <method> domains```

#### List all `method`  
```domni list``` or ```domni ls```
