#!/bin/bash

echo "Apa yang ingin didownload? (Video/Audio)"
PS3="Pilih 1 jika video, pilih 2 jika audio -> "

select tipe in Video Audio
do
    case $tipe in
        "Video")
            source /path/to/venv/folder/bin/activate 
            python3 YTDLv.py
            ffmpeg -i "$(ls | grep .mp4)" -i "$(ls | grep .webm)" -c:v copy -c:a aac "$(ls | sed -n 's/\.webm$//p')".mp4
            rm *.webm
            rm TEMP*
            echo "Selesai"
            break;;
        "Audio")
            source /path/to/venv/folder/bin/activate 
            python3 YTDLa.py
            ffmpeg -i "$(ls | grep .webm)" -b:a 192k "$(ls | sed -n 's/\.webm$//p')".mp3
            rm *.webm
            echo "Selesai"
            break;;
        *)
            echo "Maksud??!";;
    esac
done
