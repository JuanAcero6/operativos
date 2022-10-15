if [ -z "$1" ]; then
    echo "No se recibio un parametro"
else  
    echo "Antes de eliminar lineas"
    sed -i '/^$/d' $1
    value=`cat $1`
    echo "Despues de eliminar lineas"
    echo "$value"
fi