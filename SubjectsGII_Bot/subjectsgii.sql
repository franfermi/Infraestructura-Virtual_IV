--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.5
-- Dumped by pg_dump version 9.6.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: subjectsgii; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE subjectsgii (
    asignatura character varying(5) NOT NULL,
    guia_docente character varying(200),
    fecha_examen date,
    horario text
);


ALTER TABLE subjectsgii OWNER TO postgres;

--
-- Data for Name: subjectsgii; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY subjectsgii (asignatura, guia_docente, fecha_examen, horario) FROM stdin;
IV	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/tecnologiasdelainformacion/gii_infraestructura_virtual_20172018_firmada/!	2018-01-12	Jueves:11:30-13:30
DAI	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/tecnologiasdelainformacion/etsiit_gii_dai_1718_desapint/!	2018-01-24	Martes:11:30-13:30
SPSI	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/tecnologiasdelainformacion/spsi/!	2018-01-17	Viernes:10:30-12:30
TID	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/tecnologiasdelainformacion/complementos/ficha_ginf_tid_29611fa/!	2018-01-22	Lunes:10:30-12:30
CRIM	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/tecnologiasdelainformacion/complementos/ficha_ginf_crim_29611fc/!	2018-01-15	Miercoles:10:30-12:30
NPI	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/computacionysistemasinteligentes/etsiit_gii_npi_1718_nuevosparadigmasdeinteraccion/!	2018-01-24	Martes:9:30-11:30
PL	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/computacionysistemasinteligentes/etsiit_gii_pl_1718_procesadoresdelenguajes/!	2018-01-12	Jueves:9:30-11:30
VC	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/computacionysistemasinteligentes/ficha_ginf_vc_296114b/!	2018-01-17	Viernes:9:30-11:30
DGP	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadelsoftware/etsiit_gii_dgp_1718_dirgestproy/!	2018-01-17	Viernes:9:30-11:30
MDA	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadelsoftware/etsiit_gii_mda_1718_metodologiasdesarrolloagiles/!	2018-01-12	Martes:11:30-13:30
DBA	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadelsoftware/ficha_ginf_dbag_296114f/!	2018-01-24	Jueves:9:30-11:30
CPD	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadecomputadores/gii_centro_procesamiento_datos_20172018_firmada/!	2018-01-12	Jueves:11:30-13:30
SE	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadecomputadores/sistemas-empotrados/!	2018-01-24	Martes:11:30-13:30
TR	http://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadecomputadores/tecnologias-de-red/!	2018-01-17	Viernes:11:30-13:30
\.


--
-- PostgreSQL database dump complete
--

