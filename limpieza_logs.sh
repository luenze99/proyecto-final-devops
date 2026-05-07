#!/bin/bash
echo "Limpieza de logs..."
find ~/environment -name "*.log" -type f -mtime +7 -delete
echo "Limpieza finalizada"
