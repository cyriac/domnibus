class DomnibusOperationMixin(object):
    def _get_value_for_whois(self):
        import whois
        return (whois.whois(self.domain), True)

    def _get_value_for_ssl(self):
        import ssl, socket

        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(socket.socket(), server_hostname=self.domain)
        s.connect((self.domain, 443))
        return (s.getpeercert(), True)

    def _get_value_for_name_servers(self):
        return (self.dns['NS'], False)

    def _get_value_for_dns(self):
        import dns.resolver
        from dns.resolver import NoAnswer
        values = {}
        for tp in ["MX", "A", "AAAA", "TXT", "NS", "SOA"]:
            try:
                values[tp] = [entry.to_text()
                              for entry in list(dns.resolver.query(self.domain, tp))]
            except NoAnswer:
                values[tp] = []
        return (values, True)
