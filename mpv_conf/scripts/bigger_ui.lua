-- Increase OSC (On Screen Controller) size
mp.options = require 'mp.options'
osc_opts = {
    osc_layout = "bottombar",
    seekbarstyle = "bar",
    scalefactor = 2.5,
    deadzonesize = 0.5,
    boxalpha = 0.8,
}
mp.options.read_options(osc_opts, "osc")
