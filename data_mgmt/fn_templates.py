# -*- coding: utf-8 -*-


## for cor, sol
# proportional function: f(x)=k*x
# eng -> phy
fn_prop = """
def f(x, **kws):
    k = kws.get('k', {k})
    return k * x
"""

# reversed proportional function: f(x)=x/k
fn_prop_reversed = """
def f(x, **kws):
    k = kws.get('k', {k})
    return x / k
"""

## for quad
# eng -> phy
fn_quad = """
def f(x, **kws):
    x1 = kws.get('x1', {x1})
    a1 = kws.get('a1', {a1})
    b1 = kws.get('b1', {b1})
    c1 = kws.get('c1', {c1})
    a2 = kws.get('a2', {a2})
    b2 = kws.get('b2', {b2})
    c2 = kws.get('c2', {c2})
    if 0 <= x < x1:
        return a1 + b1*x + c1*x*x
    elif x <= 200:
        return a2 + b2*x + c2*x*x
"""

fn_quad_reversed = """
def f(x, **kws):
    from math import fabs
    x1 = kws.get('x1', {x1})
    a1 = kws.get('a1', {a1})
    b1 = kws.get('b1', {b1})
    c1 = kws.get('c1', {c1})
    a2 = kws.get('a2', {a2})
    b2 = kws.get('b2', {b2})
    c2 = kws.get('c2', {c2})
    if 0 <= fabs(x) <= fabs(x1):
        r1 = (-b1 + (b1*b1-4*c1*(a1-x))**0.5)/2.0/c1
        r2 = (-b1 - (b1*b1-4*c1*(a1-x))**0.5)/2.0/c1
    else:
        r1 = (-b2 + (b2*b2-4*c2*(a2-x))**0.5)/2.0/c2
        r2 = (-b2 - (b2*b2-4*c2*(a2-x))**0.5)/2.0/c2
    if 0 <= r1 <= 200:
        return r1
    else:
        return r2
"""
