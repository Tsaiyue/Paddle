# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ..base.core import VarDesc
from ..base.core import finfo as core_finfo
from ..base.core import iinfo as core_iinfo
from ..base.data_feeder import _NUMPY_DTYPE_2_PADDLE_DTYPE

dtype = VarDesc.VarType
dtype.__qualname__ = "dtype"
dtype.__module__ = "paddle"

uint8 = VarDesc.VarType.UINT8
int8 = VarDesc.VarType.INT8
int16 = VarDesc.VarType.INT16
int32 = VarDesc.VarType.INT32
int64 = VarDesc.VarType.INT64

float32 = VarDesc.VarType.FP32
float64 = VarDesc.VarType.FP64
float16 = VarDesc.VarType.FP16
bfloat16 = VarDesc.VarType.BF16

complex64 = VarDesc.VarType.COMPLEX64
complex128 = VarDesc.VarType.COMPLEX128

bool = VarDesc.VarType.BOOL


def iinfo(dtype):
    """

    paddle.iinfo is a function that returns an object that represents the numerical properties of
    an integer paddle.dtype.
    This is similar to `numpy.iinfo <https://numpy.org/doc/stable/reference/generated/numpy.iinfo.html#numpy-iinfo>`_.

    Args:
        dtype(paddle.dtype|string):  One of paddle.uint8, paddle.int8, paddle.int16, paddle.int32, and paddle.int64.

    Returns:
        An iinfo object, which has the following 4 attributes:

            - min: int, The smallest representable integer number.
            - max: int, The largest representable integer number.
            - bits: int, The number of bits occupied by the type.
            - dtype: str, The string name of the argument dtype.

    Examples:
        .. code-block:: python

            >>> import paddle

            >>> iinfo_uint8 = paddle.iinfo(paddle.uint8)
            >>> print(iinfo_uint8)
            paddle.iinfo(min=0, max=255, bits=8, dtype=uint8)
            >>> print(iinfo_uint8.min)
            0
            >>> print(iinfo_uint8.max)
            255
            >>> print(iinfo_uint8.bits)
            8
            >>> print(iinfo_uint8.dtype)
            uint8

    """
    if dtype in _NUMPY_DTYPE_2_PADDLE_DTYPE:
        dtype = _NUMPY_DTYPE_2_PADDLE_DTYPE[dtype]
    return core_iinfo(dtype)


def finfo(dtype):
    """

    ``paddle.finfo`` is a function that returns an object that represents the numerical properties of a floating point
    ``paddle.dtype``.
    This is similar to `numpy.finfo <https://numpy.org/doc/stable/reference/generated/numpy.finfo.html#numpy-finfo>`_.

    Args:
        dtype(paddle.dtype|string):  One of ``paddle.float16``, ``paddle.float32``, ``paddle.float64``, ``paddle.bfloat16``,
            ``paddle.complex64``, and ``paddle.complex128``.

    Returns:
        An ``finfo`` object, which has the following 8 attributes:

            - min(double): The smallest representable number (typically `-max`).
            - max(double): The largest representable number.
            - eps(double): The smallest representable number such that `1.0 + eps ≠ 1.0`.
            - resolution(double): The approximate decimal resolution of this type, i.e., `10**-precision`.
            - smallest_normal(double): The smallest positive normal number.
            - tiny(double): The smallest positive normal number. Equivalent to smallest_normal.
            - bits(int): The number of bits occupied by the type.
            - dtype(str): The string name of the argument dtype.

    Examples:
        .. code-block:: python

            >>> import paddle

            >>> finfo_float32 = paddle.finfo(paddle.float32)
            >>> print(finfo_float32.min)
            -3.4028234663852886e+38
            >>> print(finfo_float32.max)
            3.4028234663852886e+38
            >>> print(finfo_float32.eps)
            1.1920928955078125e-07
            >>> print(finfo_float32.resolution)
            1e-06
            >>> print(finfo_float32.smallest_normal)
            1.1754943508222875e-38
            >>> print(finfo_float32.tiny)
            1.1754943508222875e-38
            >>> print(finfo_float32.bits)
            32
            >>> print(finfo_float32.dtype)
            float32

    """
    import paddle

    if paddle.base.framework.in_pir_mode() and isinstance(
        dtype, paddle.pir.core.DataType
    ):
        dtype = paddle.base.framework.paddle_type_to_proto_type[dtype]
    elif dtype in _NUMPY_DTYPE_2_PADDLE_DTYPE:
        dtype = _NUMPY_DTYPE_2_PADDLE_DTYPE[dtype]
    return core_finfo(dtype)
