
${par_db=la db}
${par_ot=123daw}


--******************************* validacion *************************
drop table if exists ${par_db}.xdjajaja;
create table ${par_db}.xdjajaja (
    columna,
    columna_b
)
;

drop table if exists ${par_db}.${par_ot}_xdjajaja;
create tabLE ${par_db}.${par_ot}_xdjajaja
    Select
        xd
    from algunA_TAbla
;


impala-shell -k -i aldwkjalkd -B 'select from * xd' -o
;
