-- Tipos ENUM
CREATE TYPE rol_empleado AS ENUM ('admin', 'cajero', 'sastre', 'personal_lavanderia', 'personal_alquiler');
CREATE TYPE tipo_item_producto_servicio AS ENUM ('producto', 'servicio');
CREATE TYPE estado_pedido_enum AS ENUM ('pendiente', 'en_proceso', 'listo_para_entrega', 'completado', 'cancelado', 'devuelto');
CREATE TYPE estado_item_alquiler_enum AS ENUM ('disponible', 'alquilado', 'en_mantenimiento', 'retirado');
CREATE TYPE metodo_pago_enum AS ENUM ('efectivo', 'tarjeta_credito', 'tarjeta_debito', 'nequi', 'daviplata', 'transferencia_bancaria', 'abono_parcial');

-- Tabla Clientes
CREATE TABLE Clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    telefono VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE,
    direccion TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notas_adicionales TEXT
);

-- Tabla Empleados
CREATE TABLE Empleados (
    id_empleado SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    rol rol_empleado NOT NULL,
    telefono VARCHAR(50),
    email VARCHAR(255) UNIQUE,
    activo BOOLEAN DEFAULT TRUE
);

-- Tabla CategoriasServicio
CREATE TABLE CategoriasServicio (
    id_categoria_servicio SERIAL PRIMARY KEY,
    nombre_categoria VARCHAR(100) UNIQUE NOT NULL,
    descripcion TEXT
);

-- Tabla ProductosServicios
CREATE TABLE ProductosServicios (
    id_producto_servicio SERIAL PRIMARY KEY,
    id_categoria_servicio INT NOT NULL REFERENCES CategoriasServicio(id_categoria_servicio),
    codigo_barras VARCHAR(255) UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    tipo_item tipo_item_producto_servicio NOT NULL,
    disponible BOOLEAN DEFAULT TRUE,
    imagen_url VARCHAR(255)
);

-- Tabla MedidasCliente
CREATE TABLE MedidasCliente (
    id_medida SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL REFERENCES Clientes(id_cliente),
    fecha_medicion DATE NOT NULL,
    cuello DECIMAL(5,2),
    pecho DECIMAL(5,2),
    cintura DECIMAL(5,2),
    cadera DECIMAL(5,2),
    largo_manga DECIMAL(5,2),
    largo_pantalon_exterior DECIMAL(5,2),
    largo_pantalon_interior DECIMAL(5,2),
    hombro DECIMAL(5,2),
    muneca DECIMAL(5,2),
    observaciones TEXT,
    UNIQUE (id_cliente, fecha_medicion)
);

-- Tabla Pedidos
CREATE TABLE Pedidos (
    id_pedido SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL REFERENCES Clientes(id_cliente),
    id_empleado_creador INT NOT NULL REFERENCES Empleados(id_empleado),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_entrega_estimada DATE,
    fecha_entrega_real DATE,
    estado_pedido estado_pedido_enum NOT NULL,
    total_pedido DECIMAL(12, 2) DEFAULT 0.00,
    total_abonado DECIMAL(12, 2) DEFAULT 0.00,
    notas_pedido TEXT
);

-- Tabla InventarioAlquiler
CREATE TABLE InventarioAlquiler (
    id_item_alquiler SERIAL PRIMARY KEY,
    id_producto_servicio INT NOT NULL REFERENCES ProductosServicios(id_producto_servicio),
    codigo_item_unico VARCHAR(100) UNIQUE NOT NULL,
    estado_item estado_item_alquiler_enum NOT NULL,
    fecha_adquisicion DATE,
    valor_deposito_requerido DECIMAL(10, 2) NOT NULL,
    notas_item TEXT
);

-- Tabla DetallesPedido
CREATE TABLE DetallesPedido (
    id_detalle_pedido SERIAL PRIMARY KEY,
    id_pedido INT NOT NULL REFERENCES Pedidos(id_pedido),
    id_producto_servicio INT NOT NULL REFERENCES ProductosServicios(id_producto_servicio),
    cantidad INT DEFAULT 1 NOT NULL,
    precio_unitario_momento DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    id_sastre_asignado INT REFERENCES Empleados(id_empleado),
    fecha_inicio_trabajo_sastreria TIMESTAMP,
    fecha_fin_trabajo_sastreria TIMESTAMP,
    etiqueta_lavanderia VARCHAR(100),
    id_item_alquiler INT REFERENCES InventarioAlquiler(id_item_alquiler),
    fecha_alquiler_inicio TIMESTAMP,
    fecha_alquiler_fin_esperada TIMESTAMP,
    fecha_alquiler_devolucion_real TIMESTAMP,
    notas_detalle TEXT
);

-- Tabla Alquileres
CREATE TABLE Alquileres (
    id_alquiler SERIAL PRIMARY KEY,
    id_detalle_pedido INT UNIQUE NOT NULL REFERENCES DetallesPedido(id_detalle_pedido),
    deposito_recibido DECIMAL(10, 2) DEFAULT 0.00,
    deposito_devuelto DECIMAL(10, 2) DEFAULT 0.00,
    penalizacion_aplicada DECIMAL(10, 2) DEFAULT 0.00,
    condicion_devolucion TEXT,
    notas_alquiler TEXT
);

-- Tabla Pagos
CREATE TABLE Pagos (
    id_pago SERIAL PRIMARY KEY,
    id_pedido INT NOT NULL REFERENCES Pedidos(id_pedido),
    id_empleado_receptor INT NOT NULL REFERENCES Empleados(id_empleado),
    fecha_pago TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    monto_pagado DECIMAL(10, 2) NOT NULL,
    metodo_pago metodo_pago_enum NOT NULL,
    referencia_transaccion VARCHAR(255),
    id_factura_electronica_dian VARCHAR(255),
    notas_pago TEXT
);

-- Tabla PagosSastre
CREATE TABLE PagosSastre (
    id_pago_sastre SERIAL PRIMARY KEY,
    id_detalle_pedido INT NOT NULL REFERENCES DetallesPedido(id_detalle_pedido),
    id_sastre INT NOT NULL REFERENCES Empleados(id_empleado),
    monto_pagado DECIMAL(10, 2) NOT NULL,
    fecha_pago DATE NOT NULL,
    metodo_pago VARCHAR(50) NOT NULL,
    notas TEXT
);

-- Tabla FacturasElectronicas
CREATE TABLE FacturasElectronicas (
    id_factura SERIAL PRIMARY KEY,
    id_pedido INT UNIQUE NOT NULL REFERENCES Pedidos(id_pedido),
    consecutivo_dian VARCHAR(100) UNIQUE NOT NULL,
    fecha_emision TIMESTAMP NOT NULL,
    xml_factura TEXT NOT NULL,
    pdf_factura_url VARCHAR(255),
    estado_dian VARCHAR(50) NOT NULL,
    mensaje_dian TEXT
);

-- Tabla AuditoriaSistema
CREATE TABLE AuditoriaSistema (
    id_auditoria SERIAL PRIMARY KEY,
    id_empleado INT REFERENCES Empleados(id_empleado),
    fecha_accion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo_accion VARCHAR(100) NOT NULL,
    tabla_afectada VARCHAR(100),
    id_registro_afectado INT,
    descripcion_detallada TEXT
);
