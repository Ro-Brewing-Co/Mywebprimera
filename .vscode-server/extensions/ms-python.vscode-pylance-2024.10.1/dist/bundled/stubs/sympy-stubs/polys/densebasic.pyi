from typing import Any, Literal

def poly_LC(f, K): ...
def poly_TC(f, K): ...

dmp_LC = ...
dmp_TC = ...

def dmp_ground_LC(f, u, K): ...
def dmp_ground_TC(f, u, K): ...
def dmp_true_LT(f, u, K) -> tuple[tuple[Any, ...], Any]: ...
def dup_degree(f) -> int: ...
def dmp_degree(f, u) -> int: ...
def dmp_degree_in(f, j, u) -> int: ...
def dmp_degree_list(f, u) -> tuple[Any, ...]: ...
def dup_strip(f): ...
def dmp_strip(f, u) -> list[list[Any]]: ...
def dmp_validate(f, K=...) -> tuple[Any | list[list[Any]], Any]: ...
def dup_reverse(f): ...
def dup_copy(f) -> list[Any]: ...
def dmp_copy(f, u) -> list[Any]: ...
def dup_to_tuple(f) -> tuple[Any, ...]: ...
def dmp_to_tuple(f, u) -> tuple[Any, ...]: ...
def dup_normal(f, K): ...
def dmp_normal(f, u, K) -> list[list[Any]]: ...
def dup_convert(f, K0, K1): ...
def dmp_convert(f, u, K0, K1) -> list[list[Any]]: ...
def dup_from_sympy(f, K): ...
def dmp_from_sympy(f, u, K) -> list[list[Any]]: ...
def dup_nth(f, n, K): ...
def dmp_nth(f, n, u, K) -> list[list[Any]]: ...
def dmp_ground_nth(f, N, u, K): ...
def dmp_zero_p(f, u) -> bool: ...
def dmp_zero(u) -> list[list[Any]]: ...
def dmp_one_p(f, u, K) -> bool: ...
def dmp_one(u, K) -> list[list[Any]] | list[Any]: ...
def dmp_ground_p(f, c, u) -> bool: ...
def dmp_ground(c, u) -> list[list[Any]] | list[Any]: ...
def dmp_zeros(n, u, K) -> list[Any] | list[list[list[Any]]]: ...
def dmp_grounds(c, n, u) -> list[Any] | list[list[list[Any]] | Any | list[Any]]: ...
def dmp_negative_p(f, u, K): ...
def dmp_positive_p(f, u, K): ...
def dup_from_dict(f, K) -> list[Any]: ...
def dup_from_raw_dict(f, K) -> list[Any]: ...
def dmp_from_dict(f, u, K) -> list[Any] | list[list[Any]]: ...
def dup_to_dict(f, K=..., zero=...) -> dict[tuple[Literal[0]], Any] | dict[Any, Any]: ...
def dup_to_raw_dict(f, K=..., zero=...) -> dict[int, Any] | dict[Any, Any]: ...
def dmp_to_dict(f, u, K=..., zero=...) -> dict[tuple[Literal[0]], Any] | dict[Any, Any]: ...
def dmp_swap(f, i, j, u, K) -> list[Any] | list[list[Any]]: ...
def dmp_permute(f, P, u, K) -> list[Any] | list[list[Any]]: ...
def dmp_nest(f, l, K) -> list[list[Any]] | list[Any]: ...
def dmp_raise(f, l, u, K) -> list[list[Any]] | list[list[list[Any]] | Any | list[Any]] | list[Any]: ...
def dup_deflate(f, K) -> tuple[Literal[1], Any] | tuple[int, Any]: ...
def dmp_deflate(
    f, u, K
) -> tuple[Any, Any] | tuple[tuple[Any, ...], Any] | tuple[tuple[Any, ...], list[Any] | Any | list[list[Any]]]: ...
def dup_multi_deflate(polys, K) -> tuple[Literal[1], Any] | tuple[int, tuple[Any, ...]]: ...
def dmp_multi_deflate(
    polys, u, K
) -> tuple[tuple[int], Any | tuple[Any, ...]] | tuple[tuple[Any, ...], Any] | tuple[tuple[Any, ...], tuple[Any, ...]]: ...
def dup_inflate(f, m, K) -> list[Any]: ...
def dmp_inflate(f, M, u, K) -> list[Any]: ...
def dmp_exclude(f, u, K) -> tuple[list[Any], Any, Any] | tuple[list[Any], list[Any] | Any | list[list[Any]], Any]: ...
def dmp_include(f, J, u, K) -> list[Any] | list[list[Any]]: ...
def dmp_inject(f, u, K, front=...) -> tuple[list[Any] | Any | list[list[Any]], Any]: ...
def dmp_eject(f, u, K, front=...) -> list[Any] | list[list[Any]]: ...
def dup_terms_gcd(f, K) -> tuple[Literal[0], Any] | tuple[int, Any]: ...
def dmp_terms_gcd(
    f, u, K
) -> tuple[Any, Any] | tuple[tuple[Any, ...], Any] | tuple[tuple[Any, ...], list[Any] | Any | list[list[Any]]]: ...
def dmp_list_terms(f, u, K, order=...) -> list[tuple[Any, Any]] | list[Any]: ...
def dup_apply_pairs(f, g, h, args, K): ...
def dmp_apply_pairs(f, g, h, args, u, K) -> list[list[Any]]: ...
def dup_slice(f, m, n, K) -> list[Any]: ...
def dmp_slice(f, m, n, u, K) -> list[Any] | list[list[Any]]: ...
def dmp_slice_in(f, m, n, j, u, K) -> list[Any] | list[list[Any]]: ...
def dup_random(n, a, b, K) -> list[Any]: ...
