## A simple Securirty Per Point module that you can use it on your services to provide security and prevent any spams.

### Requirements:
    PostgreSQL Database

### Configurations:
    Database(Host, User, Password, Port, Name)
    Auto fill id
    How much score per tick
    How much seconds for a tick
    Max score per user
    User default score

Example of usage:
```python
import spp

pgdb_user = 'USER'
pgdb_password = 'PASSWORD'
pgdb_name = 'NAME'

sec = spp.SPP(pgdb_name, pgdb_user, pgdb_password)

# Create the entity with default id and score
entity = sec.createEntity()

sec.increaseScore(entity.id, 5)

sec.decreaseScore(entity.id, 5)

entity = sec.getEntity(entity.id)

sec.setEntityScore(entity.id, 15)

sec.removeEntity(id)

```
