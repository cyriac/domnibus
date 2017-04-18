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
        return (self.whois['name_servers'], False)
