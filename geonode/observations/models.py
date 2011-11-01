# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2010-2011, GEM Foundation.
#
# OpenQuake is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# only, as published by the Free Software Foundation.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License version 3 for more details
# (a copy is included in the LICENSE file that accompanied this code).
#
# You should have received a copy of the GNU Lesser General Public License
# version 3 along with OpenQuake.  If not, see
# <http://www.gnu.org/licenses/lgpl-3.0.txt> for a copy of the LGPLv3 License

from django.contrib.gis.db import models

#observation db


class FaultSource(models.Model):
    name = models.CharField(max_length=30)
    length_min = models.FloatField()
    length_max = models.FloatField()
    length_pre = models.FloatField()
    u_sm_d_min = models.FloatField()
    u_sm_d_max = models.FloatField()
    u_sm_d_pre = models.FloatField()
    u_sm_d_com = models.FloatField()
    low_d_min = models.FloatField()
    low_d_max = models.FloatField()
    low_d_pref = models.FloatField()
    low_d_com = models.FloatField()
    width = models.FloatField()
    area = models.FloatField()
    dip_min = models.IntegerField()
    dip_maz = models.IntegerField()
    dip_pref = models.IntegerField()
    dip_com = models.IntegerField()
    dip_dir = models.IntegerField()
    rake_min = models.IntegerField()
    rake_max = models.IntegerField()
    rake_pref = models.IntegerField()
    rake_com = models.IntegerField()
    slip_typ = models.CharField(max_length=30)
    slip_com = models.IntegerField()
    slip_r_min = models.IntegerField()
    slip_r_max = models.IntegerField()
    slip_r_pre = models.IntegerField()
    slip_r_com = models.IntegerField()
    magnitude = models.IntegerField()
    aseis_slip = models.FloatField()
    aseis_com = models.IntegerField()
    dis_min = models.FloatField()
    dis_max = models.FloatField()
    dis_pref = models.FloatField()
    re_int_min = models.IntegerField()
    re_int_max = models.IntegerField()
    re_int_pre = models.IntegerField()
    mov_min = models.IntegerField()
    mov_max = models.IntegerField()
    mov_pref = models.IntegerField()
    all_com = models.IntegerField()
    compiler = models.CharField(max_length=30)
    contrib = models.CharField(max_length=30)
    geom = models.MultiLineStringField(srid=4326)
    created = models.DecimalField(max_digits=4, decimal_places=3)

    class Meta:
        db_table = 'fault_source'


class Fault(models.Model):
    name = models.CharField(max_length=30)
    length_min = models.FloatField()
    length_max = models.FloatField()
    length_pre = models.FloatField()
    strike = models.IntegerField()
    episodi_is = models.CharField(max_length=30)
    episodi_ac = models.CharField(max_length=30)
    u_sm_d_min = models.FloatField()
    u_sm_d_max = models.FloatField()
    u_sm_d_pre = models.FloatField()
    u_sm_d_com = models.FloatField()
    low_d_min = models.FloatField()
    low_d_max = models.FloatField()
    low_d_pref = models.FloatField()
    low_d_com = models.FloatField()
    dip_min = models.IntegerField()
    dip_maz = models.IntegerField()
    dip_pref = models.IntegerField()
    dip_com = models.IntegerField()
    dip_dir = models.IntegerField()
    down_thro = models.IntegerField()
    slip_typ = models.CharField(max_length=30)
    slip_com = models.IntegerField()
    slip_r_min = models.IntegerField()
    slip_r_max = models.IntegerField()
    slip_r_pre = models.IntegerField()
    slip_r_com = models.IntegerField()
    aseis_slip = models.FloatField()
    aseis_com = models.IntegerField()
    dis_min = models.FloatField()
    dis_max = models.FloatField()
    dis_pref = models.FloatField()
    re_int_min = models.IntegerField()
    re_int_max = models.IntegerField()
    re_int_pre = models.IntegerField()
    mov_min = models.IntegerField()
    mov_max = models.IntegerField()
    mov_pref = models.IntegerField()
    all_com = models.IntegerField()
    compiler = models.CharField(max_length=30)
    contrib = models.CharField(max_length=30)
    created = models.DecimalField(max_digits=4, decimal_places=3)

    class Meta:
        db_table = 'fault'

class FaultSection(models.Model):
    fault = models.ManyToManyField('Fault')
    name = models.CharField(max_length=30)
    length_min = models.FloatField()
    length_max = models.FloatField()
    length_pre = models.FloatField()
    strike = models.IntegerField()
    episodi_is = models.CharField(max_length=30)
    episodi_ac = models.CharField(max_length=30)
    u_sm_d_min = models.FloatField()
    u_sm_d_max = models.FloatField()
    u_sm_d_pre = models.FloatField()
    u_sm_d_com = models.FloatField()
    low_d_min = models.FloatField()
    low_d_max = models.FloatField()
    low_d_pref = models.FloatField()
    low_d_com = models.FloatField()
    dip_min = models.IntegerField()
    dip_maz = models.IntegerField()
    dip_pref = models.IntegerField()
    dip_com = models.IntegerField()
    dip_dir = models.IntegerField()
    down_thro = models.IntegerField()
    slip_typ = models.CharField(max_length=30)
    slip_com = models.IntegerField()
    slip_r_min = models.IntegerField()
    slip_r_max = models.IntegerField()
    slip_r_pre = models.IntegerField()
    slip_r_com = models.IntegerField()
    aseis_slip = models.FloatField()
    aseis_com = models.IntegerField()
    dis_min = models.FloatField()
    dis_max = models.FloatField()
    dis_pref = models.FloatField()
    re_int_min = models.IntegerField()
    re_int_max = models.IntegerField()
    re_int_pre = models.IntegerField()
    mov_min = models.IntegerField()
    mov_max = models.IntegerField()
    mov_pref = models.IntegerField()
    all_com = models.IntegerField()
    compiler = models.CharField(max_length=30)
    contrib = models.CharField(max_length=30)
    created = models.DecimalField(max_digits=4, decimal_places=3)

    class Meta:
        db_table = 'fault_section'


class Trace(models.Model):
    tid = models.IntegerField()
    name = models.IntegerField(max_length=100, default='-1', blank=True)
    fault_section = models.ManyToManyField('FaultSection')
    fault_name = models.CharField(max_length=30)
    loc_meth = models.CharField(max_length=30)
    scale = models.IntegerField()
    accuracy = models.IntegerField()
    notes = models.TextField()
    geom = models.MultiLineStringField(srid=4326)

    class Meta:
        db_table = 'trace'


class SiteObservation(models.Model):
    geom = models.MultiLineStringField(srid=4326)
    fault_section = models.ManyToManyField('FaultSection')
    scale = models.IntegerField()
    accuracy = models.IntegerField()
    feature = models.CharField(max_length=30)
    notes = models.TextField()

    class Meta:
        db_table = 'site_observation'


class Observation(models.Model):
    OBS_TYPE = (
        ('0', 'Displacement'),
        ('1', 'Event'),
        ('2', 'Recurrence Interval'),
        ('3', 'Seismogenic Geometry'),
        ('4', 'SlipRate'),
    )
    observationType = models.CharField("Observation Type", max_length=1,
                                       choices=OBS_TYPE, blank=True)
    SLIP_TYPE = (
        ('0', 'Reverse'),
        ('1', 'Thrust (dip <45)'),
        ('2', 'Normal'),
        ('3', 'Dextral'),
        ('4', 'Sinistral'),
        ('5', 'Normal dextral'),
        ('6', 'Normal sinistral'),
        ('7', 'Reverse dextral'),
        ('8', 'Reverse sinistral'),
        ('9', 'Dextral normal'),
        ('10', 'Dextral reverse'),
        ('11', 'Sinistral reverse'),
        ('12', 'Sinistral normal'),
    )
    slipType = models.CharField("Slip Type", max_length=1, choices=SLIP_TYPE,
                                blank=True)

    hv_ratio = models.CharField("H:V Ratio", max_length=100, blank=True)

    rake = models.CharField("Rake (deg)", max_length=100, blank=True)

    net_slip_rate_min = models.CharField("Net Slip Min Rate (mm/yr)",
                                         max_length=100, blank=True)
    net_slip_rate_max = models.CharField("Net Slip Max Rate (mm/yr)",
                                         max_length=100, blank=True)
    net_slip_rate_pref = models.CharField("Net Slip Pref. Rate (mm/yr)",
                                          max_length=100, blank=True)

    dip_slip_rate_min = models.CharField("Dip Slip Min Rate (mm/yr)",
                                         max_length=100, blank=True)
    dip_slip_rate_max = models.CharField("Dip Slip Max Rate (mm/yr)",
                                         max_length=100, blank=True)
    dip_slip_rate_pref = models.CharField("Dip Slip Pref. Rate (mm/yr)",
                                          max_length=100, blank=True)

    strike_slip_rate_min = models.CharField("Strike Slip Min Rate (mm/yr)",
                                            max_length=100, blank=True)
    strike_slip_rate_max = models.CharField("Strike Slip Max Rate (mm/yr)",
                                            max_length=100, blank=True)
    strike_slip_rate_pref = models.CharField("Strike Slip Pref. Rate (mm/yr)",
                                             max_length=100, blank=True)

    vertical_slip_rate_min = models.CharField("Vertical Slip Min Rate (mm/yr)",
                                              max_length=100, blank=True)
    vertical_slip_rate_max = models.CharField("Vertical Slip Max Rate (mm/yr)",
                                              max_length=100, blank=True)
    vertical_slip_rate_pref = models.CharField("Vertical Slip " \
                                               "Pref. Rate (mm/yr)",
                                               max_length=100, blank=True)

    SLIP_RATE_CAT = (
        ('0', '0.001 <0.01'),
        ('1', '0.01 <0.1'),
        ('2', '0.1 <1'),
        ('3', '1 <5'),
        ('4', '5 <10'),
        ('5', '10 <50'),
        ('6', '50 <100'),
        ('7', '100 <200'),
    )
    slip_rate_category = models.CharField("Slip Rate Category", max_length=10,
                                          choices=SLIP_RATE_CAT, blank=True)

    marker_age = models.CharField("Marker Age (yrs BP)",
                                  max_length=100, blank=True)

    site = models.CharField("Site", max_length=100, blank=True)

    notes = models.TextField("Notes", blank=True)

    summary_id = models.CharField(max_length=100,  blank=True)

    class Meta:
        db_table = 'observations_observations'


class FaultSummary(models.Model):
    fid = models.IntegerField()
    name = models.IntegerField(max_length=100, default='-1', blank=True)

    class Meta:
        db_table = 'fault_summary'
