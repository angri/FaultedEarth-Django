# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # fault section view
        db.execute("""CREATE VIEW gem.fault_section_view AS
                SELECT observations_faultsection.id,
                observations_faultsection.sec_name,
                observations_faultsection.length_min,
                observations_faultsection.length_max,
                observations_faultsection.length_pre,
                observations_faultsection.strike,
                observations_faultsection.episodi_is,
                observations_faultsection.episodi_ac,
                observations_faultsection.u_sm_d_min,
                observations_faultsection.u_sm_d_max,
                observations_faultsection.u_sm_d_pre,
                observations_faultsection.u_sm_d_com,
                observations_faultsection.low_d_min,
                observations_faultsection.low_d_max,
                observations_faultsection.low_d_pref,
                observations_faultsection.low_d_com,
                observations_faultsection.dip_min,
                observations_faultsection.dip_max,
                observations_faultsection.dip_pref,
                observations_faultsection.dip_com,
                observations_faultsection.dip_dir,
                observations_faultsection.down_thro,
                observations_faultsection.slip_typ,
                observations_faultsection.slip_com,
                observations_faultsection.slip_r_min,
                observations_faultsection.slip_r_max,
                observations_faultsection.slip_r_pre,
                observations_faultsection.slip_r_com,
                observations_faultsection.aseis_slip,
                observations_faultsection.aseis_com,
                observations_faultsection.dis_min,
                observations_faultsection.dis_max,
                observations_faultsection.dis_pref,
                observations_faultsection.re_int_min,
                observations_faultsection.re_int_max,
                observations_faultsection.re_int_pre, observations_trace.geom,
                observations_faultsection.mov_min,
                observations_faultsection.mov_max,
                observations_faultsection.mov_pref,
                observations_faultsection.all_com,
                observations_faultsection.compiler,
                observations_faultsection.contrib,
                observations_faultsection.created
                   FROM gem.observations_faultsection
                      JOIN gem.observations_trace_fault_section ON
                      observations_faultsection.id =
                      observations_trace_fault_section.faultsection_id
                         JOIN gem.observations_trace ON
                         observations_trace_fault_section.trace_id =
                         observations_trace.id""")


        # fault view
        db.execute("""CREATE VIEW gem.fault_view AS
                SELECT observations_fault.id,
                observations_fault.fault_name, observations_fault.length_min,
                observations_fault.length_max, observations_fault.length_pre,
                observations_fault.strike, observations_fault.episodi_is,
                observations_fault.episodi_ac, observations_fault.u_sm_d_min,
                observations_fault.u_sm_d_max, observations_fault.u_sm_d_pre,
                observations_fault.u_sm_d_com, observations_fault.low_d_min,
                observations_fault.low_d_max, observations_fault.low_d_pref,
                observations_fault.low_d_com, observations_fault.dip_min,
                observations_fault.dip_max, observations_fault.dip_pref,
                observations_fault.dip_com, observations_fault.dip_dir,
                observations_fault.down_thro, observations_fault.slip_typ,
                observations_fault.slip_com, observations_fault.slip_r_min,
                observations_fault.slip_r_max, observations_fault.slip_r_pre,
                observations_fault.slip_r_com, observations_fault.aseis_slip,
                observations_fault.aseis_com, observations_fault.dis_min,
                observations_fault.dis_max, observations_fault.dis_pref,
                observations_fault.re_int_min, observations_fault.re_int_max,
                observations_fault.re_int_pre, observations_fault.mov_min,
                observations_fault.mov_max, observations_fault.mov_pref,
                observations_fault.all_com, observations_fault.compiler,
                observations_fault.contrib, observations_fault.created
                    FROM gem.observations_fault
                JOIN gem.observations_faultsection_fault ON
                observations_fault.id = observations_faultsection_fault.fault_id
                JOIN gem.observations_faultsection ON observations_fault.id =
                observations_faultsection_fault.fault_id""")

        # simple geometry view

        db.execute("""CREATE VIEW gem.simple_geom_view AS
                 SELECT f.id, f.fault_name, f.simple_geom
                 FROM gem.observations_fault f""")

        # manual observations_trace geometry table insert
        db.execute("""INSERT INTO public.geometry_columns VALUES ('', 'gem',
                'fault_section_view', 'geom', '2', 4326, 'MULTILINESTRING')""");

        db.execute("""INSERT INTO public.geometry_columns VALUES ('', 'gem',
                'fault_view', 'simple_geom', '2', 4326,
                'MULTILINESTRING')""");

    def backwards(self, orm):
        db.execute("DROP VIEW fault_section_view")
        db.execute("DROP VIEW fault_view")


    models = {
        'observations.fault': {
            'Meta': {'object_name': 'Fault'},
            'all_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {}),
            'dis_max': ('django.db.models.fields.FloatField', [], {}),
            'dis_min': ('django.db.models.fields.FloatField', [], {}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {}),
            'down_thro': ('django.db.models.fields.IntegerField', [], {}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fault_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {}),
            'length_min': ('django.db.models.fields.FloatField', [], {}),
            'length_pre': ('django.db.models.fields.FloatField', [], {}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_max': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_min': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'strike': ('django.db.models.fields.IntegerField', [], {}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {})
        },
        'observations.faultsection': {
            'Meta': {'object_name': 'FaultSection'},
            'all_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {}),
            'dis_max': ('django.db.models.fields.FloatField', [], {}),
            'dis_min': ('django.db.models.fields.FloatField', [], {}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {}),
            'down_thro': ('django.db.models.fields.IntegerField', [], {}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fault': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.Fault']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {}),
            'length_min': ('django.db.models.fields.FloatField', [], {}),
            'length_pre': ('django.db.models.fields.FloatField', [], {}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {}),
            'sec_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_max': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_min': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'strike': ('django.db.models.fields.IntegerField', [], {}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {})
        },
        'observations.faultsource': {
            'Meta': {'object_name': 'FaultSource'},
            'all_com': ('django.db.models.fields.IntegerField', [], {}),
            'area': ('django.db.models.fields.FloatField', [], {}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {}),
            'dis_max': ('django.db.models.fields.FloatField', [], {}),
            'dis_min': ('django.db.models.fields.FloatField', [], {}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {}),
            'length_min': ('django.db.models.fields.FloatField', [], {}),
            'length_pre': ('django.db.models.fields.FloatField', [], {}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {}),
            'magnitude': ('django.db.models.fields.IntegerField', [], {}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {}),
            'rake_com': ('django.db.models.fields.IntegerField', [], {}),
            'rake_max': ('django.db.models.fields.IntegerField', [], {}),
            'rake_min': ('django.db.models.fields.IntegerField', [], {}),
            'rake_pref': ('django.db.models.fields.IntegerField', [], {}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_max': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_min': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'source_nm': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {}),
            'width': ('django.db.models.fields.FloatField', [], {})
        },
        'observations.faultsourcetrace': {
            'Meta': {'object_name': 'FaultSourceTrace'},
            'geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'observations.faultsummary': {
            'Meta': {'object_name': 'FaultSummary'},
            'fid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.IntegerField', [], {'default': "'-1'", 'max_length': '100', 'blank': 'True'})
        },
        'observations.observations': {
            'Meta': {'object_name': 'Observations'},
            'dip_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'dip_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'dip_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'hv_ratio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marker_age': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'net_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'net_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'net_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'observationType': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'rake': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slipType': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'slip_rate_category': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'strike_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'strike_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'strike_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'summary_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vertical_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vertical_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vertical_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'observations.siteobservation': {
            'Meta': {'object_name': 'SiteObservation'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'fault_section': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.FaultSection']", 'symmetrical': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            's_feature': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'observations.trace': {
            'Meta': {'object_name': 'Trace'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'fault_section': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.FaultSection']", 'symmetrical': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loc_meth': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {}),
            'tid': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['observations']