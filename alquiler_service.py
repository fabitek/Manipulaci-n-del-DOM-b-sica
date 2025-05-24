"""
Módulo de Alquiler: Funciones para gestionar el inventario de artículos de alquiler,
las transacciones de alquiler (registro, devolución) y el catálogo de productos de alquiler.
"""
from typing import Dict, List, Optional, Any

# Placeholder para simular una conexión a base de datos o ORM
# En una implementación real, esto sería manejado por un motor de BD.
# Por ejemplo: from database_connector import db_execute, db_query

# -------------------------------------------
# 1. Gestión de Inventario de Alquiler
# -------------------------------------------

def agregar_item_alquiler(
    id_producto_servicio: int,
    codigo_item_unico: str,
    valor_deposito_requerido: float,
    fecha_adquisicion: Optional[str] = None, # YYYY-MM-DD
    notas_item: Optional[str] = None,
    estado_inicial: str = 'disponible' # Usar valor del ENUM estado_item_alquiler_enum
) -> Dict[str, Any]:
    """
    Agrega un nuevo ítem físico al inventario de alquiler.
    Cada ítem es una instancia única de un ProductoServicio que es alquilable.

    Interactúa con las tablas: InventarioAlquiler, ProductosServicios (para validar id_producto_servicio).

    Args:
        id_producto_servicio: ID del producto/servicio general al que pertenece este ítem.
        codigo_item_unico: Código único para identificar este ítem físico (ej: TRAJE-001-AZUL-T42).
        valor_deposito_requerido: Monto del depósito necesario para alquilar este ítem.
        fecha_adquisicion: (Opcional) Fecha en que se adquirió el ítem (YYYY-MM-DD).
        notas_item: (Opcional) Notas adicionales sobre el ítem.
        estado_inicial: (Opcional) Estado inicial del ítem, por defecto 'disponible'.
                        Debe ser un valor del ENUM estado_item_alquiler_enum.

    Returns:
        Un diccionario representando el ítem de alquiler creado, incluyendo su ID.
        Ejemplo: {'id_item_alquiler': 1, 'codigo_item_unico': 'TRAJE-001-AZUL-T42', ...}
    """
    print(f"Agregando ítem de alquiler: {codigo_item_unico} para producto ID {id_producto_servicio}")
    # Lógica de base de datos (INSERT en InventarioAlquiler)
    # Validar que id_producto_servicio existe en ProductosServicios y es de tipo alquilable.
    # Validar que 'estado_inicial' sea un valor válido del ENUM 'estado_item_alquiler_enum'.
    return {
        "id_item_alquiler": 1, # ID simulado
        "id_producto_servicio": id_producto_servicio,
        "codigo_item_unico": codigo_item_unico,
        "estado_item": estado_inicial,
        "fecha_adquisicion": fecha_adquisicion,
        "valor_deposito_requerido": valor_deposito_requerido,
        "notas_item": notas_item
    }

def obtener_items_alquiler(filtros: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """
    Obtiene una lista de ítems de alquiler del inventario, opcionalmente filtrados.

    Interactúa con la tabla: InventarioAlquiler.
    Potencialmente JOIN con ProductosServicios para obtener detalles del producto.

    Args:
        filtros: (Opcional) Un diccionario para filtrar resultados.
                 Ejemplos: {'id_producto_servicio': 10, 'estado_item': 'disponible'}

    Returns:
        Una lista de diccionarios, donde cada diccionario es un ítem de alquiler.
    """
    print(f"Obteniendo ítems de alquiler con filtros: {filtros}")
    # Lógica de base de datos (SELECT de InventarioAlquiler)
    # Aplicar filtros si se proporcionan.
    # JOIN con ProductosServicios para incluir nombre del producto, etc.
    # Ejemplo: SELECT ia.*, ps.nombre as nombre_producto
    # FROM InventarioAlquiler ia JOIN ProductosServicios ps ON ia.id_producto_servicio = ps.id_producto_servicio
    return [
        {"id_item_alquiler": 1, "id_producto_servicio": 10, "nombre_producto": "Traje Formal Azul", "codigo_item_unico": "TRAJE-001", "estado_item": "disponible"},
        {"id_item_alquiler": 2, "id_producto_servicio": 10, "nombre_producto": "Traje Formal Azul", "codigo_item_unico": "TRAJE-002", "estado_item": "alquilado"}
    ] # Ejemplo

def actualizar_item_alquiler(id_item_alquiler: int, detalles_actualizados_dict: Dict[str, Any]) -> Dict[str, Any]:
    """
    Actualiza los detalles de un ítem de alquiler existente en el inventario.

    Interactúa con la tabla: InventarioAlquiler.

    Args:
        id_item_alquiler: El ID del ítem de alquiler a actualizar.
        detalles_actualizados_dict: Diccionario con los campos y nuevos valores.
                                    Ej: {'estado_item': 'en_mantenimiento', 'notas_item': 'Requiere limpieza'}
                                    Asegurarse que 'estado_item' sea un valor del ENUM 'estado_item_alquiler_enum'.

    Returns:
        Un diccionario representando el ítem de alquiler actualizado.
        O un diccionario con un error si no se encuentra el id_item_alquiler.
    """
    print(f"Actualizando ítem de alquiler {id_item_alquiler} con datos: {detalles_actualizados_dict}")
    # Lógica de base de datos (UPDATE en InventarioAlquiler WHERE id_item_alquiler = %s)
    # Validar que 'estado_item' (si se provee) sea un valor válido del ENUM.
    # Debería verificar si el id_item_alquiler existe.
    return {
        "id_item_alquiler": id_item_alquiler,
        **detalles_actualizados_dict # Simula que se actualizaron los campos
    }

def consultar_disponibilidad_item(
    id_producto_servicio: int,
    fecha_inicio_deseada: str, # YYYY-MM-DD
    fecha_fin_deseada: str # YYYY-MM-DD
) -> List[Dict[str, Any]]:
    """
    Consulta la disponibilidad de ítems específicos de un producto de alquiler
    para un rango de fechas deseado.

    Interactúa con: InventarioAlquiler, DetallesPedido (para ver alquileres activos o futuros).

    Args:
        id_producto_servicio: El ID del producto general que se desea alquilar.
        fecha_inicio_deseada: Fecha de inicio del alquiler deseado.
        fecha_fin_deseada: Fecha de fin del alquiler deseado.

    Returns:
        Una lista de diccionarios, cada uno representando un ítem de InventarioAlquiler
        que está disponible en esas fechas. Incluye 'id_item_alquiler', 'codigo_item_unico'.
        Lista vacía si no hay ninguno disponible.
    """
    print(f"Consultando disponibilidad para producto {id_producto_servicio} de {fecha_inicio_deseada} a {fecha_fin_deseada}")
    # Lógica de base de datos:
    # 1. Encontrar todos los items en InventarioAlquiler para el id_producto_servicio.
    # 2. Para cada item, verificar en DetallesPedido si existe algún alquiler activo o futuro
    #    cuyas fechas (fecha_alquiler_inicio, fecha_alquiler_fin_esperada) se solapen
    #    con el rango [fecha_inicio_deseada, fecha_fin_deseada].
    #    Un item está ocupado si:
    #    NOT (dp.fecha_alquiler_fin_esperada < fecha_inicio_deseada OR dp.fecha_alquiler_inicio > fecha_fin_deseada)
    # 3. Devolver la lista de items de InventarioAlquiler que NO estén ocupados y cuyo estado_item sea 'disponible'.
    return [
        {"id_item_alquiler": 1, "codigo_item_unico": "TRAJE-001", "id_producto_servicio": id_producto_servicio, "estado_item": "disponible"},
        # ... otros items disponibles
    ] # Ejemplo

# -------------------------------------------
# 2. Gestión de Alquileres (Transacciones)
# -------------------------------------------

def registrar_alquiler(id_detalle_pedido: int, deposito_recibido: float) -> Dict[str, Any]:
    """
    Registra la formalización de un alquiler para un ítem específico en un detalle de pedido.
    Esto se hace después de que un ítem de alquiler ha sido asignado a un DetallesPedido.
    Crea una entrada en la tabla Alquileres.

    Interactúa con: Alquileres, DetallesPedido (para obtener id_item_alquiler y validar).
                   InventarioAlquiler (para actualizar estado del ítem a 'alquilado').

    Args:
        id_detalle_pedido: El ID del detalle del pedido que incluye el ítem de alquiler.
        deposito_recibido: El monto del depósito recibido por el ítem.

    Returns:
        Un diccionario representando el registro de alquiler creado.
        Ejemplo: {'id_alquiler': 1, 'id_detalle_pedido': 15, 'deposito_recibido': 50.00, ...}
    """
    print(f"Registrando alquiler para detalle de pedido {id_detalle_pedido}, depósito: {deposito_recibido}")
    # Lógica de base de datos:
    # 1. Validar que id_detalle_pedido existe y tiene un id_item_alquiler asignado.
    #    SELECT id_item_alquiler FROM DetallesPedido WHERE id_detalle_pedido = %s.
    # 2. INSERT en Alquileres (id_detalle_pedido, deposito_recibido).
    # 3. UPDATE InventarioAlquiler SET estado_item = 'alquilado' WHERE id_item_alquiler = [el ID del paso 1].
    # 4. (Opcional) Actualizar fechas en DetallesPedido: fecha_alquiler_inicio = CURRENT_TIMESTAMP.
    return {
        "id_alquiler": 1, # ID simulado
        "id_detalle_pedido": id_detalle_pedido,
        "deposito_recibido": deposito_recibido,
        "deposito_devuelto": 0.00,
        "penalizacion_aplicada": 0.00
    }

def registrar_devolucion_alquiler(
    id_detalle_pedido: int,
    fecha_devolucion_real: str, # YYYY-MM-DD HH:MM:SS
    condicion_devolucion: str,
    penalizacion_calculada: float = 0.0,
    deposito_a_devolver: float = 0.0
) -> Dict[str, Any]:
    """
    Registra la devolución de un ítem alquilado.
    Actualiza el registro en Alquileres y el estado del ítem en InventarioAlquiler.

    Interactúa con: Alquileres, DetallesPedido (para actualizar fecha_alquiler_devolucion_real),
                   InventarioAlquiler (para actualizar estado del ítem, ej: 'disponible' o 'en_mantenimiento').

    Args:
        id_detalle_pedido: ID del detalle del pedido asociado al alquiler.
        fecha_devolucion_real: Fecha y hora de la devolución.
        condicion_devolucion: Descripción del estado del ítem al ser devuelto.
        penalizacion_calculada: Monto de penalización si aplica (calculado previamente).
        deposito_a_devolver: Monto del depósito que se devuelve al cliente.

    Returns:
        Un diccionario representando el registro de alquiler actualizado.
    """
    print(f"Registrando devolución para detalle pedido {id_detalle_pedido}, fecha: {fecha_devolucion_real}")
    # Lógica de base de datos:
    # 1. Validar que existe un alquiler para id_detalle_pedido (SELECT en Alquileres).
    # 2. UPDATE Alquileres SET deposito_devuelto = %s, penalizacion_aplicada = %s, condicion_devolucion = %s
    #    WHERE id_detalle_pedido = %s.
    # 3. UPDATE DetallesPedido SET fecha_alquiler_devolucion_real = %s WHERE id_detalle_pedido = %s.
    # 4. Determinar nuevo estado para InventarioAlquiler (ej: 'disponible' si condicion_devolucion es buena,
    #    'en_mantenimiento' si está dañado).
    #    SELECT id_item_alquiler FROM DetallesPedido WHERE id_detalle_pedido = %s.
    #    UPDATE InventarioAlquiler SET estado_item = [nuevo_estado] WHERE id_item_alquiler = ...
    return {
        "id_alquiler": 1, # ID simulado del alquiler existente
        "id_detalle_pedido": id_detalle_pedido,
        "fecha_devolucion_real": fecha_devolucion_real,
        "condicion_devolucion": condicion_devolucion,
        "penalizacion_aplicada": penalizacion_calculada,
        "deposito_devuelto": deposito_a_devolver,
        "mensaje": "Devolución registrada."
    }

def calcular_penalizacion_alquiler(id_detalle_pedido: int, fecha_devolucion_real: str) -> float:
    """
    Calcula la penalización por devolución tardía u otros factores.
    Este es un cálculo, no guarda nada en BD directamente, pero puede ser usado por otras funciones.

    Interactúa con: DetallesPedido (para obtener fecha_alquiler_fin_esperada),
                   ProductosServicios (para obtener precio_unitario que podría ser base para la penalización).

    Args:
        id_detalle_pedido: ID del detalle del pedido asociado al alquiler.
        fecha_devolucion_real: Fecha y hora de la devolución.

    Returns:
        El monto de la penalización calculada.
    """
    print(f"Calculando penalización para detalle pedido {id_detalle_pedido}, devolución: {fecha_devolucion_real}")
    # Lógica de cálculo:
    # 1. Obtener fecha_alquiler_fin_esperada de DetallesPedido.
    # 2. Comparar con fecha_devolucion_real.
    # 3. Si fecha_devolucion_real > fecha_alquiler_fin_esperada, calcular días de retraso.
    # 4. Obtener el precio_unitario (precio_alquiler_dia) del ProductosServicios asociado.
    # 5. Penalización podría ser: dias_retraso * precio_alquiler_dia * factor_penalizacion (ej: 1.5).
    #    Otras reglas podrían aplicar (daños, etc., aunque eso se manejaría más en 'condicion_devolucion').
    return 10.0 # Ejemplo de penalización
# -------------------------------------------
# 3. Gestión de Catálogo de Alquiler
# -------------------------------------------

def agregar_producto_alquiler(
    nombre: str,
    descripcion: str,
    precio_unitario_alquiler_dia: float,
    id_categoria_servicio: int,
    otros_detalles_dict: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Agrega un nuevo tipo de producto que se puede alquilar al catálogo general.
    Estos son los "modelos" de los ítems, no los ítems físicos.
    Son registros en ProductosServicios con tipo_item='producto' (o un tipo específico para alquiler).

    Interactúa con: ProductosServicios, CategoriasServicio.

    Args:
        nombre: Nombre del producto de alquiler (ej: "Traje Formal Azul Marino").
        descripcion: Descripción detallada.
        precio_unitario_alquiler_dia: Precio de alquiler por día para este tipo de producto.
        id_categoria_servicio: ID de la categoría a la que pertenece (debe existir en CategoriasServicio).
        otros_detalles_dict: (Opcional) Otros campos como 'codigo_barras', 'imagen_url', 'disponible'.
                             El campo 'tipo_item' se puede manejar internamente como 'producto' o uno específico.

    Returns:
        Un diccionario representando el producto de alquiler creado en el catálogo.
    """
    if otros_detalles_dict is None:
        otros_detalles_dict = {}
    print(f"Agregando producto de alquiler: {nombre}, precio día: {precio_unitario_alquiler_dia}")
    # Lógica de base de datos (INSERT en ProductosServicios)
    # Validar que id_categoria_servicio existe.
    # Establecer tipo_item a 'producto' o un ENUM específico si se diferencia de venta.
    # 'precio_unitario' en la tabla se interpretaría como precio_alquiler_dia para estos items.
    return {
        "id_producto_servicio": 301, # ID simulado
        "id_categoria_servicio": id_categoria_servicio,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio_unitario": precio_unitario_alquiler_dia, # Mapeado a precio_unitario
        "tipo_item": "producto", # O un tipo específico como 'alquiler_producto'
        "disponible": otros_detalles_dict.get("disponible", True),
        "codigo_barras": otros_detalles_dict.get("codigo_barras"),
        "imagen_url": otros_detalles_dict.get("imagen_url")
    }

def obtener_productos_alquiler(filtros: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """
    Obtiene una lista de tipos de productos de alquiler del catálogo, opcionalmente filtrados.

    Interactúa con: ProductosServicios.

    Args:
        filtros: (Opcional) Un diccionario para filtrar resultados.
                 Ejemplos: {'id_categoria_servicio': 3, 'disponible': True}
                 Implícitamente, se debería filtrar por tipo_item que identifica productos de alquiler.

    Returns:
        Una lista de diccionarios, donde cada diccionario es un tipo de producto de alquiler.
    """
    print(f"Obteniendo productos de alquiler con filtros: {filtros}")
    # Lógica de base de datos (SELECT de ProductosServicios)
    # Aplicar filtros. Importante: WHERE tipo_item = 'producto' (o el tipo para alquiler).
    return [
        {"id_producto_servicio": 301, "nombre": "Traje Formal Azul Marino", "precio_unitario": 50.00, "tipo_item": "producto"},
        {"id_producto_servicio": 302, "nombre": "Vestido de Gala Rojo", "precio_unitario": 70.00, "tipo_item": "producto"}
    ] # Ejemplo

def actualizar_producto_alquiler(id_producto_servicio: int, detalles_actualizados_dict: Dict[str, Any]) -> Dict[str, Any]:
    """
    Actualiza los detalles de un tipo de producto de alquiler en el catálogo.

    Interactúa con: ProductosServicios.

    Args:
        id_producto_servicio: El ID del producto de alquiler a actualizar.
        detalles_actualizados_dict: Diccionario con los campos y nuevos valores.
                                    Ej: {'precio_unitario_alquiler_dia': 55.00, 'disponible': False}
                                    (el precio se mapearía a 'precio_unitario' en la tabla).

    Returns:
        Un diccionario representando el producto de alquiler actualizado.
    """
    print(f"Actualizando producto de alquiler {id_producto_servicio} con datos: {detalles_actualizados_dict}")
    # Lógica de base de datos (UPDATE en ProductosServicios WHERE id_producto_servicio = %s)
    # Asegurarse que el producto es de tipo alquiler.
    # Mapear 'precio_unitario_alquiler_dia' a 'precio_unitario' si es necesario.
    if 'precio_unitario_alquiler_dia' in detalles_actualizados_dict:
        detalles_actualizados_dict['precio_unitario'] = detalles_actualizados_dict.pop('precio_unitario_alquiler_dia')

    return {
        "id_producto_servicio": id_producto_servicio,
        **detalles_actualizados_dict # Simula que se actualizaron los campos
    }
