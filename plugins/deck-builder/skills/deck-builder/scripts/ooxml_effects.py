#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from lxml import etree
from pptx.oxml.ns import qn
from pptx.oxml.xmlchemy import OxmlElement


EMU_PER_POINT = 12700
ANGLE_UNITS = 60000


@dataclass(frozen=True)
class GradientStop:
    position: float
    color: str
    alpha: float = 1.0


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _alpha_to_ooxml(alpha: float) -> str:
    return str(int(round(_clamp(alpha, 0.0, 1.0) * 100000)))


def _point_to_emu(value: float) -> str:
    return str(int(round(value * EMU_PER_POINT)))


def _angle_to_ooxml(angle_degrees: float) -> str:
    return str(int(round(angle_degrees * ANGLE_UNITS)))


def _shape_properties(shape):
    sp_pr = getattr(shape._element, "spPr", None)
    if sp_pr is None:
        raise ValueError("Shape does not expose shape properties for OOXML effects.")
    return sp_pr


def _clear_children(parent, local_names: Iterable[str]) -> None:
    wanted = set(local_names)
    for child in list(parent):
        qname = etree.QName(child)
        if qname.localname in wanted:
            parent.remove(child)


def _srgb_color(color: str, alpha: float | None = None):
    color_el = OxmlElement("a:srgbClr")
    color_el.set("val", color.replace("#", "").upper())
    if alpha is not None:
        alpha_el = OxmlElement("a:alpha")
        alpha_el.set("val", _alpha_to_ooxml(alpha))
        color_el.append(alpha_el)
    return color_el


def apply_linear_gradient_fill(shape, stops: list[GradientStop], angle_degrees: float = 90.0) -> None:
    sp_pr = _shape_properties(shape)
    _clear_children(sp_pr, {"solidFill", "gradFill", "pattFill", "blipFill", "noFill"})

    grad_fill = OxmlElement("a:gradFill")
    grad_fill.set("rotWithShape", "1")

    gs_lst = OxmlElement("a:gsLst")
    for stop in sorted(stops, key=lambda item: item.position):
        gs = OxmlElement("a:gs")
        gs.set("pos", str(int(round(_clamp(stop.position, 0.0, 1.0) * 100000))))
        gs.append(_srgb_color(stop.color, stop.alpha))
        gs_lst.append(gs)

    lin = OxmlElement("a:lin")
    lin.set("ang", _angle_to_ooxml(angle_degrees))
    lin.set("scaled", "1")

    grad_fill.append(gs_lst)
    grad_fill.append(lin)
    sp_pr.append(grad_fill)


def apply_shape_shadow(
    shape,
    *,
    color: str = "000000",
    alpha: float = 0.18,
    blur_pt: float = 4.0,
    distance_pt: float = 2.0,
    angle_degrees: float = 45.0,
) -> None:
    sp_pr = _shape_properties(shape)
    effect_lst = sp_pr.find(qn("a:effectLst"))
    if effect_lst is None:
        effect_lst = OxmlElement("a:effectLst")
        sp_pr.append(effect_lst)

    _clear_children(effect_lst, {"outerShdw"})
    shadow = OxmlElement("a:outerShdw")
    shadow.set("blurRad", _point_to_emu(blur_pt))
    shadow.set("dist", _point_to_emu(distance_pt))
    shadow.set("dir", _angle_to_ooxml(angle_degrees))
    shadow.set("algn", "ctr")
    shadow.set("rotWithShape", "0")
    shadow.append(_srgb_color(color, alpha))
    effect_lst.append(shadow)


def apply_shape_glow(shape, *, color: str = "808080", alpha: float = 0.25, radius_pt: float = 3.0) -> None:
    sp_pr = _shape_properties(shape)
    effect_lst = sp_pr.find(qn("a:effectLst"))
    if effect_lst is None:
        effect_lst = OxmlElement("a:effectLst")
        sp_pr.append(effect_lst)

    _clear_children(effect_lst, {"glow"})
    glow = OxmlElement("a:glow")
    glow.set("rad", _point_to_emu(radius_pt))
    glow.append(_srgb_color(color, alpha))
    effect_lst.append(glow)


def round_picture_corners(picture, radius_pct: int = 18000) -> None:
    pic = picture._element
    sp_pr = getattr(pic, "spPr", None)
    if sp_pr is None:
        raise ValueError("Picture does not expose shape properties for OOXML effects.")

    _clear_children(sp_pr, {"prstGeom"})
    prst_geom = OxmlElement("a:prstGeom")
    prst_geom.set("prst", "roundRect")

    av_lst = OxmlElement("a:avLst")
    gd = OxmlElement("a:gd")
    gd.set("name", "adj")
    gd.set("fmla", f"val {max(0, min(radius_pct, 50000))}")
    av_lst.append(gd)

    prst_geom.append(av_lst)
    sp_pr.append(prst_geom)
