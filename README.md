# Patrones de Diseño

[Python](https://refactoring.guru/es/design-patterns/python) 
[JS/TS](https://refactoring.guru/es/design-patterns/typescript)

## Patrones Creacionales (Crean objetos de manera eficiente)

1. Singleton: Asegura que una clase tenga solo una instancia y proporciona un punto de acceso global a ella.
2. Factory Method: Define una interfaz para crear objetos, pero deja que las subclases decidan qué clase instanciar.
3. Abstract Factory: Proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas.
4. Builder: Separa la construcción de un objeto complejo de su representación, permitiendo la creación paso a paso.
5. Prototype: Permite crear nuevos objetos copiando una instancia existente en lugar de crearla desde cero.

## Patrones Estructurales (Componen clases u objetos para formar estructuras más grandes)

1. Adapter: Permite que interfaces incompatibles trabajen juntas.
2. Bridge: Desacopla una abstracción de su implementación, permitiendo que ambas evolucionen independientemente.
3. Composite: Compone objetos en estructuras de árbol para representar jerarquías parte-todo, permitiendo tratar objetos individuales y compuestos de la misma manera.
4. Decorator: Añade responsabilidades adicionales a un objeto de manera dinámica.
5. Facade: Proporciona una interfaz simplificada para un sistema complejo.
6. Flyweight: Reduce el uso de memoria compartiendo tantos datos como sea posible con objetos similares.
7. Proxy: Proporciona un sustituto o representante de otro objeto para controlar el acceso a él.
8. Patrones Comportamentales (Gestionan la interacción y responsabilidad entre objetos)
9. Chain of Responsibility: Pasa una solicitud por una cadena de manejadores hasta que uno la maneje.
10. Command: Encapsula una solicitud como un objeto, permitiendo parametrizar clientes con diferentes solicitudes, encolar solicitudes o registrar operaciones.
11. Interpreter: Define una representación gramatical para un lenguaje y un intérprete para interpretar las frases de ese lenguaje.
12. Iterator: Proporciona un modo de acceder a los elementos de un objeto agregado secuencialmente sin exponer su representación subyacente.
13. Mediator: Define un objeto que encapsula cómo interactúan un conjunto de objetos, promoviendo un bajo acoplamiento.
14. Memento: Permite capturar y restaurar el estado interno de un objeto sin violar su encapsulamiento.
15. Observer: Define una dependencia de uno a muchos, de modo que cuando un objeto cambia de estado, todos sus dependientes son notificados.
16. State: Permite que un objeto altere su comportamiento cuando su estado interno cambia.
17. Strategy: Define una familia de algoritmos, encapsulándolos e intercambiándolos dinámicamente.
18. Template Method: Define el esqueleto de un algoritmo en una operación, permitiendo que las subclases redefinan ciertos pasos del algoritmo sin cambiar su estructura.
19. Visitor: Representa una operación que se va a realizar sobre los elementos de una estructura de objetos, permitiendo definir nuevas operaciones sin cambiar las clases de los elementos.