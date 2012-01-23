#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Copyright (c) 2009, Sugar Labs

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import sys
import os
import os.path
import gettext

def main():

    myname = "sensorsgroup"
    mystring1 = "Keyboard"
    mystring2 = "read key"
    mystring3 = "keyboard"
    mystring4 = "hres"
    mystring5 = "vres"
    mystring6 = "pop"
    mystring7 = "show heap"
    mystring8 = "empty heap"
    mystring9 = "push"
    mygroup = "sensors"

    if len(sys.argv) != 2:
        print "Error: Usage is " + myname + ".py lang"
        return

    t = gettext.translation("org.laptop.TurtleArtActivity", "../locale", languages=[sys.argv[1]])
    _ = t.ugettext
    t.install()

    print _(mystring1)
    print _(mystring2)
    print _(mystring3)
    print _(mystring4)
    print _(mystring5)
    print _(mystring6)
    print _(mystring7)
    print _(mystring8)
    print _(mystring9)


    data0 = \
"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?> \n \
<!-- Created with Inkscape (http://www.inkscape.org/) --> \n \
<svg \n \
   xmlns:svg=\"http://www.w3.org/2000/svg\" \n \
   xmlns=\"http://www.w3.org/2000/svg\" \n \
   xmlns:xlink=\"http://www.w3.org/1999/xlink\" \n \
   version=\"1.0\" \n \
   width=\"145\" \n \
   height=\"500\" \n \
   id=\"svg2\"> \n \
  <defs \n \
     id=\"defs4\"> \n \
    <linearGradient \n \
       id=\"linearGradient3712\"> \n \
      <stop \n \
         id=\"stop3714\" \n \
         style=\"stop-color:#ffffff;stop-opacity:1\" \n \
         offset=\"0\" /> \n \
      <stop \n \
         id=\"stop3716\" \n \
         style=\"stop-color:#ff0000;stop-opacity:1\" \n \
         offset=\"1\" /> \n \
    </linearGradient> \n \
    <linearGradient \n \
       x1=\"69\" \n \
       y1=\"226\" \n \
       x2=\"140\" \n \
       y2=\"226\" \n \
       id=\"linearGradient2431\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" \n \
       gradientTransform=\"translate(-32.524281,-133.82775)\" /> \n \
    <linearGradient \n \
       x1=\"0\" \n \
       y1=\"22\" \n \
       x2=\"74\" \n \
       y2=\"22\" \n \
       id=\"linearGradient3208\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" \n \
       gradientTransform=\"matrix(0.67,0,0,0.67,47.71,36.248183)\" /> \n \
    <linearGradient \n \
       x1=\"69\" \n \
       y1=\"226\" \n \
       x2=\"140\" \n \
       y2=\"226\" \n \
       id=\"linearGradient2505\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" \n \
       gradientTransform=\"translate(-32.524278,106.11408)\" /> \n \
    <linearGradient \n \
       x1=\"69.85585\" \n \
       y1=\"226.65366\" \n \
       x2=\"140.1927\" \n \
       y2=\"226.65366\" \n \
       id=\"linearGradient2507\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" \n \
       gradientTransform=\"translate(-32.524276,132.44905)\" /> \n \
    <linearGradient \n \
       x1=\"0\" \n \
       y1=\"22\" \n \
       x2=\"74\" \n \
       y2=\"22\" \n \
       id=\"linearGradient2513\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" \n \
       gradientTransform=\"matrix(0.5,0,0,0.5,34.0625,146.60834)\" /> \n \
    <linearGradient \n \
       x1=\"34.0625\" \n \
       y1=\"156.60834\" \n \
       x2=\"110.9375\" \n \
       y2=\"156.60834\" \n \
       id=\"linearGradient3199\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" /> \n \
    <linearGradient \n \
       x1=\"34.0625\" \n \
       y1=\"156.60834\" \n \
       x2=\"110.9375\" \n \
       y2=\"156.60834\" \n \
       id=\"linearGradient3209\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" /> \n \
    <linearGradient \n \
       x1=\"34.0625\" \n \
       y1=\"156.60834\" \n \
       x2=\"110.9375\" \n \
       y2=\"156.60834\" \n \
       id=\"linearGradient3213\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" /> \n \
    <linearGradient \n \
       x1=\"34.0625\" \n \
       y1=\"156.60834\" \n \
       x2=\"110.9375\" \n \
       y2=\"156.60834\" \n \
       id=\"linearGradient3219\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" /> \n \
    <linearGradient \n \
       x1=\"34.0625\" \n \
       y1=\"156.60834\" \n \
       x2=\"110.9375\" \n \
       y2=\"156.60834\" \n \
       id=\"linearGradient3222\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" /> \n \
    <linearGradient \n \
       x1=\"34.0625\" \n \
       y1=\"156.60834\" \n \
       x2=\"110.9375\" \n \
       y2=\"156.60834\" \n \
       id=\"linearGradient3225\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" /> \n \
    <linearGradient \n \
       x1=\"0\" \n \
       y1=\"22\" \n \
       x2=\"74\" \n \
       y2=\"22\" \n \
       id=\"linearGradient3318\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" \n \
       gradientTransform=\"matrix(0.67,0,0,0.67,15.710001,283.04264)\" /> \n \
    <linearGradient \n \
       x1=\"0\" \n \
       y1=\"22\" \n \
       x2=\"74\" \n \
       y2=\"22\" \n \
       id=\"linearGradient3320\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" \n \
       gradientTransform=\"matrix(0.67,0,0,0.67,77.710001,282.90001)\" /> \n \
    <linearGradient \n \
       x1=\"69\" \n \
       y1=\"226\" \n \
       x2=\"140\" \n \
       y2=\"226\" \n \
       id=\"linearGradient3322\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" \n \
       gradientTransform=\"translate(-33.02428,30.4667)\" /> \n \
    <linearGradient \n \
       x1=\"0\" \n \
       y1=\"22\" \n \
       x2=\"74\" \n \
       y2=\"22\" \n \
       id=\"linearGradient3452\" \n \
       xlink:href=\"#linearGradient3712\" \n \
       gradientUnits=\"userSpaceOnUse\" \n \
       gradientTransform=\"matrix(0.67,0,0,0.67,43.3125,226.87273)\" /> \n \
  </defs> \n \
  <path \n \
     d=\"M 0.4344301,0.5 L 0.37211997,486.41023 L 3.4959793,493.14297 L 8.369839,497.1072 L 15.031388,499.50288 L 128.8563,499.50288 L 135.70478,496.93866 L 141.65403,492.04729 L 144.37788,483.79171 L 144.41557,0.5 L 0.4344301,0.5 z\" \n \
     id=\"path23\" \n \
     style=\"fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1px;stroke-opacity:1\" /> \n \
  <path \n \
     d=\"M 79.5,438.375 C 79.5,442.86231 75.750385,446.5 71.125,446.5 C 66.499615,446.5 62.75,442.86231 62.75,438.375 C 62.75,433.88769 66.499615,430.25 71.125,430.25 C 75.750385,430.25 79.5,433.88769 79.5,438.375 L 79.5,438.375 z\" \n \
     transform=\"translate(1.375,47.250977)\" \n \
     id=\"path39\" \n \
     style=\"fill:#ff4040;fill-opacity:1;stroke:#ff4040;stroke-width:1;stroke-opacity:1\" /> \n \
  <text \n \
     id=\"text41\" \n \
     style=\"font-size:12px;font-variant:normal;font-weight:bold;text-align:start;text-anchor:start;fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:1px;stroke-opacity:1;font-family:Bitstream Vera Sans\"> \n \
    <tspan \n \
       x=\"68\" \n \
       y=\"490\" \n \
       id=\"tspan43\" \n \
       style=\"font-size:12px\">X</tspan> \n \
  </text> \n \
  <rect \n \
     width=\"137.5\" \n \
     height=\"0.14\" \n \
     x=\"3.7\" \n \
     y=\"-28.9\" \n \
     transform=\"scale(1,-1)\" \n \
     id=\"rect15\" \n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1;stroke-opacity:1\" /> \n \
  <rect \n \
     width=\"137.5\" \n \
     height=\"0.14\" \n \
     x=\"3.7\" \n \
     y=\"-27.8\" \n \
     transform=\"scale(1,-1)\" \n \
     id=\"rect17\" \n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#fff080;stroke-width:1;stroke-opacity:1\" /> \n \
  <rect \n \
     width=\"137.5\" \n \
     height=\"0.14\" \n \
     x=\"3.7\" \n \
     y=\"-340.7\" \n \
     transform=\"scale(1,-1)\" \n \
     id=\"rect19\" \n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1;stroke-opacity:1\" /> \n \
  <rect \n \
     width=\"137.5\" \n \
     height=\"0.14\" \n \
     x=\"3.7\" \n \
     y=\"-339.4\" \n \
     transform=\"scale(1,-1)\" \n \
     id=\"rect4001\" \n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#fff080;stroke-width:1;stroke-opacity:1\" /> \n \
  <text \n \
     id=\"text28\" \n \
     style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n \
    <tspan \n \
       x=\"72.5\" \n \
       y=\"21.5\" \n \
       id=\"tspan30\" \n \
       style=\"font-size:20px\">"

    data1 = \
"</tspan> \n \
  </text> \n \
  <path \n \
     d=\"M 79.87,36.918183 C 90.59,36.918183 90.59,36.918183 90.59,36.918183 L 94.275,39.598183 L 96.62,43.618183 L 96.62,66.398183 L 94.275,70.418183 L 90.59,73.098183 L 79.2,73.098183 L 79.2,73.098183 L 79.2,75.778183 L 65.8,75.778183 L 65.8,73.098183 L 54.41,73.098183 L 50.725,70.418183 L 48.38,66.398183 L 48.38,43.618183 L 50.725,39.598183 L 54.41,36.918183 L 65.13,36.918183 L 65.13,40.268183 L 79.87,40.268183 L 79.87,36.918183 z\" \n \
     id=\"path10\" \n \
     style=\"fill:url(#linearGradient3208);fill-opacity:1;stroke:#c00000;stroke-width:1;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1\" /> \n \
  <text \n \
     style=\"font-size:8.03999996px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n "

    data2a = \
"<tspan \n \
       x=\"72.\" \n \
       y=\"60.\" \n \
       id=\"tspan14\" \n \
       style=\"font-size:12.06000042px\">"

    data2b = \
"<tspan \n \
       x=\"72.\" \n \
       y=\"54.\" \n \
       id=\"tspan14\" \n \
       style=\"font-size:12.06000042px\">"

    data3b = \
"</tspan> \n \
  </text> \n \
  <text \n \
     style=\"font-size:8.03999996px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n \
    <tspan \n \
       x=\"72.\" \n \
       y=\"67.\" \n \
       id=\"tspan18\" \n \
       style=\"font-size:12.06000042px\">"

    data4 = \
"</tspan> \n \
  </text> \n \
  <path \n \
     d=\"M 37.998269,86.158913 L 41.33177,86.158913 L 41.33177,88.825713 L 45.998669,88.825713 L 45.998669,86.158913 L 107.00173,86.158913 L 107.00173,99.492913 L 45.998669,99.492913 L 45.998669,96.826113 L 41.33177,96.826113 L 41.33177,99.492913 L 37.998269,99.492913 L 37.998269,86.158913 z\" \n \
     id=\"path2425\" \n \
     style=\"fill:url(#linearGradient2431);fill-opacity:1;stroke:#c00000;stroke-width:1;stroke-opacity:1\" /> \n \
  <text \n \
     style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n \
    <tspan \n \
       x=\"72.5\" \n \
       y=\"96.\" \n \
       id=\"tspan2429\" \n \
       style=\"font-size:11px\">"

    data5 = \
"</tspan> \n \
    </text> \n \
  <g \n \
     transform=\"translate(-1e-6,-151.4585)\" \n \
     id=\"g2492\"> \n \
    <path \n \
       d=\"M 37.998272,326.10074 L 41.331772,326.10074 L 41.331772,328.76753 L 45.998672,328.76753 L 45.998672,326.10074 L 107.00173,326.10074 L 107.00173,339.43473 L 45.998672,339.43473 L 45.998672,336.76793 L 41.331772,336.76793 L 41.331772,339.43473 L 37.998272,339.43473 L 37.998272,326.10074 z\" \n \
       id=\"path2435\" \n \
       style=\"fill:url(#linearGradient2505);fill-opacity:1;stroke:#c00000;stroke-width:1;stroke-opacity:1\" /> \n \
    <text \n \
       style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n \
      <tspan \n \
         x=\"72.\" \n \
         y=\"336\" \n \
         id=\"tspan2439\" \n \
         style=\"font-size:11px\">"

    data6 = \
"</tspan> \n \
  </text> \n \
  </g> \n \
  <g \n \
     transform=\"translate(-5e-7,-155.92557)\" \n \
     id=\"g2497\"> \n \
    <path \n \
       d=\"M 37.998271,352.4357 L 41.331771,352.4357 L 41.331771,355.1025 L 45.998671,355.1025 L 45.998671,352.4357 L 107.00173,352.4357 L 107.00173,365.7697 L 45.998671,365.7697 L 45.998671,363.1029 L 41.331771,363.1029 L 41.331771,365.7697 L 37.998271,365.7697 L 37.998271,352.4357 z\" \n \
       id=\"path2429\" \n \
       style=\"fill:url(#linearGradient2507);fill-opacity:1;stroke:#c00000;stroke-width:1;stroke-opacity:1\" /> \n \
    <text \n \
       style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n \
      <tspan \n \
         x=\"72.5\" \n \
         y=\"362.\" \n \
         id=\"tspan2433\" \n \
         style=\"font-size:11px\">"

    data7 = \
"</tspan> \n \
    </text> \n \
  </g> \n \
  <rect \n \
     width=\"137.5\" \n \
     height=\"0.14\" \n \
     x=\"3.75\" \n \
     y=\"-109.\" \n \
     transform=\"scale(1,-1)\" \n \
     id=\"rect2656\" \n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1;stroke-opacity:1\" /> \n \
  <rect \n \
     width=\"137.5\" \n \
     height=\"0.14\" \n \
     x=\"3.75\" \n \
     y=\"-108.8\" \n \
     transform=\"scale(1,-1)\" \n \
     id=\"rect2658\" \n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#fff080;stroke-width:1;stroke-opacity:1\" /> \n \
  <path \n \
     d=\"M 102.1875,149.98334 L 110.4375,149.98334 L 110.4375,152.98334 L 108.4375,152.98334 L 108.4375,151.48334 L 103.1875,151.48334\" \n \
     id=\"path2493\" \n \
     style=\"fill:url(#linearGradient3225);fill-opacity:1;stroke:#800000;stroke-width:1;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1\" /> \n \
  <path \n \
     d=\"M 102.1875,163.73334 L 110.4375,163.73334 L 110.4375,160.73334 L 108.4375,160.73334 L 108.4375,162.23334 L 103.1875,162.23334\" \n \
     id=\"path2495\" \n \
     style=\"fill:url(#linearGradient3222);fill-opacity:1;stroke:#800000;stroke-width:1;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1\" /> \n \
  <path \n \
     d=\"M 63.3125,147.10834 C 71.3125,147.10834 99.8125,147.10834 99.8125,147.10834 C 99.8125,147.10834 101.8784,148.35162 102.5625,149.10834 C 103.26124,149.88125 104.3125,152.10834 104.3125,152.10834 L 104.3125,161.60834 C 104.3125,161.60834 103.20397,163.45517 102.5625,164.10834 C 101.84772,164.83615 99.8125,166.10834 99.8125,166.10834 L 63.3125,166.10834 L 63.3125,166.10834 L 53.3125,166.10834 L 44.8125,166.10834 C 44.8125,166.10834 42.777281,165.22627 42.0625,164.49846 C 41.421025,163.84529 40.3125,162.60834 40.3125,162.60834 L 40.181985,160.60834 L 36.8125,160.60834 L 36.8125,162.60834 L 34.5625,162.60834 L 34.5625,152.60834 L 36.8125,152.60834 L 36.8125,154.60834 L 40.3125,154.60834 L 40.3125,152.10834 C 40.3125,152.10834 41.363764,149.88125 42.0625,149.10834 C 42.746601,148.35162 44.8125,147.10834 44.8125,147.10834 L 53.3125,147.10834 L 63.3125,147.10834 z\" \n \
     id=\"path2653\" \n \
     style=\"fill:url(#linearGradient3219);fill-opacity:1;stroke:#a00000;stroke-width:1;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1\" /> \n \
  <path \n \
     d=\"M 46.3125,152.60834 L 48.8125,152.60834 L 48.8125,154.60834 L 52.3125,154.60834 L 52.3125,152.60834 L 98.062505,152.60834 L 98.062505,162.60834 L 52.3125,162.60834 L 52.3125,160.60834 L 48.8125,160.60834 L 48.8125,162.60834 L 46.3125,162.60834 L 46.3125,152.60834 z\" \n \
     id=\"path9\" \n \
     style=\"fill:#ffffff;fill-opacity:1;stroke:#a00000;stroke-width:1;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1\" /> \n \
  <text \n \
     style=\"font-size:12px;text-align:center;text-anchor:middle;fill:#000000;fill-opacity:1;font-family:Bitstream Vera Sans\"> \n \
    <tspan \n \
       x=\"72.5\" \n \
       y=\"160.7\" \n \
       id=\"tspan2696\" \n \
       style=\"font-size:11px;fill:#000000;fill-opacity:1\">x</tspan> \n \
  </text> \n \
  <rect \n \
     width=\"137.5\" \n \
     height=\"0.14\" \n \
     x=\"3.75\" \n \
     y=\"-219.6\" \n \
     transform=\"scale(1,-1)\" \n \
     id=\"rect3247\" \n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1;stroke-opacity:1\" /> \n \
  <rect \n \
     width=\"137.5\" \n \
     height=\"0.14\" \n \
     x=\"3.75\" \n \
     y=\"-218.\" \n \
     transform=\"scale(1,-1)\" \n \
     id=\"rect3249\" \n \
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#fff080;stroke-width:1;stroke-opacity:1\" /> \n \
  <g \n \
     transform=\"translate(0,14)\" \n \
     id=\"g3283\"> \n \
    <path \n \
       d=\"M 37.498269,250.45337 L 40.83177,250.45337 L 40.83177,253.12016 L 45.498669,253.12016 L 45.498669,250.45337 L 106.50173,250.45337 L 106.50173,263.78737 L 45.498669,263.78737 L 45.498669,261.12056 L 40.83177,261.12056 L 40.83177,263.78737 L 37.498269,263.78737 L 37.498269,250.45337 z\" \n \
       id=\"path3261\" \n \
       style=\"fill:url(#linearGradient3322);fill-opacity:1;stroke:#c00000;stroke-width:1;stroke-opacity:1\" /> \n \
    <text \n \
       style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n \
      <tspan \n \
         x=\"72\" \n \
         y=\"260\" \n \
         id=\"tspan3265\" \n \
         style=\"font-size:11px\">"

    data8 = \
"</tspan> \n \
    </text> \n \
  </g> \n \
  <g \n \
     transform=\"translate(1,4)\" \n \
     id=\"g3304\"> \n \
    <g \n \
       transform=\"translate(0,-0.14263)\" \n \
       id=\"g3288\"> \n \
      <path \n \
         d=\"M 47.87,283.71263 C 58.590001,283.71263 58.590001,283.71263 58.590001,283.71263 L 62.275001,286.39263 L 64.620001,290.41264 L 64.620001,313.19263 L 62.275001,317.21263 L 58.590001,319.89263 L 47.200001,319.89263 L 47.200001,319.89263 L 47.200001,322.57263 L 33.8,322.57263 L 33.8,319.89263 L 22.41,319.89263 L 18.725001,317.21263 L 16.38,313.19263 L 16.38,290.41264 L 18.725001,286.39263 L 22.41,283.71263 L 33.13,283.71263 L 33.13,287.06264 L 47.87,287.06264 L 47.87,283.71263 z\" \n \
         id=\"path3251\" \n \
         style=\"fill:url(#linearGradient3318);fill-opacity:1;stroke:#c00000;stroke-width:1;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1\" /> \n"

    data9a = \
"      <text \n \
         style=\"font-size:8.03999996px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n \
        <tspan \n \
           x=\"40\" \n \
           y=\"307\" \n \
           id=\"tspan3255\" \n \
           style=\"font-size:12.06000042px\">"

    data9b = \
"      <text \n \
         style=\"font-size:8.03999996px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n \
        <tspan \n \
           x=\"40\" \n \
           y=\"301\" \n \
           id=\"tspan3255\" \n \
           style=\"font-size:12.06000042px\">"

    data10b = \
"</tspan> \n \
      </text> \n \
      <text \n \
         style=\"font-size:8.03999996px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n \
        <tspan \n \
           x=\"40\" \n \
           y=\"313.8\" \n \
           id=\"tspan3259\" \n \
           style=\"font-size:12.06000042px\">"

    data11 = \
"</tspan> \n \
      </text> \n \
    </g> \n \
    <g \n \
       id=\"g3295\"> \n \
      <path \n \
         d=\"M 109.87,283.57 C 120.59,283.57 120.59,283.57 120.59,283.57 L 124.275,286.25 L 126.62,290.27001 L 126.62,313.05 L 124.275,317.07 L 120.59,319.75 L 109.2,319.75 L 109.2,319.75 L 109.2,322.43 L 95.8,322.43 L 95.8,319.75 L 84.41,319.75 L 80.725001,317.07 L 78.38,313.05 L 78.38,290.27001 L 80.725001,286.25 L 84.41,283.57 L 95.13,283.57 L 95.13,286.92001 L 109.87,286.92001 L 109.87,283.57 z\" \n \
         id=\"path3271\" \n \
         style=\"fill:url(#linearGradient3320);fill-opacity:1;stroke:#c00000;stroke-width:1;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1\" /> \n"

    data12a = \
"      <text \n \
         style=\"font-size:8.03999996px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n \
        <tspan \n \
           x=\"102\" \n \
           y=\"307\" \n \
           id=\"tspan3275\" \n \
           style=\"font-size:12.06000042px\">"

    data12b = \
"      <text \n \
         style=\"font-size:8.03999996px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n \
        <tspan \n \
           x=\"102\" \n \
           y=\"301\" \n \
           id=\"tspan3275\" \n \
           style=\"font-size:12.06000042px\">"

    data13b = \
"</tspan> \n \
      </text> \n \
      <text \n \
         style=\"font-size:8.03999996px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n \
        <tspan \n \
           x=\"102\" \n \
           y=\"314\" \n \
           id=\"tspan3279\" \n \
           style=\"font-size:12.06000042px\">"

    data14 = \
"</tspan> \n \
      </text> \n \
    </g> \n \
  </g> \n \
  <path \n \
     d=\"M 90.2125,230.89273 L 101.2675,230.89273 L 101.2675,234.91273 L 98.5875,234.91273 L 98.5875,232.90273 L 91.5525,232.90273\" \n \
     id=\"path3422\" \n \
     style=\"fill:#e00000;fill-opacity:1;stroke:#800000;stroke-width:1;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1\" /> \n \
  <path \n \
     d=\"M 90.2125,249.31773 L 101.2675,249.31773 L 101.2675,245.29773 L 98.5875,245.29773 L 98.5875,247.30773 L 91.5525,247.30773\" \n \
     id=\"path3424\" \n \
     style=\"fill:#e00000;fill-opacity:1;stroke:#800000;stroke-width:1;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1\" /> \n \
  <path \n \
     d=\"M 75.4725,227.54273 C 86.1925,227.54273 86.1925,227.54273 86.1925,227.54273 C 86.1925,227.54273 88.960805,229.20872 89.8775,230.22273 C 90.813806,231.25843 92.2225,234.24273 92.2225,234.24273 L 92.2225,246.97273 C 92.2225,246.97273 90.737077,249.44748 89.8775,250.32273 C 88.919695,251.298 86.1925,253.00273 86.1925,253.00273 L 74.8025,253.00273 L 74.8025,253.00273 L 74.8025,255.68273 L 61.4025,255.68273 L 61.4025,253.00273 L 50.0125,253.00273 C 50.0125,253.00273 47.285306,251.298 46.3275,250.32273 C 45.467923,249.44748 43.9825,246.97273 43.9825,246.97273 L 43.9825,234.24273 C 43.9825,234.24273 45.391194,231.25843 46.3275,230.22273 C 47.244195,229.20872 50.0125,227.54273 50.0125,227.54273 L 60.7325,227.54273 L 60.7325,230.89273 L 75.4725,230.89273 L 75.4725,227.54273 z\" \n \
     id=\"path3426\" \n \
     style=\"fill:url(#linearGradient3452);fill-opacity:1;stroke:#c00000;stroke-width:1.33000004;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1\" /> \n \
  <text \n \
     style=\"font-size:12.06000042px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\"> \n \
    <tspan \n \
       x=\"68\" \n \
       y=\"244\" \n \
       id=\"tspan3430\" \n \
       style=\"font-size:12.06000042px;font-family:Bitstream Vera Sans\">"

    data15 = \
"</tspan> \n \
  </text> \n \
</svg> \n"


    FILE = open(os.path.join("../images", sys.argv[1], mygroup, myname + ".svg"), "w")
    FILE.write(data0)
    FILE.write(_(mystring1).encode("utf-8"))
    FILE.write(data1)
    strings = _(mystring2).split(" ",2)
    if len(strings) == 1:
        FILE.write(data2a)
        FILE.write(strings[0].encode("utf-8"))
    else:
        FILE.write(data2b)
        FILE.write(strings[0].encode("utf-8"))
        FILE.write(data3b)
        FILE.write(strings[1].encode("utf-8"))
    FILE.write(data4)
    FILE.write(_(mystring3).encode("utf-8"))
    FILE.write(data5)
    FILE.write(_(mystring4).encode("utf-8"))
    FILE.write(data6)
    FILE.write(_(mystring5).encode("utf-8"))
    FILE.write(data7)
    FILE.write(_(mystring6).encode("utf-8"))
    FILE.write(data8)
    strings = _(mystring7).split(" ",2)
    if len(strings) == 1:
        FILE.write(data9a)
        FILE.write(strings[0].encode("utf-8"))
    else:
        FILE.write(data9b)
        FILE.write(strings[0].encode("utf-8"))
        FILE.write(data10b)
        FILE.write(strings[1].encode("utf-8"))
    FILE.write(data11)
    strings = _(mystring8).split(" ",2)
    if len(strings) == 1:
        FILE.write(data12a)
        FILE.write(strings[0].encode("utf-8"))
    else:
        FILE.write(data12b)
        FILE.write(strings[0].encode("utf-8"))
        FILE.write(data13b)
        FILE.write(strings[1].encode("utf-8"))
    FILE.write(data14)
    FILE.write(_(mystring9).encode("utf-8"))
    FILE.write(data15)
    FILE.close()
    return

if __name__ == "__main__":
    main()




