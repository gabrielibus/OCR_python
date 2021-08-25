echo off
echo Este script reconoce imagens con OCR - creado por compuFacilito www.compuFacilito.com
SET algo = inputecho 'alguna cosa: '

:launch
    python script.py
    echo El resultado se copio al portapapeles
    pause 
    goto:launch

pause