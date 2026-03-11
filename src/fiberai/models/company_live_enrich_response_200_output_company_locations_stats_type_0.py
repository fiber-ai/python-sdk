from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0")


@_attrs_define
class CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0:
    """
    Attributes:
        usa (float | Unset):
        gbr (float | Unset):
        fra (float | Unset):
        ind (float | Unset):
        bra (float | Unset):
        deu (float | Unset):
        esp (float | Unset):
        can (float | Unset):
        aus (float | Unset):
        nld (float | Unset):
        ita (float | Unset):
        zaf (float | Unset):
        bel (float | Unset):
        chn (float | Unset):
        tur (float | Unset):
        mex (float | Unset):
        che (float | Unset):
        nor (float | Unset):
        are (float | Unset):
        swe (float | Unset):
        pol (float | Unset):
        idn (float | Unset):
        arg (float | Unset):
        prt (float | Unset):
        col (float | Unset):
        chl (float | Unset):
        pak (float | Unset):
        dnk (float | Unset):
        jpn (float | Unset):
        nga (float | Unset):
        sgp (float | Unset):
        per (float | Unset):
        nzl (float | Unset):
        aut (float | Unset):
        irl (float | Unset):
        mys (float | Unset):
        bgd (float | Unset):
        egy (float | Unset):
        isr (float | Unset):
        sau (float | Unset):
        phl (float | Unset):
        fin (float | Unset):
        irn (float | Unset):
        rou (float | Unset):
        cze (float | Unset):
        grc (float | Unset):
        hkg (float | Unset):
        hun (float | Unset):
        ken (float | Unset):
        mar (float | Unset):
        vnm (float | Unset):
        rus (float | Unset):
        ukr (float | Unset):
        ecu (float | Unset):
        tha (float | Unset):
        lka (float | Unset):
        kor (float | Unset):
        bgr (float | Unset):
        gha (float | Unset):
        srb (float | Unset):
        twn (float | Unset):
        hrv (float | Unset):
        ltu (float | Unset):
        pri (float | Unset):
        svk (float | Unset):
        tun (float | Unset):
        est (float | Unset):
        ven (float | Unset):
        cri (float | Unset):
        pan (float | Unset):
        ury (float | Unset):
        lbn (float | Unset):
        lux (float | Unset):
        cyp (float | Unset):
        npl (float | Unset):
        jor (float | Unset):
        svn (float | Unset):
        mtq (float | Unset):
        qat (float | Unset):
        glp (float | Unset):
        uga (float | Unset):
        dza (float | Unset):
        gtm (float | Unset):
        cmr (float | Unset):
        lva (float | Unset):
        dom (float | Unset):
        aze (float | Unset):
        geo (float | Unset):
        sen (float | Unset):
        tza (float | Unset):
        zwe (float | Unset):
        kwt (float | Unset):
        mlt (float | Unset):
        omn (float | Unset):
        bol (float | Unset):
        slv (float | Unset):
        arm (float | Unset):
        pry (float | Unset):
        irq (float | Unset):
        khm (float | Unset):
        bih (float | Unset):
        ago (float | Unset):
        bhr (float | Unset):
        alb (float | Unset):
        kaz (float | Unset):
        civ (float | Unset):
        eth (float | Unset):
        mus (float | Unset):
        zmb (float | Unset):
        mkd (float | Unset):
        cod (float | Unset):
        blr (float | Unset):
        moz (float | Unset):
        reu (float | Unset):
        tto (float | Unset):
        guf (float | Unset):
        isl (float | Unset):
        mmr (float | Unset):
        hnd (float | Unset):
        rwa (float | Unset):
        mdg (float | Unset):
        ben (float | Unset):
        uzb (float | Unset):
        nam (float | Unset):
        bwa (float | Unset):
        mda (float | Unset):
        jey (float | Unset):
        nic (float | Unset):
        sdn (float | Unset):
        jam (float | Unset):
        imn (float | Unset):
        bfa (float | Unset):
        mng (float | Unset):
        mne (float | Unset):
        mco (float | Unset):
        tgo (float | Unset):
        afg (float | Unset):
        lby (float | Unset):
        xkx (float | Unset):
        cym (float | Unset):
        mwi (float | Unset):
        som (float | Unset):
        png (float | Unset):
        mdv (float | Unset):
        mli (float | Unset):
        gin (float | Unset):
        pse (float | Unset):
        gab (float | Unset):
        lie (float | Unset):
        hti (float | Unset):
        syr (float | Unset):
        brb (float | Unset):
        yem (float | Unset):
        ggy (float | Unset):
        ncl (float | Unset):
        and_ (float | Unset):
        sur (float | Unset):
        myt (float | Unset):
        kgz (float | Unset):
        bhs (float | Unset):
        gib (float | Unset):
        cog (float | Unset):
        fji (float | Unset):
        blm (float | Unset):
        cuw (float | Unset):
        cub (float | Unset):
        sle (float | Unset):
        blz (float | Unset):
        ner (float | Unset):
        lbr (float | Unset):
        vir (float | Unset):
        pyf (float | Unset):
        gum (float | Unset):
        mrt (float | Unset):
        abw (float | Unset):
        syc (float | Unset):
        guy (float | Unset):
        lso (float | Unset):
        swz (float | Unset):
        ssd (float | Unset):
        lca (float | Unset):
        mac (float | Unset):
        smr (float | Unset):
        lao (float | Unset):
        brn (float | Unset):
        tcd (float | Unset):
        bmu (float | Unset):
        vgb (float | Unset):
        prk (float | Unset):
        btn (float | Unset):
        bdi (float | Unset):
        fro (float | Unset):
        tjk (float | Unset):
        gmb (float | Unset):
        stp (float | Unset):
        ant (float | Unset):
        vct (float | Unset):
        dji (float | Unset):
        cpv (float | Unset):
        tkm (float | Unset):
        atg (float | Unset):
        tca (float | Unset):
        kna (float | Unset):
        grd (float | Unset):
        asm (float | Unset):
        vut (float | Unset):
        gnq (float | Unset):
        grl (float | Unset):
        sxm (float | Unset):
        mnp (float | Unset):
        com (float | Unset):
        tls (float | Unset):
        sjm (float | Unset):
        caf (float | Unset):
        dma (float | Unset):
        maf (float | Unset):
        wsm (float | Unset):
        bes (float | Unset):
        mhl (float | Unset):
        aia (float | Unset):
        ton (float | Unset):
        cok (float | Unset):
        slb (float | Unset):
        spm (float | Unset):
        gnb (float | Unset):
        ata (float | Unset):
        tuv (float | Unset):
        ala (float | Unset):
        iot (float | Unset):
        eri (float | Unset):
        plw (float | Unset):
        fsm (float | Unset):
        nru (float | Unset):
        pcn (float | Unset):
        flk (float | Unset):
        msr (float | Unset):
        vat (float | Unset):
        kir (float | Unset):
        shn (float | Unset):
        niu (float | Unset):
        wlf (float | Unset):
        hmd (float | Unset):
        cxr (float | Unset):
        nfk (float | Unset):
        atf (float | Unset):
        cck (float | Unset):
        sgs (float | Unset):
        bvt (float | Unset):
        umi (float | Unset):
        esh (float | Unset):
        tkl (float | Unset):
        x_south_asia (float | Unset):
        x_south_east_europe (float | Unset):
        x_northern_africa (float | Unset):
        x_pacific (float | Unset):
        x_south_west_europe (float | Unset):
        x_southern_africa (float | Unset):
        x_west_indies (float | Unset):
        x_south_america (float | Unset):
        x_south_west_asia (float | Unset):
        x_central_europe (float | Unset):
        x_eastern_europe (float | Unset):
        x_western_europe (float | Unset):
        x_central_america (float | Unset):
        x_western_africa (float | Unset):
        x_south_atlantic_ocean (float | Unset):
        x_south_east_asia (float | Unset):
        x_central_africa (float | Unset):
        x_north_america (float | Unset):
        x_east_asia (float | Unset):
        x_northern_europe (float | Unset):
        x_eastern_africa (float | Unset):
        x_southern_indian_ocean (float | Unset):
        x_southern_europe (float | Unset):
        x_central_asia (float | Unset):
        x_northern_asia (float | Unset):
        x_asia (float | Unset):
        x_europe (float | Unset):
        x_africa (float | Unset):
        x_oceania (float | Unset):
        x_americas (float | Unset):
        x_antarctica (float | Unset):
        x_atlantic_ocean (float | Unset):
        x_indian_ocean (float | Unset):
        x_middle_east (float | Unset):
        x_mena (float | Unset):
        x_emea (float | Unset):
        x_european_union (float | Unset):
        x_efta (float | Unset):
        x_apac (float | Unset):
        x_latam (float | Unset):
        x_anglosphere (float | Unset):
        x_dach (float | Unset):
        x_nordics (float | Unset):
        x_benelux (float | Unset):
        x_gcc (float | Unset):
        x_brics (float | Unset):
        x_g20 (float | Unset):
        x_oecd (float | Unset):
        x_sanctioned (float | Unset):
    """

    usa: float | Unset = UNSET
    gbr: float | Unset = UNSET
    fra: float | Unset = UNSET
    ind: float | Unset = UNSET
    bra: float | Unset = UNSET
    deu: float | Unset = UNSET
    esp: float | Unset = UNSET
    can: float | Unset = UNSET
    aus: float | Unset = UNSET
    nld: float | Unset = UNSET
    ita: float | Unset = UNSET
    zaf: float | Unset = UNSET
    bel: float | Unset = UNSET
    chn: float | Unset = UNSET
    tur: float | Unset = UNSET
    mex: float | Unset = UNSET
    che: float | Unset = UNSET
    nor: float | Unset = UNSET
    are: float | Unset = UNSET
    swe: float | Unset = UNSET
    pol: float | Unset = UNSET
    idn: float | Unset = UNSET
    arg: float | Unset = UNSET
    prt: float | Unset = UNSET
    col: float | Unset = UNSET
    chl: float | Unset = UNSET
    pak: float | Unset = UNSET
    dnk: float | Unset = UNSET
    jpn: float | Unset = UNSET
    nga: float | Unset = UNSET
    sgp: float | Unset = UNSET
    per: float | Unset = UNSET
    nzl: float | Unset = UNSET
    aut: float | Unset = UNSET
    irl: float | Unset = UNSET
    mys: float | Unset = UNSET
    bgd: float | Unset = UNSET
    egy: float | Unset = UNSET
    isr: float | Unset = UNSET
    sau: float | Unset = UNSET
    phl: float | Unset = UNSET
    fin: float | Unset = UNSET
    irn: float | Unset = UNSET
    rou: float | Unset = UNSET
    cze: float | Unset = UNSET
    grc: float | Unset = UNSET
    hkg: float | Unset = UNSET
    hun: float | Unset = UNSET
    ken: float | Unset = UNSET
    mar: float | Unset = UNSET
    vnm: float | Unset = UNSET
    rus: float | Unset = UNSET
    ukr: float | Unset = UNSET
    ecu: float | Unset = UNSET
    tha: float | Unset = UNSET
    lka: float | Unset = UNSET
    kor: float | Unset = UNSET
    bgr: float | Unset = UNSET
    gha: float | Unset = UNSET
    srb: float | Unset = UNSET
    twn: float | Unset = UNSET
    hrv: float | Unset = UNSET
    ltu: float | Unset = UNSET
    pri: float | Unset = UNSET
    svk: float | Unset = UNSET
    tun: float | Unset = UNSET
    est: float | Unset = UNSET
    ven: float | Unset = UNSET
    cri: float | Unset = UNSET
    pan: float | Unset = UNSET
    ury: float | Unset = UNSET
    lbn: float | Unset = UNSET
    lux: float | Unset = UNSET
    cyp: float | Unset = UNSET
    npl: float | Unset = UNSET
    jor: float | Unset = UNSET
    svn: float | Unset = UNSET
    mtq: float | Unset = UNSET
    qat: float | Unset = UNSET
    glp: float | Unset = UNSET
    uga: float | Unset = UNSET
    dza: float | Unset = UNSET
    gtm: float | Unset = UNSET
    cmr: float | Unset = UNSET
    lva: float | Unset = UNSET
    dom: float | Unset = UNSET
    aze: float | Unset = UNSET
    geo: float | Unset = UNSET
    sen: float | Unset = UNSET
    tza: float | Unset = UNSET
    zwe: float | Unset = UNSET
    kwt: float | Unset = UNSET
    mlt: float | Unset = UNSET
    omn: float | Unset = UNSET
    bol: float | Unset = UNSET
    slv: float | Unset = UNSET
    arm: float | Unset = UNSET
    pry: float | Unset = UNSET
    irq: float | Unset = UNSET
    khm: float | Unset = UNSET
    bih: float | Unset = UNSET
    ago: float | Unset = UNSET
    bhr: float | Unset = UNSET
    alb: float | Unset = UNSET
    kaz: float | Unset = UNSET
    civ: float | Unset = UNSET
    eth: float | Unset = UNSET
    mus: float | Unset = UNSET
    zmb: float | Unset = UNSET
    mkd: float | Unset = UNSET
    cod: float | Unset = UNSET
    blr: float | Unset = UNSET
    moz: float | Unset = UNSET
    reu: float | Unset = UNSET
    tto: float | Unset = UNSET
    guf: float | Unset = UNSET
    isl: float | Unset = UNSET
    mmr: float | Unset = UNSET
    hnd: float | Unset = UNSET
    rwa: float | Unset = UNSET
    mdg: float | Unset = UNSET
    ben: float | Unset = UNSET
    uzb: float | Unset = UNSET
    nam: float | Unset = UNSET
    bwa: float | Unset = UNSET
    mda: float | Unset = UNSET
    jey: float | Unset = UNSET
    nic: float | Unset = UNSET
    sdn: float | Unset = UNSET
    jam: float | Unset = UNSET
    imn: float | Unset = UNSET
    bfa: float | Unset = UNSET
    mng: float | Unset = UNSET
    mne: float | Unset = UNSET
    mco: float | Unset = UNSET
    tgo: float | Unset = UNSET
    afg: float | Unset = UNSET
    lby: float | Unset = UNSET
    xkx: float | Unset = UNSET
    cym: float | Unset = UNSET
    mwi: float | Unset = UNSET
    som: float | Unset = UNSET
    png: float | Unset = UNSET
    mdv: float | Unset = UNSET
    mli: float | Unset = UNSET
    gin: float | Unset = UNSET
    pse: float | Unset = UNSET
    gab: float | Unset = UNSET
    lie: float | Unset = UNSET
    hti: float | Unset = UNSET
    syr: float | Unset = UNSET
    brb: float | Unset = UNSET
    yem: float | Unset = UNSET
    ggy: float | Unset = UNSET
    ncl: float | Unset = UNSET
    and_: float | Unset = UNSET
    sur: float | Unset = UNSET
    myt: float | Unset = UNSET
    kgz: float | Unset = UNSET
    bhs: float | Unset = UNSET
    gib: float | Unset = UNSET
    cog: float | Unset = UNSET
    fji: float | Unset = UNSET
    blm: float | Unset = UNSET
    cuw: float | Unset = UNSET
    cub: float | Unset = UNSET
    sle: float | Unset = UNSET
    blz: float | Unset = UNSET
    ner: float | Unset = UNSET
    lbr: float | Unset = UNSET
    vir: float | Unset = UNSET
    pyf: float | Unset = UNSET
    gum: float | Unset = UNSET
    mrt: float | Unset = UNSET
    abw: float | Unset = UNSET
    syc: float | Unset = UNSET
    guy: float | Unset = UNSET
    lso: float | Unset = UNSET
    swz: float | Unset = UNSET
    ssd: float | Unset = UNSET
    lca: float | Unset = UNSET
    mac: float | Unset = UNSET
    smr: float | Unset = UNSET
    lao: float | Unset = UNSET
    brn: float | Unset = UNSET
    tcd: float | Unset = UNSET
    bmu: float | Unset = UNSET
    vgb: float | Unset = UNSET
    prk: float | Unset = UNSET
    btn: float | Unset = UNSET
    bdi: float | Unset = UNSET
    fro: float | Unset = UNSET
    tjk: float | Unset = UNSET
    gmb: float | Unset = UNSET
    stp: float | Unset = UNSET
    ant: float | Unset = UNSET
    vct: float | Unset = UNSET
    dji: float | Unset = UNSET
    cpv: float | Unset = UNSET
    tkm: float | Unset = UNSET
    atg: float | Unset = UNSET
    tca: float | Unset = UNSET
    kna: float | Unset = UNSET
    grd: float | Unset = UNSET
    asm: float | Unset = UNSET
    vut: float | Unset = UNSET
    gnq: float | Unset = UNSET
    grl: float | Unset = UNSET
    sxm: float | Unset = UNSET
    mnp: float | Unset = UNSET
    com: float | Unset = UNSET
    tls: float | Unset = UNSET
    sjm: float | Unset = UNSET
    caf: float | Unset = UNSET
    dma: float | Unset = UNSET
    maf: float | Unset = UNSET
    wsm: float | Unset = UNSET
    bes: float | Unset = UNSET
    mhl: float | Unset = UNSET
    aia: float | Unset = UNSET
    ton: float | Unset = UNSET
    cok: float | Unset = UNSET
    slb: float | Unset = UNSET
    spm: float | Unset = UNSET
    gnb: float | Unset = UNSET
    ata: float | Unset = UNSET
    tuv: float | Unset = UNSET
    ala: float | Unset = UNSET
    iot: float | Unset = UNSET
    eri: float | Unset = UNSET
    plw: float | Unset = UNSET
    fsm: float | Unset = UNSET
    nru: float | Unset = UNSET
    pcn: float | Unset = UNSET
    flk: float | Unset = UNSET
    msr: float | Unset = UNSET
    vat: float | Unset = UNSET
    kir: float | Unset = UNSET
    shn: float | Unset = UNSET
    niu: float | Unset = UNSET
    wlf: float | Unset = UNSET
    hmd: float | Unset = UNSET
    cxr: float | Unset = UNSET
    nfk: float | Unset = UNSET
    atf: float | Unset = UNSET
    cck: float | Unset = UNSET
    sgs: float | Unset = UNSET
    bvt: float | Unset = UNSET
    umi: float | Unset = UNSET
    esh: float | Unset = UNSET
    tkl: float | Unset = UNSET
    x_south_asia: float | Unset = UNSET
    x_south_east_europe: float | Unset = UNSET
    x_northern_africa: float | Unset = UNSET
    x_pacific: float | Unset = UNSET
    x_south_west_europe: float | Unset = UNSET
    x_southern_africa: float | Unset = UNSET
    x_west_indies: float | Unset = UNSET
    x_south_america: float | Unset = UNSET
    x_south_west_asia: float | Unset = UNSET
    x_central_europe: float | Unset = UNSET
    x_eastern_europe: float | Unset = UNSET
    x_western_europe: float | Unset = UNSET
    x_central_america: float | Unset = UNSET
    x_western_africa: float | Unset = UNSET
    x_south_atlantic_ocean: float | Unset = UNSET
    x_south_east_asia: float | Unset = UNSET
    x_central_africa: float | Unset = UNSET
    x_north_america: float | Unset = UNSET
    x_east_asia: float | Unset = UNSET
    x_northern_europe: float | Unset = UNSET
    x_eastern_africa: float | Unset = UNSET
    x_southern_indian_ocean: float | Unset = UNSET
    x_southern_europe: float | Unset = UNSET
    x_central_asia: float | Unset = UNSET
    x_northern_asia: float | Unset = UNSET
    x_asia: float | Unset = UNSET
    x_europe: float | Unset = UNSET
    x_africa: float | Unset = UNSET
    x_oceania: float | Unset = UNSET
    x_americas: float | Unset = UNSET
    x_antarctica: float | Unset = UNSET
    x_atlantic_ocean: float | Unset = UNSET
    x_indian_ocean: float | Unset = UNSET
    x_middle_east: float | Unset = UNSET
    x_mena: float | Unset = UNSET
    x_emea: float | Unset = UNSET
    x_european_union: float | Unset = UNSET
    x_efta: float | Unset = UNSET
    x_apac: float | Unset = UNSET
    x_latam: float | Unset = UNSET
    x_anglosphere: float | Unset = UNSET
    x_dach: float | Unset = UNSET
    x_nordics: float | Unset = UNSET
    x_benelux: float | Unset = UNSET
    x_gcc: float | Unset = UNSET
    x_brics: float | Unset = UNSET
    x_g20: float | Unset = UNSET
    x_oecd: float | Unset = UNSET
    x_sanctioned: float | Unset = UNSET

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

        field_dict.update({})
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
