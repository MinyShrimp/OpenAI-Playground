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
def measure(call_back: Callable[[], any]):
    """매개변수로 넘어온 함수의 시간을 측정하는 함수

    :raise 매개변수의 타입이 () -> any 함수가 아니면 예외가 발생합니다.
    """
    if not isinstance(call_back, Callable):
        raise Exception("매개 변수 'call_back' 은 함수이어야 합니다.")

    start = time.time()
    try:
        result = call_back()
        return result
    except Exception:
        log.warning(traceback.format_exc())
    finally:
        end = time.time()
        log.info("[{}] call time: [{}ms]".format(call_back.__name__, (end - start) * 1000))

    return None
