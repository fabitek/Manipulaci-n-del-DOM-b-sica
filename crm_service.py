"""
Módulo CRM (Customer Relationship Management): Funciones para la gestión avanzada
de clientes, su historial, preferencias y comunicaciones.
"""
from typing import Dict, List, Optional, Any

# Placeholder para simular una conexión a base de datos o ORM
# En una implementación real, esto sería manejado por un motor de BD.
# Por ejemplo: from database_connector import db_execute, db_query

# Nota: Algunas funciones como agregar_nota_cliente o registrar_preferencia_cliente
# podrían requerir tablas adicionales no definidas en el schema.sql inicial,
# como 'NotasCliente' o 'PreferenciasCliente'. Se asumirá su existencia conceptual.

# -------------------------------------------
# 1. Gestión Avanzada de Clientes
# -------------------------------------------

def actualizar_informacion_cliente(id_cliente: int, datos_actualizados: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Actualiza la información de un cliente existente.

    Interactúa con la tabla: Clientes.

    Args:
        id_cliente: El ID del cliente a actualizar.
        datos_actualizados: Un diccionario con los campos a actualizar y sus nuevos valores.
                            Ej: {'email': 'nuevo@email.com', 'telefono': '3001112233', 'notas_adicionales': 'Cliente VIP'}

    Returns:
        Un diccionario representando el cliente con la información actualizada si se encontró y actualizó.
        None si el cliente con id_cliente no existe.
    """
    print(f"Actualizando información para cliente ID: {id_cliente} con datos: {datos_actualizados}")
    # Lógica de base de datos:
    # 1. Verificar si el cliente existe (SELECT 1 FROM Clientes WHERE id_cliente = %s).
    #    Si no existe, retornar None.
    # 2. Construir la sentencia UPDATE dinámicamente basada en `datos_actualizados`.
    #    UPDATE Clientes SET email = %s, telefono = %s, ... WHERE id_cliente = %s.
    # 3. Ejecutar UPDATE.
    # 4. SELECT * FROM Clientes WHERE id_cliente = %s para devolver el registro actualizado.

    # Simulación:
    if id_cliente == 1: # Asumir que el cliente 1 existe
        # Simular la obtención del cliente antes de actualizar
        cliente_simulado = {
            "id_cliente": 1, "nombre": "Juan", "apellido": "Perez", "telefono": "3001234567",
            "email": "juan.perez@email.com", "direccion": "Calle Falsa 123",
            "fecha_registro": "2023-01-15T10:00:00", "notas_adicionales": None
        }
        cliente_simulado.update(datos_actualizados)
        return cliente_simulado
    return None

def obtener_perfil_completo_cliente(id_cliente: int) -> Optional[Dict[str, Any]]:
    """
    Obtiene un perfil completo de un cliente, incluyendo su información básica,
    historial de pedidos, medidas (si aplica), y notas.

    Interactúa con: Clientes, Pedidos, MedidasCliente.
                   Potencialmente con una tabla 'NotasCliente' o similar.

    Args:
        id_cliente: El ID del cliente.

    Returns:
        Un diccionario anidado con el perfil completo del cliente si se encuentra.
        None si el cliente con id_cliente no existe.
        Ejemplo:
        {
            'info_basica': {'id_cliente': 1, 'nombre': 'Juan', ...},
            'pedidos': [{'id_pedido': 101, 'fecha_creacion': ..., 'total_pedido': ...}, ...],
            'medidas': [{'id_medida': 1, 'fecha_medicion': ..., 'pecho': ...}, ...],
            'notas_cliente': [{'id_nota': 1, 'fecha_nota': ..., 'nota': ..., 'id_empleado': ...}, ...]
        }
    """
    print(f"Obteniendo perfil completo para cliente ID: {id_cliente}")
    # Lógica de base de datos:
    # 1. SELECT * FROM Clientes WHERE id_cliente = %s. Si no existe, retornar None.
    # 2. SELECT * FROM Pedidos WHERE id_cliente = %s ORDER BY fecha_creacion DESC.
    # 3. SELECT * FROM MedidasCliente WHERE id_cliente = %s ORDER BY fecha_medicion DESC.
    # 4. (Si existe tabla NotasCliente) SELECT * FROM NotasCliente WHERE id_cliente = %s ORDER BY fecha_nota DESC.
    # 5. Ensamblar el diccionario.

    if id_cliente == 1: # Simulación
        return {
            "info_basica": {
                "id_cliente": 1, "nombre": "Juan", "apellido": "Perez", "telefono": "3001234567",
                "email": "juan.perez@email.com", "direccion": "Calle Falsa 123",
                "fecha_registro": "2023-01-15T10:00:00", "notas_adicionales": "Cliente frecuente"
            },
            "pedidos": [
                {"id_pedido": 101, "fecha_creacion": "2023-10-31T09:00:00", "total_pedido": 150.00, "estado_pedido": "completado"},
                {"id_pedido": 55, "fecha_creacion": "2023-05-20T14:30:00", "total_pedido": 75.00, "estado_pedido": "completado"}
            ],
            "medidas": [
                {"id_medida": 1, "fecha_medicion": "2023-01-20", "cuello": 38.0, "pecho": 102.0, "cintura": 85.0}
            ],
            "notas_cliente_simuladas": [ # Asumiendo una tabla 'NotasCliente'
                {"id_nota": 1, "fecha_nota": "2023-06-01T11:00:00", "nota": "Prefiere contacto por WhatsApp.", "id_empleado": 2}
            ]
        }
    return None

def buscar_clientes_avanzado(criterios: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Realiza una búsqueda avanzada de clientes basada en múltiples criterios.

    Interactúa con la tabla: Clientes.
    Podría requerir JOINs con Pedidos, MedidasCliente si los criterios incluyen datos de esas tablas
    (ej: buscar clientes con > N pedidos, o con medidas registradas en cierto rango de fechas).

    Args:
        criterios: Un diccionario con los criterios de búsqueda.
                   Ej: {'nombre': 'Juan', 'ciudad_direccion': 'Bogota', 'fecha_registro_desde': '2023-01-01'}
                       {'min_pedidos': 5, 'ultima_compra_hace_meses': 6}

    Returns:
        Una lista de diccionarios, donde cada diccionario es un cliente que coincide con los criterios.
    """
    print(f"Buscando clientes con criterios avanzados: {criterios}")
    # Lógica de base de datos:
    # 1. Construir una consulta SQL dinámica basada en los `criterios`.
    #    Esto puede ser complejo y requiere cuidado para evitar inyección SQL.
    #    Ej: SELECT * FROM Clientes WHERE nombre ILIKE %s AND email LIKE %s ...
    #    Para criterios más complejos (min_pedidos), se necesitarían subconsultas o JOINs con COUNT.
    #    SELECT c.* FROM Clientes c
    #    LEFT JOIN (SELECT id_cliente, COUNT(*) as num_pedidos FROM Pedidos GROUP BY id_cliente) p_count
    #    ON c.id_cliente = p_count.id_cliente
    #    WHERE (p_count.num_pedidos >= %s OR %s IS NULL) AND ...

    # Simulación básica:
    resultados_simulados = []
    if criterios.get("nombre") == "Juan":
        resultados_simulados.append({
            "id_cliente": 1, "nombre": "Juan", "apellido": "Perez", "telefono": "3001234567", "email": "juan.perez@email.com"
        })
    if criterios.get("email_contiene") == "test.com":
         resultados_simulados.append({
            "id_cliente": 2, "nombre": "Maria", "apellido": "Lopez", "telefono": "3101234567", "email": "maria@test.com"
        })
    return resultados_simulados

def agregar_nota_cliente(id_cliente: int, nota: str, id_empleado: Optional[int] = None) -> Optional[Dict[str, Any]]:
    """
    Agrega una nota al perfil de un cliente.
    Esto podría usar el campo 'notas_adicionales' de la tabla Clientes si es una nota general,
    o interactuar con una tabla dedicada 'NotasCliente' si se requiere un historial de notas.
    Para este placeholder, asumiremos una tabla 'NotasCliente' conceptual.

    Interactúa con: Clientes (para validar) y una tabla conceptual 'NotasCliente'.

    Args:
        id_cliente: ID del cliente.
        nota: Contenido de la nota.
        id_empleado: (Opcional) ID del empleado que agrega la nota.

    Returns:
        Un diccionario representando la nota creada si el cliente existe.
        None si el cliente no existe.
        Ejemplo: {'id_nota': 10, 'id_cliente': 1, 'nota': 'Llamó para preguntar...', 'fecha_creacion': '...', 'id_empleado': 2}
    """
    print(f"Agregando nota para cliente ID: {id_cliente}: '{nota}' por empleado ID: {id_empleado}")
    # Lógica de base de datos:
    # 1. Validar que id_cliente existe en Clientes. Si no, retornar None.
    # 2. INSERT en la tabla 'NotasCliente' (id_cliente, nota, fecha_creacion, id_empleado).
    #    (Si se usa Clientes.notas_adicionales, sería un UPDATE y se concatenaría la nota).

    if id_cliente == 1: # Simulación de cliente existente
        return {
            "id_nota_simulada": 10, # ID de la nueva nota
            "id_cliente": id_cliente,
            "nota": nota,
            "fecha_creacion_simulada": "2023-11-01T10:00:00",
            "id_empleado": id_empleado
        }
    return None

# -------------------------------------------
# 2. Historial y Preferencias
# -------------------------------------------

def obtener_historial_compras_cliente(id_cliente: int) -> List[Dict[str, Any]]:
    """
    Obtiene el historial de compras (pedidos) de un cliente.

    Interactúa con: Pedidos, DetallesPedido, ProductosServicios.

    Args:
        id_cliente: El ID del cliente.

    Returns:
        Una lista de diccionarios, donde cada diccionario representa un pedido
        con detalles de los ítems comprados.
        Ejemplo:
        [
            {
                'id_pedido': 101, 'fecha_creacion': '...', 'total_pedido': ..., 'estado_pedido': 'completado',
                'items': [{'nombre_producto': 'Ajuste Pantalon', 'cantidad': 1, 'subtotal': ...}, ...]
            }, ...
        ]
    """
    print(f"Obteniendo historial de compras para cliente ID: {id_cliente}")
    # Lógica de base de datos:
    # 1. Validar id_cliente.
    # 2. SELECT * FROM Pedidos WHERE id_cliente = %s ORDER BY fecha_creacion DESC.
    # 3. Para cada pedido, SELECT dp.*, ps.nombre as nombre_producto
    #    FROM DetallesPedido dp JOIN ProductosServicios ps ON dp.id_producto_servicio = ps.id_producto_servicio
    #    WHERE dp.id_pedido = [ID del pedido actual].
    # 4. Ensamblar la respuesta.

    if id_cliente == 1: # Simulación
        return [
            {
                "id_pedido": 101, "fecha_creacion": "2023-10-31T09:00:00", "total_pedido": 150.00, "estado_pedido": "completado",
                "items": [
                    {"id_detalle_pedido": 501, "id_producto_servicio": 101, "nombre_producto": "Ajuste de Pantalón", "cantidad": 1, "subtotal": 30.00},
                    {"id_detalle_pedido": 502, "id_producto_servicio": 301, "nombre_producto": "Traje Formal Azul Marino", "cantidad": 1, "subtotal": 120.00}
                ]
            },
            {
                "id_pedido": 55, "fecha_creacion": "2023-05-20T14:30:00", "total_pedido": 75.00, "estado_pedido": "completado",
                "items": [
                    {"id_detalle_pedido": 210, "id_producto_servicio": 25, "nombre_producto": "Camisa Blanca Formal", "cantidad": 1, "subtotal": 75.00}
                ]
            }
        ]
    return []

def registrar_preferencia_cliente(
    id_cliente: int,
    tipo_preferencia: str, # Ej: 'color_favorito', 'tipo_tela_preferido', 'comunicacion_canal'
    valor_preferencia: str # Ej: 'azul', 'algodon', 'whatsapp'
) -> Optional[Dict[str, Any]]:
    """
    Registra una preferencia específica para un cliente.
    Esto requeriría una tabla dedicada 'PreferenciasCliente' (id_preferencia, id_cliente, tipo, valor).

    Interactúa con: Clientes (para validar) y una tabla conceptual 'PreferenciasCliente'.

    Args:
        id_cliente: ID del cliente.
        tipo_preferencia: El tipo de preferencia que se registra.
        valor_preferencia: El valor de la preferencia.

    Returns:
        Un diccionario representando la preferencia registrada si el cliente existe.
        None si el cliente no existe.
        Ejemplo: {'id_preferencia': 1, 'id_cliente': 1, 'tipo_preferencia': 'color_favorito', 'valor_preferencia': 'azul'}
    """
    print(f"Registrando preferencia para cliente ID: {id_cliente}: Tipo='{tipo_preferencia}', Valor='{valor_preferencia}'")
    # Lógica de base de datos:
    # 1. Validar que id_cliente existe en Clientes. Si no, retornar None.
    # 2. INSERT o UPDATE en la tabla 'PreferenciasCliente'.
    #    (Podría ser un UPDATE si la preferencia de ese tipo ya existe y se quiere sobrescribir).
    #    INSERT INTO PreferenciasCliente (id_cliente, tipo_preferencia, valor_preferencia) VALUES (%s, %s, %s)
    #    ON CONFLICT (id_cliente, tipo_preferencia) DO UPDATE SET valor_preferencia = %s;

    if id_cliente == 1: # Simulación
        return {
            "id_preferencia_simulada": 1,
            "id_cliente": id_cliente,
            "tipo_preferencia": tipo_preferencia,
            "valor_preferencia": valor_preferencia
        }
    return None

# ---------------------------------------------------------------------
# 3. Comunicación con Clientes (Placeholders para Integraciones)
# ---------------------------------------------------------------------

def enviar_notificacion_cliente(id_cliente: int, mensaje: str, canal: str = 'email') -> Dict[str, Any]:
    """
    (Placeholder) Envía una notificación (mensaje) a un cliente a través de un canal específico.
    Esto requeriría integración con servicios externos de Email (ej: SendGrid, Mailgun)
    o SMS (ej: Twilio, Vonage).

    Interactúa con: Clientes (para obtener email/teléfono).
                   API Externa de Email/SMS.

    Args:
        id_cliente: ID del cliente.
        mensaje: El contenido del mensaje a enviar.
        canal: El canal de comunicación ('email', 'sms', 'whatsapp'). Por defecto 'email'.

    Returns:
        Un diccionario indicando el resultado del envío (simulado).
        Ejemplo: {'status': 'enviado_simulado', 'canal': 'email', 'id_mensaje_externo': '...'}
    """
    print(f"Enviando notificación a cliente ID: {id_cliente} por {canal}: '{mensaje[:50]}...'")
    # Lógica:
    # 1. Obtener información de contacto del cliente (email, teléfono) de la tabla Clientes.
    #    SELECT email, telefono FROM Clientes WHERE id_cliente = %s.
    #    Si no hay datos de contacto para el canal, error.
    # 2. **Placeholder: Integración con API externa según el canal.**
    #    If canal == 'email': email_api.send(to=cliente.email, body=mensaje)
    #    If canal == 'sms': sms_api.send(to=cliente.telefono, body=mensaje)
    #    If canal == 'whatsapp': whatsapp_api.send(to=cliente.telefono, body=mensaje) # Más complejo

    cliente_info_simulada = {"email": "juan.perez@email.com", "telefono": "3001234567"} # Simulación
    if id_cliente == 1 and ( (canal == 'email' and cliente_info_simulada.get('email')) or \
                             (canal in ['sms', 'whatsapp'] and cliente_info_simulada.get('telefono')) ):
        return {
            "status": "enviado_simulado",
            "canal": canal,
            "id_mensaje_externo_simulado": f"{canal.upper()}_MSG_{abs(hash(mensaje))}",
            "mensaje_enviado": mensaje
        }
    elif id_cliente != 1:
        return {"status": "error_simulado", "mensaje": "Cliente no encontrado."}
    else:
        return {"status": "error_simulado", "mensaje": f"No hay información de contacto para el canal '{canal}'."}


def programar_recordatorio_cliente(
    id_cliente: int,
    id_pedido: Optional[int], # Puede ser un recordatorio general o asociado a un pedido
    tipo_recordatorio: str, # Ej: 'cita_medidas', 'entrega_pedido', 'mantenimiento_prenda'
    fecha_recordatorio: str # YYYY-MM-DD HH:MM:SS
) -> Dict[str, Any]:
    """
    (Placeholder) Programa un recordatorio para un cliente.
    Esto podría implicar crear una tarea en un sistema de "cron jobs" o "task scheduler"
    que luego llame a `enviar_notificacion_cliente` en la fecha programada.
    O podría registrarse en una tabla `Recordatorios` para ser procesada por un worker.

    Interactúa con: Una tabla conceptual `Recordatorios` o un sistema de tareas.
                   Clientes (para validar). Pedidos (si id_pedido se proporciona).

    Args:
        id_cliente: ID del cliente.
        id_pedido: (Opcional) ID del pedido asociado al recordatorio.
        tipo_recordatorio: Descripción del tipo de recordatorio.
        fecha_recordatorio: Fecha y hora para enviar el recordatorio (YYYY-MM-DD HH:MM:SS).

    Returns:
        Un diccionario confirmando la programación del recordatorio (simulado).
        Ejemplo: {'id_recordatorio_simulado': 1, 'status': 'programado', 'fecha_envio_programada': '...'}
    """
    print(f"Programando recordatorio '{tipo_recordatorio}' para cliente ID: {id_cliente} en fecha {fecha_recordatorio}")
    # Lógica:
    # 1. Validar id_cliente.
    # 2. Validar id_pedido si se proporciona.
    # 3. **Placeholder: Lógica de programación.**
    #    - Opción A: INSERT en tabla `Recordatorios` (id_cliente, id_pedido, tipo, fecha_programada, estado='pendiente').
    #                Un worker externo consultaría esta tabla y enviaría notificaciones.
    #    - Opción B: Usar una biblioteca de scheduling (APScheduler en Python) para programar una tarea
    #                que llame a `enviar_notificacion_cliente`.

    if id_cliente == 1: # Simulación de cliente existente
        return {
            "id_recordatorio_simulado": 123,
            "id_cliente": id_cliente,
            "id_pedido": id_pedido,
            "tipo_recordatorio": tipo_recordatorio,
            "fecha_envio_programada": fecha_recordatorio,
            "status": "programado_simulado"
        }
    return {"status": "error_simulado", "mensaje": "Cliente no encontrado, no se pudo programar recordatorio."}
