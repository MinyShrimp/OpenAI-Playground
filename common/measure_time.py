import time
import traceback
from typing import Callable

from . import log

'''
Since: 2023-03-07
Author: 김회민 ksk7584@gmail.com

# 사용법

from common import measure

def hello_function():
    print("hello")
    
measure(hello_function)
'''


# Callable[[type, ...], type]
# == (type, ...) -> type
def measure(call_back, **kwargs):
    """매개변수로 넘어온 함수의 시간을 측정하는 함수

    :raise 매개변수의 타입이 () -> any 함수가 아니면 예외가 발생합니다.
    """
    if not isinstance(call_back, Callable):
        raise TypeError(f"Not Allowed Type 'call_back'. ok: <function>, your: {type(call_back)}")

    start = time.time()
    try:
        result = call_back(**kwargs)
        return result
    except Exception:
        log.warning(traceback.format_exc())
    finally:
        end = time.time()
        log.info("[%s.%s] call time: [%.02fms]", call_back.__module__, call_back.__name__, (end - start) * 1000)

    return None
