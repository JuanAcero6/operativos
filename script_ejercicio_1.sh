if [ -z "$1" ]; then
    echo "No se recibio un parametro"
else
    if [ -d "$1" ]; then
        echo "Es un directorio"
    else
        if [ -f "$1" ]; then
            echo "Es un archivo"
        else 
            echo "No es directorio ni archivo"
            exit 1
        fi
    fi
fi