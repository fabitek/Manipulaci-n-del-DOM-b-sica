"""
Módulo de Punto de Venta Integrado (POS): Funciones para gestionar la creación
y modificación de pedidos, búsqueda de clientes y productos, y la finalización
de pedidos para el proceso de pago.
"""
from typing import Dict, List, Optional, Any

# Placeholder para simular una conexión a base de datos o ORM
# En una implementación real, esto sería manejado por un motor de BD.
# Por ejemplo: from database_connector import db_execute, db_query

# Asumimos que los otros módulos de servicio podrían ser importados si es necesario
# para una lógica más compleja, ej:
# from sastreria_service import registrar_medidas_cliente
# from alquiler_service import consultar_disponibilidad_item
# from pagos_service import iniciar_pago_nequi

# -------------------------------------------
# 1. Gestión de Pedidos (Órdenes)
# -------------------------------------------

def crear_nuevo_pedido(
    id_cliente: int,
    id_empleado_creador: int,
    notas_pedido: Optional[str] = None
) -> Dict[str, Any]:
    """
    Crea un nuevo pedido (orden) en el sistema.

    Interactúa con las tablas: Pedidos.
    Valida contra Clientes (id_cliente) y Empleados (id_empleado_creador).

    Args:
        id_cliente: ID del cliente que realiza el pedido.
        id_empleado_creador: ID del empleado que crea el pedido.
        notas_pedido: (Opcional) Notas adicionales para el pedido.

    Returns:
        Un diccionario representando el pedido creado, incluyendo su ID.
        Ejemplo: {'id_pedido': 101, 'id_cliente': 1, 'id_empleado_creador': 2, 'estado_pedido': 'pendiente', ...}
    """
    print(f"Creando nuevo pedido para cliente {id_cliente} por empleado {id_empleado_creador}")
    # Lógica de base de datos:
    # 1. Validar id_cliente.
    # 2. Validar id_empleado_creador.
    # 3. INSERT en Pedidos con estado_pedido inicial ('pendiente' o similar).
    #    total_pedido y total_abonado se inicializan en 0.00.
    return {
        "id_pedido": 101, # ID simulado
        "id_cliente": id_cliente,
        "id_empleado_creador": id_empleado_creador,
        "fecha_creacion": "2023-10-31T09:00:00", # Simulación CURRENT_TIMESTAMP
        "fecha_entrega_estimada": None,
        "fecha_entrega_real": None,
        "estado_pedido": "pendiente", # Valor del ENUM estado_pedido_enum
        "total_pedido": 0.00,
        "total_abonado": 0.00,
        "notas_pedido": notas_pedido
    }

def agregar_item_a_pedido(
    id_pedido: int,
    id_producto_servicio: int,
    cantidad: int,
    detalles_especificos_item: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Agrega un ítem (producto o servicio) a un pedido existente.
    Calcula el subtotal y actualiza el total del pedido.

    Interactúa con las tablas: DetallesPedido, ProductosServicios (para obtener precio), Pedidos (para actualizar total).

    Podría llamar a funciones de otros servicios para lógicas específicas:
    - `alquiler_service.consultar_disponibilidad_item` si es un item de alquiler.
    - `sastreria_service` si es un servicio de sastrería que requiere medidas o asignación.

    Args:
        id_pedido: ID del pedido al que se agregará el ítem.
        id_producto_servicio: ID del producto/servicio a agregar.
        cantidad: Cantidad del producto/servicio.
        detalles_especificos_item: (Opcional) Diccionario con detalles adicionales para el ítem.
            Ej: Para sastrería: {'id_sastre_asignado': 5, 'medidas_ref': 12}
                Para alquiler: {'id_item_alquiler': 3, 'fecha_alquiler_inicio': 'YYYY-MM-DD', 'fecha_alquiler_fin_esperada': 'YYYY-MM-DD'}
                Para lavandería: {'etiqueta_lavanderia': 'LAV-001'}

    Returns:
        Un diccionario representando el detalle del pedido creado.
        Ejemplo: {'id_detalle_pedido': 501, 'id_pedido': 101, 'id_producto_servicio': 20, 'subtotal': 100.00, ...}
    """
    if detalles_especificos_item is None:
        detalles_especificos_item = {}
    print(f"Agregando item {id_producto_servicio} (cantidad {cantidad}) al pedido {id_pedido}")

    # Lógica de base de datos y de negocio:
    # 1. Validar id_pedido (existe y no está en estado final como 'completado' o 'cancelado').
    # 2. Validar id_producto_servicio (existe en ProductosServicios y está disponible).
    # 3. Obtener precio_unitario_momento de ProductosServicios.
    # 4. Calcular subtotal = cantidad * precio_unitario_momento.
    # 5. Si es un item de alquiler (identificado por id_producto_servicio o detalles_especificos_item):
    #    - Validar disponibilidad usando `alquiler_service.consultar_disponibilidad_item`.
    #    - Asignar `id_item_alquiler` específico de `detalles_especificos_item`.
    #    - Registrar `fecha_alquiler_inicio`, `fecha_alquiler_fin_esperada`.
    # 6. Si es un servicio de sastrería:
    #    - Podría requerir `id_sastre_asignado` de `detalles_especificos_item`.
    # 7. INSERT en DetallesPedido con todos los campos relevantes.
    # 8. UPDATE Pedidos SET total_pedido = total_pedido + subtotal WHERE id_pedido = %s.
    #    (Considerar transacciones para mantener consistencia).

    # Simulación:
    precio_unitario_simulado = 50.00 # Obtenido de ProductosServicios
    subtotal_simulado = cantidad * precio_unitario_simulado

    # Actualizar total_pedido (esto normalmente se haría en la capa de datos)
    # pedido_actual = db_query("SELECT total_pedido FROM Pedidos WHERE id_pedido = %s", (id_pedido,))
    # nuevo_total_pedido = pedido_actual['total_pedido'] + subtotal_simulado
    # db_execute("UPDATE Pedidos SET total_pedido = %s WHERE id_pedido = %s", (nuevo_total_pedido, id_pedido))

    return {
        "id_detalle_pedido": 501, # ID simulado
        "id_pedido": id_pedido,
        "id_producto_servicio": id_producto_servicio,
        "cantidad": cantidad,
        "precio_unitario_momento": precio_unitario_simulado,
        "subtotal": subtotal_simulado,
        **detalles_especificos_item # Incluye campos como id_sastre_asignado, id_item_alquiler, etc.
    }

def quitar_item_de_pedido(id_detalle_pedido: int) -> Dict[str, Any]:
    """
    Quita un ítem de un pedido.
    Recalcula el total del pedido.

    Interactúa con las tablas: DetallesPedido (para eliminar o marcar como quitado), Pedidos (para actualizar total).
    Si el ítem era un alquiler reservado, podría necesitar llamar a `alquiler_service` para liberar el ítem.

    Args:
        id_detalle_pedido: ID del detalle del pedido (ítem) a quitar.

    Returns:
        Un diccionario confirmando la acción.
        Ejemplo: {'status': 'exitoso', 'mensaje': 'Item quitado', 'id_pedido_afectado': 101}
    """
    print(f"Quitando item (detalle_pedido_id {id_detalle_pedido}) del pedido.")
    # Lógica de base de datos:
    # 1. Validar id_detalle_pedido (existe en DetallesPedido).
    # 2. Obtener id_pedido y subtotal del ítem a quitar.
    #    SELECT id_pedido, subtotal, id_item_alquiler FROM DetallesPedido WHERE id_detalle_pedido = %s.
    # 3. DELETE from DetallesPedido WHERE id_detalle_pedido = %s.
    #    (O marcar como inactivo/cancelado si se prefiere no borrar).
    # 4. UPDATE Pedidos SET total_pedido = total_pedido - subtotal_quitado WHERE id_pedido = %s.
    # 5. Si el item era un alquiler (id_item_alquiler no es NULL):
    #    - Llamar a una función en `alquiler_service` para actualizar el estado del `InventarioAlquiler`
    #      (ej: `alquiler_service.actualizar_item_alquiler(id_item_alquiler, {'estado_item': 'disponible'})`).

    id_pedido_afectado_simulado = 101 # Obtenido de la consulta
    return {
        "status": "exitoso_simulado",
        "mensaje": f"Item {id_detalle_pedido} quitado del pedido {id_pedido_afectado_simulado}.",
        "id_pedido_afectado": id_pedido_afectado_simulado
    }

def obtener_detalle_pedido_completo(id_pedido: int) -> Dict[str, Any]:
    """
    Obtiene todos los detalles de un pedido, incluyendo información del cliente,
    empleado, y todos los ítems del pedido con sus detalles.

    Interactúa con: Pedidos, Clientes, Empleados, DetallesPedido, ProductosServicios.
    Potencialmente con InventarioAlquiler si hay items de alquiler.

    Args:
        id_pedido: El ID del pedido a obtener.

    Returns:
        Un diccionario anidado con toda la información del pedido.
        None si el pedido no se encuentra.
        Ejemplo:
        {
            'pedido_info': {'id_pedido': 101, 'fecha_creacion': ..., 'total_pedido': ..., 'estado_pedido': ...},
            'cliente_info': {'id_cliente': 1, 'nombre': 'Juan Perez', ...},
            'empleado_info': {'id_empleado': 2, 'nombre': 'Ana Gomez', ...},
            'items_pedido': [
                {'id_detalle_pedido': 501, 'producto_nombre': 'Ajuste Pantalon', 'cantidad': 1, ...},
                {'id_detalle_pedido': 502, 'producto_nombre': 'Traje Azul (Alquiler)', 'cantidad': 1, ...}
            ]
        }
    """
    print(f"Obteniendo detalle completo del pedido ID: {id_pedido}")
    # Lógica de base de datos:
    # 1. SELECT * FROM Pedidos WHERE id_pedido = %s. Si no existe, retornar None.
    # 2. SELECT * FROM Clientes WHERE id_cliente = [Pedidos.id_cliente].
    # 3. SELECT * FROM Empleados WHERE id_empleado = [Pedidos.id_empleado_creador].
    # 4. SELECT dp.*, ps.nombre as producto_nombre, ps.tipo_item
    #    FROM DetallesPedido dp
    #    JOIN ProductosServicios ps ON dp.id_producto_servicio = ps.id_producto_servicio
    #    WHERE dp.id_pedido = %s.
    #    (Para items de alquiler, se podría hacer un JOIN adicional a InventarioAlquiler).
    # 5. Ensamblar el diccionario de respuesta.

    if id_pedido == 101: # Simulación
        return {
            "pedido_info": {"id_pedido": 101, "fecha_creacion": "2023-10-31T09:00:00", "total_pedido": 150.00, "total_abonado": 0.00, "estado_pedido": "pendiente"},
            "cliente_info": {"id_cliente": 1, "nombre": "Juan", "apellido": "Perez", "telefono": "3001234567"},
            "empleado_info": {"id_empleado": 2, "nombre": "Ana", "apellido": "Gomez"},
            "items_pedido": [
                {"id_detalle_pedido": 501, "id_producto_servicio": 101, "producto_nombre": "Ajuste de Pantalón", "cantidad": 1, "subtotal": 30.00, "tipo_item": "servicio"},
                {"id_detalle_pedido": 502, "id_producto_servicio": 301, "producto_nombre": "Traje Formal Azul Marino", "cantidad": 1, "subtotal": 120.00, "tipo_item": "producto", "id_item_alquiler": 1, "fecha_alquiler_inicio": "2023-11-05", "fecha_alquiler_fin_esperada": "2023-11-08"}
            ]
        }
    return {"status": "error", "mensaje": "Pedido no encontrado"} # O retornar None directamente

def actualizar_estado_pedido(id_pedido: int, nuevo_estado: str) -> Dict[str, Any]:
    """
    Actualiza el estado de un pedido.

    Interactúa con la tabla: Pedidos.
    Valida que `nuevo_estado` sea un valor del ENUM `estado_pedido_enum`.

    Args:
        id_pedido: ID del pedido a actualizar.
        nuevo_estado: Nuevo estado del pedido (ej: 'en_proceso', 'listo_para_entrega').

    Returns:
        Un diccionario del pedido actualizado o un mensaje de error.
    """
    print(f"Actualizando estado del pedido {id_pedido} a '{nuevo_estado}'")
    # Lógica de base de datos:
    # 1. Validar que id_pedido existe.
    # 2. Validar que nuevo_estado es un valor válido del ENUM estado_pedido_enum.
    # 3. UPDATE Pedidos SET estado_pedido = %s WHERE id_pedido = %s.
    #    (Considerar lógica adicional si el estado cambia a 'completado' o 'cancelado',
    #     como validaciones de pago, liberación de items de alquiler, etc.).
    return {
        "id_pedido": id_pedido,
        "estado_pedido_anterior_simulado": "pendiente",
        "estado_pedido_nuevo": nuevo_estado,
        "mensaje": "Estado del pedido actualizado."
    }

def buscar_producto_por_codigo_barras(codigo_barras: str) -> Optional[Dict[str, Any]]:
    """
    Busca un producto o servicio en el catálogo usando su código de barras.

    Interactúa con la tabla: ProductosServicios.

    Args:
        codigo_barras: El código de barras a buscar.

    Returns:
        Un diccionario con la información del producto/servicio si se encuentra.
        None si no se encuentra.
        Ejemplo: {'id_producto_servicio': 25, 'nombre': 'Camisa Blanca Formal', 'precio_unitario': 75.00, ...}
    """
    print(f"Buscando producto por código de barras: {codigo_barras}")
    # Lógica de base de datos:
    # SELECT * FROM ProductosServicios WHERE codigo_barras = %s AND disponible = TRUE.
    if codigo_barras == "7701234567890": # Simulación
        return {
            "id_producto_servicio": 25,
            "nombre": "Camisa Blanca Formal",
            "descripcion": "Camisa de algodón, talla M",
            "precio_unitario": 75.00,
            "tipo_item": "producto", # Podría ser 'servicio' también
            "id_categoria_servicio": 1,
            "codigo_barras": codigo_barras,
            "disponible": True
        }
    return None

# -------------------------------------------
# 2. Gestión de Clientes (desde el POS)
# -------------------------------------------

def buscar_cliente_pos(termino_busqueda: str) -> List[Dict[str, Any]]:
    """
    Busca clientes por nombre, apellido o teléfono para el POS.

    Interactúa con la tabla: Clientes.

    Args:
        termino_busqueda: El texto a buscar (puede ser parte del nombre, apellido o teléfono).

    Returns:
        Una lista de diccionarios, cada uno representando un cliente que coincide.
        Ejemplo: [{'id_cliente': 1, 'nombre': 'Juan Perez', 'telefono': '3001234567'}, ...]
    """
    print(f"Buscando cliente en POS con término: {termino_busqueda}")
    # Lógica de base de datos:
    # SELECT id_cliente, nombre, apellido, telefono, email FROM Clientes
    # WHERE nombre ILIKE %s OR apellido ILIKE %s OR telefono LIKE %s
    # (usando '%' para búsquedas parciales)
    search_term_like = f"%{termino_busqueda}%"
    return [
        {"id_cliente": 1, "nombre": "Juan", "apellido": "Perez", "telefono": "3001234567", "email": "juan.perez@email.com"},
        {"id_cliente": 15, "nombre": "Juana", "apellido": "Martinez", "telefono": "3109876543", "email": "juana.m@email.com"}
    ] # Ejemplo

def crear_cliente_rapido_pos(
    nombre: str,
    apellido: str,
    telefono: str,
    email: Optional[str] = None,
    direccion: Optional[str] = None
) -> Dict[str, Any]:
    """
    Crea un nuevo cliente de forma rápida desde el POS.

    Interactúa con la tabla: Clientes.
    Podría considerarse una versión simplificada de una función más completa en un `clientes_service`.

    Args:
        nombre: Nombre del cliente.
        apellido: Apellido del cliente.
        telefono: Teléfono del cliente (usualmente UNIQUE y NOT NULL).
        email: (Opcional) Email del cliente (usualmente UNIQUE).
        direccion: (Opcional) Dirección del cliente.

    Returns:
        Un diccionario representando el cliente creado.
        Ejemplo: {'id_cliente': 10, 'nombre': 'Pedro', 'apellido': 'Gomez', 'telefono': '3201112233', ...}
    """
    print(f"Creando cliente rápido desde POS: {nombre} {apellido}, Tel: {telefono}")
    # Lógica de base de datos:
    # 1. Validar que el teléfono no exista ya (si es UNIQUE).
    # 2. Validar que el email no exista ya (si es UNIQUE y se proporciona).
    # 3. INSERT en Clientes.
    return {
        "id_cliente": 201, # ID simulado
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "fecha_registro": "2023-10-31T09:30:00" # Simulación CURRENT_TIMESTAMP
    }

# -------------------------------------------------------
# 3. Finalización de Pedido y Transición a Pago
# -------------------------------------------------------

def finalizar_pedido_para_pago(id_pedido: int) -> Dict[str, Any]:
    """
    Prepara un pedido para el proceso de pago.
    Puede implicar actualizar el estado del pedido y devolver el total final.
    Esta función NO procesa el pago, solo lo deja listo para que el módulo de pagos tome el control.

    Interactúa con la tabla: Pedidos (para obtener total y quizás actualizar estado).

    Podría llamar a funciones de `pagos_service` si se inicia algún proceso de pago aquí,
    o simplemente devolver la info para que la UI llame a `pagos_service`.

    Args:
        id_pedido: ID del pedido a finalizar.

    Returns:
        Un diccionario con la información necesaria para el pago.
        Ejemplo: {'id_pedido': 101, 'total_a_pagar': 150.00, 'estado_pedido': 'listo_para_pago', ...}
        O un error si el pedido no se puede finalizar (ej: no tiene items, ya está pagado).
    """
    print(f"Finalizando pedido {id_pedido} para transición a pago.")
    # Lógica de base de datos:
    # 1. Validar que id_pedido existe.
    # 2. Obtener total_pedido, total_abonado y estado_pedido actual de la tabla Pedidos.
    # 3. Validar que el pedido no esté ya pagado o cancelado.
    # 4. Validar que tenga items (total_pedido > 0).
    # 5. Calcular total_a_pagar = total_pedido - total_abonado.
    # 6. (Opcional) Actualizar estado_pedido a 'listo_para_pago' o similar.
    #    UPDATE Pedidos SET estado_pedido = 'listo_para_pago' WHERE id_pedido = %s.

    # Simulación
    pedido_data = obtener_detalle_pedido_completo(id_pedido) # Usamos la función anterior para simular datos
    if not pedido_data or "error" in pedido_data:
        return {"status": "error", "mensaje": "Pedido no encontrado o inválido."}

    total_pedido = pedido_data["pedido_info"]["total_pedido"]
    total_abonado = pedido_data["pedido_info"]["total_abonado"]
    total_a_pagar = total_pedido - total_abonado

    if total_a_pagar <= 0 and total_pedido > 0 : # Asumiendo que si total_pedido es 0, no hay items
        return {"status": "error", "mensaje": "El pedido ya está completamente pagado o no requiere pago."}
    if total_pedido == 0:
        return {"status": "error", "mensaje": "El pedido no tiene items."}

    # Simular actualización de estado si es parte de la lógica
    # actualizar_estado_pedido(id_pedido, 'listo_para_pago')

    return {
        "id_pedido": id_pedido,
        "total_pedido_bruto": total_pedido,
        "total_ya_abonado": total_abonado,
        "total_a_pagar_neto": total_a_pagar,
        "estado_pedido_actualizado_simulado": "listo_para_pago",
        "mensaje": "Pedido listo para procesar el pago."
        # Aquí se podría incluir información del cliente para el pago, si es necesario.
    }
