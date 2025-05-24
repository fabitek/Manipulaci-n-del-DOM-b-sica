"""
Módulo de Sastrería: Funciones para gestionar medidas de clientes,
catálogo de sastrería, trabajos de sastrería y pagos a sastres.
"""
from typing import Dict, List, Optional, Tuple, Any

# Placeholder para simular una conexión a base de datos o ORM
# En una implementación real, esto sería manejado por un motor de BD.
# Por ejemplo: from database_connector import db_execute, db_query

# -------------------------------------
# 1. Gestión de Medidas del Cliente
# -------------------------------------

def registrar_medidas_cliente(id_cliente: int, fecha_medicion: str, medidas_dict: Dict[str, float]) -> Dict[str, Any]:
    """
    Registra un nuevo conjunto de medidas para un cliente específico.

    Interactúa con la tabla: MedidasCliente.

    Args:
        id_cliente: El ID del cliente.
        fecha_medicion: La fecha en que se tomaron las medidas (formato YYYY-MM-DD).
        medidas_dict: Un diccionario con las medidas, por ejemplo:
                      {'cuello': 38.5, 'pecho': 102.0, ...}.

    Returns:
        Un diccionario representando el registro de medidas creado, incluyendo su ID.
        Ejemplo: {'id_medida': 1, 'id_cliente': 1, 'fecha_medicion': '2023-10-26', ...}
    """
    print(f"Registrando medidas para cliente {id_cliente} en fecha {fecha_medicion} con datos: {medidas_dict}")
    # Lógica de base de datos (INSERT en MedidasCliente)
    # SELECT currval(pg_get_serial_sequence('medidascliente','id_medida')); para obtener el ID.
    return {
        "id_medida": 1, # ID simulado
        "id_cliente": id_cliente,
        "fecha_medicion": fecha_medicion,
        **medidas_dict,
        "observaciones": medidas_dict.get("observaciones", None)
    }

def obtener_medidas_cliente(id_cliente: int, fecha_medicion: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Obtiene los registros de medidas para un cliente.
    Si se proporciona fecha_medicion, busca un registro específico.
    Si no, devuelve todos los registros de medidas para ese cliente.

    Interactúa con la tabla: MedidasCliente.

    Args:
        id_cliente: El ID del cliente.
        fecha_medicion: (Opcional) La fecha específica de medición a buscar (YYYY-MM-DD).

    Returns:
        Una lista de diccionarios, donde cada diccionario es un registro de medidas.
        Si se busca por fecha y no se encuentra, devuelve lista vacía.
    """
    print(f"Obteniendo medidas para cliente {id_cliente}, fecha: {fecha_medicion if fecha_medicion else 'todas'}")
    # Lógica de base de datos (SELECT de MedidasCliente)
    if fecha_medicion:
        # SELECT * FROM MedidasCliente WHERE id_cliente = %s AND fecha_medicion = %s
        return [{
            "id_medida": 1, "id_cliente": id_cliente, "fecha_medicion": fecha_medicion,
            "cuello": 38.0, "pecho": 100.0 # ... y otras medidas
        }] # Ejemplo
    else:
        # SELECT * FROM MedidasCliente WHERE id_cliente = %s
        return [
            {"id_medida": 1, "id_cliente": id_cliente, "fecha_medicion": "2023-10-26", "cuello": 38.0},
            {"id_medida": 2, "id_cliente": id_cliente, "fecha_medicion": "2023-01-15", "cuello": 37.5}
        ] # Ejemplo

def actualizar_medidas_cliente(id_medida: int, nuevas_medidas_dict: Dict[str, Any]) -> Dict[str, Any]:
    """
    Actualiza un registro de medidas existente.

    Interactúa con la tabla: MedidasCliente.

    Args:
        id_medida: El ID del registro de medida a actualizar.
        nuevas_medidas_dict: Un diccionario con los campos y nuevos valores a actualizar.
                             Puede incluir 'fecha_medicion' o cualquier medida.

    Returns:
        Un diccionario representando el registro de medidas actualizado.
        O un diccionario con un error si no se encuentra el id_medida.
    """
    print(f"Actualizando medidas con ID {id_medida} con datos: {nuevas_medidas_dict}")
    # Lógica de base de datos (UPDATE en MedidasCliente WHERE id_medida = %s)
    # Debería verificar si el id_medida existe primero.
    return {
        "id_medida": id_medida,
        **nuevas_medidas_dict # Simula que se actualizaron los campos
    }

# -------------------------------------
# 2. Gestión de Catálogo de Sastrería
# -------------------------------------

def agregar_producto_sastreria(
    nombre: str,
    descripcion: str,
    precio_unitario: float,
    id_categoria_servicio: int, # Asumiendo que se pasa el ID de una categoría existente
    tipo_item: str = 'servicio',
    otros_detalles_dict: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Agrega un nuevo producto o servicio de sastrería al catálogo.
    Los servicios de sastrería son ítems en la tabla ProductosServicios.

    Interactúa con las tablas: ProductosServicios, CategoriasServicio (para validación de id_categoria_servicio).

    Args:
        nombre: Nombre del producto/servicio.
        descripcion: Descripción detallada.
        precio_unitario: Precio del servicio.
        id_categoria_servicio: ID de la categoría a la que pertenece (debe existir en CategoriasServicio).
        tipo_item: 'producto' o 'servicio'. Por defecto 'servicio' para sastrería.
        otros_detalles_dict: (Opcional) Otros campos como 'codigo_barras', 'imagen_url', 'disponible'.

    Returns:
        Un diccionario representando el producto/servicio creado, incluyendo su ID.
    """
    if otros_detalles_dict is None:
        otros_detalles_dict = {}
    print(f"Agregando producto/servicio de sastrería: {nombre}, precio: {precio_unitario}")
    # Lógica de base de datos (INSERT en ProductosServicios)
    # Validar que id_categoria_servicio existe en CategoriasServicio.
    # tipo_item debe ser uno de los valores del ENUM tipo_item_producto_servicio.
    return {
        "id_producto_servicio": 101, # ID simulado
        "nombre": nombre,
        "descripcion": descripcion,
        "precio_unitario": precio_unitario,
        "id_categoria_servicio": id_categoria_servicio,
        "tipo_item": tipo_item,
        "disponible": otros_detalles_dict.get("disponible", True),
        "codigo_barras": otros_detalles_dict.get("codigo_barras"),
        "imagen_url": otros_detalles_dict.get("imagen_url")
    }

def obtener_productos_sastreria(filtros: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """
    Obtiene una lista de productos/servicios de sastrería, opcionalmente filtrados.
    Se asume que los servicios de sastrería pueden tener una categoría específica.

    Interactúa con la tabla: ProductosServicios (y potencialmente CategoriasServicio para filtrar por categoría).

    Args:
        filtros: (Opcional) Un diccionario para filtrar resultados.
                 Ejemplos: {'id_categoria_servicio': 1, 'disponible': True, 'tipo_item': 'servicio'}

    Returns:
        Una lista de diccionarios, donde cada diccionario es un producto/servicio.
    """
    print(f"Obteniendo productos/servicios de sastrería con filtros: {filtros}")
    # Lógica de base de datos (SELECT de ProductosServicios)
    # Aplicar filtros si se proporcionan. Por ejemplo, WHERE tipo_item = 'servicio'
    # JOIN con CategoriasServicio si se filtra por nombre_categoria.
    return [
        {"id_producto_servicio": 101, "nombre": "Ajuste de Pantalón", "precio_unitario": 15.00, "tipo_item": "servicio"},
        {"id_producto_servicio": 102, "nombre": "Confección Camisa a Medida", "precio_unitario": 120.00, "tipo_item": "servicio"}
    ] # Ejemplo

def actualizar_producto_sastreria(id_producto_servicio: int, detalles_actualizados_dict: Dict[str, Any]) -> Dict[str, Any]:
    """
    Actualiza los detalles de un producto/servicio de sastrería existente.

    Interactúa con la tabla: ProductosServicios.

    Args:
        id_producto_servicio: El ID del producto/servicio a actualizar.
        detalles_actualizados_dict: Diccionario con los campos y nuevos valores.
                                    Ej: {'precio_unitario': 125.00, 'disponible': False}

    Returns:
        Un diccionario representando el producto/servicio actualizado.
        O un diccionario con un error si no se encuentra el id_producto_servicio.
    """
    print(f"Actualizando producto/servicio {id_producto_servicio} con datos: {detalles_actualizados_dict}")
    # Lógica de base de datos (UPDATE en ProductosServicios WHERE id_producto_servicio = %s)
    # Debería verificar si el id_producto_servicio existe.
    return {
        "id_producto_servicio": id_producto_servicio,
        **detalles_actualizados_dict # Simula que se actualizaron los campos
    }

# -------------------------------------------------------------
# 3. Gestión de Trabajos de Sastrería (dentro de un Pedido)
# -------------------------------------------------------------

def asignar_sastre_a_trabajo(id_detalle_pedido: int, id_sastre: int) -> Dict[str, Any]:
    """
    Asigna un sastre específico a un trabajo de sastrería en un detalle de pedido.
    Un "trabajo de sastrería" es un ítem en DetallesPedido que requiere un sastre.

    Interactúa con la tabla: DetallesPedido, Empleados (para validar rol de sastre).

    Args:
        id_detalle_pedido: El ID del detalle del pedido que representa el trabajo.
        id_sastre: El ID del empleado (sastre) a asignar.

    Returns:
        Un diccionario del detalle del pedido actualizado con el sastre asignado.
        O un error si el id_sastre no es un sastre válido o el id_detalle_pedido no existe.
    """
    print(f"Asignando sastre {id_sastre} al detalle de pedido {id_detalle_pedido}")
    # Lógica de base de datos:
    # 1. Validar que id_sastre corresponde a un empleado con rol 'sastre' (SELECT en Empleados).
    # 2. Validar que id_detalle_pedido existe y es un servicio que requiere sastre (SELECT en DetallesPedido JOIN ProductosServicios).
    # 3. UPDATE DetallesPedido SET id_sastre_asignado = %s WHERE id_detalle_pedido = %s.
    # 4. SELECT * FROM DetallesPedido WHERE id_detalle_pedido = %s.
    return {
        "id_detalle_pedido": id_detalle_pedido,
        "id_sastre_asignado": id_sastre,
        "status": "Sastre asignado"
        # ... otros campos del detalle del pedido
    }

def actualizar_estado_trabajo_sastreria(
    id_detalle_pedido: int,
    estado: str, # Podría ser un ENUM en el futuro ('pendiente_sastre', 'en_proceso_sastre', 'finalizado_sastre')
    fecha_inicio: Optional[str] = None,
    fecha_fin: Optional[str] = None
) -> Dict[str, Any]:
    """
    Actualiza el estado de un trabajo de sastrería y opcionalmente sus fechas de inicio/fin.
    El estado podría ser una columna específica en DetallesPedido o manejado a través de notas/fechas.

    Interactúa con la tabla: DetallesPedido.

    Args:
        id_detalle_pedido: El ID del detalle del pedido (trabajo de sastrería).
        estado: Nuevo estado del trabajo (ej: "en_proceso_sastre", "finalizado_sastre").
        fecha_inicio: (Opcional) Fecha de inicio del trabajo (YYYY-MM-DD HH:MM:SS).
        fecha_fin: (Opcional) Fecha de finalización del trabajo (YYYY-MM-DD HH:MM:SS).

    Returns:
        Un diccionario del detalle del pedido actualizado.
    """
    print(f"Actualizando estado del trabajo {id_detalle_pedido} a '{estado}'")
    # Lógica de base de datos (UPDATE en DetallesPedido).
    # Puede que se necesite actualizar campos como:
    # estado_sastreria (si existiera), fecha_inicio_trabajo_sastreria, fecha_fin_trabajo_sastreria.
    update_data = {"estado_sastreria_simulado": estado}
    if fecha_inicio:
        update_data["fecha_inicio_trabajo_sastreria"] = fecha_inicio
    if fecha_fin:
        update_data["fecha_fin_trabajo_sastreria"] = fecha_fin

    return {
        "id_detalle_pedido": id_detalle_pedido,
        **update_data
        # ... otros campos del detalle del pedido
    }

def registrar_fechas_trabajo_sastreria(
    id_detalle_pedido: int,
    fecha_inicio: Optional[str] = None,
    fecha_fin: Optional[str] = None
) -> Dict[str, Any]:
    """
    Registra o actualiza las fechas de inicio y/o fin de un trabajo de sastrería.

    Interactúa con la tabla: DetallesPedido.

    Args:
        id_detalle_pedido: El ID del detalle del pedido.
        fecha_inicio: (Opcional) Fecha de inicio del trabajo (YYYY-MM-DD HH:MM:SS o YYYY-MM-DD).
        fecha_fin: (Opcional) Fecha de finalización del trabajo (YYYY-MM-DD HH:MM:SS o YYYY-MM-DD).

    Returns:
        Un diccionario del detalle del pedido actualizado con las fechas.
    """
    print(f"Registrando fechas para trabajo {id_detalle_pedido}: Inicio {fecha_inicio}, Fin {fecha_fin}")
    # Lógica de base de datos (UPDATE en DetallesPedido).
    # UPDATE DetallesPedido SET fecha_inicio_trabajo_sastreria = %s, fecha_fin_trabajo_sastreria = %s
    # WHERE id_detalle_pedido = %s.
    # Solo actualizar las fechas proporcionadas.
    updated_fields = {}
    if fecha_inicio:
        updated_fields["fecha_inicio_trabajo_sastreria"] = fecha_inicio
    if fecha_fin:
        updated_fields["fecha_fin_trabajo_sastreria"] = fecha_fin

    if not updated_fields:
        # Devolver el registro actual si no hay nada que actualizar o manejar como error/advertencia
        return {"id_detalle_pedido": id_detalle_pedido, "mensaje": "No se proporcionaron fechas para actualizar."}

    return {
        "id_detalle_pedido": id_detalle_pedido,
        **updated_fields
        # ... otros campos
    }

# -------------------------------------
# 4. Gestión de Pagos a Sastres
# -------------------------------------

def registrar_pago_sastre(
    id_detalle_pedido: int,
    id_sastre: int,
    monto_pagado: float,
    fecha_pago: str, # YYYY-MM-DD
    metodo_pago: str, # Podría ser un ENUM: 'efectivo', 'transferencia', etc.
    notas: Optional[str] = None
) -> Dict[str, Any]:
    """
    Registra un pago realizado a un sastre por un trabajo específico.

    Interactúa con la tabla: PagosSastre.
    También podría consultar DetallesPedido para validar el trabajo y Empleados para validar el sastre.

    Args:
        id_detalle_pedido: ID del detalle del pedido por el cual se paga.
        id_sastre: ID del sastre que recibe el pago.
        monto_pagado: Cantidad pagada.
        fecha_pago: Fecha del pago (YYYY-MM-DD).
        metodo_pago: Método de pago utilizado.
        notas: (Opcional) Notas adicionales sobre el pago.

    Returns:
        Un diccionario representando el registro de pago creado.
    """
    print(f"Registrando pago de {monto_pagado} al sastre {id_sastre} por trabajo {id_detalle_pedido}")
    # Lógica de base de datos:
    # 1. Validar que id_detalle_pedido existe y está asociado a id_sastre (o que id_sastre es el asignado).
    # 2. INSERT en PagosSastre.
    return {
        "id_pago_sastre": 501, # ID simulado
        "id_detalle_pedido": id_detalle_pedido,
        "id_sastre": id_sastre,
        "monto_pagado": monto_pagado,
        "fecha_pago": fecha_pago,
        "metodo_pago": metodo_pago,
        "notas": notas
    }

def obtener_pagos_sastre(
    id_sastre: Optional[int] = None,
    id_detalle_pedido: Optional[int] = None,
    rango_fechas: Optional[Tuple[str, str]] = None # (fecha_inicio_str, fecha_fin_str)
) -> List[Dict[str, Any]]:
    """
    Obtiene una lista de pagos realizados a sastres, con filtros opcionales.

    Interactúa con la tabla: PagosSastre.
    Podría hacer JOIN con DetallesPedido y Empleados para más detalles.

    Args:
        id_sastre: (Opcional) Filtrar pagos por ID de sastre.
        id_detalle_pedido: (Opcional) Filtrar pagos por ID de detalle de pedido.
        rango_fechas: (Opcional) Tupla (fecha_inicio_str, fecha_fin_str) para filtrar por fecha de pago.

    Returns:
        Una lista de diccionarios, donde cada diccionario es un registro de pago.
    """
    print(f"Obteniendo pagos a sastres. Filtros: Sastre ID {id_sastre}, Detalle Pedido ID {id_detalle_pedido}, Fechas {rango_fechas}")
    # Lógica de base de datos (SELECT de PagosSastre)
    # Aplicar filtros según los argumentos.
    # Ejemplo: SELECT ps.*, e.nombre as nombre_sastre, dp.descripcion_trabajo
    # FROM PagosSastre ps
    # JOIN Empleados e ON ps.id_sastre = e.id_empleado
    # JOIN DetallesPedido dp ON ps.id_detalle_pedido = dp.id_detalle_pedido
    # WHERE (ps.id_sastre = %s OR %s IS NULL) AND ...
    return [
        {"id_pago_sastre": 501, "id_detalle_pedido": 201, "id_sastre": 3, "monto_pagado": 50.00, "fecha_pago": "2023-10-25"},
        {"id_pago_sastre": 502, "id_detalle_pedido": 202, "id_sastre": 3, "monto_pagado": 75.00, "fecha_pago": "2023-10-28"}
    ] # Ejemplo
