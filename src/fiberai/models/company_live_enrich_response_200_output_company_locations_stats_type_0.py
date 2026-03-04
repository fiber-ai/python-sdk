from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0")



@_attrs_define
class CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0:
    """ 
        Attributes:
            usa (Union[Unset, float]):
            gbr (Union[Unset, float]):
            fra (Union[Unset, float]):
            ind (Union[Unset, float]):
            bra (Union[Unset, float]):
            deu (Union[Unset, float]):
            esp (Union[Unset, float]):
            can (Union[Unset, float]):
            aus (Union[Unset, float]):
            nld (Union[Unset, float]):
            ita (Union[Unset, float]):
            zaf (Union[Unset, float]):
            bel (Union[Unset, float]):
            chn (Union[Unset, float]):
            tur (Union[Unset, float]):
            mex (Union[Unset, float]):
            che (Union[Unset, float]):
            nor (Union[Unset, float]):
            are (Union[Unset, float]):
            swe (Union[Unset, float]):
            pol (Union[Unset, float]):
            idn (Union[Unset, float]):
            arg (Union[Unset, float]):
            prt (Union[Unset, float]):
            col (Union[Unset, float]):
            chl (Union[Unset, float]):
            pak (Union[Unset, float]):
            dnk (Union[Unset, float]):
            jpn (Union[Unset, float]):
            nga (Union[Unset, float]):
            sgp (Union[Unset, float]):
            per (Union[Unset, float]):
            nzl (Union[Unset, float]):
            aut (Union[Unset, float]):
            irl (Union[Unset, float]):
            mys (Union[Unset, float]):
            bgd (Union[Unset, float]):
            egy (Union[Unset, float]):
            isr (Union[Unset, float]):
            sau (Union[Unset, float]):
            phl (Union[Unset, float]):
            fin (Union[Unset, float]):
            irn (Union[Unset, float]):
            rou (Union[Unset, float]):
            cze (Union[Unset, float]):
            grc (Union[Unset, float]):
            hkg (Union[Unset, float]):
            hun (Union[Unset, float]):
            ken (Union[Unset, float]):
            mar (Union[Unset, float]):
            vnm (Union[Unset, float]):
            rus (Union[Unset, float]):
            ukr (Union[Unset, float]):
            ecu (Union[Unset, float]):
            tha (Union[Unset, float]):
            lka (Union[Unset, float]):
            kor (Union[Unset, float]):
            bgr (Union[Unset, float]):
            gha (Union[Unset, float]):
            srb (Union[Unset, float]):
            twn (Union[Unset, float]):
            hrv (Union[Unset, float]):
            ltu (Union[Unset, float]):
            pri (Union[Unset, float]):
            svk (Union[Unset, float]):
            tun (Union[Unset, float]):
            est (Union[Unset, float]):
            ven (Union[Unset, float]):
            cri (Union[Unset, float]):
            pan (Union[Unset, float]):
            ury (Union[Unset, float]):
            lbn (Union[Unset, float]):
            lux (Union[Unset, float]):
            cyp (Union[Unset, float]):
            npl (Union[Unset, float]):
            jor (Union[Unset, float]):
            svn (Union[Unset, float]):
            mtq (Union[Unset, float]):
            qat (Union[Unset, float]):
            glp (Union[Unset, float]):
            uga (Union[Unset, float]):
            dza (Union[Unset, float]):
            gtm (Union[Unset, float]):
            cmr (Union[Unset, float]):
            lva (Union[Unset, float]):
            dom (Union[Unset, float]):
            aze (Union[Unset, float]):
            geo (Union[Unset, float]):
            sen (Union[Unset, float]):
            tza (Union[Unset, float]):
            zwe (Union[Unset, float]):
            kwt (Union[Unset, float]):
            mlt (Union[Unset, float]):
            omn (Union[Unset, float]):
            bol (Union[Unset, float]):
            slv (Union[Unset, float]):
            arm (Union[Unset, float]):
            pry (Union[Unset, float]):
            irq (Union[Unset, float]):
            khm (Union[Unset, float]):
            bih (Union[Unset, float]):
            ago (Union[Unset, float]):
            bhr (Union[Unset, float]):
            alb (Union[Unset, float]):
            kaz (Union[Unset, float]):
            civ (Union[Unset, float]):
            eth (Union[Unset, float]):
            mus (Union[Unset, float]):
            zmb (Union[Unset, float]):
            mkd (Union[Unset, float]):
            cod (Union[Unset, float]):
            blr (Union[Unset, float]):
            moz (Union[Unset, float]):
            reu (Union[Unset, float]):
            tto (Union[Unset, float]):
            guf (Union[Unset, float]):
            isl (Union[Unset, float]):
            mmr (Union[Unset, float]):
            hnd (Union[Unset, float]):
            rwa (Union[Unset, float]):
            mdg (Union[Unset, float]):
            ben (Union[Unset, float]):
            uzb (Union[Unset, float]):
            nam (Union[Unset, float]):
            bwa (Union[Unset, float]):
            mda (Union[Unset, float]):
            jey (Union[Unset, float]):
            nic (Union[Unset, float]):
            sdn (Union[Unset, float]):
            jam (Union[Unset, float]):
            imn (Union[Unset, float]):
            bfa (Union[Unset, float]):
            mng (Union[Unset, float]):
            mne (Union[Unset, float]):
            mco (Union[Unset, float]):
            tgo (Union[Unset, float]):
            afg (Union[Unset, float]):
            lby (Union[Unset, float]):
            xkx (Union[Unset, float]):
            cym (Union[Unset, float]):
            mwi (Union[Unset, float]):
            som (Union[Unset, float]):
            png (Union[Unset, float]):
            mdv (Union[Unset, float]):
            mli (Union[Unset, float]):
            gin (Union[Unset, float]):
            pse (Union[Unset, float]):
            gab (Union[Unset, float]):
            lie (Union[Unset, float]):
            hti (Union[Unset, float]):
            syr (Union[Unset, float]):
            brb (Union[Unset, float]):
            yem (Union[Unset, float]):
            ggy (Union[Unset, float]):
            ncl (Union[Unset, float]):
            and_ (Union[Unset, float]):
            sur (Union[Unset, float]):
            myt (Union[Unset, float]):
            kgz (Union[Unset, float]):
            bhs (Union[Unset, float]):
            gib (Union[Unset, float]):
            cog (Union[Unset, float]):
            fji (Union[Unset, float]):
            blm (Union[Unset, float]):
            cuw (Union[Unset, float]):
            cub (Union[Unset, float]):
            sle (Union[Unset, float]):
            blz (Union[Unset, float]):
            ner (Union[Unset, float]):
            lbr (Union[Unset, float]):
            vir (Union[Unset, float]):
            pyf (Union[Unset, float]):
            gum (Union[Unset, float]):
            mrt (Union[Unset, float]):
            abw (Union[Unset, float]):
            syc (Union[Unset, float]):
            guy (Union[Unset, float]):
            lso (Union[Unset, float]):
            swz (Union[Unset, float]):
            ssd (Union[Unset, float]):
            lca (Union[Unset, float]):
            mac (Union[Unset, float]):
            smr (Union[Unset, float]):
            lao (Union[Unset, float]):
            brn (Union[Unset, float]):
            tcd (Union[Unset, float]):
            bmu (Union[Unset, float]):
            vgb (Union[Unset, float]):
            prk (Union[Unset, float]):
            btn (Union[Unset, float]):
            bdi (Union[Unset, float]):
            fro (Union[Unset, float]):
            tjk (Union[Unset, float]):
            gmb (Union[Unset, float]):
            stp (Union[Unset, float]):
            ant (Union[Unset, float]):
            vct (Union[Unset, float]):
            dji (Union[Unset, float]):
            cpv (Union[Unset, float]):
            tkm (Union[Unset, float]):
            atg (Union[Unset, float]):
            tca (Union[Unset, float]):
            kna (Union[Unset, float]):
            grd (Union[Unset, float]):
            asm (Union[Unset, float]):
            vut (Union[Unset, float]):
            gnq (Union[Unset, float]):
            grl (Union[Unset, float]):
            sxm (Union[Unset, float]):
            mnp (Union[Unset, float]):
            com (Union[Unset, float]):
            tls (Union[Unset, float]):
            sjm (Union[Unset, float]):
            caf (Union[Unset, float]):
            dma (Union[Unset, float]):
            maf (Union[Unset, float]):
            wsm (Union[Unset, float]):
            bes (Union[Unset, float]):
            mhl (Union[Unset, float]):
            aia (Union[Unset, float]):
            ton (Union[Unset, float]):
            cok (Union[Unset, float]):
            slb (Union[Unset, float]):
            spm (Union[Unset, float]):
            gnb (Union[Unset, float]):
            ata (Union[Unset, float]):
            tuv (Union[Unset, float]):
            ala (Union[Unset, float]):
            iot (Union[Unset, float]):
            eri (Union[Unset, float]):
            plw (Union[Unset, float]):
            fsm (Union[Unset, float]):
            nru (Union[Unset, float]):
            pcn (Union[Unset, float]):
            flk (Union[Unset, float]):
            msr (Union[Unset, float]):
            vat (Union[Unset, float]):
            kir (Union[Unset, float]):
            shn (Union[Unset, float]):
            niu (Union[Unset, float]):
            wlf (Union[Unset, float]):
            hmd (Union[Unset, float]):
            cxr (Union[Unset, float]):
            nfk (Union[Unset, float]):
            atf (Union[Unset, float]):
            cck (Union[Unset, float]):
            sgs (Union[Unset, float]):
            bvt (Union[Unset, float]):
            umi (Union[Unset, float]):
            esh (Union[Unset, float]):
            tkl (Union[Unset, float]):
            x_south_asia (Union[Unset, float]):
            x_south_east_europe (Union[Unset, float]):
            x_northern_africa (Union[Unset, float]):
            x_pacific (Union[Unset, float]):
            x_south_west_europe (Union[Unset, float]):
            x_southern_africa (Union[Unset, float]):
            x_west_indies (Union[Unset, float]):
            x_south_america (Union[Unset, float]):
            x_south_west_asia (Union[Unset, float]):
            x_central_europe (Union[Unset, float]):
            x_eastern_europe (Union[Unset, float]):
            x_western_europe (Union[Unset, float]):
            x_central_america (Union[Unset, float]):
            x_western_africa (Union[Unset, float]):
            x_south_atlantic_ocean (Union[Unset, float]):
            x_south_east_asia (Union[Unset, float]):
            x_central_africa (Union[Unset, float]):
            x_north_america (Union[Unset, float]):
            x_east_asia (Union[Unset, float]):
            x_northern_europe (Union[Unset, float]):
            x_eastern_africa (Union[Unset, float]):
            x_southern_indian_ocean (Union[Unset, float]):
            x_southern_europe (Union[Unset, float]):
            x_central_asia (Union[Unset, float]):
            x_northern_asia (Union[Unset, float]):
            x_asia (Union[Unset, float]):
            x_europe (Union[Unset, float]):
            x_africa (Union[Unset, float]):
            x_oceania (Union[Unset, float]):
            x_americas (Union[Unset, float]):
            x_antarctica (Union[Unset, float]):
            x_atlantic_ocean (Union[Unset, float]):
            x_indian_ocean (Union[Unset, float]):
            x_middle_east (Union[Unset, float]):
            x_mena (Union[Unset, float]):
            x_emea (Union[Unset, float]):
            x_european_union (Union[Unset, float]):
            x_efta (Union[Unset, float]):
            x_apac (Union[Unset, float]):
            x_latam (Union[Unset, float]):
            x_anglosphere (Union[Unset, float]):
            x_dach (Union[Unset, float]):
            x_nordics (Union[Unset, float]):
            x_benelux (Union[Unset, float]):
            x_gcc (Union[Unset, float]):
            x_brics (Union[Unset, float]):
            x_g20 (Union[Unset, float]):
            x_oecd (Union[Unset, float]):
            x_sanctioned (Union[Unset, float]):
     """

    usa: Union[Unset, float] = UNSET
    gbr: Union[Unset, float] = UNSET
    fra: Union[Unset, float] = UNSET
    ind: Union[Unset, float] = UNSET
    bra: Union[Unset, float] = UNSET
    deu: Union[Unset, float] = UNSET
    esp: Union[Unset, float] = UNSET
    can: Union[Unset, float] = UNSET
    aus: Union[Unset, float] = UNSET
    nld: Union[Unset, float] = UNSET
    ita: Union[Unset, float] = UNSET
    zaf: Union[Unset, float] = UNSET
    bel: Union[Unset, float] = UNSET
    chn: Union[Unset, float] = UNSET
    tur: Union[Unset, float] = UNSET
    mex: Union[Unset, float] = UNSET
    che: Union[Unset, float] = UNSET
    nor: Union[Unset, float] = UNSET
    are: Union[Unset, float] = UNSET
    swe: Union[Unset, float] = UNSET
    pol: Union[Unset, float] = UNSET
    idn: Union[Unset, float] = UNSET
    arg: Union[Unset, float] = UNSET
    prt: Union[Unset, float] = UNSET
    col: Union[Unset, float] = UNSET
    chl: Union[Unset, float] = UNSET
    pak: Union[Unset, float] = UNSET
    dnk: Union[Unset, float] = UNSET
    jpn: Union[Unset, float] = UNSET
    nga: Union[Unset, float] = UNSET
    sgp: Union[Unset, float] = UNSET
    per: Union[Unset, float] = UNSET
    nzl: Union[Unset, float] = UNSET
    aut: Union[Unset, float] = UNSET
    irl: Union[Unset, float] = UNSET
    mys: Union[Unset, float] = UNSET
    bgd: Union[Unset, float] = UNSET
    egy: Union[Unset, float] = UNSET
    isr: Union[Unset, float] = UNSET
    sau: Union[Unset, float] = UNSET
    phl: Union[Unset, float] = UNSET
    fin: Union[Unset, float] = UNSET
    irn: Union[Unset, float] = UNSET
    rou: Union[Unset, float] = UNSET
    cze: Union[Unset, float] = UNSET
    grc: Union[Unset, float] = UNSET
    hkg: Union[Unset, float] = UNSET
    hun: Union[Unset, float] = UNSET
    ken: Union[Unset, float] = UNSET
    mar: Union[Unset, float] = UNSET
    vnm: Union[Unset, float] = UNSET
    rus: Union[Unset, float] = UNSET
    ukr: Union[Unset, float] = UNSET
    ecu: Union[Unset, float] = UNSET
    tha: Union[Unset, float] = UNSET
    lka: Union[Unset, float] = UNSET
    kor: Union[Unset, float] = UNSET
    bgr: Union[Unset, float] = UNSET
    gha: Union[Unset, float] = UNSET
    srb: Union[Unset, float] = UNSET
    twn: Union[Unset, float] = UNSET
    hrv: Union[Unset, float] = UNSET
    ltu: Union[Unset, float] = UNSET
    pri: Union[Unset, float] = UNSET
    svk: Union[Unset, float] = UNSET
    tun: Union[Unset, float] = UNSET
    est: Union[Unset, float] = UNSET
    ven: Union[Unset, float] = UNSET
    cri: Union[Unset, float] = UNSET
    pan: Union[Unset, float] = UNSET
    ury: Union[Unset, float] = UNSET
    lbn: Union[Unset, float] = UNSET
    lux: Union[Unset, float] = UNSET
    cyp: Union[Unset, float] = UNSET
    npl: Union[Unset, float] = UNSET
    jor: Union[Unset, float] = UNSET
    svn: Union[Unset, float] = UNSET
    mtq: Union[Unset, float] = UNSET
    qat: Union[Unset, float] = UNSET
    glp: Union[Unset, float] = UNSET
    uga: Union[Unset, float] = UNSET
    dza: Union[Unset, float] = UNSET
    gtm: Union[Unset, float] = UNSET
    cmr: Union[Unset, float] = UNSET
    lva: Union[Unset, float] = UNSET
    dom: Union[Unset, float] = UNSET
    aze: Union[Unset, float] = UNSET
    geo: Union[Unset, float] = UNSET
    sen: Union[Unset, float] = UNSET
    tza: Union[Unset, float] = UNSET
    zwe: Union[Unset, float] = UNSET
    kwt: Union[Unset, float] = UNSET
    mlt: Union[Unset, float] = UNSET
    omn: Union[Unset, float] = UNSET
    bol: Union[Unset, float] = UNSET
    slv: Union[Unset, float] = UNSET
    arm: Union[Unset, float] = UNSET
    pry: Union[Unset, float] = UNSET
    irq: Union[Unset, float] = UNSET
    khm: Union[Unset, float] = UNSET
    bih: Union[Unset, float] = UNSET
    ago: Union[Unset, float] = UNSET
    bhr: Union[Unset, float] = UNSET
    alb: Union[Unset, float] = UNSET
    kaz: Union[Unset, float] = UNSET
    civ: Union[Unset, float] = UNSET
    eth: Union[Unset, float] = UNSET
    mus: Union[Unset, float] = UNSET
    zmb: Union[Unset, float] = UNSET
    mkd: Union[Unset, float] = UNSET
    cod: Union[Unset, float] = UNSET
    blr: Union[Unset, float] = UNSET
    moz: Union[Unset, float] = UNSET
    reu: Union[Unset, float] = UNSET
    tto: Union[Unset, float] = UNSET
    guf: Union[Unset, float] = UNSET
    isl: Union[Unset, float] = UNSET
    mmr: Union[Unset, float] = UNSET
    hnd: Union[Unset, float] = UNSET
    rwa: Union[Unset, float] = UNSET
    mdg: Union[Unset, float] = UNSET
    ben: Union[Unset, float] = UNSET
    uzb: Union[Unset, float] = UNSET
    nam: Union[Unset, float] = UNSET
    bwa: Union[Unset, float] = UNSET
    mda: Union[Unset, float] = UNSET
    jey: Union[Unset, float] = UNSET
    nic: Union[Unset, float] = UNSET
    sdn: Union[Unset, float] = UNSET
    jam: Union[Unset, float] = UNSET
    imn: Union[Unset, float] = UNSET
    bfa: Union[Unset, float] = UNSET
    mng: Union[Unset, float] = UNSET
    mne: Union[Unset, float] = UNSET
    mco: Union[Unset, float] = UNSET
    tgo: Union[Unset, float] = UNSET
    afg: Union[Unset, float] = UNSET
    lby: Union[Unset, float] = UNSET
    xkx: Union[Unset, float] = UNSET
    cym: Union[Unset, float] = UNSET
    mwi: Union[Unset, float] = UNSET
    som: Union[Unset, float] = UNSET
    png: Union[Unset, float] = UNSET
    mdv: Union[Unset, float] = UNSET
    mli: Union[Unset, float] = UNSET
    gin: Union[Unset, float] = UNSET
    pse: Union[Unset, float] = UNSET
    gab: Union[Unset, float] = UNSET
    lie: Union[Unset, float] = UNSET
    hti: Union[Unset, float] = UNSET
    syr: Union[Unset, float] = UNSET
    brb: Union[Unset, float] = UNSET
    yem: Union[Unset, float] = UNSET
    ggy: Union[Unset, float] = UNSET
    ncl: Union[Unset, float] = UNSET
    and_: Union[Unset, float] = UNSET
    sur: Union[Unset, float] = UNSET
    myt: Union[Unset, float] = UNSET
    kgz: Union[Unset, float] = UNSET
    bhs: Union[Unset, float] = UNSET
    gib: Union[Unset, float] = UNSET
    cog: Union[Unset, float] = UNSET
    fji: Union[Unset, float] = UNSET
    blm: Union[Unset, float] = UNSET
    cuw: Union[Unset, float] = UNSET
    cub: Union[Unset, float] = UNSET
    sle: Union[Unset, float] = UNSET
    blz: Union[Unset, float] = UNSET
    ner: Union[Unset, float] = UNSET
    lbr: Union[Unset, float] = UNSET
    vir: Union[Unset, float] = UNSET
    pyf: Union[Unset, float] = UNSET
    gum: Union[Unset, float] = UNSET
    mrt: Union[Unset, float] = UNSET
    abw: Union[Unset, float] = UNSET
    syc: Union[Unset, float] = UNSET
    guy: Union[Unset, float] = UNSET
    lso: Union[Unset, float] = UNSET
    swz: Union[Unset, float] = UNSET
    ssd: Union[Unset, float] = UNSET
    lca: Union[Unset, float] = UNSET
    mac: Union[Unset, float] = UNSET
    smr: Union[Unset, float] = UNSET
    lao: Union[Unset, float] = UNSET
    brn: Union[Unset, float] = UNSET
    tcd: Union[Unset, float] = UNSET
    bmu: Union[Unset, float] = UNSET
    vgb: Union[Unset, float] = UNSET
    prk: Union[Unset, float] = UNSET
    btn: Union[Unset, float] = UNSET
    bdi: Union[Unset, float] = UNSET
    fro: Union[Unset, float] = UNSET
    tjk: Union[Unset, float] = UNSET
    gmb: Union[Unset, float] = UNSET
    stp: Union[Unset, float] = UNSET
    ant: Union[Unset, float] = UNSET
    vct: Union[Unset, float] = UNSET
    dji: Union[Unset, float] = UNSET
    cpv: Union[Unset, float] = UNSET
    tkm: Union[Unset, float] = UNSET
    atg: Union[Unset, float] = UNSET
    tca: Union[Unset, float] = UNSET
    kna: Union[Unset, float] = UNSET
    grd: Union[Unset, float] = UNSET
    asm: Union[Unset, float] = UNSET
    vut: Union[Unset, float] = UNSET
    gnq: Union[Unset, float] = UNSET
    grl: Union[Unset, float] = UNSET
    sxm: Union[Unset, float] = UNSET
    mnp: Union[Unset, float] = UNSET
    com: Union[Unset, float] = UNSET
    tls: Union[Unset, float] = UNSET
    sjm: Union[Unset, float] = UNSET
    caf: Union[Unset, float] = UNSET
    dma: Union[Unset, float] = UNSET
    maf: Union[Unset, float] = UNSET
    wsm: Union[Unset, float] = UNSET
    bes: Union[Unset, float] = UNSET
    mhl: Union[Unset, float] = UNSET
    aia: Union[Unset, float] = UNSET
    ton: Union[Unset, float] = UNSET
    cok: Union[Unset, float] = UNSET
    slb: Union[Unset, float] = UNSET
    spm: Union[Unset, float] = UNSET
    gnb: Union[Unset, float] = UNSET
    ata: Union[Unset, float] = UNSET
    tuv: Union[Unset, float] = UNSET
    ala: Union[Unset, float] = UNSET
    iot: Union[Unset, float] = UNSET
    eri: Union[Unset, float] = UNSET
    plw: Union[Unset, float] = UNSET
    fsm: Union[Unset, float] = UNSET
    nru: Union[Unset, float] = UNSET
    pcn: Union[Unset, float] = UNSET
    flk: Union[Unset, float] = UNSET
    msr: Union[Unset, float] = UNSET
    vat: Union[Unset, float] = UNSET
    kir: Union[Unset, float] = UNSET
    shn: Union[Unset, float] = UNSET
    niu: Union[Unset, float] = UNSET
    wlf: Union[Unset, float] = UNSET
    hmd: Union[Unset, float] = UNSET
    cxr: Union[Unset, float] = UNSET
    nfk: Union[Unset, float] = UNSET
    atf: Union[Unset, float] = UNSET
    cck: Union[Unset, float] = UNSET
    sgs: Union[Unset, float] = UNSET
    bvt: Union[Unset, float] = UNSET
    umi: Union[Unset, float] = UNSET
    esh: Union[Unset, float] = UNSET
    tkl: Union[Unset, float] = UNSET
    x_south_asia: Union[Unset, float] = UNSET
    x_south_east_europe: Union[Unset, float] = UNSET
    x_northern_africa: Union[Unset, float] = UNSET
    x_pacific: Union[Unset, float] = UNSET
    x_south_west_europe: Union[Unset, float] = UNSET
    x_southern_africa: Union[Unset, float] = UNSET
    x_west_indies: Union[Unset, float] = UNSET
    x_south_america: Union[Unset, float] = UNSET
    x_south_west_asia: Union[Unset, float] = UNSET
    x_central_europe: Union[Unset, float] = UNSET
    x_eastern_europe: Union[Unset, float] = UNSET
    x_western_europe: Union[Unset, float] = UNSET
    x_central_america: Union[Unset, float] = UNSET
    x_western_africa: Union[Unset, float] = UNSET
    x_south_atlantic_ocean: Union[Unset, float] = UNSET
    x_south_east_asia: Union[Unset, float] = UNSET
    x_central_africa: Union[Unset, float] = UNSET
    x_north_america: Union[Unset, float] = UNSET
    x_east_asia: Union[Unset, float] = UNSET
    x_northern_europe: Union[Unset, float] = UNSET
    x_eastern_africa: Union[Unset, float] = UNSET
    x_southern_indian_ocean: Union[Unset, float] = UNSET
    x_southern_europe: Union[Unset, float] = UNSET
    x_central_asia: Union[Unset, float] = UNSET
    x_northern_asia: Union[Unset, float] = UNSET
    x_asia: Union[Unset, float] = UNSET
    x_europe: Union[Unset, float] = UNSET
    x_africa: Union[Unset, float] = UNSET
    x_oceania: Union[Unset, float] = UNSET
    x_americas: Union[Unset, float] = UNSET
    x_antarctica: Union[Unset, float] = UNSET
    x_atlantic_ocean: Union[Unset, float] = UNSET
    x_indian_ocean: Union[Unset, float] = UNSET
    x_middle_east: Union[Unset, float] = UNSET
    x_mena: Union[Unset, float] = UNSET
    x_emea: Union[Unset, float] = UNSET
    x_european_union: Union[Unset, float] = UNSET
    x_efta: Union[Unset, float] = UNSET
    x_apac: Union[Unset, float] = UNSET
    x_latam: Union[Unset, float] = UNSET
    x_anglosphere: Union[Unset, float] = UNSET
    x_dach: Union[Unset, float] = UNSET
    x_nordics: Union[Unset, float] = UNSET
    x_benelux: Union[Unset, float] = UNSET
    x_gcc: Union[Unset, float] = UNSET
    x_brics: Union[Unset, float] = UNSET
    x_g20: Union[Unset, float] = UNSET
    x_oecd: Union[Unset, float] = UNSET
    x_sanctioned: Union[Unset, float] = UNSET





    def to_dict(self) -> dict[str, Any]:
        usa = self.usa

        gbr = self.gbr

        fra = self.fra

        ind = self.ind

        bra = self.bra

        deu = self.deu

        esp = self.esp

        can = self.can

        aus = self.aus

        nld = self.nld

        ita = self.ita

        zaf = self.zaf

        bel = self.bel

        chn = self.chn

        tur = self.tur

        mex = self.mex

        che = self.che

        nor = self.nor

        are = self.are

        swe = self.swe

        pol = self.pol

        idn = self.idn

        arg = self.arg

        prt = self.prt

        col = self.col

        chl = self.chl

        pak = self.pak

        dnk = self.dnk

        jpn = self.jpn

        nga = self.nga

        sgp = self.sgp

        per = self.per

        nzl = self.nzl

        aut = self.aut

        irl = self.irl

        mys = self.mys

        bgd = self.bgd

        egy = self.egy

        isr = self.isr

        sau = self.sau

        phl = self.phl

        fin = self.fin

        irn = self.irn

        rou = self.rou

        cze = self.cze

        grc = self.grc

        hkg = self.hkg

        hun = self.hun

        ken = self.ken

        mar = self.mar

        vnm = self.vnm

        rus = self.rus

        ukr = self.ukr

        ecu = self.ecu

        tha = self.tha

        lka = self.lka

        kor = self.kor

        bgr = self.bgr

        gha = self.gha

        srb = self.srb

        twn = self.twn

        hrv = self.hrv

        ltu = self.ltu

        pri = self.pri

        svk = self.svk

        tun = self.tun

        est = self.est

        ven = self.ven

        cri = self.cri

        pan = self.pan

        ury = self.ury

        lbn = self.lbn

        lux = self.lux

        cyp = self.cyp

        npl = self.npl

        jor = self.jor

        svn = self.svn

        mtq = self.mtq

        qat = self.qat

        glp = self.glp

        uga = self.uga

        dza = self.dza

        gtm = self.gtm

        cmr = self.cmr

        lva = self.lva

        dom = self.dom

        aze = self.aze

        geo = self.geo

        sen = self.sen

        tza = self.tza

        zwe = self.zwe

        kwt = self.kwt

        mlt = self.mlt

        omn = self.omn

        bol = self.bol

        slv = self.slv

        arm = self.arm

        pry = self.pry

        irq = self.irq

        khm = self.khm

        bih = self.bih

        ago = self.ago

        bhr = self.bhr

        alb = self.alb

        kaz = self.kaz

        civ = self.civ

        eth = self.eth

        mus = self.mus

        zmb = self.zmb

        mkd = self.mkd

        cod = self.cod

        blr = self.blr

        moz = self.moz

        reu = self.reu

        tto = self.tto

        guf = self.guf

        isl = self.isl

        mmr = self.mmr

        hnd = self.hnd

        rwa = self.rwa

        mdg = self.mdg

        ben = self.ben

        uzb = self.uzb

        nam = self.nam

        bwa = self.bwa

        mda = self.mda

        jey = self.jey

        nic = self.nic

        sdn = self.sdn

        jam = self.jam

        imn = self.imn

        bfa = self.bfa

        mng = self.mng

        mne = self.mne

        mco = self.mco

        tgo = self.tgo

        afg = self.afg

        lby = self.lby

        xkx = self.xkx

        cym = self.cym

        mwi = self.mwi

        som = self.som

        png = self.png

        mdv = self.mdv

        mli = self.mli

        gin = self.gin

        pse = self.pse

        gab = self.gab

        lie = self.lie

        hti = self.hti

        syr = self.syr

        brb = self.brb

        yem = self.yem

        ggy = self.ggy

        ncl = self.ncl

        and_ = self.and_

        sur = self.sur

        myt = self.myt

        kgz = self.kgz

        bhs = self.bhs

        gib = self.gib

        cog = self.cog

        fji = self.fji

        blm = self.blm

        cuw = self.cuw

        cub = self.cub

        sle = self.sle

        blz = self.blz

        ner = self.ner

        lbr = self.lbr

        vir = self.vir

        pyf = self.pyf

        gum = self.gum

        mrt = self.mrt

        abw = self.abw

        syc = self.syc

        guy = self.guy

        lso = self.lso

        swz = self.swz

        ssd = self.ssd

        lca = self.lca

        mac = self.mac

        smr = self.smr

        lao = self.lao

        brn = self.brn

        tcd = self.tcd

        bmu = self.bmu

        vgb = self.vgb

        prk = self.prk

        btn = self.btn

        bdi = self.bdi

        fro = self.fro

        tjk = self.tjk

        gmb = self.gmb

        stp = self.stp

        ant = self.ant

        vct = self.vct

        dji = self.dji

        cpv = self.cpv

        tkm = self.tkm

        atg = self.atg

        tca = self.tca

        kna = self.kna

        grd = self.grd

        asm = self.asm

        vut = self.vut

        gnq = self.gnq

        grl = self.grl

        sxm = self.sxm

        mnp = self.mnp

        com = self.com

        tls = self.tls

        sjm = self.sjm

        caf = self.caf

        dma = self.dma

        maf = self.maf

        wsm = self.wsm

        bes = self.bes

        mhl = self.mhl

        aia = self.aia

        ton = self.ton

        cok = self.cok

        slb = self.slb

        spm = self.spm

        gnb = self.gnb

        ata = self.ata

        tuv = self.tuv

        ala = self.ala

        iot = self.iot

        eri = self.eri

        plw = self.plw

        fsm = self.fsm

        nru = self.nru

        pcn = self.pcn

        flk = self.flk

        msr = self.msr

        vat = self.vat

        kir = self.kir

        shn = self.shn

        niu = self.niu

        wlf = self.wlf

        hmd = self.hmd

        cxr = self.cxr

        nfk = self.nfk

        atf = self.atf

        cck = self.cck

        sgs = self.sgs

        bvt = self.bvt

        umi = self.umi

        esh = self.esh

        tkl = self.tkl

        x_south_asia = self.x_south_asia

        x_south_east_europe = self.x_south_east_europe

        x_northern_africa = self.x_northern_africa

        x_pacific = self.x_pacific

        x_south_west_europe = self.x_south_west_europe

        x_southern_africa = self.x_southern_africa

        x_west_indies = self.x_west_indies

        x_south_america = self.x_south_america

        x_south_west_asia = self.x_south_west_asia

        x_central_europe = self.x_central_europe

        x_eastern_europe = self.x_eastern_europe

        x_western_europe = self.x_western_europe

        x_central_america = self.x_central_america

        x_western_africa = self.x_western_africa

        x_south_atlantic_ocean = self.x_south_atlantic_ocean

        x_south_east_asia = self.x_south_east_asia

        x_central_africa = self.x_central_africa

        x_north_america = self.x_north_america

        x_east_asia = self.x_east_asia

        x_northern_europe = self.x_northern_europe

        x_eastern_africa = self.x_eastern_africa

        x_southern_indian_ocean = self.x_southern_indian_ocean

        x_southern_europe = self.x_southern_europe

        x_central_asia = self.x_central_asia

        x_northern_asia = self.x_northern_asia

        x_asia = self.x_asia

        x_europe = self.x_europe

        x_africa = self.x_africa

        x_oceania = self.x_oceania

        x_americas = self.x_americas

        x_antarctica = self.x_antarctica

        x_atlantic_ocean = self.x_atlantic_ocean

        x_indian_ocean = self.x_indian_ocean

        x_middle_east = self.x_middle_east

        x_mena = self.x_mena

        x_emea = self.x_emea

        x_european_union = self.x_european_union

        x_efta = self.x_efta

        x_apac = self.x_apac

        x_latam = self.x_latam

        x_anglosphere = self.x_anglosphere

        x_dach = self.x_dach

        x_nordics = self.x_nordics

        x_benelux = self.x_benelux

        x_gcc = self.x_gcc

        x_brics = self.x_brics

        x_g20 = self.x_g20

        x_oecd = self.x_oecd

        x_sanctioned = self.x_sanctioned


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if usa is not UNSET:
            field_dict["USA"] = usa
        if gbr is not UNSET:
            field_dict["GBR"] = gbr
        if fra is not UNSET:
            field_dict["FRA"] = fra
        if ind is not UNSET:
            field_dict["IND"] = ind
        if bra is not UNSET:
            field_dict["BRA"] = bra
        if deu is not UNSET:
            field_dict["DEU"] = deu
        if esp is not UNSET:
            field_dict["ESP"] = esp
        if can is not UNSET:
            field_dict["CAN"] = can
        if aus is not UNSET:
            field_dict["AUS"] = aus
        if nld is not UNSET:
            field_dict["NLD"] = nld
        if ita is not UNSET:
            field_dict["ITA"] = ita
        if zaf is not UNSET:
            field_dict["ZAF"] = zaf
        if bel is not UNSET:
            field_dict["BEL"] = bel
        if chn is not UNSET:
            field_dict["CHN"] = chn
        if tur is not UNSET:
            field_dict["TUR"] = tur
        if mex is not UNSET:
            field_dict["MEX"] = mex
        if che is not UNSET:
            field_dict["CHE"] = che
        if nor is not UNSET:
            field_dict["NOR"] = nor
        if are is not UNSET:
            field_dict["ARE"] = are
        if swe is not UNSET:
            field_dict["SWE"] = swe
        if pol is not UNSET:
            field_dict["POL"] = pol
        if idn is not UNSET:
            field_dict["IDN"] = idn
        if arg is not UNSET:
            field_dict["ARG"] = arg
        if prt is not UNSET:
            field_dict["PRT"] = prt
        if col is not UNSET:
            field_dict["COL"] = col
        if chl is not UNSET:
            field_dict["CHL"] = chl
        if pak is not UNSET:
            field_dict["PAK"] = pak
        if dnk is not UNSET:
            field_dict["DNK"] = dnk
        if jpn is not UNSET:
            field_dict["JPN"] = jpn
        if nga is not UNSET:
            field_dict["NGA"] = nga
        if sgp is not UNSET:
            field_dict["SGP"] = sgp
        if per is not UNSET:
            field_dict["PER"] = per
        if nzl is not UNSET:
            field_dict["NZL"] = nzl
        if aut is not UNSET:
            field_dict["AUT"] = aut
        if irl is not UNSET:
            field_dict["IRL"] = irl
        if mys is not UNSET:
            field_dict["MYS"] = mys
        if bgd is not UNSET:
            field_dict["BGD"] = bgd
        if egy is not UNSET:
            field_dict["EGY"] = egy
        if isr is not UNSET:
            field_dict["ISR"] = isr
        if sau is not UNSET:
            field_dict["SAU"] = sau
        if phl is not UNSET:
            field_dict["PHL"] = phl
        if fin is not UNSET:
            field_dict["FIN"] = fin
        if irn is not UNSET:
            field_dict["IRN"] = irn
        if rou is not UNSET:
            field_dict["ROU"] = rou
        if cze is not UNSET:
            field_dict["CZE"] = cze
        if grc is not UNSET:
            field_dict["GRC"] = grc
        if hkg is not UNSET:
            field_dict["HKG"] = hkg
        if hun is not UNSET:
            field_dict["HUN"] = hun
        if ken is not UNSET:
            field_dict["KEN"] = ken
        if mar is not UNSET:
            field_dict["MAR"] = mar
        if vnm is not UNSET:
            field_dict["VNM"] = vnm
        if rus is not UNSET:
            field_dict["RUS"] = rus
        if ukr is not UNSET:
            field_dict["UKR"] = ukr
        if ecu is not UNSET:
            field_dict["ECU"] = ecu
        if tha is not UNSET:
            field_dict["THA"] = tha
        if lka is not UNSET:
            field_dict["LKA"] = lka
        if kor is not UNSET:
            field_dict["KOR"] = kor
        if bgr is not UNSET:
            field_dict["BGR"] = bgr
        if gha is not UNSET:
            field_dict["GHA"] = gha
        if srb is not UNSET:
            field_dict["SRB"] = srb
        if twn is not UNSET:
            field_dict["TWN"] = twn
        if hrv is not UNSET:
            field_dict["HRV"] = hrv
        if ltu is not UNSET:
            field_dict["LTU"] = ltu
        if pri is not UNSET:
            field_dict["PRI"] = pri
        if svk is not UNSET:
            field_dict["SVK"] = svk
        if tun is not UNSET:
            field_dict["TUN"] = tun
        if est is not UNSET:
            field_dict["EST"] = est
        if ven is not UNSET:
            field_dict["VEN"] = ven
        if cri is not UNSET:
            field_dict["CRI"] = cri
        if pan is not UNSET:
            field_dict["PAN"] = pan
        if ury is not UNSET:
            field_dict["URY"] = ury
        if lbn is not UNSET:
            field_dict["LBN"] = lbn
        if lux is not UNSET:
            field_dict["LUX"] = lux
        if cyp is not UNSET:
            field_dict["CYP"] = cyp
        if npl is not UNSET:
            field_dict["NPL"] = npl
        if jor is not UNSET:
            field_dict["JOR"] = jor
        if svn is not UNSET:
            field_dict["SVN"] = svn
        if mtq is not UNSET:
            field_dict["MTQ"] = mtq
        if qat is not UNSET:
            field_dict["QAT"] = qat
        if glp is not UNSET:
            field_dict["GLP"] = glp
        if uga is not UNSET:
            field_dict["UGA"] = uga
        if dza is not UNSET:
            field_dict["DZA"] = dza
        if gtm is not UNSET:
            field_dict["GTM"] = gtm
        if cmr is not UNSET:
            field_dict["CMR"] = cmr
        if lva is not UNSET:
            field_dict["LVA"] = lva
        if dom is not UNSET:
            field_dict["DOM"] = dom
        if aze is not UNSET:
            field_dict["AZE"] = aze
        if geo is not UNSET:
            field_dict["GEO"] = geo
        if sen is not UNSET:
            field_dict["SEN"] = sen
        if tza is not UNSET:
            field_dict["TZA"] = tza
        if zwe is not UNSET:
            field_dict["ZWE"] = zwe
        if kwt is not UNSET:
            field_dict["KWT"] = kwt
        if mlt is not UNSET:
            field_dict["MLT"] = mlt
        if omn is not UNSET:
            field_dict["OMN"] = omn
        if bol is not UNSET:
            field_dict["BOL"] = bol
        if slv is not UNSET:
            field_dict["SLV"] = slv
        if arm is not UNSET:
            field_dict["ARM"] = arm
        if pry is not UNSET:
            field_dict["PRY"] = pry
        if irq is not UNSET:
            field_dict["IRQ"] = irq
        if khm is not UNSET:
            field_dict["KHM"] = khm
        if bih is not UNSET:
            field_dict["BIH"] = bih
        if ago is not UNSET:
            field_dict["AGO"] = ago
        if bhr is not UNSET:
            field_dict["BHR"] = bhr
        if alb is not UNSET:
            field_dict["ALB"] = alb
        if kaz is not UNSET:
            field_dict["KAZ"] = kaz
        if civ is not UNSET:
            field_dict["CIV"] = civ
        if eth is not UNSET:
            field_dict["ETH"] = eth
        if mus is not UNSET:
            field_dict["MUS"] = mus
        if zmb is not UNSET:
            field_dict["ZMB"] = zmb
        if mkd is not UNSET:
            field_dict["MKD"] = mkd
        if cod is not UNSET:
            field_dict["COD"] = cod
        if blr is not UNSET:
            field_dict["BLR"] = blr
        if moz is not UNSET:
            field_dict["MOZ"] = moz
        if reu is not UNSET:
            field_dict["REU"] = reu
        if tto is not UNSET:
            field_dict["TTO"] = tto
        if guf is not UNSET:
            field_dict["GUF"] = guf
        if isl is not UNSET:
            field_dict["ISL"] = isl
        if mmr is not UNSET:
            field_dict["MMR"] = mmr
        if hnd is not UNSET:
            field_dict["HND"] = hnd
        if rwa is not UNSET:
            field_dict["RWA"] = rwa
        if mdg is not UNSET:
            field_dict["MDG"] = mdg
        if ben is not UNSET:
            field_dict["BEN"] = ben
        if uzb is not UNSET:
            field_dict["UZB"] = uzb
        if nam is not UNSET:
            field_dict["NAM"] = nam
        if bwa is not UNSET:
            field_dict["BWA"] = bwa
        if mda is not UNSET:
            field_dict["MDA"] = mda
        if jey is not UNSET:
            field_dict["JEY"] = jey
        if nic is not UNSET:
            field_dict["NIC"] = nic
        if sdn is not UNSET:
            field_dict["SDN"] = sdn
        if jam is not UNSET:
            field_dict["JAM"] = jam
        if imn is not UNSET:
            field_dict["IMN"] = imn
        if bfa is not UNSET:
            field_dict["BFA"] = bfa
        if mng is not UNSET:
            field_dict["MNG"] = mng
        if mne is not UNSET:
            field_dict["MNE"] = mne
        if mco is not UNSET:
            field_dict["MCO"] = mco
        if tgo is not UNSET:
            field_dict["TGO"] = tgo
        if afg is not UNSET:
            field_dict["AFG"] = afg
        if lby is not UNSET:
            field_dict["LBY"] = lby
        if xkx is not UNSET:
            field_dict["XKX"] = xkx
        if cym is not UNSET:
            field_dict["CYM"] = cym
        if mwi is not UNSET:
            field_dict["MWI"] = mwi
        if som is not UNSET:
            field_dict["SOM"] = som
        if png is not UNSET:
            field_dict["PNG"] = png
        if mdv is not UNSET:
            field_dict["MDV"] = mdv
        if mli is not UNSET:
            field_dict["MLI"] = mli
        if gin is not UNSET:
            field_dict["GIN"] = gin
        if pse is not UNSET:
            field_dict["PSE"] = pse
        if gab is not UNSET:
            field_dict["GAB"] = gab
        if lie is not UNSET:
            field_dict["LIE"] = lie
        if hti is not UNSET:
            field_dict["HTI"] = hti
        if syr is not UNSET:
            field_dict["SYR"] = syr
        if brb is not UNSET:
            field_dict["BRB"] = brb
        if yem is not UNSET:
            field_dict["YEM"] = yem
        if ggy is not UNSET:
            field_dict["GGY"] = ggy
        if ncl is not UNSET:
            field_dict["NCL"] = ncl
        if and_ is not UNSET:
            field_dict["AND"] = and_
        if sur is not UNSET:
            field_dict["SUR"] = sur
        if myt is not UNSET:
            field_dict["MYT"] = myt
        if kgz is not UNSET:
            field_dict["KGZ"] = kgz
        if bhs is not UNSET:
            field_dict["BHS"] = bhs
        if gib is not UNSET:
            field_dict["GIB"] = gib
        if cog is not UNSET:
            field_dict["COG"] = cog
        if fji is not UNSET:
            field_dict["FJI"] = fji
        if blm is not UNSET:
            field_dict["BLM"] = blm
        if cuw is not UNSET:
            field_dict["CUW"] = cuw
        if cub is not UNSET:
            field_dict["CUB"] = cub
        if sle is not UNSET:
            field_dict["SLE"] = sle
        if blz is not UNSET:
            field_dict["BLZ"] = blz
        if ner is not UNSET:
            field_dict["NER"] = ner
        if lbr is not UNSET:
            field_dict["LBR"] = lbr
        if vir is not UNSET:
            field_dict["VIR"] = vir
        if pyf is not UNSET:
            field_dict["PYF"] = pyf
        if gum is not UNSET:
            field_dict["GUM"] = gum
        if mrt is not UNSET:
            field_dict["MRT"] = mrt
        if abw is not UNSET:
            field_dict["ABW"] = abw
        if syc is not UNSET:
            field_dict["SYC"] = syc
        if guy is not UNSET:
            field_dict["GUY"] = guy
        if lso is not UNSET:
            field_dict["LSO"] = lso
        if swz is not UNSET:
            field_dict["SWZ"] = swz
        if ssd is not UNSET:
            field_dict["SSD"] = ssd
        if lca is not UNSET:
            field_dict["LCA"] = lca
        if mac is not UNSET:
            field_dict["MAC"] = mac
        if smr is not UNSET:
            field_dict["SMR"] = smr
        if lao is not UNSET:
            field_dict["LAO"] = lao
        if brn is not UNSET:
            field_dict["BRN"] = brn
        if tcd is not UNSET:
            field_dict["TCD"] = tcd
        if bmu is not UNSET:
            field_dict["BMU"] = bmu
        if vgb is not UNSET:
            field_dict["VGB"] = vgb
        if prk is not UNSET:
            field_dict["PRK"] = prk
        if btn is not UNSET:
            field_dict["BTN"] = btn
        if bdi is not UNSET:
            field_dict["BDI"] = bdi
        if fro is not UNSET:
            field_dict["FRO"] = fro
        if tjk is not UNSET:
            field_dict["TJK"] = tjk
        if gmb is not UNSET:
            field_dict["GMB"] = gmb
        if stp is not UNSET:
            field_dict["STP"] = stp
        if ant is not UNSET:
            field_dict["ANT"] = ant
        if vct is not UNSET:
            field_dict["VCT"] = vct
        if dji is not UNSET:
            field_dict["DJI"] = dji
        if cpv is not UNSET:
            field_dict["CPV"] = cpv
        if tkm is not UNSET:
            field_dict["TKM"] = tkm
        if atg is not UNSET:
            field_dict["ATG"] = atg
        if tca is not UNSET:
            field_dict["TCA"] = tca
        if kna is not UNSET:
            field_dict["KNA"] = kna
        if grd is not UNSET:
            field_dict["GRD"] = grd
        if asm is not UNSET:
            field_dict["ASM"] = asm
        if vut is not UNSET:
            field_dict["VUT"] = vut
        if gnq is not UNSET:
            field_dict["GNQ"] = gnq
        if grl is not UNSET:
            field_dict["GRL"] = grl
        if sxm is not UNSET:
            field_dict["SXM"] = sxm
        if mnp is not UNSET:
            field_dict["MNP"] = mnp
        if com is not UNSET:
            field_dict["COM"] = com
        if tls is not UNSET:
            field_dict["TLS"] = tls
        if sjm is not UNSET:
            field_dict["SJM"] = sjm
        if caf is not UNSET:
            field_dict["CAF"] = caf
        if dma is not UNSET:
            field_dict["DMA"] = dma
        if maf is not UNSET:
            field_dict["MAF"] = maf
        if wsm is not UNSET:
            field_dict["WSM"] = wsm
        if bes is not UNSET:
            field_dict["BES"] = bes
        if mhl is not UNSET:
            field_dict["MHL"] = mhl
        if aia is not UNSET:
            field_dict["AIA"] = aia
        if ton is not UNSET:
            field_dict["TON"] = ton
        if cok is not UNSET:
            field_dict["COK"] = cok
        if slb is not UNSET:
            field_dict["SLB"] = slb
        if spm is not UNSET:
            field_dict["SPM"] = spm
        if gnb is not UNSET:
            field_dict["GNB"] = gnb
        if ata is not UNSET:
            field_dict["ATA"] = ata
        if tuv is not UNSET:
            field_dict["TUV"] = tuv
        if ala is not UNSET:
            field_dict["ALA"] = ala
        if iot is not UNSET:
            field_dict["IOT"] = iot
        if eri is not UNSET:
            field_dict["ERI"] = eri
        if plw is not UNSET:
            field_dict["PLW"] = plw
        if fsm is not UNSET:
            field_dict["FSM"] = fsm
        if nru is not UNSET:
            field_dict["NRU"] = nru
        if pcn is not UNSET:
            field_dict["PCN"] = pcn
        if flk is not UNSET:
            field_dict["FLK"] = flk
        if msr is not UNSET:
            field_dict["MSR"] = msr
        if vat is not UNSET:
            field_dict["VAT"] = vat
        if kir is not UNSET:
            field_dict["KIR"] = kir
        if shn is not UNSET:
            field_dict["SHN"] = shn
        if niu is not UNSET:
            field_dict["NIU"] = niu
        if wlf is not UNSET:
            field_dict["WLF"] = wlf
        if hmd is not UNSET:
            field_dict["HMD"] = hmd
        if cxr is not UNSET:
            field_dict["CXR"] = cxr
        if nfk is not UNSET:
            field_dict["NFK"] = nfk
        if atf is not UNSET:
            field_dict["ATF"] = atf
        if cck is not UNSET:
            field_dict["CCK"] = cck
        if sgs is not UNSET:
            field_dict["SGS"] = sgs
        if bvt is not UNSET:
            field_dict["BVT"] = bvt
        if umi is not UNSET:
            field_dict["UMI"] = umi
        if esh is not UNSET:
            field_dict["ESH"] = esh
        if tkl is not UNSET:
            field_dict["TKL"] = tkl
        if x_south_asia is not UNSET:
            field_dict["X-SOUTH_ASIA"] = x_south_asia
        if x_south_east_europe is not UNSET:
            field_dict["X-SOUTH_EAST_EUROPE"] = x_south_east_europe
        if x_northern_africa is not UNSET:
            field_dict["X-NORTHERN_AFRICA"] = x_northern_africa
        if x_pacific is not UNSET:
            field_dict["X-PACIFIC"] = x_pacific
        if x_south_west_europe is not UNSET:
            field_dict["X-SOUTH_WEST_EUROPE"] = x_south_west_europe
        if x_southern_africa is not UNSET:
            field_dict["X-SOUTHERN_AFRICA"] = x_southern_africa
        if x_west_indies is not UNSET:
            field_dict["X-WEST_INDIES"] = x_west_indies
        if x_south_america is not UNSET:
            field_dict["X-SOUTH_AMERICA"] = x_south_america
        if x_south_west_asia is not UNSET:
            field_dict["X-SOUTH_WEST_ASIA"] = x_south_west_asia
        if x_central_europe is not UNSET:
            field_dict["X-CENTRAL_EUROPE"] = x_central_europe
        if x_eastern_europe is not UNSET:
            field_dict["X-EASTERN_EUROPE"] = x_eastern_europe
        if x_western_europe is not UNSET:
            field_dict["X-WESTERN_EUROPE"] = x_western_europe
        if x_central_america is not UNSET:
            field_dict["X-CENTRAL_AMERICA"] = x_central_america
        if x_western_africa is not UNSET:
            field_dict["X-WESTERN_AFRICA"] = x_western_africa
        if x_south_atlantic_ocean is not UNSET:
            field_dict["X-SOUTH_ATLANTIC_OCEAN"] = x_south_atlantic_ocean
        if x_south_east_asia is not UNSET:
            field_dict["X-SOUTH_EAST_ASIA"] = x_south_east_asia
        if x_central_africa is not UNSET:
            field_dict["X-CENTRAL_AFRICA"] = x_central_africa
        if x_north_america is not UNSET:
            field_dict["X-NORTH_AMERICA"] = x_north_america
        if x_east_asia is not UNSET:
            field_dict["X-EAST_ASIA"] = x_east_asia
        if x_northern_europe is not UNSET:
            field_dict["X-NORTHERN_EUROPE"] = x_northern_europe
        if x_eastern_africa is not UNSET:
            field_dict["X-EASTERN_AFRICA"] = x_eastern_africa
        if x_southern_indian_ocean is not UNSET:
            field_dict["X-SOUTHERN_INDIAN_OCEAN"] = x_southern_indian_ocean
        if x_southern_europe is not UNSET:
            field_dict["X-SOUTHERN_EUROPE"] = x_southern_europe
        if x_central_asia is not UNSET:
            field_dict["X-CENTRAL_ASIA"] = x_central_asia
        if x_northern_asia is not UNSET:
            field_dict["X-NORTHERN_ASIA"] = x_northern_asia
        if x_asia is not UNSET:
            field_dict["X-ASIA"] = x_asia
        if x_europe is not UNSET:
            field_dict["X-EUROPE"] = x_europe
        if x_africa is not UNSET:
            field_dict["X-AFRICA"] = x_africa
        if x_oceania is not UNSET:
            field_dict["X-OCEANIA"] = x_oceania
        if x_americas is not UNSET:
            field_dict["X-AMERICAS"] = x_americas
        if x_antarctica is not UNSET:
            field_dict["X-ANTARCTICA"] = x_antarctica
        if x_atlantic_ocean is not UNSET:
            field_dict["X-ATLANTIC_OCEAN"] = x_atlantic_ocean
        if x_indian_ocean is not UNSET:
            field_dict["X-INDIAN_OCEAN"] = x_indian_ocean
        if x_middle_east is not UNSET:
            field_dict["X-MIDDLE_EAST"] = x_middle_east
        if x_mena is not UNSET:
            field_dict["X-MENA"] = x_mena
        if x_emea is not UNSET:
            field_dict["X-EMEA"] = x_emea
        if x_european_union is not UNSET:
            field_dict["X-EUROPEAN_UNION"] = x_european_union
        if x_efta is not UNSET:
            field_dict["X-EFTA"] = x_efta
        if x_apac is not UNSET:
            field_dict["X-APAC"] = x_apac
        if x_latam is not UNSET:
            field_dict["X-LATAM"] = x_latam
        if x_anglosphere is not UNSET:
            field_dict["X-ANGLOSPHERE"] = x_anglosphere
        if x_dach is not UNSET:
            field_dict["X-DACH"] = x_dach
        if x_nordics is not UNSET:
            field_dict["X-NORDICS"] = x_nordics
        if x_benelux is not UNSET:
            field_dict["X-BENELUX"] = x_benelux
        if x_gcc is not UNSET:
            field_dict["X-GCC"] = x_gcc
        if x_brics is not UNSET:
            field_dict["X-BRICS"] = x_brics
        if x_g20 is not UNSET:
            field_dict["X-G20"] = x_g20
        if x_oecd is not UNSET:
            field_dict["X-OECD"] = x_oecd
        if x_sanctioned is not UNSET:
            field_dict["X-SANCTIONED"] = x_sanctioned

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        usa = d.pop("USA", UNSET)

        gbr = d.pop("GBR", UNSET)

        fra = d.pop("FRA", UNSET)

        ind = d.pop("IND", UNSET)

        bra = d.pop("BRA", UNSET)

        deu = d.pop("DEU", UNSET)

        esp = d.pop("ESP", UNSET)

        can = d.pop("CAN", UNSET)

        aus = d.pop("AUS", UNSET)

        nld = d.pop("NLD", UNSET)

        ita = d.pop("ITA", UNSET)

        zaf = d.pop("ZAF", UNSET)

        bel = d.pop("BEL", UNSET)

        chn = d.pop("CHN", UNSET)

        tur = d.pop("TUR", UNSET)

        mex = d.pop("MEX", UNSET)

        che = d.pop("CHE", UNSET)

        nor = d.pop("NOR", UNSET)

        are = d.pop("ARE", UNSET)

        swe = d.pop("SWE", UNSET)

        pol = d.pop("POL", UNSET)

        idn = d.pop("IDN", UNSET)

        arg = d.pop("ARG", UNSET)

        prt = d.pop("PRT", UNSET)

        col = d.pop("COL", UNSET)

        chl = d.pop("CHL", UNSET)

        pak = d.pop("PAK", UNSET)

        dnk = d.pop("DNK", UNSET)

        jpn = d.pop("JPN", UNSET)

        nga = d.pop("NGA", UNSET)

        sgp = d.pop("SGP", UNSET)

        per = d.pop("PER", UNSET)

        nzl = d.pop("NZL", UNSET)

        aut = d.pop("AUT", UNSET)

        irl = d.pop("IRL", UNSET)

        mys = d.pop("MYS", UNSET)

        bgd = d.pop("BGD", UNSET)

        egy = d.pop("EGY", UNSET)

        isr = d.pop("ISR", UNSET)

        sau = d.pop("SAU", UNSET)

        phl = d.pop("PHL", UNSET)

        fin = d.pop("FIN", UNSET)

        irn = d.pop("IRN", UNSET)

        rou = d.pop("ROU", UNSET)

        cze = d.pop("CZE", UNSET)

        grc = d.pop("GRC", UNSET)

        hkg = d.pop("HKG", UNSET)

        hun = d.pop("HUN", UNSET)

        ken = d.pop("KEN", UNSET)

        mar = d.pop("MAR", UNSET)

        vnm = d.pop("VNM", UNSET)

        rus = d.pop("RUS", UNSET)

        ukr = d.pop("UKR", UNSET)

        ecu = d.pop("ECU", UNSET)

        tha = d.pop("THA", UNSET)

        lka = d.pop("LKA", UNSET)

        kor = d.pop("KOR", UNSET)

        bgr = d.pop("BGR", UNSET)

        gha = d.pop("GHA", UNSET)

        srb = d.pop("SRB", UNSET)

        twn = d.pop("TWN", UNSET)

        hrv = d.pop("HRV", UNSET)

        ltu = d.pop("LTU", UNSET)

        pri = d.pop("PRI", UNSET)

        svk = d.pop("SVK", UNSET)

        tun = d.pop("TUN", UNSET)

        est = d.pop("EST", UNSET)

        ven = d.pop("VEN", UNSET)

        cri = d.pop("CRI", UNSET)

        pan = d.pop("PAN", UNSET)

        ury = d.pop("URY", UNSET)

        lbn = d.pop("LBN", UNSET)

        lux = d.pop("LUX", UNSET)

        cyp = d.pop("CYP", UNSET)

        npl = d.pop("NPL", UNSET)

        jor = d.pop("JOR", UNSET)

        svn = d.pop("SVN", UNSET)

        mtq = d.pop("MTQ", UNSET)

        qat = d.pop("QAT", UNSET)

        glp = d.pop("GLP", UNSET)

        uga = d.pop("UGA", UNSET)

        dza = d.pop("DZA", UNSET)

        gtm = d.pop("GTM", UNSET)

        cmr = d.pop("CMR", UNSET)

        lva = d.pop("LVA", UNSET)

        dom = d.pop("DOM", UNSET)

        aze = d.pop("AZE", UNSET)

        geo = d.pop("GEO", UNSET)

        sen = d.pop("SEN", UNSET)

        tza = d.pop("TZA", UNSET)

        zwe = d.pop("ZWE", UNSET)

        kwt = d.pop("KWT", UNSET)

        mlt = d.pop("MLT", UNSET)

        omn = d.pop("OMN", UNSET)

        bol = d.pop("BOL", UNSET)

        slv = d.pop("SLV", UNSET)

        arm = d.pop("ARM", UNSET)

        pry = d.pop("PRY", UNSET)

        irq = d.pop("IRQ", UNSET)

        khm = d.pop("KHM", UNSET)

        bih = d.pop("BIH", UNSET)

        ago = d.pop("AGO", UNSET)

        bhr = d.pop("BHR", UNSET)

        alb = d.pop("ALB", UNSET)

        kaz = d.pop("KAZ", UNSET)

        civ = d.pop("CIV", UNSET)

        eth = d.pop("ETH", UNSET)

        mus = d.pop("MUS", UNSET)

        zmb = d.pop("ZMB", UNSET)

        mkd = d.pop("MKD", UNSET)

        cod = d.pop("COD", UNSET)

        blr = d.pop("BLR", UNSET)

        moz = d.pop("MOZ", UNSET)

        reu = d.pop("REU", UNSET)

        tto = d.pop("TTO", UNSET)

        guf = d.pop("GUF", UNSET)

        isl = d.pop("ISL", UNSET)

        mmr = d.pop("MMR", UNSET)

        hnd = d.pop("HND", UNSET)

        rwa = d.pop("RWA", UNSET)

        mdg = d.pop("MDG", UNSET)

        ben = d.pop("BEN", UNSET)

        uzb = d.pop("UZB", UNSET)

        nam = d.pop("NAM", UNSET)

        bwa = d.pop("BWA", UNSET)

        mda = d.pop("MDA", UNSET)

        jey = d.pop("JEY", UNSET)

        nic = d.pop("NIC", UNSET)

        sdn = d.pop("SDN", UNSET)

        jam = d.pop("JAM", UNSET)

        imn = d.pop("IMN", UNSET)

        bfa = d.pop("BFA", UNSET)

        mng = d.pop("MNG", UNSET)

        mne = d.pop("MNE", UNSET)

        mco = d.pop("MCO", UNSET)

        tgo = d.pop("TGO", UNSET)

        afg = d.pop("AFG", UNSET)

        lby = d.pop("LBY", UNSET)

        xkx = d.pop("XKX", UNSET)

        cym = d.pop("CYM", UNSET)

        mwi = d.pop("MWI", UNSET)

        som = d.pop("SOM", UNSET)

        png = d.pop("PNG", UNSET)

        mdv = d.pop("MDV", UNSET)

        mli = d.pop("MLI", UNSET)

        gin = d.pop("GIN", UNSET)

        pse = d.pop("PSE", UNSET)

        gab = d.pop("GAB", UNSET)

        lie = d.pop("LIE", UNSET)

        hti = d.pop("HTI", UNSET)

        syr = d.pop("SYR", UNSET)

        brb = d.pop("BRB", UNSET)

        yem = d.pop("YEM", UNSET)

        ggy = d.pop("GGY", UNSET)

        ncl = d.pop("NCL", UNSET)

        and_ = d.pop("AND", UNSET)

        sur = d.pop("SUR", UNSET)

        myt = d.pop("MYT", UNSET)

        kgz = d.pop("KGZ", UNSET)

        bhs = d.pop("BHS", UNSET)

        gib = d.pop("GIB", UNSET)

        cog = d.pop("COG", UNSET)

        fji = d.pop("FJI", UNSET)

        blm = d.pop("BLM", UNSET)

        cuw = d.pop("CUW", UNSET)

        cub = d.pop("CUB", UNSET)

        sle = d.pop("SLE", UNSET)

        blz = d.pop("BLZ", UNSET)

        ner = d.pop("NER", UNSET)

        lbr = d.pop("LBR", UNSET)

        vir = d.pop("VIR", UNSET)

        pyf = d.pop("PYF", UNSET)

        gum = d.pop("GUM", UNSET)

        mrt = d.pop("MRT", UNSET)

        abw = d.pop("ABW", UNSET)

        syc = d.pop("SYC", UNSET)

        guy = d.pop("GUY", UNSET)

        lso = d.pop("LSO", UNSET)

        swz = d.pop("SWZ", UNSET)

        ssd = d.pop("SSD", UNSET)

        lca = d.pop("LCA", UNSET)

        mac = d.pop("MAC", UNSET)

        smr = d.pop("SMR", UNSET)

        lao = d.pop("LAO", UNSET)

        brn = d.pop("BRN", UNSET)

        tcd = d.pop("TCD", UNSET)

        bmu = d.pop("BMU", UNSET)

        vgb = d.pop("VGB", UNSET)

        prk = d.pop("PRK", UNSET)

        btn = d.pop("BTN", UNSET)

        bdi = d.pop("BDI", UNSET)

        fro = d.pop("FRO", UNSET)

        tjk = d.pop("TJK", UNSET)

        gmb = d.pop("GMB", UNSET)

        stp = d.pop("STP", UNSET)

        ant = d.pop("ANT", UNSET)

        vct = d.pop("VCT", UNSET)

        dji = d.pop("DJI", UNSET)

        cpv = d.pop("CPV", UNSET)

        tkm = d.pop("TKM", UNSET)

        atg = d.pop("ATG", UNSET)

        tca = d.pop("TCA", UNSET)

        kna = d.pop("KNA", UNSET)

        grd = d.pop("GRD", UNSET)

        asm = d.pop("ASM", UNSET)

        vut = d.pop("VUT", UNSET)

        gnq = d.pop("GNQ", UNSET)

        grl = d.pop("GRL", UNSET)

        sxm = d.pop("SXM", UNSET)

        mnp = d.pop("MNP", UNSET)

        com = d.pop("COM", UNSET)

        tls = d.pop("TLS", UNSET)

        sjm = d.pop("SJM", UNSET)

        caf = d.pop("CAF", UNSET)

        dma = d.pop("DMA", UNSET)

        maf = d.pop("MAF", UNSET)

        wsm = d.pop("WSM", UNSET)

        bes = d.pop("BES", UNSET)

        mhl = d.pop("MHL", UNSET)

        aia = d.pop("AIA", UNSET)

        ton = d.pop("TON", UNSET)

        cok = d.pop("COK", UNSET)

        slb = d.pop("SLB", UNSET)

        spm = d.pop("SPM", UNSET)

        gnb = d.pop("GNB", UNSET)

        ata = d.pop("ATA", UNSET)

        tuv = d.pop("TUV", UNSET)

        ala = d.pop("ALA", UNSET)

        iot = d.pop("IOT", UNSET)

        eri = d.pop("ERI", UNSET)

        plw = d.pop("PLW", UNSET)

        fsm = d.pop("FSM", UNSET)

        nru = d.pop("NRU", UNSET)

        pcn = d.pop("PCN", UNSET)

        flk = d.pop("FLK", UNSET)

        msr = d.pop("MSR", UNSET)

        vat = d.pop("VAT", UNSET)

        kir = d.pop("KIR", UNSET)

        shn = d.pop("SHN", UNSET)

        niu = d.pop("NIU", UNSET)

        wlf = d.pop("WLF", UNSET)

        hmd = d.pop("HMD", UNSET)

        cxr = d.pop("CXR", UNSET)

        nfk = d.pop("NFK", UNSET)

        atf = d.pop("ATF", UNSET)

        cck = d.pop("CCK", UNSET)

        sgs = d.pop("SGS", UNSET)

        bvt = d.pop("BVT", UNSET)

        umi = d.pop("UMI", UNSET)

        esh = d.pop("ESH", UNSET)

        tkl = d.pop("TKL", UNSET)

        x_south_asia = d.pop("X-SOUTH_ASIA", UNSET)

        x_south_east_europe = d.pop("X-SOUTH_EAST_EUROPE", UNSET)

        x_northern_africa = d.pop("X-NORTHERN_AFRICA", UNSET)

        x_pacific = d.pop("X-PACIFIC", UNSET)

        x_south_west_europe = d.pop("X-SOUTH_WEST_EUROPE", UNSET)

        x_southern_africa = d.pop("X-SOUTHERN_AFRICA", UNSET)

        x_west_indies = d.pop("X-WEST_INDIES", UNSET)

        x_south_america = d.pop("X-SOUTH_AMERICA", UNSET)

        x_south_west_asia = d.pop("X-SOUTH_WEST_ASIA", UNSET)

        x_central_europe = d.pop("X-CENTRAL_EUROPE", UNSET)

        x_eastern_europe = d.pop("X-EASTERN_EUROPE", UNSET)

        x_western_europe = d.pop("X-WESTERN_EUROPE", UNSET)

        x_central_america = d.pop("X-CENTRAL_AMERICA", UNSET)

        x_western_africa = d.pop("X-WESTERN_AFRICA", UNSET)

        x_south_atlantic_ocean = d.pop("X-SOUTH_ATLANTIC_OCEAN", UNSET)

        x_south_east_asia = d.pop("X-SOUTH_EAST_ASIA", UNSET)

        x_central_africa = d.pop("X-CENTRAL_AFRICA", UNSET)

        x_north_america = d.pop("X-NORTH_AMERICA", UNSET)

        x_east_asia = d.pop("X-EAST_ASIA", UNSET)

        x_northern_europe = d.pop("X-NORTHERN_EUROPE", UNSET)

        x_eastern_africa = d.pop("X-EASTERN_AFRICA", UNSET)

        x_southern_indian_ocean = d.pop("X-SOUTHERN_INDIAN_OCEAN", UNSET)

        x_southern_europe = d.pop("X-SOUTHERN_EUROPE", UNSET)

        x_central_asia = d.pop("X-CENTRAL_ASIA", UNSET)

        x_northern_asia = d.pop("X-NORTHERN_ASIA", UNSET)

        x_asia = d.pop("X-ASIA", UNSET)

        x_europe = d.pop("X-EUROPE", UNSET)

        x_africa = d.pop("X-AFRICA", UNSET)

        x_oceania = d.pop("X-OCEANIA", UNSET)

        x_americas = d.pop("X-AMERICAS", UNSET)

        x_antarctica = d.pop("X-ANTARCTICA", UNSET)

        x_atlantic_ocean = d.pop("X-ATLANTIC_OCEAN", UNSET)

        x_indian_ocean = d.pop("X-INDIAN_OCEAN", UNSET)

        x_middle_east = d.pop("X-MIDDLE_EAST", UNSET)

        x_mena = d.pop("X-MENA", UNSET)

        x_emea = d.pop("X-EMEA", UNSET)

        x_european_union = d.pop("X-EUROPEAN_UNION", UNSET)

        x_efta = d.pop("X-EFTA", UNSET)

        x_apac = d.pop("X-APAC", UNSET)

        x_latam = d.pop("X-LATAM", UNSET)

        x_anglosphere = d.pop("X-ANGLOSPHERE", UNSET)

        x_dach = d.pop("X-DACH", UNSET)

        x_nordics = d.pop("X-NORDICS", UNSET)

        x_benelux = d.pop("X-BENELUX", UNSET)

        x_gcc = d.pop("X-GCC", UNSET)

        x_brics = d.pop("X-BRICS", UNSET)

        x_g20 = d.pop("X-G20", UNSET)

        x_oecd = d.pop("X-OECD", UNSET)

        x_sanctioned = d.pop("X-SANCTIONED", UNSET)

        company_live_enrich_response_200_output_company_locations_stats_type_0 = cls(
            usa=usa,
            gbr=gbr,
            fra=fra,
            ind=ind,
            bra=bra,
            deu=deu,
            esp=esp,
            can=can,
            aus=aus,
            nld=nld,
            ita=ita,
            zaf=zaf,
            bel=bel,
            chn=chn,
            tur=tur,
            mex=mex,
            che=che,
            nor=nor,
            are=are,
            swe=swe,
            pol=pol,
            idn=idn,
            arg=arg,
            prt=prt,
            col=col,
            chl=chl,
            pak=pak,
            dnk=dnk,
            jpn=jpn,
            nga=nga,
            sgp=sgp,
            per=per,
            nzl=nzl,
            aut=aut,
            irl=irl,
            mys=mys,
            bgd=bgd,
            egy=egy,
            isr=isr,
            sau=sau,
            phl=phl,
            fin=fin,
            irn=irn,
            rou=rou,
            cze=cze,
            grc=grc,
            hkg=hkg,
            hun=hun,
            ken=ken,
            mar=mar,
            vnm=vnm,
            rus=rus,
            ukr=ukr,
            ecu=ecu,
            tha=tha,
            lka=lka,
            kor=kor,
            bgr=bgr,
            gha=gha,
            srb=srb,
            twn=twn,
            hrv=hrv,
            ltu=ltu,
            pri=pri,
            svk=svk,
            tun=tun,
            est=est,
            ven=ven,
            cri=cri,
            pan=pan,
            ury=ury,
            lbn=lbn,
            lux=lux,
            cyp=cyp,
            npl=npl,
            jor=jor,
            svn=svn,
            mtq=mtq,
            qat=qat,
            glp=glp,
            uga=uga,
            dza=dza,
            gtm=gtm,
            cmr=cmr,
            lva=lva,
            dom=dom,
            aze=aze,
            geo=geo,
            sen=sen,
            tza=tza,
            zwe=zwe,
            kwt=kwt,
            mlt=mlt,
            omn=omn,
            bol=bol,
            slv=slv,
            arm=arm,
            pry=pry,
            irq=irq,
            khm=khm,
            bih=bih,
            ago=ago,
            bhr=bhr,
            alb=alb,
            kaz=kaz,
            civ=civ,
            eth=eth,
            mus=mus,
            zmb=zmb,
            mkd=mkd,
            cod=cod,
            blr=blr,
            moz=moz,
            reu=reu,
            tto=tto,
            guf=guf,
            isl=isl,
            mmr=mmr,
            hnd=hnd,
            rwa=rwa,
            mdg=mdg,
            ben=ben,
            uzb=uzb,
            nam=nam,
            bwa=bwa,
            mda=mda,
            jey=jey,
            nic=nic,
            sdn=sdn,
            jam=jam,
            imn=imn,
            bfa=bfa,
            mng=mng,
            mne=mne,
            mco=mco,
            tgo=tgo,
            afg=afg,
            lby=lby,
            xkx=xkx,
            cym=cym,
            mwi=mwi,
            som=som,
            png=png,
            mdv=mdv,
            mli=mli,
            gin=gin,
            pse=pse,
            gab=gab,
            lie=lie,
            hti=hti,
            syr=syr,
            brb=brb,
            yem=yem,
            ggy=ggy,
            ncl=ncl,
            and_=and_,
            sur=sur,
            myt=myt,
            kgz=kgz,
            bhs=bhs,
            gib=gib,
            cog=cog,
            fji=fji,
            blm=blm,
            cuw=cuw,
            cub=cub,
            sle=sle,
            blz=blz,
            ner=ner,
            lbr=lbr,
            vir=vir,
            pyf=pyf,
            gum=gum,
            mrt=mrt,
            abw=abw,
            syc=syc,
            guy=guy,
            lso=lso,
            swz=swz,
            ssd=ssd,
            lca=lca,
            mac=mac,
            smr=smr,
            lao=lao,
            brn=brn,
            tcd=tcd,
            bmu=bmu,
            vgb=vgb,
            prk=prk,
            btn=btn,
            bdi=bdi,
            fro=fro,
            tjk=tjk,
            gmb=gmb,
            stp=stp,
            ant=ant,
            vct=vct,
            dji=dji,
            cpv=cpv,
            tkm=tkm,
            atg=atg,
            tca=tca,
            kna=kna,
            grd=grd,
            asm=asm,
            vut=vut,
            gnq=gnq,
            grl=grl,
            sxm=sxm,
            mnp=mnp,
            com=com,
            tls=tls,
            sjm=sjm,
            caf=caf,
            dma=dma,
            maf=maf,
            wsm=wsm,
            bes=bes,
            mhl=mhl,
            aia=aia,
            ton=ton,
            cok=cok,
            slb=slb,
            spm=spm,
            gnb=gnb,
            ata=ata,
            tuv=tuv,
            ala=ala,
            iot=iot,
            eri=eri,
            plw=plw,
            fsm=fsm,
            nru=nru,
            pcn=pcn,
            flk=flk,
            msr=msr,
            vat=vat,
            kir=kir,
            shn=shn,
            niu=niu,
            wlf=wlf,
            hmd=hmd,
            cxr=cxr,
            nfk=nfk,
            atf=atf,
            cck=cck,
            sgs=sgs,
            bvt=bvt,
            umi=umi,
            esh=esh,
            tkl=tkl,
            x_south_asia=x_south_asia,
            x_south_east_europe=x_south_east_europe,
            x_northern_africa=x_northern_africa,
            x_pacific=x_pacific,
            x_south_west_europe=x_south_west_europe,
            x_southern_africa=x_southern_africa,
            x_west_indies=x_west_indies,
            x_south_america=x_south_america,
            x_south_west_asia=x_south_west_asia,
            x_central_europe=x_central_europe,
            x_eastern_europe=x_eastern_europe,
            x_western_europe=x_western_europe,
            x_central_america=x_central_america,
            x_western_africa=x_western_africa,
            x_south_atlantic_ocean=x_south_atlantic_ocean,
            x_south_east_asia=x_south_east_asia,
            x_central_africa=x_central_africa,
            x_north_america=x_north_america,
            x_east_asia=x_east_asia,
            x_northern_europe=x_northern_europe,
            x_eastern_africa=x_eastern_africa,
            x_southern_indian_ocean=x_southern_indian_ocean,
            x_southern_europe=x_southern_europe,
            x_central_asia=x_central_asia,
            x_northern_asia=x_northern_asia,
            x_asia=x_asia,
            x_europe=x_europe,
            x_africa=x_africa,
            x_oceania=x_oceania,
            x_americas=x_americas,
            x_antarctica=x_antarctica,
            x_atlantic_ocean=x_atlantic_ocean,
            x_indian_ocean=x_indian_ocean,
            x_middle_east=x_middle_east,
            x_mena=x_mena,
            x_emea=x_emea,
            x_european_union=x_european_union,
            x_efta=x_efta,
            x_apac=x_apac,
            x_latam=x_latam,
            x_anglosphere=x_anglosphere,
            x_dach=x_dach,
            x_nordics=x_nordics,
            x_benelux=x_benelux,
            x_gcc=x_gcc,
            x_brics=x_brics,
            x_g20=x_g20,
            x_oecd=x_oecd,
            x_sanctioned=x_sanctioned,
        )

        return company_live_enrich_response_200_output_company_locations_stats_type_0

