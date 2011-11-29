--
-- Joins fault and faultsection tables along with bridging table.
-- Is used in "Fault summary" accordion tab.
--
CREATE VIEW
    gem.fault_view
AS SELECT

    observations_fault.id,
    observations_fault.fault_name,

    observations_fault.length_min,
    observations_fault.length_max,
    observations_fault.length_pre,

    observations_fault.strike,

    observations_fault.episodi_is,
    observations_fault.episodi_ac,

    observations_fault.u_sm_d_min,
    observations_fault.u_sm_d_max,
    observations_fault.u_sm_d_pre,
    observations_fault.u_sm_d_com,

    observations_fault.low_d_min,
    observations_fault.low_d_max,
    observations_fault.low_d_pref,
    observations_fault.low_d_com,

    observations_fault.dip_min,
    observations_fault.dip_max,
    observations_fault.dip_pref,
    observations_fault.dip_com,
    observations_fault.dip_dir,

    observations_fault.down_thro,

    observations_fault.slip_typ,
    observations_fault.slip_com,
    observations_fault.slip_r_min,
    observations_fault.slip_r_max,
    observations_fault.slip_r_pre,
    observations_fault.slip_r_com,

    observations_fault.aseis_slip,
    observations_fault.aseis_com,

    observations_fault.dis_min,
    observations_fault.dis_max,
    observations_fault.dis_pref,

    observations_fault.re_int_min,
    observations_fault.re_int_max,
    observations_fault.re_int_pre,

    observations_fault.mov_min,
    observations_fault.mov_max,
    observations_fault.mov_pref,

    observations_fault.all_com,
    observations_fault.compiler,
    observations_fault.contrib,
    observations_fault.created

FROM
    gem.observations_fault
    JOIN
    gem.observations_faultsection_fault
        ON observations_fault.id = observations_faultsection_fault.fault_id
    JOIN
    gem.observations_faultsection
        ON observations_fault.id = observations_faultsection_fault.fault_id;


--
-- Joins faultsection and trace tables along with a bridging table.
-- Is used in "Neotectonic Section summary" accordion tab.
--
CREATE VIEW
    gem.fault_section_view
AS SELECT

    observations_faultsection.id,
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
    observations_faultsection.re_int_pre,

    observations_trace.geom,

    observations_faultsection.mov_min,
    observations_faultsection.mov_max,
    observations_faultsection.mov_pref,

    observations_faultsection.all_com,
    observations_faultsection.compiler,
    observations_faultsection.contrib,
    observations_faultsection.created

FROM
    gem.observations_faultsection
    JOIN
    gem.observations_trace_fault_section
        ON
        observations_faultsection.id = observations_trace_fault_section.faultsection_id
    JOIN
    gem.observations_trace
        ON
        observations_trace_fault_section.trace_id = observations_trace.id;


--
-- Manual observations_trace geometry table insert
--
INSERT INTO
    public.geometry_columns
VALUES
    ('', 'gem', 'fault_section_view', 'geom', '2', 4326, 'MULTILINESTRING');



--
-- Joins fault, faultsection and faultsummary.
-- Is used in "Simple Fault Geometry" UI tab.
--
CREATE VIEW
    gem.simple_geom_view
AS SELECT
    fault.id,
    fault.fault_name,
    fault.simple_geom
FROM
    gem.observations_fault
    JOIN
    gem.observations_faultsection_fault
        ON observations_fault.id = observations_faultsection_fault.fault_id
    JOIN
    gem.observations_faultsection
        ON observations_fault.id = observations_faultsection.fault_id
    JOIN
    gem.observations_faultsection_faultsummary
        ON observations_faultsection_faultsummary.fault_section_id = observations_faultsection.id
    JOIN
    gem.observations_faultsummary
        ON observations_faultsection_faultsummary.fault_summary_id = observations_faultsummary.id;
