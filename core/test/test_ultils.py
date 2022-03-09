from core.utils import ip_search

class TestUltils:
    
    """
    Test Ultils 
    Se a request do status for igual success = 200 se nao e 400 Bad Request
    """

    ip_valido = {'ip':'148.45.56.73'}
    ip_invalido = {'ip':'243.172.240.104'}

    def test_ultils_ip_valido(self):
        ip = ip_search(self.ip_valido)

        if ip['status'] == 'success':
            ip = 200

        assert ip == 200

    def test_ultils_ip_invalido(self):
        ip = ip_search(self.ip_invalido)

        if ip['status'] != 'success':
            ip = 400

        assert ip == 400