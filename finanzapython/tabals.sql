CREATE TABLE Ingresos (
    id INT PRIMARY KEY IDENTITY(1,1),
    cantidad DECIMAL(18, 2),
    descripcion NVARCHAR(255)
);

CREATE TABLE Gastos (
    id INT PRIMARY KEY IDENTITY(1,1),
    cantidad DECIMAL(18, 2),
    descripcion NVARCHAR(255)
);

CREATE TABLE Prestamos (
    id INT PRIMARY KEY IDENTITY(1,1),
    cantidad DECIMAL(18, 2),
    tasa_interes DECIMAL(18, 2),
    plazo INT
);
select *from Ingresos;
select *from Prestamos;
select *from Gastos;