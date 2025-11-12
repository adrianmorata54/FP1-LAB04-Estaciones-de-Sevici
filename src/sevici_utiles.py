from collections import namedtuple
from math import sqrt

EstacionSevici = namedtuple("EstacionSevici", 
    "nombre, direccion, latitud, longitud, capacidad, puestos_libres, bicicletas_disponibles")

def selecciona_color(estacion:EstacionSevici) -> str:
    """
    Devuelve el color en que debe pintarse cada estación según su disponibilidad.

    Parámetros:
    estacion: EstacionSevici

    Devuelve:
    str: "green", "orange", "red" o "gray"
    """
    # TODO: Ejercicio 1
    if estacion.bicicletas_disponibles == 0 or estacion.capacidad == 0:
        return 'gray'
    
    disponibilidad = estacion.bicicletas_disponibles/estacion.capacidad

    if disponibilidad >= 2/3:
        return 'green'
    elif disponibilidad >= 1/3:
        return 'orange'
    elif disponibilidad < 1/3 and disponibilidad > 0:
        return 'red'

def calcula_estadisticas(estaciones: list[EstacionSevici]) -> tuple[int, int, float, int]:
    """
    Calcula estadísticas de las estaciones.
    Parametros:
    estaciones: lista de EstacionSevici
    Devuelve:
    tupla con (total de bicicletas libres, total de capacidad, porcentaje de ocupación, total de estaciones)
    """
    # TODO: Ejercicio 2
    total_bicis_libres = 0
    total_capacidad = 0
    total_estaciones = len(estaciones)
    for e in estaciones:
        total_bicis_libres += e.bicicletas_disponibles
        total_capacidad += e.capacidad
    if total_capacidad == 0:
        porcentaje_ocupacion = 0.0
    else:
        porcentaje_ocupacion = (1-total_bicis_libres/total_capacidad)*100
    return (total_bicis_libres, total_capacidad, porcentaje_ocupacion, total_estaciones)

def busca_estaciones_direccion(estaciones: list[EstacionSevici], direccion_parcial: str) -> list[EstacionSevici]:
    """
    Busca las estaciones que contengan en su dirección (subcadena, sin distinguir mayúsculas/minúsculas) la dirección parcial dada.    

    Parametros:
    estaciones: lista de EstacionSevici
    direccion_parcial: subcadena a buscar en la dirección de las estaciones

    Devuelve:
    lista de EstacionSevici que cumplen el criterio
    """
    # TODO: Ejercicio 3
    lista = list()
    for e in estaciones:
        direccion_parcial = str(direccion_parcial)
        if direccion_parcial in e.direccion or direccion_parcial in e.direccion.lower():
            lista.append(e)
    return lista


def busca_estaciones_con_disponibilidad(estaciones:list[EstacionSevici], min_disponibilidad: float = 0.5) -> list[EstacionSevici]:
    """
    Devuelve una lista de EstacionSevici con al menos el porcentaje mínimo de bicicletas disponible
    indicado.

    Parametros:
    estaciones: lista de EstacionSevici
    min_disponibilidad: porcentaje mínimo de bicicletas disponibles (0.0 a 1.0)
    
    Devuelve:
    lista de EstacionSevici
    """
    # TODO: Ejercicio 4
    lista = []
    for e in estaciones:
        if e.capacidad == 0:
            porcentaje = 0.0
        else:
            porcentaje = e.bicicletas_disponibles/e.capacidad
        if min_disponibilidad < porcentaje:
            lista.append(e)
    return lista

 
def calcula_distancia(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """
    Calcula la distancia euclídea entre dos puntos (latitud, longitud).

    Parámetros:
    p1: tupla (latitud, longitud) del primer punto
    p2: tupla (latitud, longitud) del segundo punto

    Devuelve:
    float: distancia euclídea entre los dos puntos
    """
    # TODO: Ejercicio 5
    distancia = sqrt((p2[0]- p1[0])**2 + (p2[1]- p1[1])**2)
    return distancia
    

def busca_estacion_mas_cercana(estaciones:list[EstacionSevici], punto:tuple[float, float]) -> EstacionSevici | None:
    """
    Devuelve la estación más cercana al punto dado (latitud, longitud) que tenga al menos una bicicleta disponible.
    
    Parametros:
    estaciones: lista de EstacionSevici
    punto: tupla (latitud, longitud)

    Devuelve:
    EstacionSevici más cercana con al menos una bicicleta disponible, o None si no hay ninguna.
    """ 
    # TODO: Ejercicio 5
    mejor_estacion = None
    mejor_dist = None
    for e in estaciones:
        if e.bicicletas_disponibles <= 0:
            continue
        d = calcula_distancia((e.latitud, e.longitud), punto)
        if mejor_estacion is None or d < mejor_dist:
            mejor_estacion = e
            mejor_dist = d
    return mejor_estacion


def calcula_ruta(estaciones:list[EstacionSevici], origen:tuple[float, float], destino:tuple[float, float]) -> tuple[EstacionSevici | None, EstacionSevici | None]   :
    """
    Devuelve las estaciones más cercanas al punto de origen y destino dados, que tengan al menos una bicicleta disponible.

    Parametros: 
    estaciones: lista de EstacionSevici
    origen: tupla (latitud, longitud) del punto de origen
    destino: tupla (latitud, longitud) del punto de destino

    Devuelve:
    tupla con (estacion_origen, estacion_destino)
    """
    # TODO: Ejercicio 5
    posibilidades = busca_estaciones_con_disponibilidad(estaciones, 0.00000001)
    estacion_final = busca_estacion_mas_cercana(posibilidades, destino)
    estacion_origen = busca_estacion_mas_cercana(posibilidades, origen)
    return [estacion_origen, estacion_final]

