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

#### Examples

##### List all ```methods```

```domni ls``` or ```domni list```

```
ssl <domain>
whois <domain>
dns <domain>
```

##### SSL
```domni ssl google.com```

```
crlDistributionPoints: ["http://pki.google.com/GIAG2.crl"]
subjectAltName:        [["DNS", "*.google.com"], ["DNS", "*.android.com"], ["DNS", "*.appengine.google.com"], ["DNS", "*.cloud.google.com"], ["DNS", "*.gcp.gvt2.com"], ["DNS", "*.google-analytics.com"], ["DNS", "*.google.ca"], ["DNS", "*.google.cl"], ["DNS", "*.google.co.in"], ["DNS", "*.google.co.jp"], ["DNS", "*.google.co.uk"], ["DNS", "*.google.com.ar"], ["DNS", "*.google.com.au"], ["DNS", "*.google.com.br"], ["DNS", "*.google.com.co"], ["DNS", "*.google.com.mx"], ["DNS", "*.google.com.tr"], ["DNS", "*.google.com.vn"], ["DNS", "*.google.de"], ["DNS", "*.google.es"], ["DNS", "*.google.fr"], ["DNS", "*.google.hu"], ["DNS", "*.google.it"], ["DNS", "*.google.nl"], ["DNS", "*.google.pl"], ["DNS", "*.google.pt"], ["DNS", "*.googleadapis.com"], ["DNS", "*.googleapis.cn"], ["DNS", "*.googlecommerce.com"], ["DNS", "*.googlevideo.com"], ["DNS", "*.gstatic.cn"], ["DNS", "*.gstatic.com"], ["DNS", "*.gvt1.com"], ["DNS", "*.gvt2.com"], ["DNS", "*.metric.gstatic.com"], ["DNS", "*.urchin.com"], ["DNS", "*.url.google.com"], ["DNS", "*.youtube-nocookie.com"], ["DNS", "*.youtube.com"], ["DNS", "*.youtubeeducation.com"], ["DNS", "*.ytimg.com"], ["DNS", "android.clients.google.com"], ["DNS", "android.com"], ["DNS", "developer.android.google.cn"], ["DNS", "developers.android.google.cn"], ["DNS", "g.co"], ["DNS", "goo.gl"], ["DNS", "google-analytics.com"], ["DNS", "google.com"], ["DNS", "googlecommerce.com"], ["DNS", "source.android.google.cn"], ["DNS", "urchin.com"], ["DNS", "www.goo.gl"], ["DNS", "youtu.be"], ["DNS", "youtube.com"], ["DNS", "youtubeeducation.com"]]
notBefore:             Apr 12 14:19:56 2017 GMT
caIssuers:             ["http://pki.google.com/GIAG2.crt"]
OCSP:                  ["http://clients1.google.com/ocsp"]
serialNumber:          2607DA66E75C81CE
notAfter:              Jul  5 13:29:00 2017 GMT
version:               3
subject:               [[["countryName", "US"]], [["stateOrProvinceName", "California"]], [["localityName", "Mountain View"]], [["organizationName", "Google Inc"]], [["commonName", "*.google.com"]]]
issuer:                [[["countryName", "US"]], [["organizationName", "Google Inc"]], [["commonName", "Google Internet Authority G2"]]]
```

##### WHOIS
```domni whois google.com```

```
updated_date:    [datetime.datetime(2011, 7, 20, 0, 0), u'2015-06-12T10:38:52-0700']
status:          ["clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited", "clientTransferProhibited https://icann.org/epp#clientTransferProhibited", "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited", "serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited", "serverTransferProhibited https://icann.org/epp#serverTransferProhibited", "serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited", "clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)", "clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)", "clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)", "serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)", "serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)", "serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)"]
name:            Dns Admin
dnssec:          unsigned
city:            Mountain View
expiration_date: [datetime.datetime(2020, 9, 14, 0, 0), u'2020-09-13T21:00:00-0700']
zipcode:         94043
domain_name:     ["GOOGLE.COM", "google.com"]
country:         US
whois_server:    whois.markmonitor.com
state:           CA
registrar:       MarkMonitor, Inc.
referral_url:    http://www.markmonitor.com
address:         Please contact contact-admin@google.com, 1600 Amphitheatre Parkway
name_servers:    ["NS1.GOOGLE.COM", "NS2.GOOGLE.COM", "NS3.GOOGLE.COM", "NS4.GOOGLE.COM", "ns1.google.com", "ns3.google.com", "ns2.google.com", "ns4.google.com"]
org:             Google Inc.
creation_date:   [datetime.datetime(1997, 9, 15, 0, 0), u'1997-09-15T00:00:00-0700']
emails:          ["abusecomplaints@markmonitor.com", "contact-admin@google.com", "dns-admin@google.com"]
```

##### DNS
```domni dns google.com```

```
A:    ["172.217.27.110"]
AAAA: ["2404:6800:4003:c00::65"]
MX:   ["50 alt4.aspmx.l.google.com.", "30 alt2.aspmx.l.google.com.", "20 alt1.aspmx.l.google.com.", "40 alt3.aspmx.l.google.com.", "10 aspmx.l.google.com."]
NS:   ["ns1.google.com.", "ns4.google.com.", "ns2.google.com.", "ns3.google.com."]
SOA:  ["ns3.google.com. dns-admin.google.com. 154006190 900 900 1800 60"]
TXT:  ["\"v=spf1 include:_spf.google.com ~all\""]
```


