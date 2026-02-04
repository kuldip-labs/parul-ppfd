## First install mongodb orm
`pip install pymongo`

## The CRUD Script
* This script connects to a local instance (or Atlas), creates a database named company_db, and performs the four core operations on a users collection.
* The _id field: MongoDB automatically generates a unique _id for every document unless you provide one.

* The $set operator: When updating, always use $set. If you omit it, MongoDB will replace the entire document with your update object instead of just changing one field.

* Closing Connections: While pymongo handles connection pooling automatically, you can call client.close() at the very end of your application lifecycle.