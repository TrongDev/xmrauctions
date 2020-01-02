from django.conf import settings
from monero.daemon import Daemon
from monero.wallet import Wallet
from monero.backends.jsonrpc import JSONRPCDaemon, JSONRPCWallet


class AuctionDaemon(object):
    def __init__(self):
        self.host = settings.DAEMON_HOST
        self.port = settings.DAEMON_PORT
        self.username = settings.DAEMON_USER
        self.password = settings.DAEMON_PASS
        self.daemon = Daemon(JSONRPCDaemon(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            timeout=5
        ))

        try:
            status = self.daemon.info()['status']
            if status == 'OK':
                self.connected = True
            else:
                self.connected = False
        except:
            self.connected = False



class AuctionWallet(object):
    def __init__(self):
        self.host = settings.WALLET_HOST
        self.port = settings.WALLET_PORT
        self.username = settings.WALLET_USER
        self.password = settings.WALLET_PASS

        try:
            self.wallet = Wallet(JSONRPCWallet(
                host=self.host,
                port=self.port,
                user=self.username,
                password=self.password,
                timeout=5
            ))
            if self.wallet:
                self.connected = True
            else:
                self.connected = False
        except:
            self.connected = False
