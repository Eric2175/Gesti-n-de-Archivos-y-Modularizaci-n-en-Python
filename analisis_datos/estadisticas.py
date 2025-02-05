# estadisticas.py
def media(datos):
    """Esta función calcula la media aritmética con valores numéricos

    Args:
        datos (Lista): Lista de números

    Returns:
        Float
    """
    return sum(datos) / len(datos)

def calcular_mediana(datos):
    """Calcula la mediana

    Args:
        datos (Lista): Lista de números

    Returns:
        Float: da la mediana de una lista
    """
    datos_sorted = sorted(datos)
    n = len(datos)
    mid = n // 2
    if n % 2 == 0:
        return (datos_sorted[mid - 1] + datos_sorted[mid]) / 2.0
    else:
        return datos_sorted[mid]