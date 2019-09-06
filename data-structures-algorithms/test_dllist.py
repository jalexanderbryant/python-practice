from dllist import *

def test_create_list():
    colors = DoubleLinkedList()
    colors.dump()

def test_push():
    print(f"\n\nTesting Push.")
    colors = DoubleLinkedList()
    colors.push("Pthalo Blue")
    colors._invariant()
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
    colors._invariant()
    colors.dump()

def test_pop():
    print(f"\n\nTesting pop.")
    colors = DoubleLinkedList()
    colors.push("Magenta")
    colors._invariant()
    colors.push("Alizarin")
    colors.push("Van Dyke")
    colors._invariant()
    colors.dump("before first pop()")
    assert colors.pop() == "Van Dyke"
    colors._invariant()
    colors.dump("After pop()")
#    assert colors.get(1) == "Alizarin"
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    colors._invariant()
    assert colors.pop() == None


def test_shift():
    print(f"\n\nTesting Shift")
    colors = DoubleLinkedList()
    colors.shift("Cadmium Orange")
    assert colors.count() == 1

    colors.shift("Carbazole Violet")
    assert colors.count() == 2

    assert colors.pop() == "Carbazole Violet"
    assert colors.count() == 1
    assert colors.pop() == "Cadmium Orange"
    assert colors.count() == 0
    colors.dump()


def test_unshift():
    print(f"\n\nTesting Unshift")
    colors = DoubleLinkedList()
    colors.shift("Viridian")
    colors.shift("Sap Green")
    colors.shift("Van Dyke")
    colors.dump("Before unshifting.")
    assert colors.unshift() == "Viridian"
    assert colors.unshift() == "Sap Green"
    assert colors.unshift() == "Van Dyke"
    assert colors.unshift() == None


def test_remove():
    print(f"\n\nTesting Unshift")
    colors = DoubleLinkedList()
    colors.push("Cobalt")
    colors.push("Zinc White")
    colors.push("Nickle Yellow")
    colors.push("Perinone")
    colors.dump("Before Removing.")
    assert colors.remove("Cobalt") == 0
    colors._invariant()
    colors.dump("before perinone")
    assert colors.remove("Perinone") == 2
    colors._invariant()
    colors.dump("after perinone")
    assert colors.remove("Nickle Yellow") == 1
    colors._invariant()
    assert colors.remove("Zinc White") == 0
    colors._invariant()


def test_first():
    print(f"\n\nTesting first()")
    colors = DoubleLinkedList()
    colors.push("Cadmium Red Light")
    colors.dump("before first()")
    assert colors.first() == "Cadmium Red Light"
    colors.dump("before first()")
    colors.push("Hansa Yellow")
    assert colors.first() == "Cadmium Red Light"
    colors.dump("before first()")
    colors.shift("Pthalo Green")
    assert colors.first() == "Cadmium Red Light"

def test_last():
    colors = DoubleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.last() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.last() == "Hansa Yellow"
    colors.shift("Pthalo Green")
    assert colors.last() == "Pthalo Green"

def test_get():
    print(f"\n\nTesting get()")
    colors = DoubleLinkedList()
    colors.push("Vermillion")
    colors.dump("B4 first get()")
    assert colors.get(0) == "Vermillion"
    colors.push("Sap Green")
    colors.dump("B4 next get()")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    colors.push("Cadmium Yellow Light")
    colors.dump("Before next get()")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == "Cadmium Yellow Light"
    assert colors.pop() == "Cadmium Yellow Light"
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == None
    colors.pop()
    colors.dump("After pop()")
    assert colors.get(0) == "Vermillion"
    colors.pop()
    assert colors.get(0) == None

def test_reverse():
    print("\n\nTesting Reverse")
    colors = DoubleLinkedList()
    colors.push("Vermillion")
    colors.push("Sap Green")
    colors.push("Cadmium Yellow Light")
    colors.push("Hansa Yellow")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == "Cadmium Yellow Light"
    assert colors.get(3) == "Hansa Yellow"
    colors.dump()
    colors.reverse()
    colors.dump()
    assert colors.get(0) is "Hansa Yellow"
    assert colors.get(1) is "Cadmium Yellow Light"
    assert colors.get(2) is "Sap Green"
    assert colors.get(3) is "Vermillion"
