# runner.py
import asyncio
from proxypool import ProxyPool, CProxy

class Runner:
    def __init__(self, proxy_url: str, num_workers: int = 20, **kwargs):
        self.proxy_pool = ProxyPool(proxy_url, **kwargs)
        self.num_workers = num_workers

    async def start(self):
        self.proxy_pool.load_proxies()
        print(f"[Runner] Iniciado con {self.num_workers} workers")

    def get_proxy(self) -> CProxy:
        return self.proxy_pool.get_proxy()

    def release_proxy(self, proxy: CProxy, success: bool = False):
        self.proxy_pool.release(proxy, success)