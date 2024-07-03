discussing basic architecture of a database.
components to cover: database engine, query processor, storage manager, transaction manager
Database engine: a database engine, also known as a database management system, is the underlying software to a database, it allows users to create, read, update, and delete data from a database. it is responsible for managing the database's storage, retrieval, and manipulation of data.
Query processor: a query processor is an important part of a database engine that interprets and executes database queries. it converts high level queries that are typically in SQL into low level instructions that the database engine can perform to grab or manipulate data.
Storage manager: a storage manager is another critical component of a database engine which is responsible for managing the physical storage of data. it handles the allocation, organization, and retrieval of data on storage devices such as hard disks and ssds. the storage manager ensures that data is stored efficiently and can be accessed quickly and reliably 
Transaction manager: a transaction manager is a component of a database engine that ensures transactions are processed reliably and adhere to some certain properties which are: Atomicity (a process which guarantees that each transaction is a single unit of work. which means that a transaction must either be completed entirely or not executed at all), consistency, isolation, and durability. this component is crucial for maintaining data integrity especially in multi user environments where many people connect to the database at once.

Explaining the fundamental operations of relational algebra


Selection: selection is used to filter rows based on a specified condition such as age or salary. Example: σage>30​(Employees) <- selects all employees under the age of 30

Projection: projection is used to select certain columns from a relation, reducing the number of properties available such as reducing all employee information into name and age. Example: πname, age(Employees)πname, age​(Employees) <- selects only name and age from the employees list

Union: a union is used to combine lists of two relations, the relations must be compatible. Example: Employees∪Contractors

Set difference: set difference is used to find lists that are in one relation but not in another, they must adhere to the same compatibility requirements as unions. Example: Employees−Contractors

Cartesian product: a cartesian product combines lists from two relations in a pairwise(things occurring in pairs) manner, producing a relation whose lists are all possible combinations of tuples from the two input relations. Example: Employees×Departments

Rename: rename is used to rename the attributes of a relation or give a relation a new name. Example:  ρEmp(EmpID, EmpName, EmpAge)(Employees)ρEmp(EmpID, EmpName, EmpAge)​ <- renames employee relations to "emp" and its attributes to "empid" "empname" and "empage"

Explaining the  components of an entity relationship model.

Entities: entities are objects or things in the real world that have an independent existence and can be distinctly identified. Entities represent the key components of the database and can be tangible objects or concepts. consist of entity types and instances.

Attributes: are properties or characteristics of entities. each attribute describes some aspect of an entity and has a specific value for each instance. Could be an employee as an entity

Entity sets:a collection of similar types of entities 

relationships: these are associations between entities, relationships show how entities interact with eachother 

relationship sets: relationship sets are collections of similar types of relationships

primary keys: primary keys are attributes that uniquely identify an entity in a set

foreign keys: foreign keys are attributes in one entity that are primary keys in another entity, they establish a link between two entities 

cardinality: this defines the number of instances of one entity that can or must be connected to each instance of another entity

participation constraints: these constraints can specift whether all or some entity instances participate in a relationship, could be total participation or partial participation

generalization and specialization: generalization is the process of extracting common characteristics from one or two entities and making them into a generalized supertype. specilization is the opposite, where an entity is divided into subtypes bassed off of some characteristics

aggregation: aggregation is a concept used when we need to express a relationship between a relationship set and an enetity set, this allows for a more complex structure.