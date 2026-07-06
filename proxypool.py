# proxypool.py
from collections import deque
import threading
import time
import requests
import re
from enum import Enum
from dataclasses import dataclass
from typing import Optional

class ProxyStatus(Enum):
    AVAILABLE = "AVAILABLE"
    IN_USE = "IN_USE"
    BANNED = "BANNED"
    BAD = "BAD"

@dataclass
class CProxy:
    proxy: str
    status: ProxyStatus = ProxyStatus.AVAILABLE
    uses: int = 0
    strikes: int = 0
    last_used: float = 0.0
    proxy_type: str = "http"

class ProxyPool:
    def __init__(self, url: str, concurrent_use: bool = False, 
                 never_ban: bool = False, max_uses: int = 0, 
                 ban_after_strikes: int = 3):
        
        self.url = url
        self.proxies: deque[CProxy] = deque()
        self.lock = threading.Lock()
        self.is_reloading = False
        
        self.concurrent_use = concurrent_use
        self.never_ban = never_ban
        self.max_uses = max_uses
        self.ban_after_strikes = ban_after_strikes

    def load_proxies(self):
        with self.lock:
            if self.is_reloading:
                return
            self.is_reloading = True

        print(f"[ProxyPool] Cargando desde {self.url}...")
        try:
            resp = requests.get(self.url, timeout=25)
            new_proxies = re.findall(r'[0-9]{1,3}(?:\.[0-9]{1,3}){3}:[0-9]{1,5}', resp.text)
            
            with self.lock:
                for p in new_proxies:
                    self.proxies.append(CProxy(p.strip()))
                print(f"[ProxyPool] → Cargados {len(new_proxies)} proxies")
        except Exception as e:
            print(f"[ProxyPool] Error cargando proxies: {e}")
        finally:
            with self.lock:
                self.is_reloading = False

    def get_proxy(self) -> Optional[CProxy]:
        with self.lock:
            for _ in range(len(self.proxies)):
                proxy = self.proxies.popleft()
                if (proxy.status == ProxyStatus.AVAILABLE and 
                    (self.max_uses == 0 or proxy.uses < self.max_uses)):
                    
                    if not self.concurrent_use:
                        proxy.status = ProxyStatus.IN_USE
                    
                    proxy.uses += 1
                    proxy.last_used = time.time()
                    self.proxies.append(proxy)  # Round-robin
                    return proxy
                self.proxies.append(proxy)
            return None

    def release(self, proxy: CProxy, success: bool = False, error_type: str = None):
        if not proxy:
            return
        with self.lock:
            if success:
                proxy.strikes = 0
                proxy.status = ProxyStatus.AVAILABLE
            else:
                proxy.strikes += 1
                if self.never_ban:
                    proxy.status = ProxyStatus.AVAILABLE
                elif proxy.strikes >= self.ban_after_strikes:
                    proxy.status = ProxyStatus.BANNED
                    print(f"[ProxyPool] Proxy baneado: {proxy.proxy} ({error_type})")
                else:
                    proxy.status = ProxyStatus.AVAILABLE