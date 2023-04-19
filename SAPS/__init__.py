import requests
import os
from . import api
from .exceptions import *
from requests.utils import requote_uri
requests.packages.urllib3.disable_warnings()  # Suppress HTTP warnings


def is_identification_card_exists(identification_card: str) -> bool:
    '''
        identification_card
            Your identification card in string. E.g. '012345678900'
    '''
    a = requests.get(api.API+f'&nokp={identification_card}', verify=False)
    return a.text.strip() == api.exist


def is_school_code_exists(identification_card: str, school_code: str) -> bool:
    '''
        identification_card
            Your identification card in string. E.g. '012345678900'
        school_code
            E.g. 'ABC0123'
    '''
    a = requests.get(
        api.API+f'&nokp={identification_card}&kodsek={school_code}', verify=False)
    return a.text.strip() == api.exist


def is_exam_year_exists(identification_card: str, school_code: str, year: str) -> bool:
    '''
        identification_card
            Your identification card in string. E.g. '012345678900'
        school_code
            E.g. 'ABC0123'
        year
            E.g. '2023'
    '''
    s = requests.Session()
    a = s.get(
        api.API+f'&nokp={identification_card}&kodsek={school_code}', verify=False)
    if not a.text.strip() == api.exist:
        raise UserDoesNotExist
    a = s.get(api.API_2+f'&tahun={year}')
    return not api.not_exist in a.text.strip()


def is_exam_results_exists(identification_card: str, school_code: str, tingkatan: str, kelas: str, tahun: str, exam_type: int = 2) -> bool:
    '''
        identification_card
            Your identification card in string. E.g. '012345678900'
        school_code
            E.g. 'ABC0123'
        tingkatan
            E.g. '4'
        kelas
            E.g. 'AMETIS_DLP', 'KENANGA', 'AMANAH', 'ORKID'
        exam_type
            1 >> PEPERIKSAAN PERTENGAHAN TAHUN
            2 >> PEPERIKSAAN AKHIR TAHUN
            default: 2
    '''
    s = requests.Session()
    # Stage 1
    a = s.get(
        api.API+f'&nokp={identification_card}', verify=False)
    if not a.text.strip() == api.exist:
        raise UserDoesNotExist
    a = s.get(
        api.API+f'&nokp={identification_card}&kodsek={school_code}', verify=False)
    if not a.text.strip() == api.exist:
        raise SchoolCodeDoesNotExist
    # Stage 2
    a = s.get(api.API_2+f'&tahun={tahun}')
    if api.not_exist in a.text.strip():
        raise ExamYearDoesNotExist
    # Stage 3
    exam_type = 'PPT' if exam_type == 1 else 'PAT'
    a = s.get(
        api.API_3+f'&nokp={identification_card}&kodsek={school_code}&ting=T{tingkatan}&kelas={tingkatan}_{kelas}&tahun={tahun}&jpep={exam_type}')
    # Stage 4
    o = f'&nokp={identification_card}&kodsek={school_code}&ting=T{tingkatan}&kelas={tingkatan}_{kelas}&cboPep={exam_type}'
    a = s.post(api.API_4+o, verify=False)
    return not "Maklumat markah pelajar masih belum lagi dikemaskini." in a.text


def save_exam_results(identification_card: str, school_code: str, tingkatan: str, kelas: str, tahun: str, exam_type: int = 2, filename: str = 'exam_results.html'):
    '''
        identification_card
            Your identification card in string. E.g. '012345678900'
        school_code
            E.g. 'ABC0123'
        tingkatan
            E.g. '4'
        kelas
            E.g. 'AMETIS_DLP', 'KENANGA', 'AMANAH', 'ORKID'
        exam_type
            1 >> PEPERIKSAAN PERTENGAHAN TAHUN
            2 >> PEPERIKSAAN AKHIR TAHUN
            default: 2
    '''
    s = requests.Session()
    # Stage 1
    a = s.get(
        api.API+f'&nokp={identification_card}', verify=False)
    if not a.text.strip() == api.exist:
        raise UserDoesNotExist
    a = s.get(
        api.API+f'&nokp={identification_card}&kodsek={school_code}', verify=False)
    if not a.text.strip() == api.exist:
        raise SchoolCodeDoesNotExist
    # Stage 2
    a = s.get(api.API_2+f'&tahun={tahun}')
    if api.not_exist in a.text.strip():
        raise ExamYearDoesNotExist
    # Stage 3
    exam_type = 'PPT' if exam_type == 1 else 'PAT'
    a = s.get(
        api.API_3+f'&nokp={identification_card}&kodsek={school_code}&ting=T{tingkatan}&kelas={tingkatan}_{kelas}&tahun={tahun}&jpep={exam_type}')
    # Stage 4
    o = f'&nokp={identification_card}&kodsek={school_code}&ting=T{tingkatan}&kelas={tingkatan}_{kelas}&cboPep={exam_type}'
    a = s.post(api.API_4+o, verify=False)
    if "Maklumat markah pelajar masih belum lagi dikemaskini." in a.text:
        raise ExamResultsDoesNotExist
    open(filename, 'wb').write(a.content)
    print(f'Saved {filename}')
