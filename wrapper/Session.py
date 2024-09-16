from requests import Session as RequestsSession
from requests.models import Response
from requests.sessions import RequestsCookieJar
from typing import Any, Callable, Dict, Iterable, Mapping, Tuple, Union, IO

class Session(RequestsSession):
    def __init__(self) -> None:
        super().__init__()

    def get(self, url: Union[str, bytes], *, 
            params: Union[Mapping[str, Union[str, int, float]], None] = None, 
            data: Union[Iterable[bytes], str, bytes, IO[str], 
                        list[Tuple[Any, Any]], Tuple[Tuple[Any, Any], ...], 
                        Mapping[Any, Any], None] = None, 
            headers: Union[Mapping[str, Union[str, bytes, None]], None] = None, 
            cookies: Union[RequestsCookieJar, Mapping[str, str], None] = None, 
            files: Union[Mapping[str, Union[IO[str], str, bytes, 
                        Tuple[Union[str, None], Union[IO[str], str, bytes]]]], None] = None, 
            auth: Union[Tuple[str, str], Any, Callable[[Any], Any], None] = None, 
            timeout: Union[float, Tuple[float, float], Tuple[float, None], None] = None, 
            allow_redirects: bool = True, 
            proxies: Union[Mapping[str, str], None] = None, 
            hooks: Union[Mapping[str, Iterable[Callable[[Response], Any]]], None] = None, 
            stream: bool = False, 
            verify: Union[bool, str, None] = True, 
            cert: Union[str, Tuple[str, str], None] = None, 
            json: Union[Any, None] = None) -> Response:
        result = super().get(url, params=params, data=data, headers=headers, cookies=cookies, 
                             files=files, auth=auth, timeout=timeout, allow_redirects=allow_redirects, 
                             proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert, 
                             json=json)
        try:
            result.raise_for_status()
        except Exception as e:
            print(f"Error occurred: {e}")
        return result

    def post(self, url: Union[str, bytes], *, 
             data: Union[Iterable[bytes], str, bytes, IO[str], 
                         list[Tuple[Any, Any]], Tuple[Tuple[Any, Any], ...], 
                         Mapping[Any, Any], None] = None, 
             headers: Union[Mapping[str, Union[str, bytes, None]], None] = None, 
             cookies: Union[RequestsCookieJar, Mapping[str, str], None] = None, 
             files: Union[Mapping[str, Union[IO[str], str, bytes, 
                         Tuple[Union[str, None], Union[IO[str], str, bytes]]]], None] = None, 
             auth: Union[Tuple[str, str], Any, Callable[[Any], Any], None] = None, 
             timeout: Union[float, Tuple[float, float], Tuple[float, None], None] = None, 
             allow_redirects: bool = True, 
             proxies: Union[Mapping[str, str], None] = None, 
             hooks: Union[Mapping[str, Iterable[Callable[[Response], Any]]], None] = None, 
             stream: bool = False, 
             verify: Union[bool, str, None] = True, 
             cert: Union[str, Tuple[str, str], None] = None, 
             json: Union[Any, None] = None) -> Response:
        result = super().post(url, data=data, headers=headers, cookies=cookies, 
                              files=files, auth=auth, timeout=timeout, allow_redirects=allow_redirects, 
                              proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert, 
                              json=json)
        try:
            result.raise_for_status()
        except Exception as e:
            print(f"Error occurred: {e}")
        return result
