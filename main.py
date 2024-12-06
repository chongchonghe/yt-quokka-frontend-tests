#!/usr/bin/env python3
"""
This script is used to test the QUOKKA frontend of the yt library.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import yt

yt.set_log_level("ERROR")

def test_basic():
    #ds = yt.load("/Users/cche/softwares/quokka/quokka.copy2/tests/plt00005")
    # data_dir = "quokka_data/star_rotation/plt15000"
    data_dir = "quokka_data/radiating_particles/plt00032"
    ds = yt.load(data_dir)
    ad = ds.all_data()
    df = ds.derived_field_list

    print("ds =")
    print(ds)
    print("ad =")
    print(ad)
    print("df =")
    for f in df:
        print(f)

def plot_Erad(ds, axis_on=True, ylim=None):
    # field = {'temperature': ('boxlib', 'temperature'), 'rad': ('boxlib', 'radEnergy-Group0')}[field]
    field = ('rad', 'energy_density_0')
    p = yt.SlicePlot(ds, "z", field, center='c')
    p.set_cmap(field, 'hot')
    if ylim is not None:
        p.set_zlim(field, ylim[0], ylim[1])
    if axis_on:
        length_unit = ds.unit_system['length']
        energy_unit = ds.unit_system['energy']
        cb_unit = "{}/{}^3".format(energy_unit, length_unit)
        p.set_xlabel("x [{}]".format(length_unit))
        p.set_ylabel("y [{}]".format(length_unit))
        p.set_colorbar_label(field, "{} [{}]".format(field, cb_unit))
    else:
        p.hide_axes()
        p.hide_colorbar()

    # annotate particles
    p.annotate_particles(1, p_size=400., col='blue', marker='*', ptype='Rad_particles')
    return p

def plot_Frad(ds, axis_on=True, ylim=None):
    # field = ('boxlib', 'x-RadFlux-Group0')  # CCH: this works
    field = ('rad', 'flux_density_x_0')   # CCH: this doesn't work
    p = yt.SlicePlot(ds, "z", field, center='c')
    p.set_cmap(field, 'bwr')
    if ylim is not None:
        p.set_zlim(field, ylim[0], ylim[1])
    if axis_on:
        length_unit = ds.unit_system['length']
        energy_unit = ds.unit_system['energy']
        time_unit = ds.unit_system['time']
        cb_unit = "{}.{}^-2.{}^-1".format(energy_unit, length_unit, time_unit)
        p.set_xlabel("x [{}]".format(length_unit))
        p.set_ylabel("y [{}]".format(length_unit))
        p.set_colorbar_label(field, "{} [{}]".format(field, cb_unit))
    else:
        p.hide_axes()
        p.hide_colorbar()

    # annotate particles
    p.annotate_particles(1, p_size=400., col='blue', marker='*', ptype='Rad_particles')
    return p

def test_radiating_particles():
    data_dir = "quokka_data/radiating_particles/plt00032"
    ds = yt.load(data_dir)
    print("ds.field_list =")
    print(ds.field_list)

    # plot slice
    p = plot_Erad(ds, axis_on=True, ylim=[1e-5, 2e1])
    p.save()

    ylim = None
    p = plot_Frad(ds, axis_on=True, ylim=ylim)
    p.save()
    return

def main():
    test_basic()
    test_radiating_particles()
    return


if __name__ == "__main__":
    main()
