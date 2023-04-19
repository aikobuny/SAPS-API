[![license](https://img.shields.io/github/license/aikobuny/SAPS-API.svg?style=for-the-badge)](https://github.com/aikobuny/SAPS-API/blob/master/LICENSE) ![GitHub last commit](https://img.shields.io/github/last-commit/aikobuny/SAPS-API.svg?style=for-the-badge) ![GitHub top language](https://img.shields.io/github/languages/top/aikobuny/SAPS-API?style=for-the-badge)

# SAPS-API
The API to check your exam results from SAPS Malaysia.

# Installation

SAPS-API requires [Python 3.9+](https://python.org) to run.
Follow the instructions below:
## With git
```sh
git clone https://github.com/aikobuny/SAPS-API.git
cd SAPS-API
```
## Without git
1. Download it as zip file
2. Extract it and place it in the same folder as your project file

# Usage example
```py
import SAPS

SAPS.open_exam_results(
  identification_card = '001234567890',
  school_code = 'ABC1234',
  tingkatan = '5',
  kelas = 'AMETIS_DLP',
  tahun = '2023',
  exam_type = 1, # PEPERIKSAAN PERTENGAHAN TAHUN, 2 > PEPERIKSAAN AKHIR TAHUN
  filename = 'exam_results.html',
)
```
