from producto import Producto


def test_cp01_crear_producto():
    p = Producto("P001", "Teclado", 350, 10)
    assert p is not None


def test_cp02_mostrar_codigo():
    p = Producto("P001", "Teclado", 350, 10)
    assert p.codigo == "P001"


def test_cp03_mostrar_nombre():
    p = Producto("P001", "Teclado", 350, 10)
    assert p.nombre == "Teclado"


def test_cp04_mostrar_precio():
    p = Producto("P001", "Teclado", 350, 10)
    assert p.precio == 350


def test_cp05_mostrar_existencia():
    p = Producto("P001", "Teclado", 350, 10)
    assert p.existencia == 10


def test_cp06_mostrar_informacion_completa():
    p = Producto("P001", "Teclado", 350, 10)
    info = p.mostrar_informacion()
    assert "P001" in info
    assert "Teclado" in info
    assert "350" in info
    assert "10" in info


def test_cp07_crear_otro_producto():
    p1 = Producto("P001", "Teclado", 350, 10)
    p2 = Producto("P002", "Mouse", 180, 5)
    assert p2.codigo == "P002"
    assert p2.nombre == "Mouse"
    assert p2.precio == 180
    assert p2.existencia == 5
    assert p1.codigo == "P001"
    assert p1.nombre == "Teclado"
