create table usuarios (
	usuarioId serial,
	nombre character varying(40),
	pass character varying(40),
	constraint idUs primary key(usuarioId)
	);
create table  almacenes (
	almacenId serial,
	usuarioId integer,
	constraint idA primary key(almacenId),
	constraint fId foreign key(usuarioId) references usuarios(usuarioId) on delete cascade
	);
create table  cajeros (
	cajeroId serial,
	usuarioId integer,
	constraint idC primary key(cajeroId),
	constraint fId foreign key(usuarioId) references usuarios(usuarioId) on delete cascade
	);
create table  administradores (
	administradorID serial,
	usuarioId integer,
	constraint idAd primary key(administradorId),
	constraint fId foreign key(usuarioId) references usuarios(usuarioId) on delete cascade
	);
create table products (
	productoId SERIAL,
	nombre character varying(150),
	precio float,
	stock integer,
	constraint prodId primary key(productoId)
	
);
create table facturs(
	facturaId serial,
	fecha character varying(150),
	subtotal decimal,
	ivg decimal,
	total decimal,
	constraint 	facId primary key(facturaId)
	
);
create table factursProducts(
	facturaProdId serial,
	facturaId serial,
	productoId serial,
	cantidad integer,
	constraint fId foreign key(facturaId) references facturs(facturaId) on delete cascade,
	constraint pId foreign key(productoId) references products(productoId) on delete cascade,
	constraint primA primary key(facturaProdId)
	
	
);
insert into usuarios(nombre, pass) values ('administrador','pass');
insert into usuarios(nombre, pass) values ('cajero','pass');
insert into usuarios(nombre, pass) values ('almacen','pass');
inserto into administradores(usuarioId) values(1);
insert into cajeros(usuariosId) values(2);
insert into almacenes(usuarioId) values(3);